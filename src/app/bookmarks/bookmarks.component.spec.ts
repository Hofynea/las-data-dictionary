/**
 * Unit Tests for BookmarksComponent
 * 
 * This file contains the test suite for BookmarksComponent, verifying that
 * the component can be properly created and initialized.
 * 
 */

import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BookmarksComponent } from './bookmarks.component';

describe('BookmarksComponent', () => {
  let component: BookmarksComponent;
  let fixture: ComponentFixture<BookmarksComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BookmarksComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BookmarksComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});