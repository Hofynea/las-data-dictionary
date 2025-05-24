/**
 * HeaderComponent Test
 * 
 * This test suite verifies the proper creation of the HeaderComponent.
 * It uses Angular's TestBed along with HttpClientTestingModule to mock HTTP requests.
 * 
 */


import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeaderComponent } from './header.component';
import { HttpClientTestingModule } from '@angular/common/http/testing'; // Import testing module to mock HttpClient

describe('HeaderComponent', () => {
  let component: HeaderComponent;
  let fixture: ComponentFixture<HeaderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HeaderComponent, HttpClientTestingModule] // Import HttpClientTestingModule to resolve HttpClient dependency in services
    })
    .compileComponents();

    fixture = TestBed.createComponent(HeaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
