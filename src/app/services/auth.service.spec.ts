/**
 * AuthService Unit Test
 * 
 * This test suite verifies the behavior of the AuthService's `fetchUserRole` method.
 * It tests responses for admin, non-admin, unknown users, and handles API errors 
 * using mocked HTTP requests through the HttpClientTestingModule.
 * 
 */


import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { AuthService } from './auth.service';

describe('AuthService', () => {
  let service: AuthService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [AuthService],
    });
    service = TestBed.inject(AuthService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should return true for admin role', () => {
    const userId = 'P001';
    service.fetchUserRole(userId).subscribe((isAdmin) => {
      expect(isAdmin).toBeTrue();
    });

    const req = httpMock.expectOne('app/mocks/user_roles.json');
    expect(req.request.method).toBe('GET');
    req.flush([{ id: 'P001', name: 'John Doe', role: 'admin' }]);
  });

  it('should return false for non-admin role', () => {
    const userId = 'P002';
    service.fetchUserRole(userId).subscribe((isAdmin) => {
      expect(isAdmin).toBeFalse();
    });

    const req = httpMock.expectOne('app/mocks/user_roles.json');
    expect(req.request.method).toBe('GET');
    req.flush([{ id: 'P002', name: 'Jane Smith', role: 'user' }]);
  });

  it('should return false when user is not found', () => {
    const userId = 'P999'; // Non-existent user
    service.fetchUserRole(userId).subscribe((isAdmin) => {
      expect(isAdmin).toBeFalse();
    });

    const req = httpMock.expectOne('app/mocks/user_roles.json');
    expect(req.request.method).toBe('GET');
    req.flush([{ id: 'P001', name: 'John Doe', role: 'admin' }]);
  });

  it('should return false on API error', () => {
    const userId = 'P001';
    service.fetchUserRole(userId).subscribe((isAdmin) => {
      expect(isAdmin).toBeFalse();
    });

    const req = httpMock.expectOne('app/mocks/user_roles.json');
    expect(req.request.method).toBe('GET');
    req.error(new ErrorEvent('Network error'));
  });
});
