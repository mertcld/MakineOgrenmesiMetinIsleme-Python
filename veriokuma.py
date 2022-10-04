# import csv
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import GaussianNB
# data=pd.read_csv("kriptoVeri5.csv",engine='python')

# print(data)
  




    # sentences_training = [doc for doc in data.iloc[:,0]]
    # classification_training = [doc for doc in data.iloc[:,1]]

    # # yaz=open('okuduklari.txt','a',encoding="utf-8")
    # # yaz.write(str(sentences_training))
    # # yaz.write("-----------------------")
    # # yaz.write(str(classification_training))
    # # yaz.close()
    # vectorizer = TfidfVectorizer(analyzer='word', lowercase = True)
    # sen_train_vector = vectorizer.fit_transform(sentences_training)

        
    # print(sen_train_vector.toarray())
    # clf = GaussianNB()
    # model = clf.fit(X=sen_train_vector.toarray(), y=classification_training)
    # sen_test_vector = vectorizer.transform(['bu kadar kötü bir ürün görmedim'])
    # #print(sen_test_vector.toarray())
    # y_pred = model.predict(sen_test_vector.toarray())
    # print(y_pred)