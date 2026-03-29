from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

result = generator(
    "Linux is",
    max_new_tokens=30,
    do_sample=True
)

print(result[0]["generated_text"])

