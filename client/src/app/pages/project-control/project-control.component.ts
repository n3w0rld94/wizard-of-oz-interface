import { animate, style, transition, trigger } from '@angular/animations';
import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { AnimusRobot } from 'src/app/models/animus-robot';
import { IProject } from 'src/app/models/i-project';
import { ApiService } from 'src/app/services/api.service';
import { RobotService } from 'src/app/services/robot.service';
import { ProjectDialogComponent } from '../project-dialog/project-dialog.component';

@Component({
    selector: 'app-project-control',
    templateUrl: './project-control.component.html',
    styleUrls: ['./project-control.component.css'],
    animations: [
        trigger(
            'inAnimation',
            [
                transition(
                    ':enter',
                    [
                        style({ opacity: 0 }),
                        animate('0.2s ease-out',
                            style({ opacity: 1 }))
                    ]
                ),
            ]
        ),
        trigger(
            'outAnimation',
            [
                transition(
                    ':leave',
                    [
                        style({ opacity: 1 }),
                        animate('0.1s ease-in',
                            style({ opacity: 0 }))
                    ]
                )
            ]
        )
    ]
})
export class ProjectControlComponent implements OnInit {
    project: IProject;
    selectedRobot: AnimusRobot;
    isConnected = false;
    isConnectedTest = true;
    isVideoFullScreen = false;
    loadingVideo = false;
    videoSrc = '';
    message = '';
    messages: any[] = [];

    originalVideoSource = '/animus/start_video_feed';

    constructor(
        private apiService: ApiService,
        private robotService: RobotService,
        private dialog: MatDialog,
    ) { }

    ngOnInit(): void {
        const project = localStorage.getItem('selectedProject') as any;
        this.project = project ? JSON.parse(project) : null;
    }

    attachOneTimeListener() {
        const videoPlayer = document.getElementById('video-player-inner') as HTMLElement;
        const thisRef = this;
        videoPlayer.addEventListener('load', displayLoader);
        this.loadingVideo = true;

        function displayLoader() {
            thisRef.loadingVideo = false;
            videoPlayer.removeEventListener('load', displayLoader);
        }
    }

    onConnect() {
        this.openDialog().subscribe({
            next: result => {
                console.log('The dialog was closed', result);

                if (result && result.robots) {
                    this.selectedRobot = result.robots;
                    if (this.selectedRobot) {
                        this.robotService.connect(this.selectedRobot).subscribe({
                            next: (success) => {
                                this.isConnected = success;
                            }
                        });
                    } else {
                        console.error('Connect - Something went wrong');
                    }
                }
            }
        });
    }

    onStartVideoStream() {
        console.log('Starting video stream');
        this.videoSrc = this.originalVideoSource;
        this.attachOneTimeListener();
    }

    onStopVideoStreaming() {
        this.videoSrc = '';
        this.apiService.get('stop_video_feed').subscribe({
            next: (result) => console.log('video stopped, response: ', result),
            error: (err) => console.error('erro stopping video', err)
        });
    }

    fullScreenVideo() {
        const localDocument = document as any;
        const elem = localDocument.getElementById('video-player') as any;

        if (localDocument.webkitFullscreenElement) {
            localDocument.webkitCancelFullScreen();
            this.isVideoFullScreen = false;
        } else {
            elem.webkitRequestFullScreen();
            this.isVideoFullScreen = true;
        }
    }

    sendMessage(event: any, userName: string, avatar: string, reply: boolean) {
        this.messages.push({
            text: event.message,
            date: new Date(),
            reply,
            type: 'text',
            files: [],
            user: {
                name: userName
            },
        });

        this.robotService.say(event.message || 'Hi there').subscribe({
            next: (response) => {
                console.log('success!', response.description);
            }
        });
    }

    openDialog() {
        const dialogRef = this.dialog.open(ProjectDialogComponent, {
            data: {
                project: this.project,
                singleSelection: true
            }
        });

        return dialogRef.afterClosed();
    }
}
