import { StudentClassComponent } from './student-class.component';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ActivatedRoute } from '@angular/router';

describe('StudentClassComponent - Sorting', () => {
  let component: StudentClassComponent;
  let fixture: ComponentFixture<StudentClassComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HttpClientTestingModule, StudentClassComponent],
      providers: [
        {
          provide: ActivatedRoute,
          useValue: {
            snapshot: { paramMap: { get: (key: string) => '1' } },
          },
        },
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(StudentClassComponent);
    component = fixture.componentInstance;

    // Mock initial rows for testing
    component.emptyRows = [
      { Label: 'C', FriendlyName: 'Alice' },
      { Label: 'A', FriendlyName: 'Bob' },
      { Label: 'B', FriendlyName: 'Charlie' },
    ];

    fixture.detectChanges();
  });

  it('should sort rows in ascending order when the column is clicked', () => {
    // Sort by "Label" (ascending)
    component.sortTable('Label');
    expect(component.emptyRows).toEqual([
      { Label: 'A', FriendlyName: 'Bob' },
      { Label: 'B', FriendlyName: 'Charlie' },
      { Label: 'C', FriendlyName: 'Alice' },
    ]);

    // Sort by "Label" (descending)
    component.sortTable('Label');
    expect(component.emptyRows).toEqual([
      { Label: 'C', FriendlyName: 'Alice' },
      { Label: 'B', FriendlyName: 'Charlie' },
      { Label: 'A', FriendlyName: 'Bob' },
    ]);
  });
  it('should reset sorting when a different column is clicked', () => {
    component.emptyRows = [
      { Label: 'C', FriendlyName: 'Charlie' },
      { Label: 'A', FriendlyName: 'Alice' },
      { Label: 'B', FriendlyName: 'Bob' },
    ];

    // Sort by "Label" (ascending)
    component.sortTable('Label');
    expect(component.emptyRows).toEqual([
      { Label: 'A', FriendlyName: 'Alice' },
      { Label: 'B', FriendlyName: 'Bob' },
      { Label: 'C', FriendlyName: 'Charlie' },
    ]);

    // Switch to sort by "FriendlyName"
    component.sortTable('FriendlyName');
    expect(component.emptyRows).toEqual([
      { Label: 'A', FriendlyName: 'Alice' },
      { Label: 'B', FriendlyName: 'Bob' },
      { Label: 'C', FriendlyName: 'Charlie' },
    ]);
  });
});
