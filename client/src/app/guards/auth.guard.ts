import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import { AuthenticationService } from '../services/authentication.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  isUserLoggedIn = false;

  constructor(
    private authService: AuthenticationService,
    private router: Router
  ) { }

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {

    if (this.isUserLoggedIn) {
      console.log('user logged in');

      return true;
    }

    console.log('user not logged in, checking cookies');

    return this.authService.checkAuthenticated()
      .pipe(tap((authenticated) => {
        console.log('Checked cookies, authenticated: ', authenticated);
        this.isUserLoggedIn = authenticated;
      }));
  }
}
