/**
 * SearchComponent Unit Test
 * 
 * This test suite verifies the correct initialization and creation of the SearchComponent.
 * It mocks dependencies such as ActivatedRoute and TableSelectionService, and 
 * uses HttpClientTestingModule to simulate API calls without making real HTTP requests.
 * 
 */


import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ActivatedRoute } from '@angular/router';
import { of } from 'rxjs';

import { SearchComponent } from './search.component';
import { TableSelectionService } from '@services/table-selection.service';

describe('SearchComponent', () => {
  let component: SearchComponent;
  let fixture: ComponentFixture<SearchComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [
        SearchComponent,           
        HttpClientTestingModule   
      ],
      providers: [
        {
          provide: ActivatedRoute, 
          useValue: {
            queryParams: of({ q: 'test' }),
            snapshot: {
              queryParamMap: {
                get: () => 'test'
              }
            }
          }
        },
        {
          provide: TableSelectionService, 
          useValue: {}
        }
      ]
    }).compileComponents();

    fixture = TestBed.createComponent(SearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges(); // triggers ngOnInit()
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});