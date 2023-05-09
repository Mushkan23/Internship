from flask import Flask, render_template, request
import json
from brain import Brain

app = Flask(__name__)

with open('intent.json') as file:
    intents = json.load(file)

bot = Brain(intents)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=['POST'])
def get_response():
    user_message = request.form["user_message"]
    bot_message = bot.get_response(user_message)
    return {"bot_message": bot_message}

if __name__ == "__main__":
     app.run(debug=True)