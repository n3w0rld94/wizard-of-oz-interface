import { Injectable } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { BehaviorSubject } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { IProject } from '../models/i-project';
import { AnimusServerResponse } from '../models/server-response';
import { ApiService } from './api.service';
import { LoaderService } from './loader.service';

@Injectable({
    providedIn: 'root'
})
export class ProjectService {
    #projects = new BehaviorSubject<IProject[]>([]);

    constructor(
        private apiService: ApiService,
        private toastService: ToastrService,
        private loaderService: LoaderService
    ) { }

    getProjects(projectId?: string) {
        const url = 'get-projects';
        projectId = projectId || '';

        this.loaderService.show();
        this.apiService.get<AnimusServerResponse<IProject[]>>(url, { projectId }).pipe(
            tap(response => {
                this.loaderService.hide();

                if (response.success) {
                    this.#projects.next(response.payload || []);
                    this.toastService.success('', 'Projects Retreived');
                } else {
                    this.toastService.error(response.description, 'Could not retreive projects');
                }
            }),
            catchError((err, caught) => {
                this.loaderService.hide();
                console.log(err);
                return caught;
            })
        );
    }


}
