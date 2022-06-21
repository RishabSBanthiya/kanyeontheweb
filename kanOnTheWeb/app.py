from flask import Flask, render_template,request
from twilio.rest import Client
import requests
from flask_apscheduler import APScheduler
import os

app = Flask(__name__)
scheduler = APScheduler()


def send_message():
    # Twillio login details
    client = Client("AC48b47ce7b8681f797d83129026a95751", "6ac9816f3218654b4e0d78ff0ad44f66")
    r = requests.get("http://api.kanye.rest")
    client.messages.create(to="+12172006074",
                           from_="+19108128778",
                           body=r.json()["quote"])


@app.route('/', methods=['GET', 'POST'])
def home():
    # templates
    if request.method == 'POST':
        send_message()
        return render_template("index.html")
    else:
        return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)