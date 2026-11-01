from langchain.messages import HumanMessage, SystemMessage

from config import chat_model, rule
from corpus import DOCS

model = chat_model()

QUESTION = (
    "I am growing Bg 300 paddy under irrigation in the Dry Zone. "
    "Exactly how much urea should I apply, and at what times? "
    "Give me the schedule in kg per hectare."
)

SYSTEM = SystemMessage("You are an advisor for Sri Lankan paddy farmers.")

rule("ASK IT THREE TIMES")
print(QUESTION)

# for attempt in (1, 2, 3):
#     print(f"\n--- attempt {attempt} " + "-" * 50)
#     print(model.invoke([SYSTEM, HumanMessage(QUESTION)]).text)


rule("COPY THE DOCS INTO THE PROMPT")

facts = "\n\n".join(f"[{d['source']}]\n{d['text']}" for d in DOCS)

print(facts)