# Fake News Detection
This repository contains code for building a fake news detector. This project was developed during <a href="https://www.correlation-one.com/ds4a">Data Science for All Women's Summit 2020</a>.

## Problem statement
* Fake news is a particularly important problem nowadays as many people rely on social media as their primary news source.<sup>[1](#footnote1)</sup>
* Impact of fake news
	* **Social**: Fake news spread faster and further than real news.<sup>[2](#footnote2)</sup>
	* **Economic**: Fake news affects stock market. For example, a hacked AP tweet in 2013 led to a 130 billion dollar loss in market cap.<sup>[3](#footnote3)</sup> 
	* **Business**: How social media platforms handle fake news affects customer trust. 
* Our solution is to develop a model for classifying news articles as real or fake. 

## Data
* Model training: <a href="https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset"> Fake and real news</a> dataset (Kaggle).
* External validation: <a href="https://www.kaggle.com/mrisdal/fake-news">Fake news dataset</a> from 2016 (Kaggle).

## Analysis
* Exploratory data analysis & text preprocessing 
* Baseline model 1: doc2vec embedding & logistic regression 
* Baseline model 2: Recurrent Neural Network
* Advanced model: BERT & transfer learning
* Model interpretability: LIME 
* External validation

## Results

Please find our results in our [project report](report/final_report.pdf) or click on the following image to view our slides.

<a href="https://onedrive.live.com/View.aspx?resid=807ED3EB316AB323!1656&wdSlideId=256&wdModeSwitchTime=1603933074942&authkey=!AH3L-XXdyE_vaz4">
  <img src="/images/slide.png" width="600" />
</a>


## Authors
Iris Yoon  
Rabiya Noori  
Jerri Zhang  
Renee G. Reynolds  
Hannah Mei

#### References
<a name="footnote1">1</a>: <a href="https://www.journalism.org/2020/07/30/americans-who-mainly-get-their-news-on-social-media-are-less-engaged-less-knowledgeable/"> Americans Who Mainly Get Their News on Social Media Are Less Engaged, Less Knowledgeable</a>  
<a name="footnote2">2</a>: <a href="https://arxiv.org/abs/1812.00315">A survey of fake news</a>  
<a name="footnote3">3</a>: <a href="https://www.cnbc.com/id/100646197">False Rumor of Explosion at White House Causes Stocks to Briefly Plunge</a>
