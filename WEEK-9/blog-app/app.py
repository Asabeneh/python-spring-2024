from flask import Flask, render_template, jsonify, request, redirect, url_for
from mysql.connector import connect

app = Flask(__name__)

db = connect(
    host ='localhost',
    user = 'root',
    password = 'root',
    database = 'blog_db'
    
)
cursor = db.cursor()
# cursor.execute('USE blog_db')
""" cursor = db.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS blog_db')
cursor.execute('USE blog_db')
query = 'create table if not exists blogs (id int primary key auto_increment, title varchar(150), subtitle varchar(150), content TEXT)'
cursor.execute(query) """

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/v1/blogs')
def blog_api():
    cursor.execute('SELECT * FROM blogs')
    items = cursor.fetchall()
    blogs = list( map(lambda lst : {
        'id': lst[0],
         'title':lst[1],
         'subtitle':lst[2],
         'content':lst[3]
    }, items))
    return jsonify(blogs)
    

@app.route('/blogs')
def blogs():
    
    cursor.execute('SELECT * FROM blogs')
   
    items = cursor.fetchall()
    blogs = list( map(lambda lst : {
        'id': lst[0],
         'title':lst[1],
         'subtitle':lst[2],
         'content':lst[3]
    }, items))
   
    

    return render_template('blogs.html', blogs = blogs, number = len(blogs))

@app.route('/blog/<id>')
def blog_details(id):
    cursor.execute('SELECT * FROM blogs WHERE id = %s', (id,))
    item = cursor.fetchone()
    blog = {
        'id': item[0],
         'title':item[1],
         'subtitle':item[2],
         'content':item[3]
    }
    return render_template('blog-details.html', blog = blog)

@app.route('/blog/create', methods = ['GET', 'POST'])
def add_blog():
    if request.method == 'POST':
        form = request.form 
        title = form.get('title') 
        subtitle = form.get('subtitle') 
        content = form.get('content')
        cursor.execute('INSERT INTO blogs (title, subtitle, content) VALUES (%s, %s, %s)', (title, subtitle, content))
        db.commit()
        return redirect(url_for('blogs'))
    return render_template('add-blog.html')

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 5000)