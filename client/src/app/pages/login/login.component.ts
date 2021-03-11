import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  form: FormGroup;
  loginInvalid = false;

  constructor(
    private formBuilder: FormBuilder,
    private apiService: ApiService
  ) { }

  async ngOnInit() {
    this.form = this.formBuilder.group({
      username: ['', Validators.email],
      password: ['', Validators.required]
    });
  }

  async login() {
    const formValue = this.form.getRawValue();
    const result = this.apiService.login(formValue.username, formValue.password);

    console.log('Login Result', result);
  }

  onSubmit() {
    return null;
  }
}
