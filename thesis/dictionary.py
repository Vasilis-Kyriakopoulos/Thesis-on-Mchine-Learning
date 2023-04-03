from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import re
data1 = pd.read_csv('datafiles/readydata1nostem.csv')
data2 = pd.read_csv('datafiles/readydata1stem.csv')
data3 = pd.read_csv('datafiles/readydata2nostem.csv')
data4 = pd.read_csv('datafiles/readydata2stem.csv')
cv1 = TfidfVectorizer(ngram_range=[1,1])
cv2 = TfidfVectorizer(ngram_range=[1,1])
cv3 = TfidfVectorizer(ngram_range=[1,1])
cv4 = TfidfVectorizer(ngram_range=[1,1])
cv5 = TfidfVectorizer(ngram_range=[2,2])
cv6 = TfidfVectorizer(ngram_range=[2,2])
cv7 = TfidfVectorizer(ngram_range=[2,2])
cv8 = TfidfVectorizer(ngram_range=[2,2])
cv9 = TfidfVectorizer(ngram_range=[1,2])
cv10 = TfidfVectorizer(ngram_range=[1,2])
cv11 = TfidfVectorizer(ngram_range=[1,2])
cv12 = TfidfVectorizer(ngram_range=[1,2])
tf1 = cv1.fit_transform(data1['content'])
tf2 = cv2.fit_transform(data2['content'])
tf3 = cv3.fit_transform(data3['content'])
tf4 = cv4.fit_transform(data4['content'])
tf5 = cv5.fit_transform(data1['content'])
tf6 = cv6.fit_transform(data2['content'])
tf7 = cv7.fit_transform(data3['content'])
tf8 = cv8.fit_transform(data4['content'])
tf9 = cv9.fit_transform(data1['content'])
tf10 = cv10.fit_transform(data2['content'])
tf11 = cv11.fit_transform(data3['content'])
tf12 = cv12.fit_transform(data4['content'])
print("Data 1 No stem N-gram 1:"+str(tf1._shape[1]))
print("Data 1 Stem N-gram 1:"+str(tf2._shape[1]))
print("Data 2 No Stem N-gram 1:"+str(tf3._shape[1]))
print("Data 2 Stem N-gram 1:"+str(tf4._shape[1]))
print("Data 1 No stem N-gram 2:"+str(tf5._shape[1]))
print("Data 1 Stem N-gram 2:"+str(tf6._shape[1]))
print("Data 2 No Stem N-gram 1-2:"+str(tf7._shape[1]))
print("Data 2 Stem N-gram  1-2:"+str(tf8._shape[1]))
print("Data 1 No stem N-gram  1-2:"+str(tf9._shape[1]))
print("Data 1 Stem N-gram  1-2:"+str(tf10._shape[1]))
print("Data 2 No Stem N-gram  1-2:"+str(tf11._shape[1]))
print("Data 2 Stem N-gram  1-2:"+str(tf12._shape[1]))