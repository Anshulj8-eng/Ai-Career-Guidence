
def analyze_skill_gap(user_skills,role):

    role_skills={
        "AI Engineer":["Python","ML","Docker","AWS","FastAPI"],
        "Data Scientist":["Python","SQL","Statistics","ML"]
    }

    required=role_skills.get(role,[])

    missing=[skill for skill in required if skill not in user_skills]

    return {
        "target_role":role,
        "missing_skills":missing
    }
