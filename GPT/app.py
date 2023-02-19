import openai
from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

# Khai báo các thông số API của OpenAI
openai.api_key = "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"
model_engine = "text-davinci-003" # đổi tên engine nếu cần thiết
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/prompt', methods=['POST'])
def generate_prompt():
    # Nhận chuỗi prompt từ yêu cầu POST
    prompt = request.json['prompt']
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return jsonify({'response': response.choices[0].text})
if __name__ == '__main__':
    app.run(debug=True)