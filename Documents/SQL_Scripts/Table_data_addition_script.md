# Table Database Data Insertion

## Overview
This document contains an SQL script that was used to  insert all tables data into the `core_table` table in the database. 
The script adds six tables into the `core_table`.

## SQL Script
```sql
INSERT INTO core_table (
    table_id,
    table_name, 
    description, 
    use_cases, 
    important_notes
) VALUES 
    (1, 'Person Demographics', '', '', ''),
    (2, 'Student Term', 
        'This table is one row for every student and term combination. A student can take one or more courses in a term. This table would provide an aggregate summary of a student for each specified term that they were enrolled or withdrawn in.', 
        'Class Attributes', 
        'The granularity of the data is one row per cls_id (combination of strm + cls_nbr_id). A class at ASU is one individual section of a course. Note that a class can be in its own Canvas Class Shell, it can be in a shared Canvas Class Shell with other classes, or it can have multiple Canvas Class Shells.'
    ),
    (3, 'Student Class', 
        'This table is one row per student and class combination. Students earn grades in their classes so this table would have grade outcome details included.', 
        'Class Attributes', 
        'The granularity of the data is one row per student (stdnt_id) and class (cls_id).'
    ),
    (4, 'Class Term', 
        'The Course Profile table includes information on ASU classes. A class is a unique section each term.', 
        'Student Activity/Engagement, Natural Language Processing', 
        'Not every submission is stored. PowerPoint, images, Excel files, code files, etc. are examples of file types that would not be included.'
    ),
    (5, 'Term', 
        'This table is one row per term. It contains factual information about a term, and how the terms are sequenced.', 
        'Term Information', 
        'The granularity of this table is one row per term. “Regular” refers to Fall and Spring terms, and excludes Summer and Winter. The trm_rel_cur columns are useful if you are always interested in a term relative to the current term. A value of 0 identifies the current term, the one before it would be -1, before that would be -2; while the term after would be 1, then 2, and so on.'
    ),
    (6, 'Canvas Discussion Entry Fields', 
        'This table contains data related to discussions that occur within the Canvas LMS. Discussions are typically conversations that occur between two or more people, although not every discussion entry will receive a response. For more information on discussion, see Canvas documentation.', 
        'Student Activity/Engagement, Natural Language Processing, Network analysis', 
        'The granularity of the data is one row per discussion entry. Discussion entries are typically replies to Discussion Threads. Discussion thread data is included in the same row as the discussion entry. A conversation can be grouped together using the de_branch field. A conversation is a series of discussion entries that occur between two or more individuals (students and staff).'
    );
