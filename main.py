from flask import Flask, render_template, url_for, request
import requests
import json

app = Flask(__name__, template_folder='templates')


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        result = request.form
        url = 'https://nodejs-project.ibrahimesraa69.now.sh/functions/'+result['Numbers']+'/'+result['Target']+'/'+result['Size']
        data = requests.get(url)
        jdata = data.json()
        return render_template('home.html', result=jdata['arr'])
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
