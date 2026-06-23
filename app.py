import json
import pandas as pd
import random
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, session

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]


creds_dict = json.loads(
    os.environ["GOOGLE_CREDENTIALS"]
)

creds = ServiceAccountCredentials.from_json_keyfile_dict(
    creds_dict,
    scope
)

client = gspread.authorize(creds)

sheet = client.open_by_key(
    "1DOGv3geh-f_p8AJkMmNmOkzliau8FaJPsFMcFynm7Ag"
).sheet1

app = Flask(__name__)
app.secret_key = "mock_test"

def load_questions(course):
    file_map = {
        'DA' : "data/da_questions.json",
        'DS' : 'data/ds_questions.json',
        'AWS' : 'data/aws_saa_c03_exam_bank.json',
        'AZURE' : 'data/azure_az104_exam_bank.json',
        'DEVOPS': 'data/devops_exam_bank.json',
        "JAVA" : 'data/java.json',
        'WEBDEV' : 'data/front-end-questions.json',
        'DJANGO': 'data/django-questions.json',
        'CYBER' : 'data/CEH_v13_50_MCQ_Set_1.json',
        'CCNA' : 'data/ccna_200_301_exam_bank.json',
        'CCNP' : 'data/ccnp.json',
        'DM' : 'data/digital_marketing_mcqs.json',
        'GENAI' : 'data/gen_ai_100_mcqs.json',
        'AGENTICAI' : 'data/agentic_ai_100_mcqs.json',
        'MONGODB' : 'data/mongodb_100_interview_questions.json'
    }

    with open(file_map[course], "r", encoding = "utf-8") as f:
        questions = json.load(f)
    return questions

def save_results(name, enroll_no, batch_no, trainer_name, course, score, percentage):
    sheet.append_row(
        [
            name, enroll_no,
            batch_no, trainer_name, 
            course, score,
            percentage,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ]
    )



# sign up page

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        session["name"] = request.form["name"]
        session["enroll_no"] = request.form["enroll_no"]
        session["batch_no"] = request.form["batch_no"]
        session["trainer_name"] = request.form["trainer_name"]
        # course = request.form["course"]

        return redirect(url_for("courses"))
    return render_template("home.html")

# courses
@app.route("/courses")
def courses():

    return render_template(
        "courses.html"
    )


# exam page
@app.route("/exam/<course>")
def exam(course):

    questions = load_questions(course)
    
    random.shuffle(questions)

    session["course"] = course

    session["questions"] = questions

    return render_template(
        "exam.html",
        questions=questions,
        course=course
    )

# submit exam
@app.route("/submit_exam", methods=["POST"])
def submit_exam():
    questions = session.get("questions", [])
    score = 0
    review = []

    for idx, question in enumerate(questions):
        selected = request.form.get(f"q{idx}")   # None if skipped
        correct_option = question["answer"]

        if selected == correct_option:
            score += 1

        review.append({
            "question":       question["question"],
            "options":        question["options"],   # list of strings
            "correct_answer": correct_option,
            "student_answer": selected               # None if skipped
        })

    total_questions = len(questions)
    percentage = round((score / total_questions) * 100, 2) if total_questions > 0 else 0
    skipped_count = sum(1 for r in review if not r["student_answer"])

    save_results(
        session["name"], session["enroll_no"],
        session["batch_no"], session["trainer_name"],
        session["course"], score,
        percentage
    )

    return render_template(
        "result.html",
        score=score,
        total=total_questions,
        percentage=percentage,
        review=review,
        skipped_count=skipped_count
    )

if __name__ == "__main__":
    app.run(debug = True)
