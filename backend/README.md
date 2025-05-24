# Django Backend Setup

This guide provides step-by-step instructions to set up the Django backend for local development.

---

## Prerequisites

Ensure the following tools are installed on your machine:
- **Python 3.8+**
- **PostgreSQL** – Confirm with: `psql --version`
- **pip** – Python package installer
- **virtualenv** – Install with `pip install virtualenv`
- **Git** – To clone the repository
- **Node.js & Angular CLI** – For frontend integration

Check Python version with:
```bash
python3 --version
```

---

## Setup Instructions

1. Fetch Origin

2. Navigate to the Backend Folder

3. Create and Activate a Virtual Environment

```bash
python3 -m venv env
```

Activate the virtual environment:
- **macOS/Linux**:
```bash
source env/bin/activate
```
- **Windows**:
```bash
env\Scripts\activate
```

4. Install Dependencies

Ensure having a `requirements.txt` file containing:
```text
Django>=4.0
djangorestframework
psycopg2-binary
django-cors-headers
```
Install all dependencies:
```bash
pip install -r requirements.txt
```

5. Apply Database Migrations
```bash
python manage.py migrate
```

6. Run the Development Server
```bash
python manage.py runserver
```

The backend will now be running at: http://127.0.0.1:8000/

---

## Verify Setup

### Health Check Endpoint
Visit the following URL in your browser to ensure the backend is running:
http://127.0.0.1:8000/api/health/

You should see the response:
```json
{
   "status": "Backend is running!"
}
```

---

# Database Connection Testing

### 1. Activate the virtual environment: **venv**

### 2. Ensure that you have **django** and **psycopg2** installed:
```bash
pip list
```

### 3. Test Database Connection
To verify that Django can connect to PostgreSQL, run:
```bash
python manage.py dbshell
```
If the connection is successful, it will enter the PostgreSQL shell (**psql**)

### 4. Inspect Tables in database
```bash
python manage.py inspectdb
```
This should return models corresponding to the existing tables in your database.

---

# SuperUser(Admin) credentials

1. Run:
```bash
python manage.py runserver
```
2. Go to http://127.0.0.1:8000/admin/

- Username: `lasdd_superuser`
- Password: `lasdd12345`

---

# Angular Service & Django REST API Integration

## **Overview**
This document provides a description of steps taken to integrate an Angular frontend "http://localhost:4200/tables" to fetch and manage data from the Django REST Framework (DRF) backend "http://127.0.0.1:8000/tables/".

---

## **Step 1: Setting Up the Backend (Django REST Framework)**

### **1.1 Create API Using ModelViewSet**
- Implemented a Django model `Table` with fields:
  - `table_id` (IntegerField, primary key)
  - `table_name` (CharField, unique=True)
  - `description`, `use_cases`, `important_notes` (TextFields)
- Created a **serializer** (`TableSerializer`) to handle data validation.
- Developed a **ViewSet** (`TableViewSet`) using `ModelViewSet` for CRUD operations.
- Registered API routes in `urls.py` using Django REST Framework’s `DefaultRouter`.
- Applied migrations to update the database.

### **1.2 Install CORS in Backend**
```bash
pip install django-cors-headers
```

---

## **Step 2: Setting Up the Frontend (Angular)**

### **2.1 Generate Angular Service**
```bash
ng generate service services/table
```

- Implemented API calls using `HttpClientModule` to interact with the Django backend.
- Methods included:
  - `getTables()`
  - `getTable(id)`
  - `createTable(table)`
  - `updateTable(id, table)`
  - `deleteTable(id)`

### **2.2 Import `HttpClientModule` in Angular**
- The Angular project used a `shared.module.ts` instead of `app.module.ts`, so we ensured `HttpClientModule` was correctly imported and provided.

---

## **Step 3: Connecting Backend & Frontend**

### **3.1 Handling CORS in Django**
In `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'corsheaders',
    'rest_framework',
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ALLOWED_ORIGINS = ["http://localhost:4200"]
```

### **3.2 Running Backend and Frontend Concurrently**
```bash
python manage.py runserver
ng serve --open
```

---

## **Step 4: Testing CRUD Operations**

### **4.1 Testing in the Browser**
- **GET (Retrieve Tables)**: Verified that tables were displayed correctly.
- **POST (Add Table)**: Successfully added new entries.
- **DELETE (Remove Table)**: Deleted entries were removed both in the frontend and backend.
- **PATCH/PUT (Update Table)**: Implemented functionality for updating table names and descriptions.

### **4.2 API Testing via Django REST Framework UI**
- Used DRF’s built-in API interface at `127.0.0.1:8000/api/tables/` to manually test CRUD operations.

### **4.3 Running Pytest Backend Unit Tests**
- Backend logic is tested using `pytest`. To run all tests from the backend directory:
```bash
pytest
```
- To run a specific test file:
```bash
pytest tests/test_tables.py
```
- To include code coverage in your test run:
```bash
pytest --cov=. --cov-report=term-missing
```
- Make sure your virtual environment is activated when running tests.

### **4.4 Testing SQL Logic Scripts**
- Database validation logic is tested using Python scripts in a separate directory.
- Navigate to the directory where SQL verification scripts are located:
```bash
cd Documents/SQL_Scripts
```
- Use the general command below to run any of the verification scripts:
```bash
python <file_name>.py
```
> Replace `<file_name>` with the appropriate script name (e.g., `Verify_Student_Class`, `Verify_Term`, etc.).

---

# Entity Relationship Diagram

Below is the ERD representing how core models relate in the backend:

![ERD](LAS_DD_ERDV2.png)

---

# Troubleshooting

Here are a few common issues and how to resolve them:

### 1. PostgreSQL Not Connecting
- Make sure PostgreSQL is running:
  ```bash
  sudo service postgresql start
  ```
- Verify `settings.py` DB credentials match your local DB setup.
- Confirm `psycopg2` is installed: `pip install psycopg2-binary`

### 2. Port 8000 Already in Use
- Kill the process using it:
  ```bash
  lsof -i :8000
  kill -9 <PID>
  ```
  Or run Django on a different port:
  ```bash
  python manage.py runserver 8001
  ```

### 3. Static Files Not Loading (Admin Panel)
- Run collectstatic if needed:
  ```bash
  python manage.py collectstatic
  ```

---

# PostgreSql database backup and restore strategy

## Overview
This document outlines steps taken for creating database backup and way to restore from it for 2 different instances: Local machine(Windows) and EC2(Linux).

## **1. Backup Strategy for Windows**
PostgreSQL backups automated using `pg_dump`, Windows Task Scheduler, and a Batch (`.bat`) script. Automatic backups are scheduled for 12:45 am daily.

### **Backup Steps:**
1. **Create a Backup Directory and Batch File:**
```bat
@echo off
set PGUSER=postgres
set PGPASSWORD=0000
set DATABASE=las_data_dictionary
set BACKUP_PATH=C:\Users\hlsoz\Desktop\ASU\SER401\Database_Backups
set TIMESTAMP=%date:~-4,4%-%date:~4,2%-%date:~7,2%_%time:~0,2%-%time:~3,2%-%time:~6,2%
set PGBIN="C:\Program Files\PostgreSQL\15\bin\pg_dump.exe"

%PGBIN% -U %PGUSER% -F c -b -v -f "%BACKUP_PATH%\backup_%TIMESTAMP%.sql" %DATABASE%
```

2. **Schedule with Task Scheduler:**
- Trigger: Daily at 12:45 AM
- Action: Run the `.bat` file

---

## **2. Restore Strategy for Windows**

### **Restore Steps:**
1. Locate Backup File
2. Drop and recreate schema:
```cmd
psql -U postgres -d las_data_dictionary -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"
```
3. Restore using pg_restore:
```cmd
pg_restore -U postgres -d las_data_dictionary -v "C:\...\Database_Backups\backup_file.sql"
```
4. Verify with pgAdmin or:
```sql
SELECT * FROM some_table;
```

---

## **3. Backup Strategy on AWS EC2 (Linux)**

### **Backup Steps:**
1. SSH into EC2 and create backup directory:
```sh
mkdir -p ~/backups/postgresql
```

2. Create shell script:
```sh
nano ~/backups/postgresql/backup.sh
```
```sh
#!/bin/bash
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_DIR="~/backups/postgresql"
BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.sql"
DB_NAME="las_data_dictionary"
DB_USER="postgres"

export PGPASSWORD="0000"
pg_dump -U $DB_USER -F c -b -v -f "$BACKUP_FILE" $DB_NAME
unset PGPASSWORD

# Keep only the last 7 backups
find $BACKUP_DIR -type f -name "backup_*.sql" -mtime +7 -exec rm {} \;
```

3. Make script executable:
```sh
chmod +x ~/backups/postgresql/backup.sh
```

4. Schedule with cron:
```sh
crontab -e
```
Add:
```sh
0 2 * * * ~/backups/postgresql/backup.sh >> ~/backups/postgresql/backup.log 2>&1
```

---

## **4. Restore Strategy for AWS EC2**

### **Restore Steps:**
1. Find backup file:
```sh
ls -lh ~/backups/postgresql/
```

2. Restore:
```sh
export PGPASSWORD="0000"
psql -U postgres -d las_data_dictionary -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"
pg_restore -U postgres -d las_data_dictionary -v "~/backups/postgresql/backup_file.sql"
unset PGPASSWORD
```

3. Verify:
```sh
psql -U postgres -d las_data_dictionary -c "SELECT * FROM some_table LIMIT 10;"
```
