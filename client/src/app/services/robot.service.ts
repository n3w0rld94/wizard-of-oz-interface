import { Injectable } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { Observable } from 'rxjs';
import { map, take, tap } from 'rxjs/operators';
import { AnimusRobot } from '../models/animus-robot';
import { AnimusBaseServerResponse, AnimusServerResponse, GetRobotsResponse } from '../models/server-response';
import { ApiService } from './api.service';
import { LoaderService } from './loader.service';

@Injectable({
  providedIn: 'root'
})
export class RobotService {

  constructor(
    private apiService: ApiService,
    private toastService: ToastrService,
    private loaderService: LoaderService
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
        map(response => response.success)
      );
  }
}
