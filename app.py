from flask import Flask, render_template, request, jsonify
import requests
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    url = None
    if request.method == 'POST':
        input_url = request.form['url']
        know_id = extract_know_id(input_url)
        if know_id:
            url = get_content_url(know_id)
    return render_template('index.html', url=url)

def extract_know_id(input_url):
    match = re.search(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", input_url)
    return match.group(0) if match else None

def get_content_url(know_id):
    api_url = f'https://apiedge-eu-central-1.knowunity.com/knows/{know_id}'
    response = requests.get(api_url)
    if response.status_code == 200:
        json_data = response.json()
        return json_data['documents'][0]['contentUrl']
    return None

if __name__ == '__main__':
    app.run()