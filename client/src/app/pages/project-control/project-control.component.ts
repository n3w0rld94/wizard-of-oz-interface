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
  videoSrc = '';

  originalVideoSource = '/animus/start_video_feed';

  constructor(private controlService: ControlService, private apiService: ApiService) { }

  ngOnInit(): void {
  }

  onStartVideoStream() {
    console.log('called startVideoStream');
    // this.controlService.startVideoStream();
    this.videoSrc = this.originalVideoSource;
  }

  onStopVideoStreaming() {
    this.videoSrc = '';
    this.apiService.get('stop_video_feed').subscribe({
      next: (result) => console.log('video stopped, response: ', result),
      error: (err) => console.error('erro stopping video', err)
    });
  }
}
