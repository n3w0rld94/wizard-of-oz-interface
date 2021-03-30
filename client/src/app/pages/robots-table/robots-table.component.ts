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
    @Input() selectedRobots: AnimusRobot[];
    @Input() singleSelection: boolean;
    @Output() selectedRobotEmitter = new EventEmitter<AnimusRobot[] | null>();
    displayedColumns = ['select', 'name', 'model', 'location', 'ip'];
    dataSource = new MatTableDataSource<AnimusRobot>([]);
    selection: SelectionModel<AnimusRobot>;

    constructor() { }

    ngOnInit(): void {
        this.dataSource.data = this.robotsList;
    }

    ngOnChanges() {
        if (!this.selection) {
            this.selection = new SelectionModel<AnimusRobot>(!this.singleSelection, []);
        }

        if (this.selectedRobots) {
            for (const robot of this.selectedRobots) {
                this.selection.toggle(robot);
            }
        }
    }

    selectRobot(robot: AnimusRobot) {
        this.selection.toggle(robot);

        this.selectedRobotEmitter.emit(this.selection.selected);
    }
}
