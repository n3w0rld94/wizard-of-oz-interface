import { Component, Input, OnInit } from '@angular/core';
import { ControlService } from 'src/app/services/control.service';

@Component({
  selector: 'app-project-control',
  templateUrl: './project-control.component.html',
  styleUrls: ['./project-control.component.css']
})
export class ProjectControlComponent implements OnInit {
  @Input() robotName = 'Pepper';
  isConnected = false;

    constructor(private controlService: ControlService) { }

  ngOnInit(): void {
  }

    onStartVideoStream() {
        console.log('called startVideoStream');
        this.controlService.startVideoStream();
    }
}
