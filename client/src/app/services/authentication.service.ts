import { Injectable } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { BehaviorSubject, Observable, throwError } from 'rxjs';
import { catchError, map, take, tap } from 'rxjs/operators';
import { AnimusBaseServerResponse, AnimusServerResponse } from '../models/server-response';
import { User } from '../models/user';
import { ApiService } from './api.service';
import { LoaderService } from './loader.service';

@Injectable({
    providedIn: 'root'
})
export class AuthenticationService {
    user = new BehaviorSubject<User | null>(null);

    constructor(
        private apiService: ApiService,
        private loaderService: LoaderService,
        private toasterService: ToastrService
    ) { }

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

        this.loaderService.show();
        return this.apiService.post<{ username: string, password: string }, AnimusServerResponse<User>>(url, { username, password })
            .pipe(
                take(1),
                tap(response => {
                    if (response.success) {
                        const user = response.success ? response.payload : null;
                        this.user.next({ ...user } as User | null);
                        delete response.payload;

                    }

                    this.loaderService.hide();
                }),
                catchError((err, caught) => {
                    this.loaderService.hide();
                    this.toasterService.error(err, 'Error');
                    return throwError(err);
                })
            );
    }

    logout(): Observable<AnimusBaseServerResponse> {
        const url = 'logout';

        this.loaderService.show();
        return this.apiService.get<AnimusBaseServerResponse>(url)
            .pipe(
                take(1),
                tap(response => {
                    if (response.success) {
                        if (response.success) {
                            this.user.next(null);
                            this.toasterService.success('Logged out.');
                        } else {
                            this.toasterService.warning(response.description, 'Unable to logout');
                        }
                    }

                    this.loaderService.hide();
                }),
                catchError((err, caught) => {
                    this.loaderService.hide();
                    this.toasterService.error(err, 'Error');
                    return throwError(err);
                })
            );
    }
}
