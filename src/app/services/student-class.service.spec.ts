/**
 * StudentClassService Unit Tests
 * 
 * This test suite verifies the creation and basic functionality of the StudentClassService.
 * It ensures the service is properly instantiated within the Angular testing module 
 * using TestBed and the HttpClient provider.
 * 
 * Includes a basic sanity check to confirm the service initializes successfully.
 */


import { TestBed } from '@angular/core/testing';
import { StudentClassService } from './student-class.service';
import { provideHttpClient } from '@angular/common/http';

describe('StudentClassService', () => {
  let service: StudentClassService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        StudentClassService,
        provideHttpClient(),
      ]
    });
    service = TestBed.inject(StudentClassService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
