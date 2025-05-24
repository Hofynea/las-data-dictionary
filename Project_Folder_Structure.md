# Project Folder Structure Documentation

This document outlines the folder structure of the project and the purpose of each module/component. It will be updated as new components and modules are added to the project.

---

## **Folder Structure**

### **`src/`**
The root folder of the project, containing all the source code.

- **`app/`**  
  Contains the main Angular application components, modules, and routing configurations.

---

### **`app/`**
The core of the application, with modules and components divided into specific domains.

#### **Components**
1. **`shared/`**  
   - Contains shared components, directives, and services used across the application.
   - **Files:**
     - `shared.module.ts`: Exports shared components/modules for reuse.

2. **`canvas-discussion/`**  
   - Manages components and logic for discussions within the canvas section of the app.

3. **`class-term/`**  
   - Manages class-term-related functionality and views.

4. **`person-demographics/`**  
   - Handles components for displaying and managing user demographic data.

5. **`student-class/`**  
   - Represents features and components related to a student’s class view.
   - **Files:**
     - `student-class.component.ts`: Logic for the component.
     - `student-class.component.html`: Template for rendering the UI.
     - `student-class.component.css`: Component-specific styling.

6. **`student-term/`**  
   - Handles functionality related to a student’s term view.
   - **Files:**
     - `student-term.component.ts`: Component logic.
     - `student-term.component.html`: UI template.
     - `student-term.component.css`: Styles for the component.

7. **`term/`**  
   - Manages term-related functionality.
   - **Files:**
     - `term.component.ts`: Component logic for term-related features.
     - `term.component.html`: HTML template.
     - `term.component.css`: Styling for the term component.

8. **`sidebar/`**  
   - Component for the application’s sidebar navigation.
   - **Files:**
     - `sidebar.component.ts`: Logic for sidebar behavior.
     - `sidebar.component.html`: Template for the sidebar layout.
     - `sidebar.component.css`: Styling specific to the sidebar.
