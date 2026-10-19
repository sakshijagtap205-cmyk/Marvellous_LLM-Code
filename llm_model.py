from transformers import pipeline

# Step 1: Load a pretrained language model
print("Loading the LLM model...")

chatbot = pipeline(
    "text-generation",
    model="distilgpt2"
)

print("LLM model loaded successfully!")

# Step 2: Take input from the user
while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("AI: Goodbye! Have a nice day!")
        break

    # Step 3: Generate text
    prompt = f"Question: {user_input}\nAnswer:"

    response = chatbot(
        prompt,
        max_new_tokens=80,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7,
        pad_token_id=50256
    )

    # Step 4: Display the generated response
    generated_text = response[0]["generated_text"]

    answer = generated_text[len(prompt):].strip()

    print("AI:", answer)