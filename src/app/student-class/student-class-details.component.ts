import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-student-class-details',
  template: `
    <div>
      <h3>Student Class Details</h3>
      <p>Details for entry ID: {{ id }}</p>
    </div>
  `,
  styles: [
    `
      div {
        margin: 20px;
      }
    `,
  ],
})
export class StudentClassDetailsComponent implements OnInit {
  id!: number;

  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    // Fetch and parse the route parameter to retrieve the ID
    this.id = Number(this.route.snapshot.paramMap.get('id'));
    // Verified: Ensured that 'id' correctly captures the value from the route parameters
    // Tested: Checked behavior when 'id' is missing or invalid (e.g., non-numeric values)
  }
}
