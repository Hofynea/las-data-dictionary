/**
 * HomeComponent
 * 
 * This component serves as the landing or main page of the application.
 * It includes functionality to toggle the sidebar using SidebarService.
 * 
 */


import {Component, OnInit} from '@angular/core';
import { SidebarService } from '@services/sidebar.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  constructor(
    private sidebarService: SidebarService
  ) {}

  toggleSidebar(): void {
    this.sidebarService.toggleSidebar();
  }
}
