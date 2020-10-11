#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:27:24 2020

"""


import torch
import torch.nn as nn
from transformers import AutoModel

# optimizer from hugging face transformers
from transformers import AdamW


RND = 2020

# import BERT-base pretrained model
bert = AutoModel.from_pretrained('bert-base-uncased')

for param in bert.parameters():
    param.requires_grad = False

class BERT_Arch(nn.Module):

    def __init__(self, bert):
      
      super(BERT_Arch, self).__init__()

      self.bert = bert 
      
      # dropout layer
      self.dropout = nn.Dropout(0.1)
      
      # relu activation function
      self.relu =  nn.ReLU()

      # dense layer 1
      self.fc1 = nn.Linear(768,512)
      
      # dense layer 2 (Output layer)
      self.fc2 = nn.Linear(512,2)

      #softmax activation function
      self.softmax = nn.LogSoftmax(dim=1)

    #define the forward pass
    def forward(self, sent_id, mask):

      #pass the inputs to the model  
      _, cls_hs = self.bert(sent_id, attention_mask=mask)
      
      x = self.fc1(cls_hs)

      x = self.relu(x)

      x = self.dropout(x)

      # output layer
      x = self.fc2(x)
      
      # apply softmax activation
      x = self.softmax(x)

      return x

# pass the pre-trained BERT to our define architecture
model = BERT_Arch(bert)

# define the optimizer
optimizer = AdamW(model.parameters(),
                  lr = 1e-5)          # learning rate

# define the loss function
cross_entropy  = nn.NLLLoss()


#load weights of best model
model_state_file = 'saved_weights.pt'
model.load_state_dict(torch.load(model_state_file))

# # get predictions for a random peice of news

# new_new = ["President Trump is a man"]

# max_len = 512

# # tokenize and encode sequences in the training set
# tokens_new = tokenizer.batch_encode_plus(
#     new_new,
#     max_length = max_len,
#     padding='max_length',
#     truncation=True
# )

# # convert lists to tensors
# new_seq = torch.tensor(tokens_new['input_ids'])
# new_mask = torch.tensor(tokens_new['attention_mask'])

# with torch.no_grad():
#   new_preds = model(new_seq.to(device), new_mask.to(device)) #push to gpu
#   new_preds = new_preds.detach().cpu().numpy()

# np.argmax(new_preds, axis = 1)


