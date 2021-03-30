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
    @Input() singleSelection: boolean;
    @Output() selectedRobotEmitter = new EventEmitter<AnimusRobot | null>();
    displayedColumns = ['select', 'name', 'model', 'location', 'ip'];
    dataSource = new MatTableDataSource<AnimusRobot>([]);
    selection = new SelectionModel<AnimusRobot>(true, []);

    constructor() { }

    ngOnInit(): void {
        this.dataSource.data = this.robotsList;
        this.selection = new SelectionModel<AnimusRobot>(!!this.singleSelection, []);
    }

    ngOnChanges() {
        this.selection.toggle(this.selectedRobot);
    }

    selectRobot(selected: any, robot: AnimusRobot) {
        this.selection.toggle(robot);
        const robotToEmit = selected ? robot : null;
        debugger;
        this.selectedRobotEmitter.emit(robotToEmit);
    }
}
