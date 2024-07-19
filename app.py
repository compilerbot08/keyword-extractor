import requests
from flask import Flask, render_template, url_for
from flask import request as req
from rake_nltk import Rake
rake_nltk_var = Rake()
import nltk
nltk.download('stopwords')
nltk.download('punkt')
# from flask_frozen import Freezer

app = Flask(__name__)
# freezer = Freezer(app)

@app.route("/", methods=["GET", "POST"])
def Index():
	return render_template("index.html")




@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
	if req.method == "POST":
		text = req.form["data"]
		rake_nltk_var.extract_keywords_from_text(text)
		keyword_extracted = rake_nltk_var.get_ranked_phrases()
		print(keyword_extracted)
		output = "\n ".join(keyword_extracted)
		return render_template("index.html", result=output)
	else:
		return render_template("index.html")

	
if __name__ == '__main__':
	app.run(debug=True)
