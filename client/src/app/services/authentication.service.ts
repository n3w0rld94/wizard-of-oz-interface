import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { map, take, tap } from 'rxjs/operators';
import { AnimusBaseServerResponse, AnimusServerResponse } from '../models/server-response';
import { User } from '../models/user';
import { ApiService } from './api.service';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  user = new BehaviorSubject<User | null>(null);

  constructor(private apiService: ApiService) { }

  checkAuthenticated(): Observable<boolean> {
    const url = 'check-authenticated';

    return this.apiService.get<AnimusServerResponse<User>>(url)
      .pipe(
        take(1),
        tap(result => {
          const user = result.success ? result.payload : null;
          this.user.next(user as User | null);
        }),
        map(result => result?.success)
      );
  }

  login(username: string, password: string): Observable<AnimusBaseServerResponse> {
    const url = 'login';

    return this.apiService.post<{ username: string, password: string }, AnimusServerResponse<User>>(url, { username, password })
      .pipe(
        take(1),
        tap(response => {
          if (response.success) {
            const user = response.success ? response.payload : null;
            this.user.next(user as User | null);

            delete response.payload;
          }
        })
      );
  }
}
