/**
 * SidebarComponent
 * 
 * This standalone Angular component displays a dynamic list of database tables 
 * in a sidebar layout. It fetches table data from the backend using TableService 
 * and allows users to select a table for navigation and interaction.
 * 
 * It communicates the selected table to other components via TableSelectionService 
 * and ensures all table items navigate to a common route (`/table`).
 * 
 * Implements Angular's OnInit lifecycle to initiate data fetching upon load.
 */


import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { TableSelectionService } from '@services/table-selection.service'
import {TableService} from '@services/table.service';

@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {
  tables: any[] = [];
  selectedTable: string = '';

  constructor(private http: HttpClient, private tableSelectionService: TableSelectionService, private tableService: TableService) {}


  ngOnInit(): void {
    this.tableService.getTableData().subscribe({
      next: (data) => {

        // Store tables dynamically
        this.tables = data.map(table => ({
          table_id: table.table_id,
          table_name: table.table_name,
          route: "/table"  // Ensure all tables navigate to /table
        }));
      },
      error: (err) => {
        console.error('Error fetching tables:', err);
      }
    });
  }

  selectTable(tableName: string): void {
    this.selectedTable = tableName;
    this.tableSelectionService.setSelectedTable(tableName);
  }
}
