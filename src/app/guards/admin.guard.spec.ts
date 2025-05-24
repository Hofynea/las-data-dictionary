/**
 * AdminGuard Unit Test
 * 
 * This spec file tests the AdminGuard, which restricts access to routes
 * based on user role. It mocks the AuthService to simulate different user
 * roles and ensures proper navigation behavior on access denial.
 * 
 */


import { TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { AdminGuard } from './admin.guard';
import { AuthService } from '../services/auth.service';
import { of } from 'rxjs';
import { Router } from '@angular/router';

describe('AdminGuard', () => {
  let guard: AdminGuard;
  let authService: jasmine.SpyObj<AuthService>;
  let router: Router;

  beforeEach(() => {
    const authServiceSpy = jasmine.createSpyObj('AuthService', ['fetchUserRole']);
    TestBed.configureTestingModule({
      imports: [RouterTestingModule],
      providers: [
        AdminGuard,
        { provide: AuthService, useValue: authServiceSpy },
      ],
    });

    guard = TestBed.inject(AdminGuard);
    authService = TestBed.inject(AuthService) as jasmine.SpyObj<AuthService>;
    router = TestBed.inject(Router);
    spyOn(router, 'navigate');
  });

  it('should allow access for admin role', (done) => {
    authService.fetchUserRole.and.returnValue(of(true)); // Simulate admin
    guard.canActivate().subscribe((result) => {
      expect(result).toBeTrue();
      expect(authService.fetchUserRole).toHaveBeenCalledWith('P001');
      done();
    });
  });

  it('should deny access for non-admin role', (done) => {
    authService.fetchUserRole.and.returnValue(of(false)); // Simulate non-admin
    guard.canActivate().subscribe((result) => {
      expect(result).toBeFalse();
      expect(authService.fetchUserRole).toHaveBeenCalledWith('P001');
      expect(router.navigate).toHaveBeenCalledWith(['/forbidden']);
      done();
    });
  });
});
