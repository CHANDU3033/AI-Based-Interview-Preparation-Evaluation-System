import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ".")

import json

from app.database import SessionLocal, create_tables
from app.models.question import JobRole, Question
from app.data.question_bank import QUESTION_BANK, JOB_ROLES


def seed_database():
    create_tables()
    db = SessionLocal()
    try:
        if db.query(JobRole).count() > 0:
            print("[OK] Database already seeded. Skipping.")
            return

        print("Seeding job roles...")
        role_map = {}
        for role_data in JOB_ROLES:
            role = JobRole(**role_data)
            db.add(role)
            db.flush()
            role_map[role_data["role_name"]] = role.id
            print(f"  + Role: {role_data['role_name']} (id={role.id})")

        print(f"\nSeeding {len(QUESTION_BANK)} questions...")
        inserted = 0
        for q_data in QUESTION_BANK:
            q = dict(q_data)
            role_name = q.pop("role")
            role_id = role_map.get(role_name)
            if not role_id:
                print(f"  [WARNING] Unknown role: {role_name}, skipping question.")
                continue
            q["role_id"] = role_id
            if isinstance(q.get("expected_concepts"), list):
                q["expected_concepts"] = json.dumps(q["expected_concepts"])
            db.add(Question(**q))
            inserted += 1

        db.commit()
        print(f"\n[SUCCESS] Seeded {len(JOB_ROLES)} roles and {inserted} questions successfully!")

    except Exception as e:
        db.rollback()
        print(f"[ERROR] Error seeding database: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
