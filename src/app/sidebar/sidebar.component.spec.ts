import { ComponentFixture, TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { provideHttpClient } from '@angular/common/http';
import { SidebarComponent } from './sidebar.component';
import { TableService } from '@services/table.service';
import { TableSelectionService } from '@services/table-selection.service';
import { of, throwError } from 'rxjs';

describe('SidebarComponent', () => {
  let component: SidebarComponent;
  let fixture: ComponentFixture<SidebarComponent>;
  let tableService: TableService;
  let tableSelectionService: TableSelectionService;

  const mockTables = [
    { table_id: 1, table_name: 'Person Demographics' },
    { table_id: 2, table_name: 'Student Term' },
  ];

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [
        RouterTestingModule.withRoutes([]),
        SidebarComponent,
      ],
      providers: [
        provideHttpClient(),
        TableService,
        TableSelectionService,
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(SidebarComponent);
    component = fixture.componentInstance;
    tableService = TestBed.inject(TableService);
    tableSelectionService = TestBed.inject(TableSelectionService);
  });

  it('should create the SidebarComponent', () => {
    expect(component).toBeTruthy();
  });


  it('should fetch and display tables synamically', () => {
    // Mocking API response
    spyOn(tableService, 'getTableData').and.returnValue(of(mockTables));

    fixture.detectChanges();

    expect(component.tables.length).toBe(2);
    expect(component.tables[0].table_name).toBe('Person Demographics');
    expect(component.tables[1].table_name).toBe('Student Term');
  });

  it('should update selected table when a table is clicked', () => {
    component.selectTable('Student Term');
    expect(component.selectedTable).toBe('Student Term');
  });

  it('should handle empty API response', () => {
    spyOn(tableService, 'getTableData').and.returnValue(of([]));

    fixture.detectChanges();

    expect(component.tables.length).toBe(0);
  });

  /////////////////////////////////////////////////
  // Adding new test cases for testing dynamic sidebar and table switching
  // Date: 03/27/25
  /////////////////////////////////////////////////

  // Verifies that selectedTable stays empty until changed.
  it('should not overwrite selectedTable if selectTable is never called', () => {
    expect(component.selectedTable).toBe('');
  });

  // Verifies that .route and table_id are correctly mapped in the tables array.
  it('should map fetched data correctly to internal format', () => {
    spyOn(tableService, 'getTableData').and.returnValue(of(mockTables));
    fixture.detectChanges();

    expect(component.tables[0].route).toBe('/table');
    expect(component.tables[1].table_id).toBe(2);
  });

  // Confirms that TableSelectionService is actually triggered on table selection
  it('should call tableSelectionService.setSelectedTable() when selectTable is called', () => {
    const serviceSpy = spyOn(tableSelectionService, 'setSelectedTable');
    component.selectTable('Student Term');
    expect(serviceSpy).toHaveBeenCalledWith('Student Term');
  });

  // Handles API failure using throwError and verifies with console.error spy.
  it('should show error in console if API call fails', () => {
    const consoleSpy = spyOn(console, 'error');
    spyOn(tableService, 'getTableData').and.returnValue(throwError(() => new Error('API Failed')));

    fixture.detectChanges();

    expect(consoleSpy).toHaveBeenCalledWith('Error fetching tables:', jasmine.any(Error));
    expect(component.tables.length).toBe(0);
  });

  // Ensures ngOnInit() calls getTableData().
  it('should initialize table list in ngOnInit()', () => {
    const getTableSpy = spyOn(tableService, 'getTableData').and.returnValue(of(mockTables));
    component.ngOnInit();
    expect(getTableSpy).toHaveBeenCalled();
  });

  // Ensures multiple selections are handled correctly.
  it('should allow clicking different tables without error', () => {
    spyOn(tableService, 'getTableData').and.returnValue(of(mockTables));
    fixture.detectChanges();

    component.selectTable('Person Demographics');
    expect(component.selectedTable).toBe('Person Demographics');

    component.selectTable('Student Term');
    expect(component.selectedTable).toBe('Student Term');
  });

  // Verifies that sidebar renders the correct number of table links
  it('should render table links dynamically', () => {
    spyOn(tableService, 'getTableData').and.returnValue(of(mockTables));
    fixture.detectChanges();

    const links = fixture.nativeElement.querySelectorAll('.nav-link-container a');
    expect(links.length).toBe(3); // 2 tables + 1 Overview link
    expect(links[1].textContent.trim()).toBe('Person Demographics');
    expect(links[2].textContent.trim()).toBe('Student Term');
  });

  // Ensures that the overview link is always present
  it('should always display Learning@Scale Overview link', () => {
    fixture.detectChanges();

    const overviewLink = fixture.nativeElement.querySelector('.nav-link[routerLink="/"]');
    expect(overviewLink).toBeTruthy();
    expect(overviewLink.textContent.trim()).toBe('Learning@Scale Overview');
  });

  // Ensures sidebar remains collapsed when initialized
  it('should have sidebar collapsed by default', () => {
    const sidebar = fixture.nativeElement.querySelector('#sidebar-left');
    expect(sidebar.classList.contains('collapse')).toBeTrue();
  });

});
