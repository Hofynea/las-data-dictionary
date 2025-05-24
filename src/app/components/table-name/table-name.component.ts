/** Manages the retrieval, creation, and deletion of the table names using TableNameService.
 * Author: Daria Ilchenko
 * Date: 02/2025
 */

import { Component, OnInit } from '@angular/core';
import { TableNameService, TableName } from '../../services/table-name.service';

@Component({
  selector: 'app-components-table-name', // Component selector
  templateUrl: './table-name.component.html', // HTML template
  styleUrls: ['./table-name.component.css'] // CSS styles
})
export class TableNameComponent implements OnInit {
  tableNames: TableName[] = []; // Stores fetched table names
  errorMessage: string = ''; // Holds error messages

  constructor(private tableNameService: TableNameService) {} // Inject TableNameService

  ngOnInit(): void {
    this.fetchTableNames(); // Fetch table names on component initialization
  }

  /** Fetch table names from the API */
  fetchTableNames(): void {
    this.errorMessage = ''; // Clear previous errors
    this.tableNameService.getTableNames().subscribe(
      (data) => {
        this.tableNames = data; // Update table list
      },
      (error) => {
        this.handleError(error);
      }
    );
  }

  /** Create a new table entry */
  addTableName(): void {
    this.errorMessage = ''; // Clear previous errors
    const newTable: TableName = { name: 'New Table', description: 'New table description' };
    
    this.tableNameService.createTableName(newTable).subscribe(
      (data) => {
        this.tableNames.push(data); // Add new table to the list
      },
      (error) => {
        this.handleError(error);
      }
    );
  }

  /** Delete a table entry */
  removeTable(id: number): void {
    this.errorMessage = ''; // Clear previous errors
    this.tableNameService.deleteTableName(id).subscribe(
      () => {
        this.tableNames = this.tableNames.filter(t => t.id !== id); // Remove deleted table from list
      },
      (error) => {
        this.handleError(error);
      }
    );
  }

  /** Handles API errors and logs them */
  private handleError(error: string): void {
    this.errorMessage = error; // Display error message in UI
    console.error('Component Error:', error); // Log error for debugging
  }
}
