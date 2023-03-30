from flask import Flask, render_template, request
# from bs4 import BeautifulSoup
import openai
import os
API_KEY = os.environ.get('API_KEY')
openai.api_key = API_KEY
app = Flask(__name__,template_folder='templates')


def modify_answer(answer:str):
    return answer #.replace("**", "<strong>")


@app.route('/', methods=['GET', 'POST'])
def index():
    answer = None
    if request.method == 'POST':
        # Add your code to process the input text and generate a response
        question = request.form["question"]
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )

        answer = modify_answer(completion["choices"][0]["message"]["content"])

    return render_template('index.html', answer=answer)

        # return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)