import { SelectionModel } from '@angular/cdk/collections';
import { Component, EventEmitter, Input, OnChanges, OnInit, Output } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { AnimusRobot } from 'src/app/models/animus-robot';

@Component({
  selector: 'app-robots-table',
  templateUrl: './robots-table.component.html',
  styleUrls: ['./robots-table.component.css'],
})
export class RobotsTableComponent implements OnInit, OnChanges {
  @Input() robotsList: AnimusRobot[] = [];
  @Input() selectedRobot: AnimusRobot;
  @Output() selectedRobotEmitter = new EventEmitter<AnimusRobot | null>();
  displayedColumns = ['select', 'name', 'model', 'location'];
  dataSource = new MatTableDataSource<AnimusRobot>([]);
  selection = new SelectionModel<AnimusRobot>(false, []);

  constructor() { }

  ngOnInit(): void {
    this.dataSource.data = this.robotsList;
  }

  ngOnChanges() {
    this.selection.toggle(this.selectedRobot);
  }

  selectRobot(selected: any, robot: AnimusRobot) {
    this.selection.toggle(robot);
    const robotToEmit = selected ? robot : null;
    this.selectedRobotEmitter.emit(robotToEmit);
  }
}
