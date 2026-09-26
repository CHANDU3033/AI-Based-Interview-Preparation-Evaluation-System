import json, os, sys
backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path: sys.path.insert(0, backend_dir)
from app.database import SessionLocal, create_tables
from app.models.question import JobRole, Question

def import_questions(json_filepath_or_data):
    create_tables()
    db = SessionLocal()
    if isinstance(json_filepath_or_data, str):
        if not os.path.exists(json_filepath_or_data):
            print(f'[ERROR] File not found: {json_filepath_or_data}')
            return
        with open(json_filepath_or_data, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = json_filepath_or_data

    roles = db.query(JobRole).all()
    role_map = {r.role_name.lower(): r.id for r in roles}
    added_count = 0
    for item in data:
        role_name_raw = item.get('role_name', 'General Technical').strip()
        role_key = role_name_raw.lower()
        role_id = role_map.get(role_key)
        if not role_id:
            for r_name, r_id in role_map.items():
                if r_name in role_key or role_key in r_name:
                    role_id = r_id
                    break
        if not role_id:
            new_role = JobRole(role_name=role_name_raw, description=f'Practice for {role_name_raw}')
            db.add(new_role)
            db.flush()
            role_id = new_role.id
            role_map[role_key] = role_id
            print(f'  + Created new Role: {role_name_raw} (id={role_id})')

        concepts = item.get('expected_concepts', [])
        concepts_str = json.dumps(concepts) if isinstance(concepts, list) else str(concepts or '')
        q = Question(
            role_id=role_id,
            category=item.get('category', 'Technical'),
            difficulty=item.get('difficulty', 'Intermediate'),
            question_text=item.get('question_text', ''),
            expected_answer=item.get('expected_answer', ''),
            expected_concepts=concepts_str
        )
        db.add(q)
        added_count += 1

    db.commit()
    db.close()
    print(f'[SUCCESS] Imported {added_count} new questions successfully into database!')

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else r'C:\Users\srika\OneDrive\Desktop\ai-interview-system\new_questions.json'
    print(f'Importing questions from: {target}')
    import_questions(target)
