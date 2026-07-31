from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def chat_response(message,resume_text):

    completion = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[

        {
        "role":"system",

        "content":f"""
        You are CareerAI assistant.

        User resume:

        {resume_text}

        Use this resume to provide
        personalized advice,
        career guidance,
        interview help,
        skill suggestions.
        """
        },

        {
        "role":"user",
        "content":message
        }

        ]

    )

    return completion.choices[0].message.content