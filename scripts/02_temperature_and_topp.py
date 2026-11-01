from config import chat_model, rule

PROMPT = "Pick a random whole number between 1 and 100. Reply with only the number."
SAMPLES = 20

def roll(model, label):
    """Roll the prompt SAMPLES times under one model config, print the spread.

    The model is asked for a bare number, so roll results are reduced to
    digits — otherwise an odd character can sneak into the printed output.
    """
    rolls = []
    for _ in range(SAMPLES):
        text = model.invoke(PROMPT).text.strip()
        rolls.append(text)
    distinct = len(set(rolls))
    print(f"   {label:12s}  " + "  ".join(rolls) + f"   ->  {distinct} distinct")
    return rolls

cold = chat_model(reasoning_effort="none", temperature=0)
hot = chat_model(reasoning_effort="none", temperature=1.6)

roll(cold, "temperature=0")

roll(hot, "temperature=2.0")