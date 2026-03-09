from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


def generate_feedback(scenario, choice):
    prompt = f"""
You are evaluating decisions in a serious training game.

Scenario:
{scenario}

Player choice:
{choice}

Give:
1. A score (0-10)
2. A short explanation
3. A suggestion
"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


def generate_summary(history):

    prompt = f"""
The player completed a serious decision-making game.

Decision history:
{history}

Provide:
1. Overall evaluation
2. Decision-making style
3. Suggestions for improvement
"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content