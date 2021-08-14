from flask import Flask , render_template, request
import os

app = Flask(__name__)

@app.route("/")
def root():
    with open('templates/front.html') as f:
        # return render_template('front.html',message="from flask" )
        return f.read()

@app.route("/describe")
def describe():
    task = []
    for code in os.listdir('code'):
        t = {}
        t['name'] = code.replace('.py','')
        with open(os.path.join('code',code)) as f :
            t['content'] = f.read()
        task.append(t.copy())
    return {'task': task}


@app.route("/runtask", methods=['POST'])
def runtask():
    # print(request.get_json(force=True))
    print(request.values)
    return {'ret': 200 }