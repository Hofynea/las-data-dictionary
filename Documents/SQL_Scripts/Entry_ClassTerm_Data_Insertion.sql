-- This sql script enters all entries for class term

INSERT INTO core_entry (
    	entry_content,
    	field_id,
    	label_id)
    VALUES 
	    -- Row One
    	('Class Section ID', 2, 174), -- Friendly Name
        ('Unique 9-character numerical identifier for a class. This is a combination of the strm (term) and SLN (class_nbr, section).', 3, 174), -- Description
        ('Identifier', 4, 174), -- Category
        ('SIS', 5, 174), --Source
        (' ', 6, 174), -- Type
        ('Peoplesoft', 7, 174), -- Name
        ('Class Term', 8, 174), -- Dataset Name
        ('217783010, 219441073, ...', 9, 174), -- Sample Data
        (' ', 10, 174), -- Null Handling
        (' ', 11, 174), -- De-Identified
        (' ', 12, 174), -- Additional Notes
        ('Categorical', 13, 174), -- Data Type

        -- Row Two
    	('Academic Term', 2, 175), -- Friendly Name
        ('4-character numerical code specifying the term the class is related to. First 3 characters represent year and last character represents term
        1 - Spring
        4 - Summer
        7 - Fall', 3, 175), -- Description
        ('Identifier', 4, 175), -- Category
        ('SIS', 5, 175), --Source
        (' ', 6, 175), -- Type
        ('Peoplesoft', 7, 175), -- Name
        ('Class Term', 8, 175), -- Dataset Name
        ('2077, 2141, 2204, ...', 9, 175), -- Sample Data
        (' ', 10, 175), -- Null Handling
        (' ', 11, 175), -- De-Identified
        (' ', 12, 175), -- Additional Notes
        ('Categorical', 13, 175), -- Data Type

        -- Row Three
    	('Class Number ID', 2, 176), -- Friendly Name
        ('5-digit numerical identifier for a class section within the indicated term. This is equivalent to the SLN, Class_nbr, section.', 3, 176), -- Description
        ('Identifier', 4, 176), -- Category
        ('SIS', 5, 176), --Source
        (' ', 6, 176), -- Type
        ('Peoplesoft', 7, 176), -- Name
        ('Class Term', 8, 176), -- Dataset Name
        ('83010, 41073, ...', 9, 176), -- Sample Data
        (' ', 10, 176), -- Null Handling
        (' ', 11, 176), -- De-Identified
        (' ', 12, 176), -- Additional Notes
        ('Categorical', 13, 176), -- Data Type

        -- Row Four
    	('Course ID', 2, 177), -- Friendly Name
        ('Uniquw 6-character numerical identifier for a course', 3, 177), -- Description
        ('Identifier', 4, 177), -- Category
        ('SIS', 5, 177), --Source
        (' ', 6, 177), -- Type
        ('Peoplesoft', 7, 177), -- Name
        ('Class Term', 8, 177), -- Dataset Name
        ('124932, 014698, ...', 9, 177), -- Sample Data
        (' ', 10, 177), -- Null Handling
        (' ', 11, 177), -- De-Identified
        (' ', 12, 177), -- Additional Notes
        ('Categorical', 13, 177), -- Data Type

        -- Row Five
    	('Course Code', 2, 178), -- Friendly Name
        ('Code specifying the course being taught (catalog code extensions are removed, but available in crs_catalog_extn_cd when needed)', 3, 178), -- Description
        ('Class Attribute', 4, 178), -- Category
        ('SIS', 5, 178), --Source
        (' ', 6, 178), -- Type
        ('Peoplesoft', 7, 178), -- Name
        ('Class Term', 8, 178), -- Dataset Name
        ('FSE 101, MAT 274, VIP 494, MKT 301', 9, 178), -- Sample Data
        (' ', 10, 178), -- Null Handling
        (' ', 11, 178), -- De-Identified
        (' ', 12, 178), -- Additional Notes
        ('Categorical', 13, 178), -- Data Type

        -- Row Six
    	('Course Subject Code', 2, 179), -- Friendly Name
        ('Code specifying the subject of the course being taught', 3, 179), -- Description
        ('Class Attribute', 4, 179), -- Category
        ('SIS', 5, 179), --Source
        (' ', 6, 179), -- Type
        ('Peoplesoft', 7, 179), -- Name
        ('Class Term', 8, 179), -- Dataset Name
        ('FSE, MAT, VIP, MKT, ...', 9, 179), -- Sample Data
        (' ', 10, 179), -- Null Handling
        (' ', 11, 179), -- De-Identified
        (' ', 12, 179), -- Additional Notes
        (' Categorical', 13, 179), -- Data Type

        -- Row Seven
    	('Course Catalog Code', 2, 180), -- Friendly Name
        ('Code specifying the level and specific theme of the subject being taught (catalog code extensions are removed, but available in crs_catalog_extn_cd when needed)', 3, 180), -- Description
        ('Class Attribute', 4, 180), -- Category
        ('SIS', 5, 180), --Source
        (' ', 6, 180), -- Type
        ('Peoplesoft', 7, 180), -- Name
        ('Class Term', 8, 180), -- Dataset Name
        ('101, 274, 494, 301, ...', 9, 180), -- Sample Data
        (' ', 10, 180), -- Null Handling
        (' ', 11, 180), -- De-Identified
        (' ', 12, 180), -- Additional Notes
        ('Categorical', 13, 180), -- Data Type

        -- Row Eight
    	('Course Catalog Code (Extension)', 2, 181), -- Friendly Name
        ('Code sometimes added to catalog number codes to specify additional details for use by colleges (removed in this table from crs_cd and crs_catalog_cd, and provided here for use when needed)', 3, 181), -- Description
        ('Class Attribute', 4, 181), -- Category
        ('SIS', 5, 181), --Source
        (' ', 6, 181), -- Type
        ('Peoplesoft', 7, 181), -- Name
        ('Class Term', 8, 181), -- Dataset Name
        ('-w, -BMI, ...', 9, 181), -- Sample Data
        (' ', 10, 181), -- Null Handling
        (' ', 11, 181), -- De-Identified
        (' ', 12, 181), -- Additional Notes
        ('Categorical', 13, 181), -- Data Type

        -- Row Nine
    	('Course Description', 2, 182), -- Friendly Name
        ('Basic Description of the course being taught', 3, 182), -- Description
        ('Class Attribute', 4, 182), -- Category
        ('SIS', 5, 182), --Source
        (' ', 6, 182), -- Type
        ('Peoplesoft', 7, 182), -- Name
        ('Class Term', 8, 182), -- Dataset Name
        ('Applied Ethics, Research Method, Psychology of Stress & Coping SOCIAL ASPECTS/OUTDOOR RECRE A, Special Topics, ...', 9, 182), -- Sample Data
        (' ', 10, 182), -- Null Handling
        (' ', 11, 182), -- De-Identified
        (' ', 12, 182), -- Additional Notes
        ('Categorical', 13, 182), -- Data Type

        -- Row Ten
    	('Course Description (Long)', 2, 183), -- Friendly Name
        ('Full description of the course, as shown in the class search system', 3, 183), -- Description
        ('Class Attribute', 4, 183), -- Category
        ('SIS', 5, 183), --Source
        (' ', 6, 183), -- Type
        ('Peoplesoft', 7, 183), -- Name
        ('Class Term', 8, 183), -- Dataset Name
        ('Applies cirricular practice and how perservice teachers wotk with students with special needs in middle and secondary levels, ...', 9, 183), -- Sample Data
        (' ', 10, 183), -- Null Handling
        (' ', 11, 183), -- De-Identified
        (' ', 12, 183), -- Additional Notes
        ('Categorical', 13, 183), -- Data Type

        -- Row Eleven
    	('Course Topic ID', 2, 184), -- Friendly Name
        ('Numeric identifier for a specific subtopic of the course -- essentially part of the course ID when determining equivalencies', 3, 184), -- Description
        ('Identifier', 4, 184), -- Category
        ('SIS', 5, 184), --Source
        (' ', 6, 184), -- Type
        ('Peoplesoft', 7, 184), -- Name
        ('Class Term', 8, 184), -- Dataset Name
        ('0, 19, 532, ...', 9, 184), -- Sample Data
        (' ', 10, 184), -- Null Handling
        (' ', 11, 184), -- De-Identified
        (' ', 12, 184), -- Additional Notes
        ('Categorical', 13, 184), -- Data Type

        -- Row Twelve
    	('Course Subtopic Description', 2, 185), -- Friendly Name
        ('Description of the subtopic being taught', 3, 185), -- Description
        ('Class Attribute', 4, 185), -- Category
        ('SIS', 5, 185), --Source
        (' ', 6, 185), -- Type
        ('Peoplesoft', 7, 185), -- Name
        ('Class Term', 8, 185), -- Dataset Name
        ('Analyzing and Exploring: Sydny, Spanish Art and Architecture, Voice, ...', 9, 185), -- Sample Data
        (' ', 10, 185), -- Null Handling
        (' ', 11, 185), -- De-Identified
        (' ', 12, 185), -- Additional Notes
        ('Categorical', 13, 185), -- Data Type

        -- Row Thirteen
    	('Class Type (Enrollment/Non-Enrollment)', 2, 186), -- Friendly Name
        ('Code specifying whether the class is a primary "enrollment" section (has associated credits and grade) or a "non-enrollment" section, where additional class components (such as labs and recitations) are not the primary section that a student enrolls in', 3, 186), -- Description
        ('Class Attribute', 4, 186), -- Category
        ('SIS', 5, 186), --Source
        (' ', 6, 186), -- Type
        ('Peoplesoft', 7, 186), -- Name
        ('Class Term', 8, 186), -- Dataset Name
        ('E, N', 9, 186), -- Sample Data
        (' ', 10, 186), -- Null Handling
        (' ', 11, 186), -- De-Identified
        (' ', 12, 186), -- Additional Notes
        ('Categorical', 13, 186), -- Data Type

        -- Row 14
    	('Instruction Method', 2, 187), -- Friendly Name
        ('Code for specifying what type of instruction method was used for the section', 3, 187), -- Description
        ('Class Attribute', 4, 187), -- Category
        ('SIS', 5, 187), --Source
        (' ', 6, 187), -- Type
        ('Peoplesoft', 7, 187), -- Name
        ('Class Term', 8, 187), -- Dataset Name
        ('LEC, LAB, REC', 9, 187), -- Sample Data
        (' ', 10, 187), -- Null Handling
        (' ', 11, 187), -- De-Identified
        (' ', 12, 187), -- Additional Notes
        ('Categorical', 13, 187), -- Data Type

        -- Row 15
    	('Implementation Status', 2, 188), -- Friendly Name
        ('Code specifying the implementation status for the class section (Active, Suspended, Tentative, Canceled)', 3, 188), -- Description
        ('Class Attribute', 4, 188), -- Category
        ('SIS', 5, 188), --Source
        (' ', 6, 188), -- Type
        ('Peoplesoft', 7, 188), -- Name
        ('Class Term', 8, 188), -- Dataset Name
        ('A, S, T, X', 9, 188), -- Sample Data
        (' ', 10, 188), -- Null Handling
        (' ', 11, 188), -- De-Identified
        (' ', 12, 188), -- Additional Notes
        ('Categorical', 13, 188), -- Data Type

        -- Row 16
    	('Registration Eligibility (Open/Closed)', 2, 189), -- Friendly Name
        ('Code specifying the registration eligibility status for the class section (open or closed) -- there is additional logic required to completely determine if a class is open for registration, and even more to know if a specific student can register in it', 3, 189), -- Description
        ('Class Attribute', 4, 189), -- Category
        ('SIS', 5, 189), --Source
        (' ', 6, 189), -- Type
        ('Peoplesoft', 7, 189), -- Name
        ('Class Term', 8, 189), -- Dataset Name
        ('Y, N', 9, 189), -- Sample Data
        (' ', 10, 189), -- Null Handling
        (' ', 11, 189), -- De-Identified
        (' ', 12, 189), -- Additional Notes
        ('Categorical', 13, 189), -- Data Type

        -- Row 17
    	('Discoverable in Class Search', 2, 190), -- Friendly Name
        ('Flag specifying whether or not the class is discoverable by students in Class Search', 3, 190), -- Description
        ('Class Attribute', 4, 190), -- Category
        ('SIS', 5, 190), --Source
        (' ', 6, 190), -- Type
        ('Peoplesoft', 7, 190), -- Name
        ('Class Term', 8, 190), -- Dataset Name
        ('Y, N', 9, 190), -- Sample Data
        (' ', 10, 190), -- Null Handling
        (' ', 11, 190), -- De-Identified
        (' ', 12, 190), -- Additional Notes
        ('Categorical', 13, 190), -- Data Type

        -- Row 18
    	('Combined Class ID', 2, 191), -- Friendly Name
        ('8-character numerical identifier for a combined class instance, such as cross-listed classes', 3, 191), -- Description
        ('Identifier', 4, 191), -- Category
        ('SIS', 5, 191), --Source
        (' ', 6, 191), -- Type
        ('Peoplesoft', 7, 191), -- Name
        ('Class Term', 8, 191), -- Dataset Name
        ('209105, 21212682, ...', 9, 191), -- Sample Data
        (' ', 10, 191), -- Null Handling
        (' ', 11, 191), -- De-Identified
        (' ', 12, 191), -- Additional Notes
        ('Categorical', 13, 191), -- Data Type

        -- Row 19
    	('Combined Class Codes', 2, 192), -- Friendly Name
        ('Set of course codes specifying which courses are included in the combined class', 3, 192), -- Description
        ('Class Attribute', 4, 192), -- Category
        ('SIS', 5, 192), --Source
        (' ', 6, 192), -- Type
        ('Peoplesoft', 7, 192), -- Name
        ('Class Term', 8, 192), -- Dataset Name
        ('MSE 494/598, VTN 101, "EEE480, 591"', 9, 192), -- Sample Data
        (' ', 10, 192), -- Null Handling
        (' ', 11, 192), -- De-Identified
        (' ', 12, 192), -- Additional Notes
        ('Categorical', 13, 192), -- Data Type

        -- Row 20
    	('Class Academic Session', 2, 193), -- Friendly Name
        ('Code specifying the academic session associated with the class', 3, 193), -- Description
        ('Class Attribute', 4, 193), -- Category
        ('SIS', 5, 193), --Source
        (' ', 6, 193), -- Type
        ('Peoplesoft', 7, 193), -- Name
        ('Class Term', 8, 193), -- Dataset Name
        ('A, B, C, DYN, TW1, 8W2, REG, WIN, ...', 9, 193), -- Sample Data
        (' ', 10, 193), -- Null Handling
        (' ', 11, 193), -- De-Identified
        (' ', 12, 193), -- Additional Notes
        ('Categorical', 13, 193), -- Data Type

        -- Row 21
    	('Class Managing Unit', 2, 194), -- Friendly Name
        ('Code specifying the unit that manages the class section', 3, 194), -- Description
        ('Class Attribute', 4, 194), -- Category
        ('SIS', 5, 194), --Source
        (' ', 6, 194), -- Type
        ('Peoplesoft', 7, 194), -- Name
        ('Class Term', 8, 194), -- Dataset Name
        ('CMUSIC, CGRAPHINFO, ZAECP, COE, ...', 9, 194), -- Sample Data
        (' ', 10, 194), -- Null Handling
        (' ', 11, 194), -- De-Identified
        (' ', 12, 194), -- Additional Notes
        ('Categorical', 13, 194), -- Data Type

        -- Row 22
    	('Class Managing College', 2, 195), -- Friendly Name
        ('Code specifying the college that manages the class section', 3, 195), -- Description
        ('Class Attribute', 4, 195), -- Category
        ('SIS', 5, 195), --Source
        (' ', 6, 195), -- Type
        ('Peoplesoft', 7, 195), -- Name
        ('Class Term', 8, 195), -- Dataset Name
        ('LA, BA, ES, HI, ...', 9, 195), -- Sample Data
        (' ', 10, 195), -- Null Handling
        (' ', 11, 195), -- De-Identified
        (' ', 12, 195), -- Additional Notes
        ('Categorical', 13, 195), -- Data Type

        -- Row 23
    	('Class Managing College - Home Campus', 2, 196), -- Friendly Name
        ('Code specifying the home campus of the managing college', 3, 196), -- Description
        ('Class Attribute', 4, 196), -- Category
        ('SIS', 5, 196), --Source
        (' ', 6, 196), -- Type
        ('Peoplesoft', 7, 196), -- Name
        ('Class Term', 8, 196), -- Dataset Name
        ('TEMPE, WEST, POLY, ...', 9, 196), -- Sample Data
        (' ', 10, 196), -- Null Handling
        (' ', 11, 196), -- De-Identified
        (' ', 12, 196), -- Additional Notes
        ('Categorical', 13, 196), -- Data Type

        -- Row 24
    	('Primary Instructor ID', 2, 197), -- Friendly Name
        ('Unique 10-character numerical ID for the instructor listed as primary for the class', 3, 197), -- Description
        ('Identifier', 4, 197), -- Category
        ('SIS', 5, 197), --Source
        (' ', 6, 197), -- Type
        ('Peoplesoft', 7, 197), -- Name
        ('Class Term', 8, 197), -- Dataset Name
        ('1000768561, ...', 9, 197), -- Sample Data
        (' ', 10, 197), -- Null Handling
        ('De-Identified', 11, 197), -- De-Identified
        (' ', 12, 197), -- Additional Notes
        ('Categorical', 13, 197), -- Data Type

        -- Row 25
    	('Class Start Date', 2, 198), -- Friendly Name
        ('Date the class officially begins', 3, 198), -- Description
        ('Class Attribute', 4, 198), -- Category
        ('SIS', 5, 198), --Source
        (' ', 6, 198), -- Type
        ('Peoplesoft', 7, 198), -- Name
        ('Class Term', 8, 198), -- Dataset Name
        ('1/11/2012', 9, 198), -- Sample Data
        (' ', 10, 198), -- Null Handling
        (' ', 11, 198), -- De-Identified
        (' ', 12, 198), -- Additional Notes
        ('Discrete', 13, 198), -- Data Type

        -- Row 26
    	('Class End Date', 2, 199), -- Friendly Name
        ('Date the class officially ends', 3, 199), -- Description
        ('Class Attribute', 4, 199), -- Category
        ('SIS', 5, 199), --Source
        (' ', 6, 199), -- Type
        ('Peoplesoft', 7, 199), -- Name
        ('Class Term', 8, 199), -- Dataset Name
        ('5/5/2012', 9, 199), -- Sample Data
        (' ', 10, 199), -- Null Handling
        (' ', 11, 199), -- De-Identified
        (' ', 12, 199), -- Additional Notes
        ('Discrete', 13, 199), -- Data Type

        -- Row 27
    	('Class Modality', 2, 200), -- Friendly Name
        ('Description of the delivery method for the class which also specifies hybrid and TV-based instruction', 3, 200), -- Description
        ('Class Attribute', 4, 200), -- Category
        ('SIS', 5, 200), --Source
        (' ', 6, 200), -- Type
        ('Peoplesoft', 7, 200), -- Name
        ('Class Term', 8, 200), -- Dataset Name
        ('HY, P, OL, TV', 9, 200), -- Sample Data
        (' ', 10, 200), -- Null Handling
        (' ', 11, 200), -- De-Identified
        (' ', 12, 200), -- Additional Notes
        ('Categorical', 13, 200), -- Data Type

        -- Row 28
    	('Class Modality, Asynchronous Delivery Method', 2, 201), -- Friendly Name
        ('Description of the delivery method for the class which distinguishes different types of asynchronous instruction', 3, 201), -- Description
        ('Class Attribute', 4, 201), -- Category
        ('SIS', 5, 201), --Source
        (' ', 6, 201), -- Type
        ('Peoplesoft', 7, 201), -- Name
        ('Class Term', 8, 201), -- Dataset Name
        ('oCourse, iCourse, GFA, Immersion', 9, 201), -- Sample Data
        (' ', 10, 201), -- Null Handling
        (' ', 11, 201), -- De-Identified
        (' ', 12, 201), -- Additional Notes
        ('Categorical', 13, 201), -- Data Type

        -- Row 29
    	('Class Modality, New - including Sync', 2, 202), -- Friendly Name
        ('Alternative/new description of the delivery method for the class which specifies Sync classes and combines i & oCourses', 3, 202), -- Description
        ('Class Attribute', 4, 202), -- Category
        ('SIS', 5, 202), --Source
        (' ', 6, 202), -- Type
        ('Peoplesoft', 7, 202), -- Name
        ('Class Term', 8, 202), -- Dataset Name
        ('TBA, Internet Only, In-person Only, ASU Sync-Eligible, ASU Sync-Only, Internet, In-Person, ASU Sync', 9, 202), -- Sample Data
        (' ', 10, 202), -- Null Handling
        (' ', 11, 202), -- De-Identified
        (' ', 12, 202), -- Additional Notes
        ('Categorical', 13, 202), -- Data Type

        -- Row 30
    	('Class Location - Campus', 2, 203), -- Friendly Name
        ('Code specifying the campus where the class is held', 3, 203), -- Description
        ('Class Attribute', 4, 203), -- Category
        ('SIS', 5, 203), --Source
        (' ', 6, 203), -- Type
        ('Peoplesoft', 7, 203), -- Name
        ('Class Term', 8, 203), -- Dataset Name
        ('ONLINE, ASUONLINE, TEMPE, ICOURSE, WEST, LAHVC, ...', 9, 203), -- Sample Data
        (' ', 10, 203), -- Null Handling
        (' ', 11, 203), -- De-Identified
        (' ', 12, 203), -- Additional Notes
        ('Categorical', 13, 203); -- Data Type


