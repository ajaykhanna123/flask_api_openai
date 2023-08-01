import openai

# Replace with your OpenAI API key
api_key = "sk-yqC2et2HiXXtWoGGS6dcT3BlbkFJwDRt"

# Set your OpenAI API key
openai.api_key = api_key

def get_answer(question, document):
    prompt = f"Question: {question}\nContext: {document}\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can change the engine if desired
        prompt=prompt,
        temperature=0,
        max_tokens=512
    )
    return response['choices'][0]['text'].strip()

# Example document and question
document = """
Optum gave EXL a contract . It will expire on 31 july 2023.
"""

question = "How many days since the contract is expired"

# Get the answer
answer = get_answer(question, document)
print("Question:", question)
print("Answer:", answer)
