/**
 * @file footer.component.spec.ts
 * @author Daria Ilchenko
 * @date December 2024
 * @description Unit tests for the FooterComponent in `footer.component.ts`.
 * This file validates that the FooterComponent:
 * - Is created successfully and renders as expected.
 * - Includes functional links for Privacy Policy and Terms of Use with the correct attributes.
 * - Ensures that all footer links have valid `href` attributes.
 * - Adheres to accessibility standards via ARIA labels and descriptive content.
 */

import { ComponentFixture, TestBed } from '@angular/core/testing';
import { FooterComponent } from './footer.component';

describe('FooterComponent', () => {
  let component: FooterComponent;
  let fixture: ComponentFixture<FooterComponent>;
  let compiled: HTMLElement;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FooterComponent], // Import the standalone FooterComponent
    }).compileComponents();

    fixture = TestBed.createComponent(FooterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
    compiled = fixture.nativeElement;
  });

  // Test 1: Component creation
  it('should create the FooterComponent', () => {
    expect(component).toBeTruthy();
  });

  // Test 2: Privacy Policy link existence
  it('should have a Privacy Policy link', () => {
    const privacyLink = compiled.querySelector('a[aria-label="Privacy"]') as HTMLAnchorElement;
    expect(privacyLink).toBeTruthy();
    expect(privacyLink.textContent).toContain('Privacy');
  });

  // Test 3: Privacy Policy link URL
  it('should have the correct URL for Privacy Policy link', () => {
    const privacyLink = compiled.querySelector('a[aria-label="Privacy"]') as HTMLAnchorElement;
    expect(privacyLink.href).toBe('https://www.asu.edu/about/privacy');
  });

  // Test 4: Privacy Policy link opens in a new tab
  it('should open the Privacy Policy link in a new tab', () => {
    const privacyLink = compiled.querySelector('a[aria-label="Privacy"]') as HTMLAnchorElement;
    expect(privacyLink.target).toBe('_blank');
    expect(privacyLink.rel).toContain('noopener noreferrer');
  });

  // Test 5: Terms of Use link existence
  it('should have a Terms of Use link', () => {
    const termsLink = compiled.querySelector('a[aria-label="Terms of Use"]') as HTMLAnchorElement;
    expect(termsLink).toBeTruthy();
    expect(termsLink.textContent).toContain('Terms of Use');
  });

  // Test 6: Terms of Use link URL
  it('should have the correct URL for Terms of Use link', () => {
    const termsLink = compiled.querySelector('a[aria-label="Terms of Use"]') as HTMLAnchorElement;
    expect(termsLink.href).toBe('https://asu.edu/about/terms-of-use');
  });

  // Test 7: Terms of Use link opens in a new tab
  it('should open the Terms of Use link in a new tab', () => {
    const termsLink = compiled.querySelector('a[aria-label="Terms of Use"]') as HTMLAnchorElement;
    expect(termsLink.target).toBe('_blank');
    expect(termsLink.rel).toContain('noopener noreferrer');
  });

  // Test 8: Ensure there are no broken links
  it('should ensure that all footer links have valid href attributes', () => {
    const links = compiled.querySelectorAll('a');
    expect(links.length).toBeGreaterThan(0); // Ensure there are links in the template

    links.forEach((link) => {
      const href = link.getAttribute('href');
      console.log(`Testing link with text: "${link.textContent}" and href: "${href}"`);
      // Fail the test if href is missing or invalid
      expect(href).toBeTruthy();
      expect(href).not.toBe('#');
      expect(href).toMatch(/^(https?:\/\/|mailto:|tel:)/); // Ensure it's a valid URL
    });
  });
});
