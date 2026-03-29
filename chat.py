from transformers import pipeline

#load model once
generator = pipeline("text-generation", model = "distilgpt2")

print ("Simple AI chat (type 'exit' to quit)\n")

while True:
	user_input = input("You: ")
	if user_input.lower() == 'exit':
		break
	
	prompt = f"You: {user_input}\nAI: "
	result = generator(prompt, max_new_tokens = 50, do_sample = True, temperature = 0.7)
	response = result[0]["generated_text"].split("AI:")[-1]

	print (f"AI: {response.strip()}\n") 
