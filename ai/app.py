from flask import Flask, request, jsonify
from gpt3_util import generate_story_with_gpt3

app = Flask(__name__)

@app.route('/api/generate-story', methods=['POST'])
def generate_story():
    data = request.get_json()
    prompt = data['prompt']
    generated_story = generate_story_with_gpt3(prompt)
    return jsonify({'story': generated_story})

if __name__ == '__main__':
    app.run(debug=True)
