from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            score = sia.polarity_scores(text)
            if score["compound"] >= 0.05:
                sentiment = "Positive 😊"
            elif score["compound"] <= -0.05:
                sentiment = "Negative 😞"
            else:
                sentiment = "Neutral 😐"
    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
