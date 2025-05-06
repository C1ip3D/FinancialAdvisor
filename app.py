from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os


client = OpenAI()
load_dotenv()

apiKey = os.getenv("OPENAI")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    stocks = data['stocks']
    result = analysis(stocks)
    return jsonify({'result': result})

@app.route('/trending')
def trending():
    result = trending()
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)


def analysis(stocks):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a financial advisor expert."},
                {"role": "user", "content": f"Analyze these stocks and provide insights based on the future and ROI: {stocks}"}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def trending():
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a financial advisor expert."},
                {"role": "user", "content": "What are the current trending stocks and why? Give specifics"}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"