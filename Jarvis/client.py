from openai import OpenAI
# pip install openai 
client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)