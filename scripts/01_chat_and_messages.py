from langchain.messages import SystemMessage, HumanMessage, AIMessage

from config import chat_model, rule

model = chat_model()

# response = model.invoke("Name the two paddy cultivation seasons in Sri Lanka.")

# print(response.content)

# print(response.usage_metadata)

rule("MESSAGES HAVE ROLES")

messages = [
    SystemMessage("You are a terse agricultural advisor for Sri Lankan farmers."),
    HumanMessage("What is Bg 300?"),
]

response = model.invoke(messages)

print(response.text)

# rule("New follow up question for Bg 300")

# print(model.invoke([HumanMessage("How long does it take to mature?")]))

rule("We need to maintain the list of messsage")

print(type(response))

messages.append(response)
messages.append(HumanMessage("How long does it take to mature?"))

print("sending", len(messages), "messages:")
for m in messages:
    print(f"   {type(m).__name__:14s} {m.text[:52]!r}")

follow_up = model.invoke(messages)
print()
print(follow_up.text)

rule("YOU CAN PUT WORDS IN ITS MOUTH")
faked = [
    SystemMessage("You are a terse agricultural advisor."),
    HumanMessage("What is Bg 300?"),
    AIMessage("Bg 300 is a three-month paddy variety."),
    HumanMessage("And how much urea does that age class need in total?"),
]

print(model.invoke(faked).text)