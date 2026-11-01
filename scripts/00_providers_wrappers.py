from openai import OpenAI
from dotenv import load_dotenv
import requests
import os
from langchain_openai import ChatOpenAI

load_dotenv()

CHAT_MODEL = "gpt-5.6-luna"

client= OpenAI()

QUESTION = "Name the two paddy cultivation seasons in Sri Lanka."

response = client.chat.completions.create(
    model= CHAT_MODEL,
    messages= [{"role":"user","content": QUESTION}],
)
print (response.choices[0].message.content)

# raw = requests.post(
#     "https://api.openai.com/v1/chat/completions",
#     headers= {
#         "Authorizations": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
#         "Content_Type":"application/json",
#     },
    # json= {"model":CHAT_MODEL, "messages":[{"role":"user","content":QUESTION}]}
# )

print ("="*100)

chat_model = ChatOpenAI(model=CHAT_MODEL)
response = chat_model.invoke(QUESTION)
print(response.text)