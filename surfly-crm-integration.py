from flask import Flask, redirect, url_for, render_template
from urllib2 import Request, urlopen
import json

    # this:

app = Flask(__name__)

    # is how you start

headers = {
    'Content-Type': 'application/json'
}

@app.route('/XmnyAf6aiAzXHpragpteeVmY', methods=['POST', 'GET']) # create sub path
def index():
    render_template('index.html')

def join():
    # get the active session list
    sessionid = request.form['sessionid']
    request = Request('https://surfly.com/v2/sessions/?api_key=6dbf75022a294e9c9cb247bb142d9e76&active_session=true', headers=headers)
    response_body = urlopen(request).read()
    # this returns a json object, so you need to parse it before you can use the data inside
    active_sessions = json.loads(response_body)
    # iterate over the active session list
    for key in active_sessions:
    # if PIN that was filled in by agent equals a PIN from the active session list
        if key == sessionid:
    # here you grab the follower link from the json file and make sure that the users are redirected to it
            follower = active_sessions["viewer_link"]
    return redirect(follower)

    # this:

if __name__ == "__main__":
    app.run()

    # is how you end
