/**
 * UserDisplayComponent
 * 
 * This Angular component displays a table of user data retrieved from the backend
 * via the UserService. It dynamically renders user attributes including ID, name, 
 * age, gender, ethnicity, and marital status.
 * 
 * Utilizes Angular's OnInit lifecycle hook to fetch data on component initialization.
 * Includes a fallback template to display a loading message while data is being fetched.
 */


import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-user-display',
  template: `
    <div>
      <h2>User Data</h2>
      <table *ngIf="users.length > 0; else loading">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Age</th>
            <th>Gender</th>
            <th>Ethnicity</th>
            <th>Marital Status</th>
          </tr>
        </thead>
        <tbody>
          <tr *ngFor="let user of users">
            <td>{{ user.id }}</td>
            <td>{{ user.name }}</td>
            <td>{{ user.age }}</td>
            <td>{{ user.gender }}</td>
            <td>{{ user.ethnicity }}</td>
            <td>{{ user.marital_status }}</td>
          </tr>
        </tbody>
      </table>
      <ng-template #loading>
        <p>Loading data...</p>
      </ng-template>
    </div>
  `,
})
export class UserDisplayComponent implements OnInit {
  users: any[] = [];

  constructor(private userService: UserService) {}

  ngOnInit(): void {
  console.log('Initializing UserDisplayComponent...');
  this.userService.getUsers().subscribe(
  (data: any[]) => {
    console.log('Data received from API:', data);
    this.users = data;
  },
  (error: any) => {
    console.error('Error during API call:', error);
  }
);

}
}
