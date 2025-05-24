/**
* UserComponent
* 
* This component manages the display of user information.
* It fetches user data from the UserService upon initialization
* and makes it available for display in the template.
* 
*/

import { Component, OnInit } from '@angular/core';
import { UserService } from '@services/user.service';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css'],
})
export class UserComponent implements OnInit {
  users: any[] = [];

  constructor(private userService: UserService) {}

  ngOnInit(): void {
    this.userService.getUsers().subscribe(
      (data: any[]) => {
        this.users = data;
        console.log(this.users);
      },
      (error: any) => {
        console.error('Error fetching users:', error);
      }
    );
  }
}
