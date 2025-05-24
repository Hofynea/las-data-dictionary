# Field Database Data Insertion

## Overview
This document contains an SQL script that was used to  insert all fields data into the `core_field` table in the database. 
The script adds 12 fields into the `core_field`.

## SQL Script
```sql
INSERT INTO core_field (
    field_id,
    field_name,
    description,
    position
) VALUES
    (1, 'Label', 'The technical label that is a specific identifier used to describe data fields, categories, or actions within the database', 1),
    (2, 'Friendly Name', 'A nontechnical name used to more easily describe and identify the data element for the data dictionary', 2),
    (3, 'Description', 'Brief description of the element and its uses within the database', 3),
    (4, 'Category', 'Defines the classification of each element within the database', 4),
    (5, 'Source', 'Source of the data element in the database', 5),
    (6, 'Type', 'The format/datatype of the data element', 6),
    (7, 'Name', 'The name of the tool used to collect the data for the element', 7),
    (8, 'Dataset Name', 'The name of the dataset that the database element belongs to', 8),
    (9, 'Sample Data', 'An example of the data element as it would be seen in the database. The examples are not representative of any real data', 9),
    (10, 'Null Handling', 'What does it mean when value is Null', 10),
    (11, 'De-Identified', 'Flag representing if the element was de-identified', 11),
    (12, 'Additional Notes', 'Important nuances not included in the definition', 12);
