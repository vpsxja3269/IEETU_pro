from flask import Flask, render_template, redirect, url_for, request
from forms import PostForm
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'

API_URL = "http://localhost:8000"

@app.route('/')
def home():
    response = requests.get(f"{API_URL}/posts/")
    posts = response.json()
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        post_data = {
            "title": form.title.data,
            "content": form.content.data,
            "author": form.author.data
        }
        requests.post(f"{API_URL}/posts/", json=post_data)
        return redirect(url_for('home'))
    return render_template('post.html', form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
