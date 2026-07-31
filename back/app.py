from db import init_db
from skill_gap import analyze_skill_gap
from flask import Flask, render_template, request , jsonify
from flask_cors import CORS
from resume_parser import extract_resume_text
from skill_gap import analyze_skill_gap
from recommendation import recommend_jobs
from chatbot import chat_response
import re
from flask import send_file
from dotenv import load_dotenv
load_dotenv()
stored_resume = ""
app = Flask(__name__)
CORS(app)

init_db(app)
@app.route("/")


def home():
    return render_template("index.html")


@app.route("/upload_resume", methods=["POST"])
def upload_resume():

    file = request.files["resume"]

    file.save("temp_resume.pdf")

    global stored_resume
    text = extract_resume_text(
    "temp_resume.pdf"
    )
    stored_resume = text

    print(text)

    text = text.lower()

    text = re.sub(
        r'[^a-zA-Z0-9 ]',
        ' ',
        text
    )

    skill_list = [

    "python","java","c","c++","c#","javascript",
    "typescript","r","php","go","rust",

    "html","css","react","angular","vue",
    "nodejs","node js","expressjs",
    "flask","django","fastapi","streamlit",

    "mysql","sql","mongodb",
    "postgresql","sqlite","oracle",
    "firebase",

    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "computer vision",
    "feature engineering",
    "supervised learning",
    "unsupervised learning",
    "regression",
    "classification",

    "tensorflow",
    "keras",
    "pytorch",
    "scikit learn",
    "scikit-learn",
    "xgboost",

    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "statistics",
    "data analysis",
    "data visualization",

    "opencv",
    "yolo",

    "aws",
    "azure",
    "gcp",
    "docker",
    "kubernetes",
    "ci cd",
    "git",
    "github",

    "hadoop",
    "spark",

    "rest api",
    "graphql",

    "jupyter",
    "vs code",
    "linux",

    "langchain",
    "rag",
    "agentic ai",
    "llm",
    "gemini",
    "groq",
    "ollama",
    "transformers"

    ]

    detected=[]

    words = set(text.split())

    for skill in skill_list:

        skill_words = skill.split()

        if len(skill_words)==1:

            if skill_words[0] in words:
                detected.append(skill)

        else:

            if skill in text:
                detected.append(skill)

    detected = list(set(detected))

    return jsonify({

        "skills": detected,
        "resume_text": text

    })
@app.route("/download_resume")
def download_resume():

    return send_file(
        "temp_resume.pdf",
        as_attachment=True
    )

@app.route("/skill_gap", methods=["POST"])
def skill_gap():

    data=request.json

    target_role=data["role"]

    skills=data["skills"]

    result=analyze_skill_gap(
        skills,
        target_role
    )

    return jsonify(result)

def analyze_skill_gap(user_skills, role):

    role_skills = {

"ai engineer":[
"Python","Machine Learning","Deep Learning",
"Flask","Docker","AWS","LangChain","RAG",
"LLM","TensorFlow","PyTorch"
],

"data scientist":[
"Python","SQL","Statistics",
"Pandas","Numpy",
"Machine Learning",
"Matplotlib","Seaborn"
],

"ml engineer":[
"Python","Machine Learning",
"TensorFlow","PyTorch",
"Docker","AWS","MLOps"
],

"data analyst":[
"Python","SQL",
"Excel","Power BI",
"Pandas","Data Visualization"
],

"frontend developer":[
"HTML",
"CSS",
"JavaScript",
"React",
"Bootstrap"
],

"backend developer":[
"Python",
"Flask",
"MySQL",
"REST API",
"Django"
],

"full stack developer":[
"HTML",
"CSS",
"JavaScript",
"React",
"NodeJS",
"MySQL",
"REST API"
],

"react developer":[
"HTML",
"CSS",
"JavaScript",
"React"
],

"android developer":[
"Java",
"Kotlin",
"Android Studio",
"Firebase"
],

"ios developer":[
"Swift",
"Xcode",
"Firebase"
],

"software engineer":[
"Python",
"Java",
"C++",
"Git",
"SQL"
],

"devops engineer":[
"Docker",
"Kubernetes",
"AWS",
"Linux",
"CI/CD",
"Git"
],

"cloud engineer":[
"AWS",
"Azure",
"GCP",
"Docker",
"Kubernetes"
],

"cyber security engineer":[
"Linux",
"Networking",
"Python",
"Cryptography",
"Wireshark"
],

"computer vision engineer":[
"Python",
"OpenCV",
"YOLO",
"Deep Learning",
"TensorFlow"
],

"nlp engineer":[
"Python",
"NLP",
"Transformers",
"Deep Learning",
"LangChain"
],

"llm engineer":[
"Python",
"LangChain",
"RAG",
"LLM",
"Transformers",
"Vector Database"
],

"database administrator":[
"MySQL",
"SQL",
"Oracle",
"PostgreSQL"
],

"ui ux designer":[
"Figma",
"Adobe XD",
"Wireframing"
],
"data engineer":[
"Python",
"SQL",
"MySQL",
"PostgreSQL",
"Pandas",
"ETL",
"Data Warehousing",
"Hadoop",
"Spark",
"AWS",
"Docker",
"Airflow"
],

"game developer":[
"C++",
"Unity",
"Unreal Engine",
"C#"
],

"blockchain developer":[
"Solidity",
"Ethereum",
"Web3",
"JavaScript"
],

"embedded engineer":[
"C",
"C++",
"Microcontrollers",
"Arduino"
],

"network engineer":[
"Networking",
"Cisco",
"Linux"
],

"qa engineer":[
"Selenium",
"Python",
"Testing"
]

}

    role = role.strip().lower()

    required = role_skills.get(role, [])

    # normalize detected skills
    user_skills_lower = set(
        skill.strip().lower()
        for skill in user_skills
    )

    detected=[]
    missing=[]

    for skill in required:

        normalized_skill = skill.strip().lower()

        if normalized_skill in user_skills_lower:

            detected.append(skill)

        else:

            missing.append(skill)

    match_score = 0

    if len(required)>0:
        match_score = (
            len(detected)/len(required)
        )*100

    return {

    "role": role.title(),
    "detected_skills": detected,
    "missing_skills": missing,
    "match_score": round(match_score,2)

    }
@app.route("/recommend_jobs", methods=["POST"])
def jobs():

    data=request.json

    skills=data["skills"]

    jobs=recommend_jobs(skills)

    return jsonify({
        "recommended_jobs":jobs
    })
def recommend_jobs(skills):

    skills = [skill.lower() for skill in skills]

    jobs=[]

    if ("python" in skills and
        "machine learning" in skills):

        jobs.append("Machine Learning Engineer")

    if ("python" in skills and
        "flask" in skills):

        jobs.append("Backend Developer")

    if ("html" in skills and
        "css" in skills and
        "javascript" in skills):

        jobs.append("Frontend Developer")

    if ("mysql" in skills and
        "sql" in skills):

        jobs.append("Database Developer")

    if ("python" in skills and
        "pandas" in skills and
        "statistics" in skills):

        jobs.append("Data Scientist")

    if ("tensorflow" in skills or
        "pytorch" in skills):

        jobs.append("Deep Learning Engineer")

    if ("opencv" in skills or
        "yolo" in skills):

        jobs.append("Computer Vision Engineer")

    if ("docker" in skills and
        "aws" in skills):

        jobs.append("Cloud Engineer")

    if ("langchain" in skills or
        "rag" in skills):

        jobs.append("LLM Engineer")

    if ("react" in skills):

        jobs.append("React Developer")

    if len(jobs)==0:

        jobs.append("Software Developer Intern")
        jobs.append("Junior Developer")
        jobs.append("Technical Trainee")

    return jobs
@app.route("/chat", methods=["POST"])
def chat():
    global stored_resume

    try:
        data = request.json
        msg = data.get("message", "")

        if not msg:
            return jsonify({"response": "Empty message"}), 400

        reply = chat_response(msg, stored_resume)
        if not stored_resume:
            stored_resume = "No resume uploaded yet"

        return jsonify({
            "response": reply,
            "recommended_jobs": []   # 👈 ADD THIS to avoid frontend crash
        })

    except Exception as e:
        print("CHAT ERROR:", e)
        return jsonify({
            "response": "Server error",
            "recommended_jobs": []
        }), 500
if __name__=="__main__":
    app.run(debug=True)