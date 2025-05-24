/**
 * AdminGuard
 * 
 * This route guard prevents unauthorized users from accessing admin-specific routes.
 * It uses AuthService to verify the user's role and redirects non-admin users
 * to the forbidden page if access is denied.
 * 
 */


import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class AdminGuard implements CanActivate {
  constructor(private authService: AuthService, private router: Router) {}

  canActivate(): Observable<boolean> {
    const userId = 'P001';
    return this.authService.fetchUserRole(userId).pipe(
      tap((isAdmin) => {
        if (!isAdmin) {
          this.router.navigate(['/forbidden']);
        }
      })
    );
  }
}
