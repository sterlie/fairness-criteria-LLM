import openai

openai.api_key = ""

def chat(inp, exp, role='user'):

  completion = openai.ChatCompletion.create(
  model = "gpt-4",
  temperature = 0.5,
  max_tokens = 2000,
  messages = [exp, {"role":role, "content": inp}]
  )
  answer = completion.choices[0].message.content
  return answer

