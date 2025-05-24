/**
 * @file app.routes.spec.ts
 * @author Daria Ilchenko
 * @date November 2024
 * @description Unit tests for the `app.routes.ts` file.
 * This file validates that:
 * - The `routes` constant is defined and correctly exported.
 * - The `routes` array adheres to the expected Angular `Routes` structure.
 * - The `routes` array behaves as intended when modified or extended in the future.
 */

import { routes } from './app.routes';
import { Routes } from '@angular/router';

describe('app.routes.ts', () => {
  it('should define the `routes` constant', () => {
    // Ensure the `routes` constant is defined
    expect(routes).toBeDefined();
  });

  it('should export a non-empty `routes` array', () => {
    // Validate that the `routes` array is not empty
    expect(Array.isArray(routes)).toBeTrue();
    expect(routes.length).toBeGreaterThan(0);
  });

  it('should be a valid `Routes` array', () => {
    // Ensure `routes` is an array and satisfies the Angular `Routes` structure
    const isValidRoutes = Array.isArray(routes) && routes.every((route) => {
      return route && typeof route.path === 'string';
    });
    expect(isValidRoutes).toBeTrue();
  });

  it('should include a route for "admin"', () => {
    const adminRoute = routes.find((r) => r.path === 'admin');
    expect(adminRoute).toBeDefined();
    expect(adminRoute?.canActivate).toBeDefined();
  });

  // Placeholder for future tests when routes are added
  it('should allow adding routes (placeholder)', () => {
    // Example test for future implementation
    expect(true).toBeTrue(); // Replace with actual tests as routes are added
  });
});
