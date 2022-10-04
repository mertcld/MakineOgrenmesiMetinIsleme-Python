import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score

data=pd.read_csv("temizlenmisTweetlerFORTFIDF.txt",engine='python', sep=',', quotechar='"', error_bad_lines=False)
print(data)

sentences_training = [doc for doc in data.iloc[:,0]]
classification_training = [doc for doc in data.iloc[:,1]]

#TfidfVectorizer sınıfından bir nesne oluşturuyoruz. 
# Biz kelimeler üzerinde çalıştığımız için analyzer=’word’ ve tüm harfleri lowercase = True ile küçük harfe çevirdik.
vectorizer = TfidfVectorizer(analyzer='word', lowercase = True)

#Burada, fit_transform fonksiyonu ile tüm cümlelerdeki kelimeleri içeren ve tf-idf değerlerini içeren büyük bir dizi oluştu. 
#Oluşan diziyi matrise dönüştürmek için toarray() fonksiyonu kullanılır.
sen_train_vector = vectorizer.fit_transform(sentences_training)
#print(sentences_training[:5])


print(sen_train_vector.toarray())
#naive bayes
clf = GaussianNB()
model = clf.fit(X=sen_train_vector.toarray(), y=classification_training)
sen_test_vector = vectorizer.transform(['bitcoin bence AZALIR']) 
y_pred = model.predict(sen_test_vector.toarray())
print(y_pred)





# Precision HESAPLAMA BAŞLANGIÇ
# calculates precision for 1:100 dataset with 90 truepositive and 30 falsepositive

# define actual
act_pos = [1 for _ in range(100)]
act_neg = [0 for _ in range(10000)]
y_true = act_pos + act_neg
# define predictions
pred_pos = [0 for _ in range(10)] + [1 for _ in range(90)]
pred_neg = [1 for _ in range(30)] + [0 for _ in range(9970)]
y_pred = pred_pos + pred_neg
# calculate prediction
precision = precision_score(y_true, y_pred, average='binary')
print('Precision: %.3f' % precision)
# Precision HESAPLAMA BİTİŞ

# RECALL HESAPLAMA BAŞLANGIÇ
# calculates recall for 1:100 dataset with 90 tp and 10 fn

# define actual
act_pos = [1 for _ in range(100)]
act_neg = [0 for _ in range(10000)]
y_true = act_pos + act_neg
# define predictions
pred_pos = [0 for _ in range(10)] + [1 for _ in range(90)]
pred_neg = [0 for _ in range(10000)]
y_pred = pred_pos + pred_neg
# calculate recall
recall = recall_score(y_true, y_pred, average='binary')
print('Recall: %.3f' % recall)
# RECALL HESAPLAMA BİTİŞ

#F-Meause HESAPLAMA BAŞLANGIÇ

# calculates f1 for 1:100 dataset with 95tp, 5fn, 55fp

# define actual
act_pos = [1 for _ in range(100)]
act_neg = [0 for _ in range(10000)]
y_true = act_pos + act_neg
# define predictions
pred_pos = [0 for _ in range(5)] + [1 for _ in range(95)]
pred_neg = [1 for _ in range(55)] + [0 for _ in range(9945)]
y_pred = pred_pos + pred_neg
# calculate score
score = f1_score(y_true, y_pred, average='binary')
print('F-Measure: %.3f' % score)

#F-Meause HESAPLAMA BİTİŞ