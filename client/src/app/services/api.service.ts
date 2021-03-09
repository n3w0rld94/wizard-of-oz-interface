import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ObservableInput, throwError } from 'rxjs';

import { retry, catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  baseApiUrl = '/api';

  constructor(private httpClient: HttpClient) { }

  login(username: string, password: string): boolean {

    const params = new HttpParams()
      .set('username', username)
      .set('password', password);

    try {
      this.httpClient.get<any>(this.baseApiUrl + '/login', { params })
        .pipe(
          retry(1),
          catchError(this.processError)
        );
    } catch (ex) {
      console.log('Error attempting to log in', ex);
    }

    return true;
  }

  processError(err: any): ObservableInput<any> {
    let message = '';
    if (err.error instanceof ErrorEvent) {
      message = err.error.message;
    } else {
      message = `Error Code: ${err.status}\nMessage: ${err.message}`;
    }
    console.error(message);
    return throwError(message);
  }
}
