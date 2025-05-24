import { TestBed } from '@angular/core/testing';
import { HttpClientModule } from '@angular/common/http'; // Import HttpClientModule
import { SearchService } from 'src/app/services/search.service';
import { SearchBarComponent } from './search-bar.component';
import { FormsModule } from '@angular/forms';

describe('SearchBarComponent', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HttpClientModule, FormsModule, SearchBarComponent], // Move SearchBarComponent here
      providers: [SearchService], // Provide the SearchService
    }).compileComponents();
  });

  it('should create', () => {
    const fixture = TestBed.createComponent(SearchBarComponent);
    const component = fixture.componentInstance;
    expect(component).toBeTruthy();
  });

  it('should initialize with an empty search term', () => {
    const fixture = TestBed.createComponent(SearchBarComponent);
    const component = fixture.componentInstance;
    expect(component.searchTerm).toBe(''); // Check if searchTerm is empty
  });

  it('should render the search input field', () => {
    const fixture = TestBed.createComponent(SearchBarComponent);
    fixture.detectChanges();

    const inputElement = fixture.nativeElement.querySelector('input[type="text"]');
    expect(inputElement).toBeTruthy(); // Check if input field exists
  });

  it('should render the search button', () => {
    const fixture = TestBed.createComponent(SearchBarComponent);
    fixture.detectChanges();

    const buttonElement = fixture.nativeElement.querySelector('button[type="submit"]');
    expect(buttonElement).toBeTruthy(); // Check if the search button exists
  });
});
