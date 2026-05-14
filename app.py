from flask import Flask, render_template
import os

app = Flask(__name__)
posts_dir = 'posts'

@app.route('/')
def index():
    files = sorted(os.listdir(posts_dir), reverse=True)
    posts = [f.replace('.md','').replace('-',' ').title() for f in files if f.endswith('.md')]
    return render_template('index.html', posts=posts)

@app.route('/post/<name>')
def show_post(name):
    path = os.path.join(posts_dir, name + '.md')
    if not os.path.exists(path):
        return "Not found", 404
    with open(path) as f:
        content = f.read()
    return render_template('post.html', title=name, content=content)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/about')
def about():
    return '<h1>About this blog</h1>'
