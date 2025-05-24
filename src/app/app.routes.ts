import { Routes } from '@angular/router';
import { provideRouter } from '@angular/router';
import { StudentClassComponent } from './student-class/student-class.component';
import { AdminDashboardComponent } from './admin-dashboard/admin-dashboard.component';
import { ForbiddenComponent } from './forbidden/forbidden.component';
import { AdminGuard } from './guards/admin.guard';
import { FaqComponent } from './faq/faq.component';
import { BookmarksComponent } from './bookmarks/bookmarks.component';
import { HomeComponent } from './home/home.component';
import { StudentClassDetailsComponent } from './student-class/student-class-details.component';
import { TableNameComponent } from './components/table-name/table-name.component'; // Import the TableNameCOmponent for routing
import { TableComponent } from './table/table.component';
import { SearchComponent } from './search/search.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'studentClass', component: StudentClassComponent },
  { path: 'admin', component: AdminDashboardComponent, canActivate: [AdminGuard] },
  { path: 'forbidden', component: ForbiddenComponent },
  { path: 'faq', component: FaqComponent },
  { path: 'bookmarks', component: BookmarksComponent },
  { path: 'studentClassDetails/:id', component: StudentClassDetailsComponent },
  { path: 'table-names', component: TableNameComponent}, // Defines a route for accessing the TableNameComponent at '/table-names'
  { path: 'table', component: TableComponent},
  { path: 'search', loadComponent: () => import('./search/search.component').then(m => m.SearchComponent) },
];

export const appConfig = {
  providers: [provideRouter(routes)], // Ensure Angular knows about the routes
};
