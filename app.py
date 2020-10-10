
import flask
import pickle

app = flask.Flask(__name__, template_folder='templates')
@app.route('/')
def main():
    return(flask.render_template('main.html'))


# Use pickle to load in the pre-trained model.
# with open(f'Downloads/bert.py', 't') as f:
#     model = pickle.load(f)
    
# app.config["DEBUG"] = True


# @app.route('/', methods=['GET'])
def predict():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


if __name__ == '__main__':
    app.run()

"""

import flask
app = flask.Flask(__name__, template_folder='templates')
@app.route('/')
def main():
    return(flask.render_template('main.html'))
if __name__ == '__main__':
    app.run()

"""