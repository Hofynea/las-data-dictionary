/**
 * AuthService
 * 
 * This service handles user role verification by fetching role data from a mock API.
 * It provides methods to determine if a user has administrative privileges and 
 * stores the last retrieved role for quick access.
 * 
 * Uses HttpClient for API calls and includes error handling for network failures.
 */


import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { map, catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private apiUrl = 'app/mocks/user_roles.json';
  private role: string | null = null;

  constructor(private http: HttpClient) {}

  fetchUserRole(userId: string): Observable<boolean> {
  console.log('Fetching role for user:', userId);
  return this.http.get<{ id: string; role: string }[]>(this.apiUrl).pipe(
    map((users) => {
      const user = users.find((u) => u.id === userId);
      console.log('Fetched user role:', user ? user.role : 'No user found');
      this.role = user ? user.role : null;
      return this.role === 'admin';
    }),
    catchError((error) => {
      console.error('Error fetching role:', error);
      this.role = null;
      return of(false);
    })
  );
}
  isAdmin(): boolean {
    return this.role === 'admin';
  }
}
