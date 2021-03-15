import { Component, Input, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api.service';
import { ControlService } from 'src/app/services/control.service';

@Component({
  selector: 'app-project-control',
  templateUrl: './project-control.component.html',
  styleUrls: ['./project-control.component.css']
})
export class ProjectControlComponent implements OnInit {
  @Input() robotName = 'Pepper';
  isConnected = false;
  isVideoFullScreen = false;
  loadingVideo = false;
  videoSrc = '';

  originalVideoSource = '/animus/start_video_feed';

  constructor(private controlService: ControlService, private apiService: ApiService) { }

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
