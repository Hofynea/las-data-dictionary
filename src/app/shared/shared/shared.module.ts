/**
 * This is a shared module where commonly used services, components,
 * pipes, and guards can all live. Please be cautious adding new
 * features to the shared module, as it is best practice to add only
 * what is needed across many components.
 *
 * Date: 11/14/2024
 *
 * SER 401 - Capstone
 * Learning_at_scale Team #42
 *
 */

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { HttpClientModule} from '@angular/common/http';
import { TableNameComponent } from 'src/app/components/table-name/table-name.component';

@NgModule({
  declarations: [
    TableNameComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule,
    HttpClientModule
  ],
  exports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule,
    HttpClientModule
  ],
  providers: [

  ],
})

export class SharedModule { }
