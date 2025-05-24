/**
 * SearchService
 * 
 * This service manages real-time search term input and provides autocomplete suggestions 
 * using a custom backend API for friendly names. It leverages RxJS to debounce and process 
 * search input efficiently, minimizing redundant API calls.
 * 
 * It maintains observable streams for the current search term, search suggestions, 
 * and loading status, making it easy for components to react to updates.
 * 
 * Uses HttpClient for backend communication and includes basic error handling 
 * to fallback to an empty result set on failure.
 */


import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { debounceTime, distinctUntilChanged, tap, switchMap, map, catchError } from 'rxjs/operators';
import { ACADEMIC_WORDS } from '../data/academic-words'; 

// Search only usin friendly name
@Injectable({
  providedIn: 'root',
})
export class SearchService {
  private searchTermSubject = new BehaviorSubject<string>('');
  searchTerm$: Observable<string> = this.searchTermSubject.asObservable();

  private searchSuggestionsSubject = new BehaviorSubject<string[]>([]);
  searchSuggestions$: Observable<string[]> = this.searchSuggestionsSubject.asObservable();

  private isLoadingSubject = new BehaviorSubject<boolean>(false);
  isLoading$ = this.isLoadingSubject.asObservable();

  private API_URL = 'https://api.datamuse.com/sug?s='; // API for word suggestions

  constructor(private http: HttpClient) {
    this.searchTerm$
      .pipe(
        debounceTime(300),
        distinctUntilChanged(),
        tap(() => this.isLoadingSubject.next(true)),
        switchMap(term => this.getFilteredSuggestions(term))
      )
      .subscribe(suggestions => {
        this.isLoadingSubject.next(false);
        this.searchSuggestionsSubject.next(suggestions);
      });
  }

  /** Update search term and trigger autocomplete */

  setSearchTerm(term: string): void {
    this.searchTermSubject.next(term);
  }

  /** Fetch filtered suggestions (local dictionary + API) */
  private getFilteredSuggestions(term: string): Observable<string[]> {
    if (!term.trim()) {
      return new BehaviorSubject<string[]>([]);
    }

    const apiUrl = `http://127.0.0.1:8000/api/friendly-name-autofill/?query=${encodeURIComponent(term)}`;

    return this.http.get<string[]>(apiUrl).pipe(
      catchError(() => new BehaviorSubject<string[]>([])) // fallback empty list
    );
  }


  /** Get the current search term */
  getSearchTerm(): string {
    return this.searchTermSubject.value;
  }
}
