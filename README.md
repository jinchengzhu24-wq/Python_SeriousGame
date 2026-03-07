# AI Serious Game for Constructive Online Conversations

## Introduction

This project explores how AI-supported serious games can help users practice constructive responses in hostile online conversations.

The system simulates online discussion scenarios and allows users to choose different responses. An AI system then provides feedback and guidance to encourage more constructive and empathetic communication.

The project is inspired by the research paper:

ExploreSelf: Fostering User-driven Exploration and Reflection on Personal Challenges with Adaptive Guidance by Large Language Models.

## Research Goal

Online discussions often become hostile due to emotional reactions and misunderstandings.

The goal of this project is to design an AI-supported interactive system that helps users reflect on their communication style and practice better responses in simulated conversations.

Instead of only asking reflective questions, the system extends the idea into a scenario-based serious game where users actively make decisions during simulated online interactions.

## Game Concept

The system presents simulated online discussion scenarios.

Example:

Someone replies to your post:

"Your opinion makes no sense."

The user can choose how to respond:

- Reply angrily
- Ignore the comment
- Calmly explain their perspective

After the user makes a choice, the AI system analyzes the response and provides feedback to encourage constructive communication.

## Technology Stack

- Python
- Flask
- OpenAI API
- HTML / CSS

## Project Structure

ai-serious-game/
│
├── app.py
├── templates/
│ └── index.html
├── static/
│ └── style.css
├── game_logic.py
└── README.md

## How to Run

1. Install dependencies

pip install flask openai python-dotenv

2. Run the server

python app.py

3. Open browser

http://127.0.0.1:5000

## Author

Jincheng Zhu