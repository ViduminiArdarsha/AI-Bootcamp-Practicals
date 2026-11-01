import os
import sys

from dotenv import load_dotenv

from langchain.chat_models import init_chat_model

load_dotenv()

CHAT_MODEL = "openai:gpt-5.6-luna"


def chat_model(**kwargs):
    return init_chat_model(CHAT_MODEL, **kwargs)

def rule(title: str = "") -> None:
    """Section heading, so a script reads like a lesson while it runs."""
    print("\n" + "=" * 78)
    if title:
        print(title)
        print("=" * 78)