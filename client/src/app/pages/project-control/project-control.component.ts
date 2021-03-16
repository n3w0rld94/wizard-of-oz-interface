import { animate, style, transition, trigger } from '@angular/animations';
import { Component, OnInit } from '@angular/core';
import { IProject } from 'src/app/models/i-project';
import { ApiService } from 'src/app/services/api.service';
import { RobotService } from 'src/app/services/robot.service';

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
  isConnected = false;
  isVideoFullScreen = false;
  loadingVideo = false;
  videoSrc = '';

  originalVideoSource = '/animus/start_video_feed';

  constructor(
    private apiService: ApiService,
    private robotService: RobotService
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
    if (this.project?.robot) {
      this.robotService.connect(this.project.robot).subscribe({
        next: (success) => {
          this.isConnected = success;
        }
      });
    } else {
      console.error('Connect - Something went wrong');
    }
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
}
