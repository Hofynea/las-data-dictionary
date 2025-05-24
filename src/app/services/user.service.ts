import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  private apiUrl = 'app/mocks/person_demographics.json';

  constructor(private http: HttpClient) {}

  // Fetch all users
  getUsers(): Observable<any[]> {
  console.log('API call initiated to:', this.apiUrl);
  return this.http.get<any[]>(this.apiUrl);
}
}
