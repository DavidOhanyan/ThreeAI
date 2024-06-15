from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import google.generativeai as genai
import anthropic


GEMINI_API_KEY = open('API-Keys/Gemini-Key', 'r').read()
OPENAI_API_KEY = open('API-Keys/Gpt-Key', 'r').read()
CLAUDE_API_KEY = open('API-Keys/Claude-Key', 'r').read()

gpt = OpenAI(api_key=OPENAI_API_KEY)
gemini = genai.configure(api_key=GEMINI_API_KEY)
claude = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gpt', methods=['POST'])
def req():
	question = request.get_json().get('message')
	if question:
		completion = gpt.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": str(question)}])
		answer = completion.choices[0].message.content.strip()
		response = {
			'message': question,
			'answer': answer
			}
		return jsonify(response), 200
	else:
		return jsonify({'error': 'Empty message received'}), 400


@app.route('/gemini', methods=["POST"])
def req2():
	question = request.get_json().get('message')
	if question:
		generation_config = {"temperature": 1, "top_p": 0.95, "top_k": 64, "max_output_tokens": 8192, "response_mime_type": "text/plain"}
		model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config)
		chat_session = model.start_chat(history=[])
		answer = chat_session.send_message(str(question)).text
		response = {
			'message': question,
			'answer': answer
		}
		return jsonify(response), 200
	else:
		return jsonify({'error': 'Empty message received'}), 400


@app.route('/claude', methods=['POST'])
def req3():
	question = request.get_json().get('message')
	if question:
		completion = claude.messages.create(model='claude-3-haiku-20240307', max_tokens=1024, messages=[{"role": "user", "content": str(question)}])
		answer = completion.content[0].text
		response = {
			'message': question,
			'answer': answer
			}
		return jsonify(response), 200
	else:
		return jsonify({'error': 'Empty message received'}), 400


def main():
	app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    main()
