from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    english_text = request.args.get('textToTranslate')
    print(english_text)
    french_text = translator.englishToFrench(english_text)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    french_text = request.args.get('textToTranslate')
    print(french_text)
    english_text = translator.frenchToEnglish(french_text)
    return english_text

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
