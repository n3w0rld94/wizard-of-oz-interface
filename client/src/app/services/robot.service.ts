import { Injectable } from '@angular/core';
import { ApiService } from './api.service';

@Injectable({
  providedIn: 'root'
})
export class RobotService {

  constructor(private apiService: ApiService) { }

  getRobots() {
    const url = 'robots';

    return this.apiService.get(url);
  }
}
