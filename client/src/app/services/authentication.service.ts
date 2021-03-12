import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map, tap } from 'rxjs/operators';
import { ApiService } from './api.service';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  isUserLoggedIn = false;

  constructor(private apiService: ApiService) { }

  checkAuthenticated(): Observable<boolean> {
    const url = 'check-authenticated';

    return this.apiService.get(url)
      .pipe(
        map(result => result?.success),
        tap(authenticated => this.isUserLoggedIn = authenticated)
      );
  }

  login(username: string, password: string): Observable<any> {
    const url = 'login';

    return this.apiService.get(url, { username, password });
  }
}
