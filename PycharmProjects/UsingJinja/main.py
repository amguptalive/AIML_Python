import random
import datetime
import requests

from flask import Flask, render_template

app = Flask(__name__)
my_params = {"name": "Amit gupta",
             "country_id": "US"}


# response = requests.get(url=my_url, params=my_params)
# print(response.text)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    today = datetime.date.today()
    year = today.year

    return render_template("index.html", num=random_number, current_year=year)


@app.route('/guess/<name>')
def guess(name):
    person_name = name
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()

    person_gender = gender_data["gender"].lower()

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    # print(age_data["age"])
    person_age = age_data["age"]
    return render_template("guess.html", name=person_name,
                           age=person_age, gender=person_gender)


@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
