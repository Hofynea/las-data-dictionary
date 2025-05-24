/**
 * Service to handle CRUD operations for TableName using Angular HttpClient.
 * Author: Daria Ilchenko
 * Date: 02/2025
 */

import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

// TableName model representing API dat astructure
export interface TableName {
  id?: number;
  name: string;
  description?: string;
  created_at?: string;
  updated_at?: string;
}

@Injectable({
  providedIn: 'root',
})
export class TableNameService {
  private apiUrl = 'http://127.0.0.1:8000/api/table-names/'; // API endpoint

  constructor(private http: HttpClient) {}

  /** Fetch all table names from the API */
  getTableNames(): Observable<TableName[]> {
    return this.http.get<TableName[]>(this.apiUrl).pipe(
      catchError(this.handleError)
    );
  }

  /** Fetch a specific table entry by ID */
  getTableName(id: number): Observable<TableName> {
    return this.http.get<TableName>(`${this.apiUrl}${id}/`).pipe(
      catchError(this.handleError)
    );
  }

  /** Create a new table entry */
  createTableName(table: TableName): Observable<TableName> {
    return this.http.post<TableName>(this.apiUrl, table).pipe(
      catchError(this.handleError)
    );
  }

  /** Update an existing table entry */
  updateTableName(id: number, table: TableName): Observable<TableName> {
    return this.http.patch<TableName>(`${this.apiUrl}${id}/`, table).pipe(
      catchError(this.handleError)
    );
  }

  /** Delete a table entry */
  deleteTableName(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}${id}/`).pipe(
      catchError(this.handleError)
    );
  }

  /** Generic error handler for API requests */
  private handleError(error: HttpErrorResponse) {
    let errorMsg = 'An unknown error occurred!';
    
    // ErrorEvent is correctly checked
    if (error.error instanceof ErrorEvent || (typeof ErrorEvent !== 'undefined' && error.error instanceof Error)) {
      // Handles client-side or network errors
      errorMsg = `Client-side error: ${error.error.message}`;
    } else {
      // Handles server-side errors
      switch (error.status) {
        case 400:
          errorMsg = error.error.details 
            ? `Validation Error: ${JSON.stringify(error.error.details)}`
            : 'Invalid request. Please check your input.';
          break;
        case 404:
          errorMsg = 'Requested resource not found.';
          break;
        case 500:
          errorMsg = 'Internal server error. Please try again later.';
          break;
        default:
          errorMsg = `Server error ${error.status}: ${error.message}`;
      }
    }
    
    console.error('API Error:', errorMsg);
    return throwError(errorMsg); // Throws error to be handled in components
  }
}
