import { Component } from '@angular/core';

@Component({
  selector: 'app-forbidden',
  template: `
    <div>
      <h1>403 - Forbidden</h1>
      <p>You do not have permission to access this page.</p>
    </div>
  `,
})
export class ForbiddenComponent {}
