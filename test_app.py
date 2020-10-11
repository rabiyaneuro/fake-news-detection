#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:14:15 2020

"""
import torch
import numpy as np
from transformers import BertTokenizerFast
import model.bert
import flask
app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        input_text = flask.request.form["exampleFormControlTextarea1"]
    
        
        # predictions
        max_len = 512
        
        # tokenize and encode sequences in the training set
        tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
        tokens = tokenizer.batch_encode_plus(
            input_text,
            max_length = max_len,
            padding='max_length',
            truncation=True
        )
        
        # convert lists to tensors
        new_seq = torch.tensor(tokens['input_ids'])
        new_mask = torch.tensor(tokens['attention_mask'])
        
        with torch.no_grad():
          new_preds = model(new_seq, new_mask)
        
        prediction = np.argmax(new_preds, axis = 1)

        return flask.render_template('main.html',
                                     result=prediction,
                                     )
    
    
"""

helpful links:
    https://blog.cambridgespark.com/deploying-a-machine-learning-model-to-the-web-725688b851c7
"""