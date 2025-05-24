/**
 * Unit tests for TableNameService to verify API interactions and error handling.
 * Author: Daria Ilchenko
 * Date: 02/2025
 */ 

import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { TableNameService, TableName } from './table-name.service';

describe('TableNameService - Error Handling Tests', () => {
  let service: TableNameService;
  let httpMock: HttpTestingController;
  const apiUrl = 'http://127.0.0.1:8000/api/table-names/';

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [TableNameService],
    });
    service = TestBed.inject(TableNameService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify(); // Ensures that no unexpected requests were made
  });

  it('should be created', () => {
    expect(service).toBeTruthy(); // Verifies that the service instance is created successfully
  });

  it('should handle 400 Bad Request errors correctly', () => {
    // Simulates an API call with invalid input that triggers a 400 error
    service.createTableName({} as TableName).subscribe(
      () => fail('Expected validation error, but got success response'),
      (error) => {
        expect(error).toContain('Validation Error'); 
      }
    );

    const req = httpMock.expectOne(apiUrl);
    req.flush({ error: 'Invalid input', details: { name: ['This field is required.'] } }, { status: 400, statusText: 'Bad Request' });
  });

  it('should handle 404 Not Found errors correctly', () => {
    // Simulates a request for a non-existent resource, expecting a 404 error
    service.getTableName(9999).subscribe(
      () => fail('Expected 404 error, but got success response'),
      (error) => {
        expect(error).toBe('Requested resource not found.');
      }
    );

    const req = httpMock.expectOne(`${apiUrl}9999/`);
    req.flush({ error: 'Not found' }, { status: 404, statusText: 'Not Found' });
  });

  it('should handle 500 Internal Server Error correctly', () => {
    // Simulates a server error (500) when fetching data
    service.getTableNames().subscribe(
      () => fail('Expected server error, but got success response'),
      (error) => {
        expect(error).toBe('Internal server error. Please try again later.');
      }
    );

    const req = httpMock.expectOne(apiUrl);
    req.flush({ error: 'Server error' }, { status: 500, statusText: 'Internal Server Error' });
  });

  it('should handle network failure correctly', () => {
    // Simulates a network failure and ensures it is properly handled
    service.getTableNames().subscribe(
      () => fail('Expected network error, but got success response'),
      (error) => {
        expect(error).toContain('Client-side error');
      }
    );

    const req = httpMock.expectOne(apiUrl);
    req.error(new ErrorEvent('Network error'));
  });
});
