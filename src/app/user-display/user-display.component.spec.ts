/**
 * UserDisplayComponent Unit Tests
 * 
 * This test suite validates the successful creation of the UserDisplayComponent.
 * It sets up the Angular testing environment using TestBed and includes the 
 * HttpClientTestingModule to mock HTTP requests.
 * 
 * Contains a basic test to confirm the component is instantiated without errors.
 */


import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { UserDisplayComponent } from './user-display.component';

describe('UserDisplayComponent', () => {
  let component: UserDisplayComponent;
  let fixture: ComponentFixture<UserDisplayComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      declarations: [UserDisplayComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(UserDisplayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
