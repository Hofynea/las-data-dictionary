import { ComponentFixture, TestBed } from '@angular/core/testing';
import { provideHttpClient } from '@angular/common/http';
import { TableComponent } from './table.component';
import { TableService } from '@services/table.service';
import { of, throwError } from 'rxjs';

describe('TableComponent', () => {
  let component: TableComponent;
  let fixture: ComponentFixture<TableComponent>;
  let tableService: TableService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TableComponent],
      providers: [provideHttpClient(), TableService],
    })
    .compileComponents();

    fixture = TestBed.createComponent(TableComponent);
    component = fixture.componentInstance;
    tableService = TestBed.inject(TableService);
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  /** Testing to ensure empty API response results in an empty table */
  it('should handle empty API response for table fields', () => {
    spyOn(tableService, 'getTableFields').and.returnValue(of([]));

    fixture.detectChanges();

    expect(component.tableFields.length).toBe(0);
  });

  it('should have an empty selectedCategory by default', () => {
    expect(component.selectedCategory).toBe(''); // Simple test for default state
  });


  it('should not show any tooltip initially', () => {
    component.tableFields = [
      { name: 'Label', description: 'Field 1 description' },
      { name: 'Friendly Name', description: 'Field 2 description' }
    ];
    fixture.detectChanges();
    expect(component.activeField).toBeNull();
  });

  it('should show tooltip when info icon is clicked', () => {
    const field = { name: 'Label', description: 'Label description' };
    component.tableFields = [field];
    component.toggleDescription(field);
    expect(component.activeField).toBe(field);
  });

  it('should hide tooltip when the same field is clicked again', () => {
    const field = { name: 'Label', description: 'Label description' };
    component.tableFields = [field];

    // First click: open
    component.toggleDescription(field);
    expect(component.activeField).toBe(field);

    // Second click: close
    component.toggleDescription(field);
    expect(component.activeField).toBeNull();
  });

  it('should switch tooltip to another field on click', () => {
    const field1 = { name: 'Label', description: 'Label description' };
    const field2 = { name: 'Category', description: 'Category description' };
    component.tableFields = [field1, field2];

    // Click first field
    component.toggleDescription(field1);
    expect(component.activeField).toBe(field1);

    // Click second field
    component.toggleDescription(field2);
    expect(component.activeField).toBe(field2);
  });

});

