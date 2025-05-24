# LaSDataDictionary - Frontend


## Prerequisites


Ensure the following tools are installed in your machine:
- **Angular CLI 18.2.11+** - For frontend integration
- **Node.js** – For frontend integration
- **Python 3.8+**
- **PostgreSQL** – Confirm with: `psql --version`
- **pip** – Python package installer
- **virtualenv** – Install with `pip install virtualenv`
- **Git** – To clone the repository


Check Angular CLI version with:
```bash
ng version
```
## Setup Instructions


1. Fetch Origin


2. Navigate to the root directory


3. (Optional, should only be needed when setting up a new package-lock.json) Gain access to the ASU Unity Stack. This can be done with the following link: https://asudev.jira.com/servicedesk/customer/portal/2


4. (Optional, should only be needed when setting up a new package-lock.json) Edit the npmrc.example folder with a valid git access token.


**IMPORTANT NOTE:**  When cloning and building the project make sure to create a git access token with the read permissions enabled. Once the token is created, edit the npmrc file to contain the token and rename the file from .npmrc.example to .npmrc so the correct dependencies can be downloaded from the ASU unity stack package directory.


5. Install all modules and dependencies with the following command in the root directory:


```bash
npm npm ci --legacy-peer-deps
```


**IMPORTANT NOTE:** When installing the node modules it is important to use `npm ci --legacy-peer-deps` to install the correct modules. DO NOT USE **npm install** as this will change the package.lock.json to your current dependency versions and your build will no longer be consistent with the development build. **npm install** should be reserved for when new tools are to being added to the build.




## Running the application


Once the backend and frontend architecture have been installed (backend instructions can be found in backend/README.md) you are ready to run the application following these steps.


1. Activate the virtual environment in the backend folder using the following command:


- **macOS/Linux**:
```bash
source env/bin/activate
```
- **Windows**:
```bash
env\Scripts\activate
```
2. Run the development backend server in the backend folder using the following command:


```bash
python manage.py runserver
```
The backend will now be running at: http://127.0.0.1:8000/


3. Run the development frontend server in the root directory using the following command:


```bash
ng serve
```
The frontend will now be running at: http://localhost:4200/


## Development server


Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.


## Code scaffolding


Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.


## Build


Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.


## Running unit tests


Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).


## Running end-to-end tests


Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.


## Further help


To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.dev/tools/cli) page.
