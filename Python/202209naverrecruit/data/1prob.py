import pandas as pd
import numpy as np
import sklearn

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix as cfm


def spam_detector(train_df, valid_df, test_df):
    
    # fit_transform train_df with tfidVectorizer
    tfidv = TfidfVectorizer(min_df=2, ngram_range=(1, 2)).fit(train_df['text'])
    train_tfidv = tfidv.transform(train_df['text'])
    valid_tfidv = tfidv.transform(valid_df['text'])
    valid_target = np.array(valid_df['label'])
    
    clf = [
        LogisticRegression(random_state=0).fit(train_tfidv, train_df['label']),
        MultinomialNB().fit(train_tfidv, train_df['label']),
        DecisionTreeClassifier(random_state=0).fit(train_tfidv, train_df['label']),
        svm.SVC(random_state=0).fit(train_tfidv, train_df['label']),
        ]

    results = {
        "LogisticRegression": cfm(clf[0].predict(valid_tfidv), valid_target),
        "MultinomialNB": cfm(clf[1].predict(valid_tfidv), valid_target),
        "DecisionTreeClassifier": cfm(clf[2].predict(valid_tfidv), valid_target),
        "LinearSVC": cfm(clf[3].predict(valid_tfidv), valid_target),
        "BestClassifier": None,
        "TfidfVectorizer": None,
        "Prediction": None,
    }

    # which one is the best classifier
    clf_min_err = 123456789
    best_model = -1
    for i,k in enumerate(["LogisticRegression",'MultinomialNB','DecisionTreeClassifier','LinearSVC']):
        tn, fp, fn, tp = results[k].ravel()
        if clf_min_err > fn:
            clf_min_err = fn
            best_model=i
            results['BestClassifier'] = k

    # TfidVectorizer and Prediction
    test_tfidv = tfidv.transform(test_df['text'])
    results['TfidfVectorizer'] = test_tfidv
    results['Prediction'] = clf[best_model].predict(test_tfidv)
    
    return results

    

    
