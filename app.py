from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8638127239:AAF92vNK_f3zuGJz3adr7HyNq3IIieF-f6A"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    response = f"Recibí: {text}"

    requests.post(URL, json={
        'chat_id': chat_id,
        'text': response
    })

    return 'ok'

if __name__ == "__main__":
    app.run()
