import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {TableService} from '@services/table.service';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { TableSelectionService } from '@services/table-selection.service';
import { SearchService } from '@services/search.service';
import { ChangeDetectorRef } from '@angular/core';
import { forkJoin } from 'rxjs';
import { FormsModule } from '@angular/forms';
import { SidebarService } from '@services/sidebar.service';

@Component({
  selector: 'app-table',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './table.component.html',
  styleUrl: './table.component.css'
})
export class TableComponent implements OnInit {
  // IMPORTANT TODO:
  // Download Synthetic data method. Currently just downloads some dummy data in CSV format. Will need to be changed to the correct data
  downloadCSV() {
    const csvData = this.generateCSVContent();
    const blob = new Blob([csvData], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.setAttribute('href', url);
    a.setAttribute('download', 'synthetic_data.csv');
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
  }

  generateCSVContent(): string {
    const data = [
      ['ID', 'Name', 'Age'],
      ['1', 'Alice', '25'],
      ['2', 'Bob', '30'],
      ['3', 'Charlie', '28'],
    ];

    return data.map(row => row.join(',')).join('\n');
  }

  // Variable that stores selected from sidebar menu table name
  selectedTable: string = '';
   // Variable that stores all the fetched data from the backend for StudentClass table
  tableEntries: any[] = [];
  // Stores all table entries (to reset when search is cleared)
  allTableEntries: any[] = [];

  // Variables to store table details
  tableName: string = '';
  tableDescription: string = '';
  tableNotes: string = '';
  tableUseCases: string = '';
  tableID: number = 0;
  tableFields: { name: string; description: string}[] = [];
  tableLabels: ({ content: string; labelId: number})[] = [];
  tableEntryContent: ({ entry: string } | null)[] = [];
  tableCategories: ({ content: string; categoryId: number})[] = [];
  selectedCategory: string = '';

  activeField: any = null;

    toggleDescription(field: any) {
      this.activeField = this.activeField === field ? null : field;
    }
  constructor(
    private http: HttpClient,
    private tableService: TableService,
    private tableSelectionService: TableSelectionService,
    private searchService: SearchService, private cdr: ChangeDetectorRef,
    private sidebarService: SidebarService,
  ) {}

  toggleSidebar(): void {
    this.sidebarService.toggleSidebar();
  }

  ngOnInit(): void {
  this.tableSelectionService.selectedTable$.subscribe((tableName) => {
    this.selectedTable = tableName;
    this.fetchTableData(); // Fetch new data when table changes
  });

  // Subscribe to search term changes and filter data dynamically
  this.searchService.searchTerm$.subscribe((term) => {
    this.filterTableData(term);
  });
}
  fetchTableLabels(tabID: number) {
    // Fetch Table labels dynamically
    this.tableService.getTableLabels(tabID).subscribe((data) => {
      this.tableLabels = data.map((item: any) => ({
        content: item.label_name,
        labelId: item.label_id
       }));
    },
  error => {
    console.error('Error', error);
    this.tableLabels = [];
  });
  }

  fetchTableCategories() {
    this.tableService.getTableCategories().subscribe((data) => {
      this.tableCategories = data.map((item: any) => ({
        content: item.category_name,
        categoryId: item.category_id
       }));
      },
      error => {
        console.error('Error', error);
        this.tableCategories = [];
      });
  }

  fetchTableEntries(tabLab: { content: string; labelId: number; }[]) {
    // Create an array of observables for each labelId
    const requests = tabLab.map(label => this.tableService.getTableEntries(label.labelId));

    // forkJoin will wait for all observables to complete and return results in the same order as the requests array
    forkJoin(requests).subscribe((results: any[][]) => {
      // Clear the tableEntryContent array before populating it
      this.tableEntryContent = [];

      // Iterate over the results array, where results[i] corresponds to tabLab[i]
      results.forEach(result => {
        result.forEach((item: any) => {
          this.tableEntryContent.push({ entry: item.entry_content });
        });
      });
    });
  }

  /**
   * Method to fetch data from API endpoint
   */
  fetchTableData(): void {
    // Fetch table headers dynamically
    this.tableService.getTableData().subscribe((data) => {
      const table = data.find(table => table.table_name === this.selectedTable);
      if (table) {
        // Assign table details
        this.allTableEntries = data; // Store full dataset
        this.tableEntries = data; // Initially display all data
        this.tableName = table.table_name;
        this.tableDescription = table.description;
        this.tableNotes = table.important_notes;
        this.tableUseCases = table.use_cases;
        this.tableID = table.table_id;

        // Updates table fields dynamically based on what fields the selected table contains
        if (table.fields) {
          this.tableFields = table.fields.map((item: any) => ({
            name: item.field_name,
            description: item.description

          }));
        }
        this.fetchTableCategories();
        // Fetch table labels, and once labels are loaded, fetch table entries
        this.tableService.getTableLabels(this.tableID).subscribe((labelsData) => {
          this.tableLabels = labelsData.map((item: any) => ({
            content: item.label_name,
            labelId: item.label_id
          }));
          // Now that tableLabels is populated, fetch table entries using these labels
          this.fetchTableEntries(this.tableLabels);
        },
        error => {
          console.error('Error fetching table labels', error);
          this.tableLabels = [];
        });
      }
    });

    /*
    // Fetch Table fields dynamically
    this.tableService.getTableFields().subscribe((data) => {
      this.tableFields = data.map((item: any) => ({ name: item.field_name }));
    });

     */
  }

  filterTableData(term: string): void {
    if (!term.trim() && !this.selectedCategory) {
      this.tableEntries = this.allTableEntries; // Reset to full dataset
      return;
    }

    const lowerCaseTerm = term.toLowerCase();

    this.tableEntries = this.allTableEntries.filter((entry) => {
      const matchesTerm = !term || Object.values(entry).some((value) =>
        String(value).toLowerCase().includes(lowerCaseTerm)
      );

      const matchesCategory = !this.selectedCategory || entry.category === this.selectedCategory;

      return matchesTerm && matchesCategory;
    });
  }

  onCategoryChange(): void {
    if (!this.selectedCategory || this.selectedCategory === '') {
      this.tableEntries = [...this.allTableEntries]; // Reset to all entries if no category is selected
      return;
    }

    this.tableEntries = this.allTableEntries.filter((entry) =>
      Object.keys(entry).some((key) =>
        key === this.selectedCategory
      )
    );
  }
}
