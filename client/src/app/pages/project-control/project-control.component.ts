import { animate, style, transition, trigger } from '@angular/animations';
import { Component, Input, OnInit } from '@angular/core';
import { AnimusRobot } from 'src/app/models/animus-robot';
import { ApiService } from 'src/app/services/api.service';
import { ControlService } from 'src/app/services/control.service';
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
  @Input() robot: AnimusRobot;
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
    if (this.robot) {
      this.robotService.connect(this.robot).subscribe({
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
