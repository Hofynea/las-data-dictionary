/**
 * AdminDashboardComponent
 * 
 * This component serves as the main dashboard for administrators.
 * It provides a simple welcome interface for admin users accessing the admin section.
 * 
 */

import { Component } from '@angular/core';

@Component({
  selector: 'app-admin-dashboard',
  standalone: true,
  template: `
    <div>
      <h1>Admin Dashboard</h1>
      <p>Welcome to the Admin Dashboard.</p>
    </div>
  `,
})
export class AdminDashboardComponent {}
