import { Component, Inject, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { IProject } from 'src/app/models/i-project';
import { RobotService } from 'src/app/services/robot.service';

@Component({
  selector: 'app-project-dialog',
  templateUrl: './project-dialog.component.html',
  styleUrls: ['./project-dialog.component.css']
})
export class ProjectDialogComponent implements OnInit {
  form: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    public dialogRef: MatDialogRef<ProjectDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public project: IProject,
    private robotService: RobotService
  ) { }

  onCancel(): void {
    this.dialogRef.close();
  }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      title: [this.project.title, Validators.required],
      description: [this.project.description, Validators.required],
      robot: [this.project.robot],
    });
  }

  searchRobots() {
    this.robotService.getRobots().subscribe({
      next: (robots => console.log('robots', robots)),
      error: (err) => console.error('error', err)
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
