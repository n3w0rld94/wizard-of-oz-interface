import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from './guards/auth.guard';
import { LoginComponent } from './pages/login/login.component';
import { ProjectControlComponent } from './pages/project-control/project-control.component';
import { ProjectManagerComponent } from './pages/project-manager/project-manager.component';

const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'project-dashboard', component: ProjectManagerComponent, canActivate: [AuthGuard] },
  { path: 'project-control-screen', component: ProjectControlComponent, canActivate: [AuthGuard] }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
