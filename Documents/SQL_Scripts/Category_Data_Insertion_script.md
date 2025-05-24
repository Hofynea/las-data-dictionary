# Category Database Data Insertion
This document contains an SQL script that inserts category data into the `core_category` table in the database. The script adds seven categories to the `core_category` table.

## SQL Script
```sql
INSERT INTO core_category (
    category_id,
    category_name
) VALUES
    (1, 'Academic'),
    (2, 'Demographic'),
    (3, 'Engagement'),
    (4, 'Enrollment'),
    (5, 'Housing'),
    (6, 'Financial'),
    (7, 'Identifier');
```

## Notes
- The `category_id` is a unique identifier for each category.
- `category_name` represents the classification of elements in the database.
