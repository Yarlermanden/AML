### Fake News

![](mp_fakenews1.png)
![](mp_fakenews.jpg)

People have been and still are easily fooled by false claims, specifically the ones tailored to cause an emotional response. Hence the purpose of this project is to build a system to identify unreliable news articles to help identify which pieces of news and information are trustworthy. 
For this task, we suggest using the data provided in [FakeNewsNet](https://github.com/KaiDMML/FakeNewsNet). The corresponding paper has been published [here](https://www.liebertpub.com/doi/abs/10.1089/big.2020.0062), and the full pdf is available [here](https://arxiv.org/abs/1809.01286). 
It consists of two datasets that include news content, social context, and dynamic information. 
When reading the article, you may find other datasets which are described. You are free to choose another database if it has a credible source. (Please reach out to us about it.)

<!-- ATTENTION: this database does not have a reliable source
and is based on the fake news [challenge](https://www.kaggle.com/competitions/fake-news/overview) and [dataset](https://www.kaggle.com/competitions/fake-news/data). -->


#### Main goals
- Research into: how is the term "fake news" defined? Clarify and reflect on the definition, which may vary among databases, sometimes non-binary. 
- Research, where the data comes from and inspect the data: what are the labels, sources, and authors? Is there a person, source or topic which is oer- or under-represented?
- Study the literature on how others approach this task. Check the related literature and select your model architecture of choice: LSTM, ... 
- Develop a classification model to predict fake news from the text. How do you judge the quality of your results, i.e. which metrics do you consider?
- Inspect the falsely classified ones. What can you learn from them?

#### Optional goals
- Investigate edge cases that you found in your data inspection with respect to how the model learned to identify these. Experiment with how you could mitigate if edge cases are covered poorly.
