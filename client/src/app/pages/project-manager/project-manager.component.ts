import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';
import { AnimusRobot } from 'src/app/models/animus-robot';
import { IProject } from 'src/app/models/i-project';
import { ProjectDialogComponent } from '../project-dialog/project-dialog.component';

@Component({
    selector: 'app-project-manager',
    templateUrl: './project-manager.component.html',
    styleUrls: ['./project-manager.component.css']
})
export class ProjectManagerComponent implements OnInit, AfterViewInit {
    displayedColumns: string[] = ['openProject', 'title', 'description', 'robot', 'edit'];
    dataSource: MatTableDataSource<any>;
    tempRobots: any = {};

    @ViewChild(MatPaginator) paginator: MatPaginator;
    @ViewChild(MatSort) sort: MatSort;

    constructor(
        private dialog: MatDialog,
        private router: Router
    ) { }

    ngOnInit(): void {
        let dataSource: IProject[] = [
            {
                title: 'Project 1',
                description: ' My first project',
                supportedRobots: [{ name: 'Pepper' } as AnimusRobot],
                supportedRobotsText: ''
            }
        ];

        dataSource = dataSource.map(item => {
            const supportedRobotsText = this.concatRobotText(item.supportedRobots);
            item.supportedRobotsText = supportedRobotsText;

            return item;
        });


        this.dataSource = new MatTableDataSource(dataSource);
    }

    ngAfterViewInit() {
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.sort;
    }

    concatRobotText(robots: { name: string }[]) {
        let supportedRobotsText = robots.length ? robots[0].name : '';

        for (let i = 1; i < robots.length; i++) {
            supportedRobotsText += ', ' + robots[i].name;
        }

        return supportedRobotsText;
    }

    onOpenProject(project: IProject): void {
        localStorage.setItem('selectedProject', JSON.stringify(project));
        this.router.navigateByUrl('/project-control-screen');
    }

    openDialog(project: IProject, i: number): void {
        const dialogRef = this.dialog.open(ProjectDialogComponent, {
            data: {
                project,
                singleSelection: false
            },
            minWidth: 600
        });

        dialogRef.afterClosed().subscribe({
            next: result => {
                console.log('The dialog was closed', result);

                if (result && result.robots) {
                    const supportedRobotsText = this.concatRobotText(result.robots);
                    (document.getElementById('input-supported-robots-text-' + i) as HTMLInputElement)
                        .value = supportedRobotsText;
                    this.tempRobots[i] = {
                        supportedRobotsText,
                        supportedRobots: result.robots
                    };
                }
            }
        });
    }

    applyFilter(event: Event) {
        const filterValue = (event.target as HTMLInputElement).value;
        this.dataSource.filter = filterValue.trim().toLowerCase();

        if (this.dataSource.paginator) {
            this.dataSource.paginator.firstPage();
        }
    }

    makeLineEditable(row: any): void {
        if (row.editable) {
            this.tempRobots = {};
        }
        row.editable = !row.editable;
    }

    newProject() {
        this.dataSource.data = [
            {
                title: '',
                description: '',
                supportedRobots: [],
                supportedRobotsText: '',
                editable: true
            },
            ...this.dataSource.data
        ];
    }

    saveProject(row: any, i: number, tempRobots: any) {
        const title = (document.getElementById('input-title-' + i) as HTMLInputElement).value;
        const description = (document.getElementById('input-description-' + i) as HTMLInputElement).value;

        row.title = title;
        row.description = description;
        row.supportedRobots = tempRobots[i]?.supportedRobots || [];
        row.supportedRobotsText = tempRobots[i]?.supportedRobotsText || '';
        row.editable = false;
    }

}
