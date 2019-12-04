# Capstone: Reduce Cyberbullying via Curbing of Toxic Comments

## Problem Statement
Given an accurately labelled dataset of toxic comments, the task is to determine if a given comment is considered offensive to another person.
This can also be further extended to determine the target of the offensive comment. 


## Executive Summary

### Contents:
- [Data Source](#Data-Source)
- [Evaluation](#Evaluation)
- [Conclusion](#Conclusion)

### Data Source
The data is taken from the Kaggle Competition: br>
[Jigsaw Unintended Bias in Toxicity Classification](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data)


### Evaluation
Logistic Regression with TFIDF-Vectorizer works the best among all the other models for the binary toxic comment classification.<br>
For the multi-label classification, Classifier Class with Countvectorizer works the best among the models.

### Conclusion
The binary classification of toxic comments work well when we under-sample the non-toxic comments and using Logistic Regression with TDIDF-Vectorizer. The multi-label classification was able to classify insult comments accurately but having rather mixed results when assigning the remaining labels.

For this capstone project, we are limited by the following areas:
- Hardware of machine used
- Time factor (6 weeks)
- Budget limitation

We can further expand the scope of the project to include the following:

- Applying deep learning to perform unsupervised learning
- Gather more data on toxic comments with more related labels
- Expand the multi-label classification to identity labels

