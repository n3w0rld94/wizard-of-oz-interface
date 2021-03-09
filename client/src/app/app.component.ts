import { Component } from '@angular/core';
import { ApiService } from './services/api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'wizard-of-oz-interface';

  constructor(private apiService: ApiService){}

  onSubmit(event: any): void {
    const form = event.value;
    const outcome = this.apiService.login(form.username, form.password);

    if (outcome) {
      alert('Successfully logged in!');
    } else {
      alert('Logged in failed.');
    }
  }
}
