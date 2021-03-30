import { DragDropModule } from '@angular/cdk/drag-drop';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NbChatModule, NbLayoutModule, NbThemeModule } from '@nebular/theme';
import { ToastrModule } from 'ngx-toastr';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MaterialModule } from './material/material.module';
import { NavigationComponent } from './navigation/navigation.component';
import { KeyboardJoystickComponent } from './pages/keyboard-joystick/keyboard-joystick.component';
import { LoginComponent } from './pages/login/login.component';
import { ProjectControlComponent } from './pages/project-control/project-control.component';
import { ProjectDialogComponent } from './pages/project-dialog/project-dialog.component';
import { ProjectManagerComponent } from './pages/project-manager/project-manager.component';
import { RobotsTableComponent } from './pages/robots-table/robots-table.component';
import { SpinnerOverlayComponent } from './pages/spinner-overlay/spinner-overlay.component';
import { SpinnerComponent } from './pages/spinner/spinner.component';


@NgModule({
    declarations: [
        AppComponent,
        LoginComponent,
        NavigationComponent,
        ProjectManagerComponent,
        ProjectControlComponent,
        ProjectDialogComponent,
        KeyboardJoystickComponent,
        RobotsTableComponent,
        SpinnerOverlayComponent,
        SpinnerComponent
        // ActivityModelerComponent
    ],
    imports: [
        HttpClientModule,
        BrowserModule,
        AppRoutingModule,
        FormsModule,
        BrowserAnimationsModule,
        ToastrModule.forRoot(),
        MaterialModule,
        FormsModule,
        ReactiveFormsModule,
        DragDropModule,
        NbThemeModule.forRoot({name: 'corporate'}),
        NbChatModule,
        NbLayoutModule
    ],
    providers: [],
    bootstrap: [AppComponent],
    entryComponents: [
        SpinnerOverlayComponent
    ]
})
export class AppModule { }
