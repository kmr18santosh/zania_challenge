import os
from dotenv import load_dotenv
from openai import OpenAI
from src.pdf_processing import get_section_from_toc

# Load environment variables
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def preprocess_questions(questions: list) -> list:
    """
    Strips whitespace from each question in the list.

    Args:
        questions (list): List of questions.

    Returns:
        list: Preprocessed list of questions.
    """
    return [question.strip() for question in questions]

def answer_questions(pdf_path: str, questions: list) -> dict:
    """
    Answers a list of questions based on the content of a PDF.

    Args:
        pdf_path (str): Path to the PDF file.
        questions (list): List of questions to answer.

    Returns:
        dict: Dictionary of questions and their corresponding answers.
    """
    answers = {}
    for question in questions:
        section_text = get_section_from_toc(pdf_path, question)
        if not section_text:
            answers[question] = "Data Not Available"
            continue
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Use the specified model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Question: {question}\n\nContext:\n{section_text}"}
            ],
            max_tokens=500,
            temperature=0.5,
        )
        answer = response.choices[0].message.content.strip()
        answers[question] = answer

    return answers
