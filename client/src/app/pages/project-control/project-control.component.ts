import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-project-control',
  templateUrl: './project-control.component.html',
  styleUrls: ['./project-control.component.css']
})
export class ProjectControlComponent implements OnInit {
  @Input() robotName = 'Pepper';
  isConnected = false;


  constructor() { }

  ngOnInit(): void {
  }

}
