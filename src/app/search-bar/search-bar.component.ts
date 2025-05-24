import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { SearchService } from 'src/app/services/search.service';

@Component({
  selector: 'app-search-bar',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent {
  searchTerm: string = '';
  searchSuggestions: string[] = [];
  isLoading: boolean = false;

  constructor(
    private searchService: SearchService,
    private router: Router
  ) {
    this.searchService.searchSuggestions$.subscribe(suggestions => {
      this.searchSuggestions = suggestions;
    });

    this.searchService.isLoading$.subscribe(loading => {
      this.isLoading = loading;
    });
  }

  /** Trigger search and navigate */
  onSearch(event?: Event): void {
    if (event) event.preventDefault(); // prevent form reload
    const trimmed = this.searchTerm.trim();
    if (!trimmed) return;
    this.searchService.setSearchTerm(trimmed);
    this.router.navigate(['/search'], { queryParams: { q: trimmed } });
  }

  onInputChange(term: string): void {
    this.searchService.setSearchTerm(term);
  }

  /** Select from suggestions */
  selectSuggestion(suggestion: string): void {
    this.searchTerm = suggestion;
    this.onSearch();
  }
}
