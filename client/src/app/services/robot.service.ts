import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { ToastrService } from 'ngx-toastr';
import { Observable, throwError } from 'rxjs';
import { catchError, map, take, tap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { AnimusRobot } from '../models/animus-robot';
import { AnimusBaseServerResponse, AnimusServerResponse, GetRobotsResponse } from '../models/server-response';
import { ApiService } from './api.service';
import { AuthenticationService } from './authentication.service';
import { LoaderService } from './loader.service';

@Injectable({
  providedIn: 'root'
})
export class WoZSocket extends Socket {

  constructor() {
    super({ url: 'ws://127.0.0.1:' + environment.webSocketPort + '/', options: { autoConnect: false } });
  }

}

@Injectable({
  providedIn: 'root'
})
export class RobotService {
  constructor(
    private apiService: ApiService,
    private toastService: ToastrService,
    private loaderService: LoaderService,
    private authenticationService: AuthenticationService,
    private socket: WoZSocket
  ) { }

  getRobots(): Observable<AnimusRobot[]> {
    const url = 'robots';

    this.loaderService.show();
    return this.apiService.get<AnimusServerResponse<GetRobotsResponse>>(url)
      .pipe(
        take(1),
        tap(response => this.loaderService.hide()),
        map(response => {
          return response.payload?.robots;
        }),
        catchError((err, caught) => {
          this.loaderService.hide();
          this.toastService.error(err, 'Error');
          return throwError(err);
        })
      ) as unknown as Observable<AnimusRobot[]>;
  }

  connect(robot: AnimusRobot): Observable<boolean> {
    const url = 'connect';

    this.loaderService.show();
    return this.apiService.post<AnimusRobot, AnimusBaseServerResponse>(url, robot)
      .pipe(
        take(1),
        tap(response => {
          this.loaderService.hide();
          if (response.success) {
            this.toastService.success('Successfully connected to ' + robot.name, 'Connected');
          } else {
            this.toastService.warning(response.description, 'Unable to connect to ' + robot.name);
          }
        }),
        map(response => response.success),
        catchError((err, caught) => {
          this.loaderService.hide();
          this.toastService.error(err, 'Error');
          return throwError(err);
        })
      );
  }

  connectToControlSocket() {
    console.log('called connectToControlSocket');

    const user = this.authenticationService.user.value;
    this.socket.ioSocket.io.opts.query = { username: user?.username };
    this.socket.connect();
    this.socket.fromEvent('move_robot').subscribe({
      next: (result) => console.log('Received: ', result)
    });
  }

  move(forward: any, left: any, rotate: any) {
    this.socket.emit('move_robot', { forward, left, rotate });
  }
}
