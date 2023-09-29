import openai

# Set your OpenAI API key
api_key = "YOUR_API_KEY"  # Replace with your actual API key
openai.api_key = api_key

def generate_story_with_gpt3(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=100,  # Limit the response to a certain number of tokens
        temperature=0.7,  # Control the randomness of the generated text
    )
    return response.choices[0].text.strip()

# Example usage
prompt = "Once upon a time in a land far, far away..."
generated_story = generate_story_with_gpt3(prompt)
print("Generated Story:", generated_story)
