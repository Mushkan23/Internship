from flask import Flask, request,render_template
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['registration']
collection = db['users']
@app.route('/')
def index():
    return render_template('register.html')
@app.route('/register',methods=["POST"])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    db.users.insert_one({'name':name,'email':email,'password':password})
    return 'Registration Successfull'
if __name__ == '__main__':
    app.run(debug=True)
