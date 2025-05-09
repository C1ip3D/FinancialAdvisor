from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

apiKey = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=apiKey)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


def get_stock_analysis(stocks, budget):  
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "system",
                    "content": "You are a financial advisor expert whose main goal is to help the user. You will let them know about stocks you believe are good and what you know they should invest in. Remember to always keep an eye on the news and make sure that stocks you tell won't have any negative event that will bring it down soon. Also you are helping an AP economics student so keep that in mind",
                },
                {
                    "role": "user",
                    "content": f"Please analyze this stock and provide insights based on the future and ROI. Mention whether it would be short or long term and what kind of returns you predict. Also include in a short sentence talking about the EPS, market cap, P/E Ratio, and Divident yield with a short explanation whether it would be good or bad. Keep the sentences more simple and also include recent news that might negatively affect this stock. You also please tell us how much money in dollars we should invest out of our mentioned ${budget} that we should use for it. Write it in the form of <li> tags from Javascript. Thank you. Make sure not to list out the syntax requirements we gave you and the header in the output.: {stocks}. ",
                },
            ],
            temperature=0.7,
            max_tokens=500,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


def get_trending_stocks(): 
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "system",
                    "content": "You are a financial advisor expert whose main goal is to help the user. You will let them know about stocks you believe are good and what you know they should invest in. Remember to always keep an eye on the news and make sure that stocks you tell won't have any negative event that will bring it down soon.",
                },
                {
                    "role": "user",
                    "content": "What are future lucrative stocks and why? Only give a bullet point list with short and simple sentences. Give us 3 sections, low, moderate, and high volatility and also the assosiated risk levels. make sure to mention whether the stock would be short term or long term. Also make sure that you only show stocks that you believe the user should invest in. Also make sure to mention in a sentence that if they have any inquiries about a specific stock they can ask about it in the other box. Thank you. Make sure not to list out the syntax requirements we gave you and the header in the output. ",
                },
            ],
            temperature=0.7,
            max_tokens=500,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    stocks = data["stocks"]
    budgets = data['budgets']
    result = get_stock_analysis(stocks, budgets) 
    return jsonify({"result": result})


@app.route("/trending")
def trending():
    result = get_trending_stocks()
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
