#coding:utf-8
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
np.set_printoptions(threshold=np.inf)

#N-Gram & generate feature vectors.
#Distinguish between uppercase and lowercase letters
vectorizer = CountVectorizer(ngram_range=(4,4), token_pattern=u'(?u)\\b\\w+\\b', lowercase=False)

#Put the symbol strings in the variable 'corpus'
corpus = [
	'O O O O O O O O L A O O O O O O O O O C A O O O O O O O O O O O O O O O O O O O w Q I O O O O O O O O A C O A O O O O O O O O E O O O O O O O O O O O O B O O O O O O O L Z O O O O A O A O O O O O O O O O O O O O B I B t Z N E O C O J C O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O C O O O O V W C A O O O J O O O O O O O E O O O O E O O O E O E O E O E J A O E O E O E O O E O E E E O O O O E B F E E E O O O O O O C O O O O O O O O O I A C O O C O O Z A O O O O O O O I O O O I O O C O O O C O O O C C O O O O O C O O O O T E A O O O B O O C O O O O O B O O C O O O O O O O C O O O O O O O O O O O O O O I A O O O O O O O O O O O O O O O O E C E O E O O O O O O O O O O O O O O O C E O O O O O O O O O O O O O O O O A O I O O J J A A J O A J J A J O J J A I C A J O O O O O O O O O O E O O O O O O O O O O O A O O E O B B E O O O O O A I E O',
	'O O A E O J C O Z Z O J A C O O O O O A A O O A O O O E O B O O O O O O O O O O O B A C O O O O O O O B B O B O O O O I B B B B I B B I A A C B B O B B B B B O B O B B B E B B',
	'A Z I C U a D C C U C Z O J D D d B O Z Z Z X C N C C O O O O O O O O O O O O O O O O l l C O O O O O O O O O O O O O O O O O O O O O O B S Z O C O O O O O O O O O O O O O O O O O O O O O J Z Z C A Z D O H O R Z Z M C O C C O C O O O O O O O O v O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O E O O O O O O O O O O O O O O O O O C O O E O O Z Z Z Z Z K C O O O O O O l Z Z O E Z Z',
	'Z Z Z Z Z Z Z Z Z Z Z Z Z Z U U Z',
	'Z Z O O O O O O O O O O O O O O O E E E O O E E O O E O E O E O O Q Z D D E E O E B Z O E E E O O E E O E O O O O E E E Z Z Z E O O O O O F F Z O O O E A E A A E A O O O O Z Z N A O O O O O J O O C B B Z b K Z O C C O O O O O O O O E C O C O O O O O O O O O O O C O C O O Z Z Z C D I O O Z Z Z O O C E Z Z Z Q C I O O O O E O O O Z',
	'E C E O O O O O C E C E C E O O O O O C O O O E O O O O O O O O O E C V Z M O E E E E E E E O O E E O E E E E F Z Z C E E E E E E O O E C O O O O O C E E O E O E O C C',
]

#output of feature vectors
X = vectorizer.fit_transform(corpus)
#get feature name
feature = vectorizer.get_feature_names()
print(feature)
print(X.toarray())

#numpy.savetxt('test.txt', X.toarray())
#path_w = '/Users/kawaikumiko/Desktop/ML_data/test.txt'
#with open(path_w, mode='w') as f:
#    f.write(X)
