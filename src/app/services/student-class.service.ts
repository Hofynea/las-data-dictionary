import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';

/**
 * This file is the Angular service used to fetch StudentClass table data from the backend
 *
 * @author Zulfina Ivanova
 * @date 02/01/25
 */


@Injectable({
  providedIn: 'root'
})

export class StudentClassService {
  // Django API endpoint for retrieving StudentClass table data
  private apiUrl = 'http://127.0.0.1:8000/api/studentclasstable/';

  // API for fetching table headers dynamically
  private tableApiUrl = 'http://127.0.0.1:8000/api/tables/';

  constructor(private http: HttpClient) { }

  getStudentClassData(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  // Method for fetching table headers dynamically
  getTableHeaders(): Observable<any[]> {
    return this.http.get<any[]>(this.tableApiUrl);
  }
}
