/**
 * FooterComponent
 * 
 * This component manages the application footer displaying branding elements,
 * contact information, and legal information.
 * It uses RouterModule for navigation links and implements ASU styling guidelines.
 * 
 */

import { Component } from '@angular/core';
import { RouterModule } from '@angular/router'; 

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent {
  termsOfServiceUrl = '#';
  privacyPolicyUrl = '#';
  contactEmail = 'contact@domain.com';
  contactPhone = '+1 (234) 567-890';
  contactAddress = '123 Placeholder St, City, State';
}
