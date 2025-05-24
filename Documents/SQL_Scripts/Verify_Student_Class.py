# ===========================================================================================
# Student Class - Label and Entry Verification Script
# ===========================================================================================
# This script verifies the correctness of data inserted into the `core_label` and 
# `core_entry` tables for the Student Class table (table_id_id = 3).
#
# Checks performed:
# - Ensures 23 `core_label` entries exist with the correct `label_index` and `label_name`.
# - Verifies that each `label_id` has all expected `field_id` values in `core_entry`.
#
# Assumptions:
# - label_ids for Student Class range from 8 to 30 (inclusive).
# - Each label must have exactly 12 rows in `core_entry` corresponding to field_id 2–13.
#
# Author: Daria Ilchenko
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

# Expected label names for Student Class (label_index 1–23)
EXPECTED_FIELDS = [
    'stdnt_id', 'trm_cd', 'cls_id', 'cls_nbr_id', 'stdnt_cls_enrl_flg',
    'stdnt_cls_add_actl_dt', 'stdnt_cls_desig_carr_cd', 'stdnt_cls_desig_ses_cd',
    'stdnt_cls_desig_instr_id', 'stdnt_cls_desig_grade_cd', 'stdnt_cls_add_eff_dt',
    'stdnt_cls_desig_grade_pts_num', 'stdnt_cls_desig_grade_in_gpa_flg',
    'stdnt_cls_desig_grade_credit_flg', 'stdnt_cls_desig_repeat_cd',
    'stdnt_cls_grade_asr_latest_seq_num', 'stdnt_cls_grade_asr_latest_cd',
    'stdnt_cls_grade_asr_latest_actn_rsn_cd_list', 'stdnt_cls_grade_asr_latest_comment_descr',
    'stdnt_cls_grade_asr_report_seq_num', 'stdnt_cls_grade_asr_report_cd',
    'stdnt_cls_grade_asr_report_actn_rsn_cd_list', 'stdnt_cls_grade_asr_report_comment_descr'
]

# Expected field_id values in core_entry for each label_id
EXPECTED_FIELD_IDS = list(range(2, 14))  # field_id 2 through 13

# Label IDs used in Student Class
EXPECTED_LABEL_IDS = list(range(8, 31))  # label_id 8 through 30 inclusive

def verify_labels(cursor):
    print("Verifying `core_label` entries...\n")
    cursor.execute("""
        SELECT label_index, label_name
        FROM core_label
        WHERE table_id_id = 3
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
