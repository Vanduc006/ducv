from flask import Flask, request, render_template
import requests
app = Flask(__name__)
    
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    url = request.form['url']
    response = requests.get(url)
    return response.text

@app.route('/token', methods=['POST'])
def token():
    if request.method == 'POST':
        name = request.form['token']
        if '1' in name:
            mess = 'true1111'
        else:
            mess = 'false1111'
        return render_template('index.html', token=mess)
    return render_template('index.html')
@app.route('/mess', methods=['POST'])
def name():
    if request.method == 'POST':
        name = request.form['name']
        if '1' in name:
            mess = 'true'
        else:
            mess = 'false'
        return render_template('index.html', token=mess)
    
@app.route('/vohan', methods=['POST'])
def vohan():
    if request.method == 'POST':
        n = 0 
        while True:
            n += 1
            return render_template('index.html', vohan=f'lần {n}')


if __name__ == '__main__':
    app.run()
