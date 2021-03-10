import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  form: FormGroup;
  loginInvalid = false;

  constructor(private formBuilder: FormBuilder) { }

  async ngOnInit() {
    this.form = this.formBuilder.group({
      username: ['', Validators.email],
      password: ['', Validators.required]
    });
  }

  onSubmit() {
    return null;
  }
}
