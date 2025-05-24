import { ComponentFixture, TestBed } from '@angular/core/testing';
import { StudentClassComponent } from './student-class.component';
import { ActivatedRoute } from '@angular/router';
import { StudentClassService} from '@services/student-class.service';
import { of } from 'rxjs';
import {provideHttpClient} from '@angular/common/http'; // For mocking Observables

describe('StudentClassComponent', () => {
  let component: StudentClassComponent;
  let fixture: ComponentFixture<StudentClassComponent>;
  let studentClassService: StudentClassService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [StudentClassComponent],

      providers: [
        provideHttpClient(),
        StudentClassService,
        {
          provide: ActivatedRoute,
          useValue: {
            // Mocked params observable
            snapshot: {paramMap: {get: (key: string) => '1'}}
          },
        },
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(StudentClassComponent);
    component = fixture.componentInstance;
    studentClassService = TestBed.inject(StudentClassService);
  });

  it('should fetch student class table data and display the "name" column', () => {
    const mockData = [
      { name: 'student_id', label: 'stdnt_id', friendly_name: 'Student Identifier', category: 'Student & Class Info', description: 'Unique identifier for each student', source: 'SIS', type: 'Integer', dataset_name: 'Student Details' },
      { name: 'class_id', label: 'cls_id', friendly_name: 'Class Section ID', category: 'Student & Class Info', description: 'Identifier for each class section', source: 'SIS', type: 'Integer', dataset_name: 'Student Details'}
    ];
    spyOn(studentClassService, 'getStudentClassData').and.returnValue(of(mockData));
    fixture.detectChanges();

    const compiled = fixture.nativeElement;
    const tableRows = compiled.querySelectorAll('tbody tr');

    // Ensure two rows are displayed
    expect(tableRows.length).toBe(2);

    const firstRowName = tableRows[0].querySelectorAll('td')[5].textContent.trim();
    const secondRowName = tableRows[1].querySelectorAll('td')[5].textContent.trim();
    expect(firstRowName).toBe('student_id');
    expect(secondRowName).toBe('class_id');
  });

  it('should fetch student class table data and display the "label" column', () => {
    const mockData = [
      { name: 'student_id', label: 'stdnt_id', friendly_name: 'Student Identifier', category: 'Student & Class Info', description: 'Unique identifier for each student', source: 'SIS', type: 'Integer', dataset_name: 'Student Details' },
      { name: 'class_id', label: 'cls_id', friendly_name: 'Class Section ID', category: 'Student & Class Info', description: 'Identifier for each class section', source: 'SIS', type: 'Integer', dataset_name: 'Student Details'}
    ];
    spyOn(studentClassService, 'getStudentClassData').and.returnValue(of(mockData));
    fixture.detectChanges();

    const compiled = fixture.nativeElement;
    const tableRows = compiled.querySelectorAll('tbody tr');

    // Ensure two rows are displayed
    expect(tableRows.length).toBe(2);

    const firstRowName = tableRows[0].querySelectorAll('td')[0].textContent.trim();
    const secondRowName = tableRows[1].querySelectorAll('td')[0].textContent.trim();
    expect(firstRowName).toBe('stdnt_id');
    expect(secondRowName).toBe('cls_id');
  });

  it('should fetch student class table data and display the "category" column', () => {
    const mockData = [
      { name: 'student_id', label: 'stdnt_id', friendly_name: 'Student Identifier', category: 'Student & Class Info', description: 'Unique identifier for each student', source: 'SIS', type: 'Integer', dataset_name: 'Student Details' },
      { name: 'class_id', label: 'cls_id', friendly_name: 'Class Section ID', category: 'Student & Class Info', description: 'Identifier for each class section', source: 'SIS', type: 'Integer', dataset_name: 'Student Details'}
    ];
    spyOn(studentClassService, 'getStudentClassData').and.returnValue(of(mockData));
    fixture.detectChanges();

    const compiled = fixture.nativeElement;
    const tableRows = compiled.querySelectorAll('tbody tr');

    // Ensure two rows are displayed
    expect(tableRows.length).toBe(2);

    const firstRowName = tableRows[0].querySelectorAll('td')[3].textContent.trim();
    const secondRowName = tableRows[1].querySelectorAll('td')[3].textContent.trim();
    expect(firstRowName).toBe('Student & Class Info');
    expect(secondRowName).toBe('Student & Class Info');
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should fetch and display the table name, description, notes, use cases dynamically', () => {
    const mockData = [
      {
        table_id: 3,
        table_name: 'Student Class',
        description: 'This table is one row per student and class combination. Students earn grades in their classes so this table would have grade outcome details included.',
        important_notes: 'The granularity of the data is one row per student (stdnt_id) and class (cls_id).',
        use_cases: 'Class Attributes',
        fields: []
      }
    ];

    spyOn(studentClassService, 'getTableHeaders').and.returnValue(of(mockData));
    fixture.detectChanges();

    const compiled = fixture.nativeElement;

    expect(compiled.querySelector('.table-title').textContent.trim()).toBe('Student Class');
    expect(compiled.querySelector('.table-description').textContent.trim()).toBe('This table is one row per student and class combination. Students earn grades in their classes so this table would have grade outcome details included.');
    expect(compiled.querySelector('.table-note').textContent.trim()).toContain('The granularity of the data is one row per student (stdnt_id) and class (cls_id).');
    expect(compiled.querySelector('.table-usecases').textContent.trim()).toContain('Class Attributes');
  });

});
