import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
//import { CommonModule } from '@angular/common';
import { SharedModule } from '../shared/shared/shared.module';
import { StudentClassService } from '@services/student-class.service'
import { forkJoin } from 'rxjs';

@Component({
  selector: 'app-student-class',
  standalone: true,
  imports: [SharedModule],
  templateUrl: './student-class.component.html',
  styleUrl: './student-class.component.css',
})

export class StudentClassComponent implements OnInit {
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
   // Variable that stores all the fetched data from the backend for StudentClass table
  studentClasses: any[] = [];

  // Variables to store table details
  tableName: string = '';
  tableDescription: string = '';
  tableNotes: string = '';
  tableUseCases: string = '';

  tableHeaders: { name: string; tooltipContent: string }[] = [];
  emptyRows = Array(50).fill({
    Label: 'Student & Class Info',
    FriendlyName: 'Example',
    Description: 'Example',
    Category: 'Example',
    Source: 'Example',
    Name: 'Example',
    DatasetName: 'Example',
  });
  sortedRows = [...this.emptyRows];
  sortColumn: string = '';
  sortDirection: 'asc' | 'desc' = 'asc';

  constructor(private http: HttpClient, private studentClassService: StudentClassService) {}

  ngOnInit(): void {
     // Fetch Student Class Data from API endpoint
    this.studentClassService.getStudentClassData().subscribe((data) => {
      // console.log('API Response:', data);  // Debugging log
      this.studentClasses = data;
    });

    // Fetch table headers dynamically
    this.studentClassService.getTableHeaders().subscribe((data) => {
      const studentClassTable = data.find(table => table.table_name === 'Student Class');

      // Assigning table details
      this.tableName = studentClassTable.table_name;
      this.tableDescription = studentClassTable.description;
      this.tableNotes = studentClassTable.important_notes;
      this.tableUseCases = studentClassTable.use_cases;

      if (studentClassTable) {
        this.tableHeaders = studentClassTable.fields.map((field: { field_name: string; description: string; }) => ({
        name: field.field_name,
        tooltipContent: field.description || '',
        }));
      }
      // console.log('API Response:', this.tableHeaders);  // Debugging log
    });


  }

  sortTable(column: string): void {
  if (this.sortColumn === column) {
    this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
  } else {
    this.sortColumn = column;
    this.sortDirection = 'asc';
  }

  // Sort rows based on the selected column and direction
  this.emptyRows = [...this.emptyRows].sort((a, b) => {
    const valueA = a[column] || ''; // Replace null/undefined with empty string
    const valueB = b[column] || ''; // Replace null/undefined with empty string

    if (valueA === null || valueA === undefined) return 1; // Push null/undefined to the end
    if (valueB === null || valueB === undefined) return -1; // Push null/undefined to the end

    if (this.sortDirection === 'asc') {
      return valueA.localeCompare(valueB); // Use localeCompare for proper string comparison
    } else {
      return valueB.localeCompare(valueA); // Reverse comparison for descending order
    }
  });
}
}
