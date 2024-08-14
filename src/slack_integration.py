# src/slack_integration.py
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def post_to_slack(channel: str, message: str):
    client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
    
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=message
        )
    except SlackApiError as e:
        print(f"Error posting to Slack: {e.response['error']}")
