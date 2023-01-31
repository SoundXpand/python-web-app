from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.form["user_question"]
    chatbot_response = "This is a response from Chatbot."
    return render_template("index.html", user_question=user_question, chatbot_response=chatbot_response)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()
