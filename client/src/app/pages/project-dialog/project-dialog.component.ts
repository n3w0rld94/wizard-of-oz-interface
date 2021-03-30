import { animate, style, transition, trigger } from '@angular/animations';
import { Component, Inject, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { AnimusRobot } from 'src/app/models/animus-robot';
import { IProject } from 'src/app/models/i-project';
import { RobotService } from 'src/app/services/robot.service';

@Component({
    selector: 'app-project-dialog',
    templateUrl: './project-dialog.component.html',
    styleUrls: ['./project-dialog.component.css'],
    animations: [
        trigger(
            'inAnimation',
            [
                transition(
                    ':enter',
                    [
                        style({ height: '0%' }),
                        animate('0.2s ease-out',
                            style({ height: '100%' }))
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
                        style({ height: '100%' }),
                        animate('0.2s ease-in',
                            style({ height: '0%' }))
                    ]
                )
            ]
        )
    ]
})
export class ProjectDialogComponent implements OnInit {
    form: FormGroup;
    availableRobots: AnimusRobot[] = [
        { name: 'Fluff Ball 1' } as AnimusRobot,
        { name: 'Fluff Ball 2' } as AnimusRobot,
        { name: 'Fluff Ball 3' } as AnimusRobot,
    ];
    selectedRobot: AnimusRobot;
    project: IProject;

    constructor(
        private formBuilder: FormBuilder,
        private robotService: RobotService,
        public dialogRef: MatDialogRef<ProjectDialogComponent>,
        @Inject(MAT_DIALOG_DATA) public config: {
            project: IProject, singleSelection: boolean
        },
    ) { }

    onCancel(): void {
        this.dialogRef.close();
    }

    ngOnInit(): void {
        this.project = this.config.project;
        this.form = this.formBuilder.group({
            robots: [this.project.supportedRobots],
        });
        this.robotService.getRobots().subscribe({
            next: (robots => {
                console.log('robots', robots);
                this.availableRobots = robots || [];
            }),
            error: (err) => {
                console.error('error retrieving robots', err);
                this.availableRobots = [];
            }
        });
    }

    searchRobots() {
        this.robotService.getRobots().subscribe({
            next: (robots => {
                console.log('robots', robots);
                this.availableRobots = robots || [];
            }),
            error: (err) => {
                console.error('error retrieving robots', err);
                this.availableRobots = [];
            }
        });
    }

    onClose(): IProject | null {
        if (this.form.valid) {
            const formProject = this.form.getRawValue();
            return formProject;
        } else {
            return null;
        }
    }
}
