import openai
MODEL_NAME = "phi3:mini"

client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)


response = client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.7,
    n=1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a Python function that returns the sum of two numbers."},
    ],
)

print("Response:")
print(response.choices[0].message.content)