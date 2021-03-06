import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { AnimusBaseServerResponse } from '../models/server-response';


@Injectable({
  providedIn: 'root'
})
export class ApiService {
  baseApiUrl = '/animus/';
  baseTestApiUrl = this.baseApiUrl + 'test/';

  constructor(private httpClient: HttpClient) { }

  get<T extends AnimusBaseServerResponse>(url: string, parameters?: Record<string, any>): Observable<T> {
    const options = this.getApiGetOptions(parameters);

    return this.httpClient.get<T>(this.baseApiUrl + url, options).pipe(
      retry(1),
      catchError<any, Observable<T>>(this.processError)
    );
  }

  post<T, J extends AnimusBaseServerResponse>(url: string, data: T): Observable<J> {
    return this.httpClient.post<J>(this.baseApiUrl + url, data, {
      headers: { 'Content-Type': 'application/json' }
    }).pipe(
      retry(1),
      catchError<any, Observable<J>>(this.processError)
    );
  }

  private getApiGetOptions(parameters?: Record<string, any>): any {
    let params;
    let options;

    if (parameters) {
      params = new HttpParams();

      for (const key of Object.keys(parameters)) {
        params = params.set(key, parameters[key]);
      }

      options = { params };
    }

    return options;
  }

  processError<T>(err: any, caught: Observable<T>) {
    let title = 'Unknown Error';
    let message = 'An unknown error has occurred';

    if (err.error instanceof ErrorEvent) {
      title = 'Internal Error';
      message = err.error.message;
    } else {
      title = `Error Code: ${err.status}`;
      message = `Message: ${err.message}`;
    }

    console.error(message);
    return throwError(message);
  }
}
