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

# creds = ServiceAccountCredentials.from_json_keyfile_name(
#     "credentials.json",
#     scope
# )

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
        'CLOUD' : 'data/aws_saa_c03_exam_bank.json'
        
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
        course = request.form["course"]

        return redirect(url_for("exam",course=course))
    return render_template("home.html")


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
@app.route("/submit_exam",methods = ["POST"])
def submit_exam():

    questions = session.get("questions", [])

    score = 0

    for idx, question in enumerate(questions):
        selected = request.form.get(f"q{idx}")

        correct_option = question["answer"]
        if selected == correct_option:
            score += 1
    
    total_questions = len(questions)

    if total_questions > 0:
        percentage = round((score / total_questions) * 100, 2)
    else:
        percentage = 0    
    save_results(
        session["name"],session["enroll_no"],
        session["batch_no"], session["trainer_name"],
        session["course"], score, 
        percentage
    )
    return render_template("result.html", score = score, total = total_questions, percentage = percentage)


if __name__ == "__main__":
    app.run(debug = True)
