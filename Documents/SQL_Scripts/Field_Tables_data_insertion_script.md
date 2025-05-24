# Field_Tables Database Data Insertion

## Overview
This document contains an SQL script that was used to  insert field_tables data into the `core_field_tables` table in the database. 
It is used to represent many-to-many relationship between field and table. INSERT INTO core_field_tables (field_id, table_id)

## SQL Script
```sql
INSERT INTO core_field_tables (field_id, table_id)
SELECT f.field_id, t.table_id
FROM core_field f, core_table t
WHERE f.field_name IN ('Label', 'Friendly Name', 'Description', 'Category', 'Source', 'Name', 'Dataset Name')
AND t.table_name = 'Student Class';
```

Updated on 3/16/25 by Zulfina Ivanova:

## Sql Script to fill up field_tables for Student Class
```sql
INSERT INTO core_field_tables (field_id, table_id)
SELECT f.field_id, t.table_id
FROM core_field f, core_table t
WHERE f.field_name IN ('Label', 'Friendly Name', 'Description', 'Category', 'Source', 'Type', 'Name', 'Dataset Name', 'Sample Data', 'Null Handling', 'Data Type', 'De-Identified', 'Additional Notes')
AND t.table_name = 'Student Class';
```

## Sql Script to fill up field_tables for Person Demographics
```sql
INSERT INTO core_field_tables (field_id, table_id)
SELECT f.field_id, t.table_id
FROM core_field f, core_table t
WHERE f.field_name IN ('Label', 'Friendly Name', 'Description', 'Category', 'Source', 'Name', 'Dataset Name', 'Sample Data', 'Data Type', 'De-Identified', 'Additional Notes')
AND t.table_name = 'Person Demographics';
```

## Sql Script to fill up field_tables for Student Term
```sql
INSERT INTO core_field_tables (field_id, table_id)
SELECT f.field_id, t.table_id
FROM core_field f, core_table t
WHERE f.field_name IN ('Label', 'Friendly Name', 'Description', 'Category', 'Source', 'Name', 'Dataset Name', 'Sample Data', 'Data Type', 'De-Identified')
AND t.table_name = 'Student Term';
```

## Sql Script to fill up field_tables for Class Term
```sql
INSERT INTO core_field_tables (field_id, table_id)
SELECT f.field_id, t.table_id
FROM core_field f, core_table t
WHERE f.field_name IN ('Label', 'Friendly Name', 'Description', 'Category', 'Source', 'Name', 'Dataset Name', 'Sample Data', 'Data Type', 'De-Identified', 'Additional Notes')
AND t.table_name = 'Class Term';
```

## Sql Script to fill up field_tables for Term
```sql
INSERT INTO core_field_tables (field_id, table_id)
SELECT f.field_id, t.table_id
FROM core_field f, core_table t
WHERE f.field_name IN ('Label', 'Friendly Name', 'Description', 'Category', 'Source', 'Name', 'Dataset Name', 'Sample Data', 'Data Type', 'Additional Notes')
AND t.table_name = 'Term';
```

## Sql Script to fill up field_tables for Canvas Discussion Entry Fields
```sql
INSERT INTO core_field_tables (field_id, table_id)
SELECT f.field_id, t.table_id
FROM core_field f, core_table t
WHERE f.field_name IN ('Label', 'Friendly Name', 'Description', 'Category', 'Source', 'Type', 'Name', 'Dataset Name', 'Sample Data', 'Null Handling','Data Type', 'De-Identified', 'Additional Notes')
AND t.table_name = 'Canvas Discussion Entry Fields';
```


