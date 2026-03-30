from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

def ask_ai(prompt):
    result = generator(
        prompt,
        max_new_tokens=50,
        do_sample=True,
        temperature=0.7,
        pad_token_id=50256
    )
    text = result[0]["generated_text"]
    return text.replace(prompt, "").strip()


print("AI CLI Tool")
print("Commands: /ask, /idea, /exit\n")

while True:
    user_input = input("> ")

    if user_input.lower() == "/exit":
        break

    elif user_input.startswith("/ask"):
        question = user_input.replace("/ask", "").strip()
        prompt = f"Question: {question}\nAnswer:"
        response = ask_ai(prompt)
        print(f"\n{response}\n")

    elif user_input.startswith("/idea"):
        topic = user_input.replace("/idea", "").strip()
        prompt = f"Give 3 startup ideas about: {topic}\nIdeas:"
        response = ask_ai(prompt)
        print(f"\n{response}\n")

    else:
        print("Unknown command\n")
