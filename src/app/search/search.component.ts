/**
 * SearchComponent
 * 
 * This component handles search functionality based on query parameters.
 * It interacts with a backend API to retrieve and display search results,
 * highlights matches, and integrates with the TableSelectionService for table interactions.
 * 
 */


import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { TableSelectionService } from '@services/table-selection.service';
import { CommonModule } from '@angular/common';
import { TableComponent } from '../table/table.component';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';

const API_BASE_URL = 'http://127.0.0.1:8000/api';

@Component({
  selector: 'app-search',
  standalone: true,
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css'],
  imports: [CommonModule, TableComponent]
})
export class SearchComponent implements OnInit {
  query = '';
  loading = false;
  error: string | null = null;
  searchResults: any[] = [];

  constructor(
    private route: ActivatedRoute,
    private http: HttpClient,
    private tableSelectionService: TableSelectionService,
    private sanitizer: DomSanitizer
  ) {}

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      this.query = params['q'] || '';
      if (this.query) {
        this.search();
      }
    });
  }

  search(): void {
    this.loading = true;
    this.error = null;

    this.http
      .get<any[]>(`${API_BASE_URL}/friendly-name-search/?query=${encodeURIComponent(this.query)}`)
      .subscribe({
        next: data => {
          this.searchResults = data;
          this.loading = false;
        },
        error: err => {
          this.error = 'Error loading search results.';
          this.loading = false;
        }
      });
  }

  highlightMatch(text: string): SafeHtml {
    if (!text || !this.query) return text;

    const escapedQuery = this.query.replace(/[-[\]/{}()*+?.\\^$|]/g, '\\$&');
    const regex = new RegExp(`\\b(${escapedQuery})\\b`, 'gi');
    const highlighted = text.replace(regex, `<span style="background-color: #FFC627;">$1</span>`);

    return this.sanitizer.bypassSecurityTrustHtml(highlighted);
  }
}
