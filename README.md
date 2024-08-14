# Zania Handbook Q&A Automation

## Project Overview
This project automates the process of extracting information from the Zania handbook PDF and answers specific questions based on the content. The answers are formatted as a JSON object and can be automatically posted to a Slack channel.

## Features
- Extracts and segments text from a PDF based on the Table of Contents.
- Uses OpenAI's GPT model to generate answers to user-defined questions.
- Posts the answers to a specified Slack channel.
- Handles both exact-match answers and low-confidence scenarios.

## Requirements
- Python 3.7+
- Libraries: `openai`, `fitz` (PyMuPDF), `dotenv`, `slack-sdk`
- A Slack workspace with a channel and a Slack app with an OAuth token.
- An OpenAI API key.

## Installation
- Clone the repository:
  ```bash
  git clone https://github.com/your-repo/zania_challenge.git

## Set up environment variables:
- Create a .env file in the project root and add your OpenAI API key and Slack bot token:
  ```bash
  OPENAI_API_KEY=your_openai_api_key
  SLACK_BOT_TOKEN=your_slack_bot_token
  
## Usage
Run the script to generate answers and post them to Slack:
  ```bash
  python main.py
