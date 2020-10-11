
import flask
import pickle

# Use pickle to load in the pre-trained model.
with open(f'Downloads/bert.py','t') as f:
     model = pickle.load(f)

     
app = flask.Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True

@app.route('/', methods=['GET', 'POST'])

#user input in text 
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    
    #if flask.request.method == 'POST':


app.run()


'''
@app.route('/', methods=['GET'])
def predict():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
'''
