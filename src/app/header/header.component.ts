/**
 * HeaderComponent
 * 
 * This component represents the application's top header section.
 * It includes the SearchBarComponent and handles layout and styling for the header.
 * 
 */


import { Component } from '@angular/core';
import { SearchBarComponent } from '../search-bar/search-bar.component';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [SearchBarComponent],
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {}
