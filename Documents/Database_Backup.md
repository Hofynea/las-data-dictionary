# PostgreSQL Backup & Restore Guide using pgAdmin

This guide explains how to create a full **backup** of the PostgreSQL database using pgAdmin, and how to **restore** it when needed.

---

## Backup Steps

### Step 1: Open pgAdmin
1. Launch pgAdmin.
2. Connect to PostgreSQL server.

### Step 2: Locate Your Database
1. Expand the appropriate **server name**.
3. Expand **Databases**.
4. Right-click the database (`las_data_dictionary`).

### Step 3: Initiate Backup
1. From the right-click menu, choose **Backup…**
2. In the **Backup Options** window:
   - **Filename**: Click the folder icon to choose where to save the backup file. Use `.sql` extension, e.g.:
     ```
     ...\las_data_dictionary_backup.sql
     ```
   - **Format**: Custom.
     - `Custom` is preferred for full backups with flexibility.
   - **Role name**: Select the correct database user (`postgres`).
3. Click **Backup**.

### Confirmation
- Dialog with progress logs will be displayed.
- Once successful, the backup file will be saved at the selected location.

---

## Restore Steps

> You must create an empty database first to restore into.

### Step 1: Create a New Database (for Restore)
1. In pgAdmin, right-click **Databases** > **Create > Database**.
2. Name it (for ex., `las_data_dictionary_restored`).
3. Set the correct **owner** (for ex., `postgres`).
4. Click **Save**.

### Step 2: Restore the Backup
1. Right-click on the database you just created.
2. Choose **Restore**
3. In the **Restore Options** window:
   - **Format**: Choose `Custom`.
   - **Filename**: Click the folder icon and select your `.sql` file.
   - **Role name**: Select appropriate role ( `postgres`).
4. Click the **Restore** button.

### Confirmation
- pgAdmin will run and display progress logs.
- Once complete, the new database will be populated with both schema and data from the backup.

---


