import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { User } from 'src/app/models/user';
import { AuthenticationService } from 'src/app/services/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  form: FormGroup;
  user: User | null;
  loginInvalid = false;

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthenticationService,
    private toasterService: ToastrService,
    private router: Router
  ) { }

  async ngOnInit() {
    this.authService.user.subscribe({
      next: user => {
        this.user = user;

        if (user) {
          this.router.navigateByUrl('project-dashboard');
        }
      }
    });
    this.form = this.formBuilder.group({
      username: ['', Validators.email],
      password: ['', Validators.required]
    });
  }

  async login() {
    const formValue = this.form.getRawValue();
    this.authService.login(formValue.username, formValue.password).subscribe({
      next: (result) => {
        if (result.success) {
          this.loginInvalid = false;
          this.toasterService.success(result.description, 'Login succeeded');
        } else {
          this.loginInvalid = true;
          this.toasterService.error(result.description, 'Login Failed');
        }
      },
      error: (err: any) => {
        console.error('Error Loggin in', err);
        this.toasterService.error(JSON.stringify(err), 'Error Loggin in');
      }
    });
  }

  async logout() {
    this.authService.logout().subscribe({
      next: (result) => {
        if (result.success) {
          this.loginInvalid = false;
          this.toasterService.success(result.description, 'Login succeeded');
        } else {
          this.loginInvalid = true;
          this.toasterService.error(result.description, 'Login Failed');
        }
      },
      error: (err: any) => {
        console.error('Error Loggin in', err);
        this.toasterService.error(JSON.stringify(err), 'Error Loggin in');
      }
    });
  }
}
