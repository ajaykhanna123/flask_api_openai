import os
from flask import Flask, request, jsonify
import openai

# Replace with your OpenAI API key
api_key = "YOUR_OPENAI_API_KEY"

# Set your OpenAI API key
openai.api_key = api_key

app = Flask(__name__)

@app.route('/answer', methods=['POST'])
def get_answer():
    try:
        question = request.form.get('question')
        document_text = request.form.get('document_text')

        if not question or not document_text:
            return jsonify({"error": "Question and Document Text must be provided."}), 400

        document_file = request.files.get('document_file')
        if document_file:
            document_text = document_file.read().decode('utf-8')

        prompt = f"Question: {question}\nContext: {document_text}\nAnswer:"
        response = openai.Completion.create(
            engine="text-davinci-002",  # You can change the engine if desired
            prompt=prompt,
            temperature=0,
            max_tokens=512
        )

        answer = response['choices'][0]['text'].strip()
        return jsonify({"question": question, "answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
