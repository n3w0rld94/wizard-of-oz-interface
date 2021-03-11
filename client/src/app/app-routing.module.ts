import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login.component';
import { ProjectControlComponent } from './pages/project-control/project-control.component';
import { ProjectManagerComponent } from './pages/project-manager/project-manager.component';

const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'project-manager', component: ProjectManagerComponent },
  { path: 'project-control-screen', component: ProjectControlComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
