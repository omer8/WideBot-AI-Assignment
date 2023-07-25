# Classification on the Hespress News Dataset
This project aims to classify news articles from the Moroccan news website "Hespress" into different categories using machine learning techniques. The dataset used in this project contains articles from various categories such as politics, sports, economy, and culture.

# Training Process
### 1- Data Preprocessing:
* Load the dataset from CSV files.
* Clean and preprocess the text data by removing stop words, punctuation, and normalization.
* Convert the target labels into numerical values.
  
### 2- Feature Engineering:

* Extract features from the tokenized data using CountVectroizer and TF-IDF.
* Split the dataset into training and testing sets.
* Model Training:

### 3 - Train and evaluate different machine learning models on the feature-engineered data, such as Logistic Regression, Random Fores, or SVM.
* Evaluate the performance of the selected model on the testing set using metrics such as accuracy, precision, recall, and F1-score.


# Brief description of each metric:

* Precision: Precision is the number of true positives divided by the total number of positive predictions. In the context of this project, precision measures how many articles were correctly classified as belonging to a specific category, out of all the articles that were predicted to belong to that category.

* Recall: Recall is the number of true positives divided by the total number of actual positives. In the context of this project, recall measures how many articles that actually belong to a specific category were correctly classified as belonging to that category.

* F1-score: F1-score is the harmonic mean of precision and recall. It provides a balance between precision and recall, and is a useful metric when the classes are imbalanced. In the context of this project, F1-score measures the overall accuracy of the model in classifying articles into different categories.

* Accuracy: Accuracy is the number of correct predictions divided by the total number of predictions. In the context of this project, accuracy measures how many articles were correctly classified into their respective categories out of all the articles in the test set


# Enhancements that could achieve better results.

* Use Word Embedding
  
* Ensemble Learning: Training multiple machine learning models and combining their outputs through techniques such as voting or stacking can help improve the overall accuracy of the model.

* Hyperparameter Tuning: Tuning the hyperparameters of the machine learning model can help improve its performance. This can be done through techniques such as grid search or random search.

* Transfer Learning: Using pre-trained models such as BERT or GPT-2 as a starting point for the model training process can help improve the model's performance, especially when dealing with limited training data.
