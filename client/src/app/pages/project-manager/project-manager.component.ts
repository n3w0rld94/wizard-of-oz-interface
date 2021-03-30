import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';
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

    @ViewChild(MatPaginator) paginator: MatPaginator;
    @ViewChild(MatSort) sort: MatSort;

    constructor(
        private dialog: MatDialog,
        private router: Router
    ) { }

    ngOnInit(): void {
        this.dataSource = new MatTableDataSource([
            {
                title: 'Project 1',
                description: ' My first project',
                robot: 'Pepper'
            },
            {
                title: 'Project 2',
                description: ' My second project',
                robot: 'Miro'
            }
        ]);
    }

    ngAfterViewInit() {
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.sort;
    }

    onOpenProject(project: IProject): void {
        localStorage.setItem('selectedProject', JSON.stringify(project));
        this.router.navigateByUrl('/project-control-screen');
    }

    openDialog(project: IProject): void {
        const dialogRef = this.dialog.open(ProjectDialogComponent, {
            data: project
        });

        dialogRef.afterClosed().subscribe({
            next: result => {
                console.log('The dialog was closed', result);

                if (result) {
                    project.supportedRobots = result;
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
        row.editable = !row.editable;
    }

    newProject() {
        this.dataSource.data = [
            {
                title: 'New Project',
                description: '',
                supportedRobots: 'None',
                editable: true
            },
            ...this.dataSource.data
        ];
    }

    saveProject(row: any, i: number) {
        const title = (document.getElementById('input-title-' + i) as HTMLInputElement).value;
        const description = (document.getElementById('input-description-' + i) as HTMLInputElement).value;
        const supportedRobots = (document.getElementById('input-supported-robots-' + i) as HTMLInputElement).value;

        row.title = title;
        row.description = description;
        row.supportedRobots = supportedRobots;
        row.editable = false;
    }

}
