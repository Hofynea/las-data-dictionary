# ===========================================================================================
# Term Table - Label and Entry Verification Script
# ===========================================================================================
# This script verifies the correctness of data inserted into the `core_label` and 
# `core_entry` tables for the Term dataset (table_id_id = 5).
#
# Checks performed:
# - Ensures 41 `core_label` entries exist with the correct `label_index` and `label_name`.
# - Verifies that each `label_id` associated with this dataset has all expected `field_id`
#   entries in `core_entry`, excluding skipped field_ids (6, 10, 11).
#
# Assumptions:
# - `label_id` ranges from 133–173 for the Term table.
# - Each label must have 10 field_id rows (field_id: 2–13, excluding 6, 10, 11).
#
# Author: Daria Ilchenko
# Date: 04/12/2025
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

# Expected label names (from label_index 1 to 41)
EXPECTED_FIELDS = [
    'ay', 'ay_sd', 'cy', 'cy_sd', 'row_current_flg', 'row_deleted_in_source_flg',
    'ry', 'ry_sd', 'trm_cd', 'trm_cur_after_prior_flg', 'trm_cur_after_prior_regular_flg',
    'trm_cur_flg', 'trm_cur_until_next_flg', 'trm_cur_until_next_regular_flg',
    'trm_end_dt', 'trm_next1_end_dt', 'trm_next1_regular_end_dt',
    'trm_next1_regular_start_dt', 'trm_next1_start_dt', 'trm_prior1_end_dt',
    'trm_prior1_regular_end_dt', 'trm_prior1_regular_start_dt', 'trm_prior1_start_dt',
    'trm_regular_flg', 'trm_regularized_cd', 'trm_rel_cur_after_prior_ct',
    'trm_rel_cur_after_prior_regular_ct', 'trm_rel_cur_ct', 'trm_rel_cur_regular_ct',
    'trm_rel_cur_until_next_ct', 'trm_rel_cur_until_next_regular_ct',
    'trm_season_cd', 'trm_season_descr', 'trm_season_sd',
    'trm_season_yr_descr', 'trm_season_yr_ld', 'trm_season_yr_sd',
    'trm_start_dt', 'trm_yr_season_descr', 'trm_yr_season_ld', 'trm_yr_season_sd'
]

# Expected field_ids for each label (skipping 6, 10, 11)
EXPECTED_FIELD_IDS = [fid for fid in range(2, 14) if fid not in (6, 10, 11)]

# Expected label_id range for Term table
EXPECTED_LABEL_IDS = list(range(133, 174))

def verify_labels(cursor):
    print("Verifying `core_label` entries...\n")
    cursor.execute("""
        SELECT label_index, label_name
        FROM core_label
        WHERE table_id_id = 5
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
