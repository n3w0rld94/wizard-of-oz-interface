import { Component, OnInit } from '@angular/core';
import { RobotBehaviour } from 'src/app/models/robot-behaviour';
import { CdkDragDrop, moveItemInArray, transferArrayItem, copyArrayItem } from '@angular/cdk/drag-drop';

@Component({
  selector: 'app-activity-modeler',
  templateUrl: './activity-modeler.component.html',
  styleUrls: ['./activity-modeler.component.css']
})
export class ActivityModelerComponent {
  // behaviour: RobotBehaviour;
  // availableBehaviours: RobotBehaviour[];

  // constructor() { }

  // ngOnInit(): void { }

  // drop(event: CdkDragDrop<string[]>) {
  //   if (event.previousContainer === event.container) {
  //     moveItemInArray(event.container.data, event.previousIndex, event.currentIndex);
  //   } else {
  //     copyArrayItem(event.previousContainer.data,
  //       event.container.data,
  //       event.previousIndex,
  //       event.currentIndex);
  //   }
  // }


}
