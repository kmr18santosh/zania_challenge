import json
from src.question_answering import preprocess_questions, answer_questions
from src.slack_integration import post_to_slack

def main(pdf_path: str, questions: list, slack_channel: str):
    """
    Main function to process PDF, generate answers, and post them to Slack.

    Args:
        pdf_path (str): Path to the PDF file.
        questions (list): List of questions to answer.
        slack_channel (str): Slack channel ID to post the results.
    """
    # Preprocess questions
    questions = preprocess_questions(questions)

    # Generate answers to the questions
    answers = answer_questions(pdf_path, questions)

    # Format the answers as structured JSON
    output_json = json.dumps(answers, indent=4)
    print(output_json)

    # Post the JSON output to Slack
    post_to_slack(slack_channel, output_json)

if __name__ == "__main__":
    pdf_path = "resource/zania handbook.pdf"  # Path to the PDF file
    questions = [
        "What is the name of the company?", 
        "Who is the CEO of the company?", 
        "What is the leave policy?", 
        "What is the termination policy?"
    ]
    slack_channel = "C07GY7UTYQ4"  # Slack channel ID
    main(pdf_path, questions, slack_channel)
