import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, ObservableInput, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class ApiService {
  baseApiUrl = '/animus/';

  constructor(private httpClient: HttpClient) { }

  get(url: string, parameters?: Record<string, any>): Observable<any> {
    console.log('parameters', parameters);
    const options = this.getApiGetOptions(parameters);

    return this.httpClient.get<any>(this.baseApiUrl + url, options).pipe(
      retry(1),
      catchError(this.processError)
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
