import { Injectable, Inject, PLATFORM_ID } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
import { BehaviorSubject } from 'rxjs';

/**
 * Service to store the selected table name so that table component can access it.
 *
 * @author: Zulfina Ivanova
 * Date: 2/26/25
 */
@Injectable({
  providedIn: 'root'
})
export class TableSelectionService {
  private selectedTableSubject = new BehaviorSubject<string>('Student Class'); // Default to Student Class
  selectedTable$ = this.selectedTableSubject.asObservable();

  setSelectedTable(tableName: string): void {
    this.selectedTableSubject.next(tableName);
  }

  getSelectedTable(): string {
    return this.selectedTableSubject.getValue();
  }
}
