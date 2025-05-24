# Entry Data Insertion - Person Demographics

## Overview
This document contains the SQL script that will be used to insert data into the database for the entry table. The labels inserted will be for person demographics.

### Person Demographics
Data will be added by rows:

#### Row 1
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Data Pull Date',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'data_pull_date')),
  
  -- Description
  ('Date the data was pulled. Currently effective fields are effective as of one day prior to this date.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'data_pull_date')),
  
  -- Category
  ('Identifier',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'data_pull_date')),
  
  -- Source
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'data_pull_date')),
  
  -- Name
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'data_pull_date')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'data_pull_date')),
  
  -- Sample Data
  ('4/13/2023',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'data_pull_date')),
  
  -- Data Type
  ('Discrete',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'data_pull_date')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'data_pull_date')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'data_pull_date'));
```

#### Row 2
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Person Id',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'person_id')),
  
  -- Description
  ('Unique 10-character numerical identifier for a person',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'person_id')),
  
  -- Category
  ('Identifier',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'person_id')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'person_id')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'person_id')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'person_id')),
  
  -- Sample Data
  ('1234567890',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'person_id')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'person_id')),
  
  -- De-Identified
  ('De-Identified',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'person_id')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'person_id'));
```

#### Row 3
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Student Age Year Number',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'stdnt_age_yr_num')),
  
  -- Description
  ('Current age of the person; this value is empty (null) if the person is known to be deceased',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'stdnt_age_yr_num')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'stdnt_age_yr_num')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'stdnt_age_yr_num')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'stdnt_age_yr_num')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'stdnt_age_yr_num')),
  
  -- Sample Data
  ('18',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'stdnt_age_yr_num')),
  
  -- Data Type
  ('Discrete',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'stdnt_age_yr_num')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'stdnt_age_yr_num')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'stdnt_age_yr_num'));
```

#### Row 4
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Deceased Flag',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'deceased_flg')),
  
  -- Description
  ('Y/N flag indicating that the person is deceased.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'deceased_flg')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'deceased_flg')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'deceased_flg')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'deceased_flg')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'deceased_flg')),
  
  -- Sample Data
  ('N',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'deceased_flg')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'deceased_flg')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'deceased_flg')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'deceased_flg'));
```

#### Row 5
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('ASU Cultural Origin Code',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_cd')),
  
  -- Description
  ('The person''s primary cultural origin code.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_cd')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_cd')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_cd')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_cd')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_cd')),
  
  -- Sample Data
  ('H720',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_cd')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_cd')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_cd')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_cd'));
```

#### Row 6
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('ASU Cultural Origin Short Description',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_sd')),
  
  -- Description
  ('Short Description of the person''s primary cultural origin code.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_sd')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_sd')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_sd')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_sd')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_sd')),
  
  -- Sample Data
  ('Latin Amer',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_sd')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_sd')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_sd')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_sd'));
```

#### Row 7
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('ASU Cultural Origin Long Description',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_ld')),
  
  -- Description
  ('Long Description of the person''s primary cultural origin code.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_ld')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_ld')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_ld')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_ld')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_ld')),
  
  -- Sample Data
  ('Latin American',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_ld')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_ld')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_ld')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_cult_origin_ld'));
```

#### Row 8
```sql
  INSERT INTO core_entry (entry_content, field_id, label_id)
  VALUES
  -- Friendly Name
  ('Ethnic Group',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group')),
  
  -- Description
  ('Ethnic Group of the person, according to this order of precedence:\n1. Students who identify as Hispanic, even if they also select additional ethnic codes, should be coded as Hispanic/Latino (H). (Ignore primary_indicator flag in all cases)\n2. Non-Hispanic students who have more than one ethnic code, not including Unspecified (U), should be coded as Two or More Races (T).\n3. All other students should be assigned to the single ethnic code they selected or to Unspecified (U) if they selected none.\n\nNote: this value is similar to ASU Minority Code; the only difference is that Ethnic Group does not take Citizenship or Visa into account; there are no ‘X’ (International) codes in Ethnic Group.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group')),
  
  -- Sample Data
  ('H',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group'));
```

#### Row 9
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Ethnic Group Short Description',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd')),
  
  -- Description
  (E'Currently effective, active short description for the ethnic_group.\n2 or more = people with more than one ethnic group.\n‘NR’ = people with ethnic group ‘U’ or no/blank ethnic group.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd')),
  
  -- Sample Data
  ('Hispanic',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd'));
```


#### Row 10
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Ethnic Group Short Description List',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd_list')),
  
  -- Description
  ('Currently effective, active comma-separated list of the person''s ethnic group short descriptions.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd_list')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd_list')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd_list')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd_list')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd_list')),
  
  -- Sample Data
  ('Hispanic,White',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd_list')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd_list')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_sd_list')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
```

#### Row 11
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Ethnic Group Long Description',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_ld')),
  
  -- Description
  ('Currently effective, active comma-separated list of the person''s ethnic group long descriptions.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_ld')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_ld')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_ld')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_ld')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_ld')),
  
  -- Sample Data
  ('Hispanic/Latino',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_ld')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_ld')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_ld')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'ethnic_group_ld'));
```

#### Row 12
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('ASU US Citizen Flag',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_us_citzn_flg')),
  
  -- Description
  ('Y/N flag indicating whether the person is a US Citizen.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_us_citzn_flg')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_us_citzn_flg')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_us_citzn_flg')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_us_citzn_flg')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_us_citzn_flg')),
  
  -- Sample Data
  ('N',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_us_citzn_flg')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_us_citzn_flg')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_us_citzn_flg')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_us_citzn_flg'));
```

#### Row 13
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('ASU Citizen Country',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country')),
  
  -- Description
  (E'Code for the person''s country of citizenship.\n\nIf the person is a citizen of USA and another country, USA takes precedence. If a non-US citizen is a citizen of two non-US countries, MIN(country) code is used as the tiebreaker.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country')),
  
  -- Sample Data
  ('BRA',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country'));
```

#### Row 14
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('ASU Citizen Country Long Description',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country_ld')),
  
  -- Description
  (E'Description of the person''s country of citizenship.\n\nIf the person is a citizen of USA and another country, USA takes precedence. If a non-US citizen is a citizen of two non-US countries, MIN(country) code is used as the tiebreaker.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country_ld')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country_ld')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country_ld')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country_ld')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country_ld')),
  
  -- Sample Data
  ('Brazil',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country_ld')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country_ld')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country_ld')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_citzn_country_ld'));

```

#### Row 15
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('ASU Multiple Citizenship Flag',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_mult_citzn_flg')),
  
  -- Description
  ('Y/N flag indicating whether the person is a citizen or more than one country, regardless of country.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_mult_citzn_flg')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_mult_citzn_flg')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_mult_citzn_flg')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_mult_citzn_flg')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_mult_citzn_flg')),
  
  -- Sample Data
  ('N',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_mult_citzn_flg')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_mult_citzn_flg')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_mult_citzn_flg')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_mult_citzn_flg'));

```

#### Row 16
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('ASU Minority Status Code',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_cd')),
  
  -- Description
  (E'High level summary of the person''s minority status:\n'
   || E'1. Persons who are International (formerly referred to as Non-Resident Alien) are coded as X.\n'
   || E'2. Persons who identify as Hispanic, even if they also select additional ethnic codes and even if they have a non-Hispanic primary ethnicity, are coded as Hispanic/Latino (H).\n'
   || E'3. Non-Hispanic persons who have more than one ethnic code, not including Unspecified (U), are coded as Two or More Races (T).\n'
   || E'4. All other persons are assigned to the single ethnic code they selected, or to Unspecified (U) if they selected none.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_cd')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_cd')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_cd')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_cd')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_cd')),
  
  -- Sample Data
  ('H',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_cd')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_cd')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_cd')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_cd'));

```

#### Row 17
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('ASU Minority Status Long Description',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_ld')),
  
  -- Description
  ('Minority status long description',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_ld')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_ld')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_ld')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_ld')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_ld')),
  
  -- Sample Data
  ('Hispanic/Latino',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_ld')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_ld')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_ld')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'asu_minrty_stat_ld'));
```

#### Row 18
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Marital Status Code',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_cd')),
  
  -- Description
  ('Currently effective Marital Status code',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_cd')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_cd')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_cd')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_cd')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_cd')),
  
  -- Sample Data
  ('U',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_cd')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_cd')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_cd')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_cd'));

```

#### Row 19
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Marital Status Long Description',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_ld')),
  
  -- Description
  ('Currently effective Marital Status long description',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_ld')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_ld')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_ld')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_ld')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_ld')),
  
  -- Sample Data
  ('Unknown',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_ld')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_ld')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_ld')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_ld'));
```

#### Row 20
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Marital Status Short Description',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_sd')),
  
  -- Description
  ('Currently effective Marital Status short description',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_sd')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_sd')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_sd')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_sd')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_sd')),
  
  -- Sample Data
  ('Unknown',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_sd')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_sd')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_sd')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'mar_stat_sd'));
```

#### Row 21
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Gender Code',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_cd')),
  
  -- Description
  ('Currently effective Gender (sex).',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_cd')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_cd')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_cd')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_cd')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_cd')),
  
  -- Sample Data
  ('F',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_cd')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_cd')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_cd')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_cd'));
```

#### Row 22
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Gender Description',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_descr')),
  
  -- Description
  ('10-character description of the person''s gender_cd',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_descr')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_descr')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_descr')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_descr')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_descr')),
  
  -- Sample Data
  ('Female',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_descr')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_descr')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_descr')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'gender_descr'));
```

#### Row 23
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Full Time Student Indicator',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'full_tm_stu_ind')),
  
  -- Description
  ('Currently effective indicator of person''s full time student status',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'full_tm_stu_ind')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'full_tm_stu_ind')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'full_tm_stu_ind')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'full_tm_stu_ind')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'full_tm_stu_ind')),
  
  -- Sample Data
  ('N',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'full_tm_stu_ind')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'full_tm_stu_ind')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'full_tm_stu_ind')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'full_tm_stu_ind'));
```

#### Row 24
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('US Work Eligibility Indicator',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'us_work_elig_ind')),
  
  -- Description
  ('Currently effective indicator of the person''s work eligibility',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'us_work_elig_ind')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'us_work_elig_ind')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'us_work_elig_ind')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'us_work_elig_ind')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'us_work_elig_ind')),
  
  -- Sample Data
  ('Y',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'us_work_elig_ind')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'us_work_elig_ind')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'us_work_elig_ind')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'us_work_elig_ind'));
```

#### Row 25
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Highest Education Level Code',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_cd')),
  
  -- Description
  ('Currently effective Highest Education Level code',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_cd')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_cd')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_cd')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_cd')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_cd')),
  
  -- Sample Data
  ('H',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_cd')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_cd')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_cd')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_cd'));
```

#### Row 26
```sql
  INSERT INTO core_entry (entry_content, field_id, label_id)
  VALUES
  -- Friendly Name
  ('Highest Education Level Long Description',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_ld')),
  
  -- Description
  ('Currently effective Highest Education Level long description',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_ld')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_ld')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_ld')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_ld')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_ld')),
  
  -- Sample Data
  ('Some Graduate School',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_ld')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_ld')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_ld')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_ld'));
```

#### Row 27
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Highest Education Level Short Description',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_sd')),
  
  -- Description
  ('Currently effective Highest Education Level short description',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_sd')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_sd')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_sd')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_sd')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_sd')),
  
  -- Sample Data
  ('Some Grad',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_sd')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_sd')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_sd')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'hi_edu_lvl_sd'));
```

#### Row 28
```sql
INSERT INTO core_entry (entry_content, field_id, label_id)
VALUES
  -- Friendly Name
  ('Residence Hall Status',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_status')),
  
  -- Description
  ('Y/N/P for Yes/No/Past. Indicates whether someone does, or did, reside in an on-campus residence hall.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_status')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_status')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_status')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_status')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_status')),
  
  -- Sample Data
  ('P',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_status')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_status')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_status')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_status'));
```

#### Row 29
```sql
  INSERT INTO core_entry (entry_content, field_id, label_id)
  VALUES
  -- Friendly Name
  ('Residence Hall Community',
   (SELECT field_id FROM core_field WHERE field_name = 'Friendly Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_community')),
  
  -- Description
  ('Residence Hall Community in which the student resides.',
   (SELECT field_id FROM core_field WHERE field_name = 'Description'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_community')),
  
  -- Category
  ('Demographic',
   (SELECT field_id FROM core_field WHERE field_name = 'Category'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_community')),
  
  -- Source
  ('SIS',
   (SELECT field_id FROM core_field WHERE field_name = 'Source'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_community')),
  
  -- Name
  ('Peoplesoft',
   (SELECT field_id FROM core_field WHERE field_name = 'Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_community')),
  
  -- Dataset Name
  ('Person Demographics',
   (SELECT field_id FROM core_field WHERE field_name = 'Dataset Name'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_community')),
  
  -- Sample Data
  ('University Towers',
   (SELECT field_id FROM core_field WHERE field_name = 'Sample Data'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_community')),
  
  -- Data Type
  ('Categorical',
   (SELECT field_id FROM core_field WHERE field_name = 'Data Type'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_community')),
  
  -- De-Identified
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'De-Identified'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_community')),
  
  -- Additional Notes
  ('',
   (SELECT field_id FROM core_field WHERE field_name = 'Additional Notes'),
   (SELECT label_id FROM core_label WHERE label_name = 'res_hall_community'));
```


