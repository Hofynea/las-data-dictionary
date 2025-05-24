import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

/**
 * This file is the Angular service used to fetch table data from the backend
 *
 * @author Zulfina Ivanova
 * @date 02/25/25
 */

@Injectable({
  providedIn: 'root'
})
export class TableService {

  // API for fetching table details dynamically
  private tableApiUrl = 'http://127.0.0.1:8000/api/tables/';

  // API for fetching field table details
  private fieldApiUrl = 'http://127.0.0.1:8000/api/fields/';

  // API for fetching label table details
  private labelapiURL = 'http://127.0.0.1:8000/api/labels/';

  private entryapiURL = 'http://127.0.0.1:8000/api/entries/';

  private categoryapiURL = 'http://127.0.0.1:8000/api/categories/';

  constructor(private http: HttpClient) { }

  // Method for fetching table headers dynamically
  getTableData(): Observable<any[]> {
    return this.http.get<any[]>(this.tableApiUrl);
  }

  // Method for fetching table Fields dynamically
  getTableFields(): Observable<any[]> {
    return this.http.get<any[]>(this.fieldApiUrl);
  }

  getTableLabels(id: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.labelapiURL}?table_id=${id}`);
  }

  getTableEntries(id: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.entryapiURL}?label_id=${id}`);
  }

  getTableCategories(): Observable<any[]> {
    return this.http.get<any[]>(this.categoryapiURL)
  }

}
