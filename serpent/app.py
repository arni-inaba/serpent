# encoding=utf-8

from flask import Flask, render_template, request
from logic import Serpent

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')


@app.route('/')
def form():
    return render_template('form_submit.html', channel=app.config['CHANNEL'])


@app.route('/whisper/', methods=['POST'])
def whisper():
    text = request.form['text']
    serpent = Serpent(
        channel=app.config['CHANNEL'],
        username=app.config['USERNAME'],
        slack_api_key=app.config['SLACK_API_KEY']
    )
    result = serpent.post_message(text)

    return render_template('form_action.html', success=result.successful, channel=app.config['CHANNEL'])


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5011
    )
