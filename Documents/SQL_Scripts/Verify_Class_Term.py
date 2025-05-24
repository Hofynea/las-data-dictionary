# ===========================================================================================
# Class Term Entry - Label and Entry Verification Script
# ===========================================================================================
# This script verifies the correctness of data inserted into the `core_label` and 
# `core_entry` tables for Class Term (table_id_id = 4).
#
# Checks performed:
# - Ensures 30 `core_label` entries exist with the correct `label_index` and `label_name`.
# - Verifies that each `label_id` associated with this dataset has all expected `field_id`
#   entries in `core_entry` (field_id: 2–13, inclusive).
#
# Assumptions:
# - `label_id` ranges from 174-203 are used for Canvas Discussion Entry Fields.
# - Each label must have exactly 12 rows (field_id 2–13) in `core_entry`.
#
# Author: Daria Ilchenko
# Modified by: Seth Cabral, Full credit to Daria Ilchenko for base code provided. 
# Code was modified to test Class Term specific entries
# Date: 04/11/2025
# ===========================================================================================

import psycopg2

# Database credentials
DB_CONFIG = {
    'dbname': 'las_data_dictionary',
    'user': 'postgres',
    'password': '0000',
    'host': '18.220.136.53',
    'port': 5432,
}

# Expected label names (label_index 1 to 34)
EXPECTED_FIELDS = [
    'cls_id', 'trm_cd', 'cls_nbr_id', 'crs_id', 'crs_cd', 'crs_subject_cd',
    'crs_catalog_cd', 'crs_catalog_extn_cd', 'crs_descr', 'crs_Id', 'crs_topic_id',
    'crs_topic_descr', 'cls_type_cd', 'cls_type_ssr_cd', 'cls_stat_sched_cd',
    'cls_stat_reg_flg', 'cls_stat_display_search_flg', 'cls_cmb_id', 'crs_cmb_cd',
    'cls_ses_cd', 'cls_unit_cd', 'cls_coll_cd', 'cls_coll_cmps_cd',
    'cls_prim_instr_id', 'cls_start_dt', 'cls_end_dt', 'cls_modality_instrn_cd',
    'cls_modality_loc_descr', 'cls_modality_extn_descr', 'cls_loc_cmps_cd'
]

# Expected field_id values in core_entry for each label_id
EXPECTED_FIELD_IDS = list(range(2, 14))  # 2 through 13 inclusive

# Label IDs used in Class Entry (hardcoded)
EXPECTED_LABEL_IDS = list(range(174, 203))


def verify_labels(cursor):
    # Verifies that all expected labels are present in the core_label table with correct names.

    print("Verifying `core_label` entries...\n")
    cursor.execute("""
        SELECT label_index, label_name
        FROM core_label
        WHERE table_id_id = 4
        ORDER BY label_index
    """)
    rows = cursor.fetchall()
    found_fields = {index: name for index, name in rows}

    for idx, expected_name in enumerate(EXPECTED_FIELDS, start=1):
        actual_name = found_fields.get(idx)
        if actual_name == expected_name:
            print(f"Field {idx}: {expected_name}")
        elif actual_name:
            print(f"Field {idx} mismatch: expected '{expected_name}', found '{actual_name}'")
        else:
            print(f"Missing field {idx}: expected '{expected_name}'")

    if len(found_fields) > len(EXPECTED_FIELDS):
        print("\nExtra fields found in `core_label`:")
        for idx in range(len(EXPECTED_FIELDS) + 1, max(found_fields.keys()) + 1):
            print(f"  - Field {idx}: {found_fields[idx]}")


def verify_entries(cursor):
    # Verifies that all expected field_id values exist for each label_id in core_entry.
    
    print("\nVerifying `core_entry` entries...\n")
    for label_id in EXPECTED_LABEL_IDS:
        cursor.execute("""
            SELECT field_id FROM core_entry
            WHERE label_id = %s
        """, (label_id,))
        rows = cursor.fetchall()
        found_field_ids = sorted(row[0] for row in rows)
        missing = [fid for fid in EXPECTED_FIELD_IDS if fid not in found_field_ids]
        extra = [fid for fid in found_field_ids if fid not in EXPECTED_FIELD_IDS]

        if not missing and not extra:
            print(f"label_id {label_id}: all expected field_id values present")
        else:
            if missing:
                print(f"label_id {label_id} is missing field_ids: {missing}")
            if extra:
                print(f"label_id {label_id} has extra unexpected field_ids: {extra}")


def main():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        verify_labels(cursor)
        verify_entries(cursor)

    except Exception as e:
        print("Error during verification:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    main()
