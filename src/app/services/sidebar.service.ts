/**
 * SidebarService
 * 
 * This service controls the visibility state of the sidebar across the application.
 * It exposes an observable for sidebar visibility that components can subscribe to 
 * in order to react to toggle events.
 * 
 * Provides a simple method to toggle the visibility state using BehaviorSubject.
 */


import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class SidebarService {
  private sidebarVisible = new BehaviorSubject<boolean>(true);
  sidebarVisible$ = this.sidebarVisible.asObservable();

  toggleSidebar(): void {
    this.sidebarVisible.next(!this.sidebarVisible.value);
  }
}
