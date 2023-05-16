# About
Phishing attacks are the practice of sending fraudulent communications that appear to come from a reputable source.Phishing URLs mainly target individuals and/or organizations through social engineering attacks by exploiting the humans' weaknesses in information security awareness. Phishing costs Internet users billions of dollars per year. It refers to luring techniques used by identity thieves to fish for personal information in a pond of unsuspecting Internet users. Phishers use spoofed e-mail, phishing software to steal personal information and financial account details such as usernames and passwords.The experiments were carried out on a dataset that originally contained 100860 labeled URLs (phishing and legitimate). We consider various data mining algorithms for evaluation of the features in order to get a better understanding of the structure of URLs that spread phishing. 
# Introduction
Natural Language processing makes it possible for computers to understand the human language. NLP analyzes the grammatical structure of sentences and the individual meaning of words, then uses algorithms to extract meaning and deliver outputs. NLP deals with how computers understand and translate human language. With NLP, machines can make sense of written or spoken text and perform tasks like translation, keyword extraction, topic classification, and more. 
Preprocessing
Data preprocessing can refer to manipulation or dropping of data before it is used in order to ensure or enhance performance, and is an important step in the data mining process. 
NLP Contains Three Steps
    Preprocessing
    Vectorization
    Model Selection
NLP preprocessing techniques
   Expand Contractions
   Lower Case
   Remove Punctuations
   Remove words and digits containing digits
   Remove Stopwords
   Rephrase Text
   Stemming and Lemmatization
   Remove White spaces
NLP Vectorization techniques
   Count Vectorizer
   TF-IDF
   Word2Vec
   GloVe
   FastText
#  Data Set
Here the train and test data sets will be given individually. The train dataset contains 100860 rows with the information of url and its property(Whether it is lezzitimate or not). By considering the dataset the natural language preprocessing steps like tokenization will be applied.
The test dataset contains 25220 row with out having the property(labels are not given).
   

# Dataset Preprocessing
The given dataset consists of URL's to detect whether the given url is malicious or legitimate. 
There exists many tokens or special characters which appear most frequently in URL string of phishing sites but not in legitimate sites. This characteristic feature is used to distinguish between phishing sites and legitimate sites. These features check the presence of special characters (@, *, $, :, |, , ’,’, _), phish-hinted words either in the base URL or path of the entire URL string.
While preprocessing we replaced some special characters like (//,/,-,.) with space(' ').

For Preprocessing of this dataset we can't use stemming or lemmatization because the context will changes and it throws falls results to the users.

# Vectorization Techniques   
Generally machines cannot identifies the text data.In order to train the machines we need to convert the text into vectorized from. such that the vectorization techniques comes into exitance.
TF-IDF:
TF-IDF or Term Frequency–Inverse Document Frequency, is a numerical statistic that’s intended to reflect how important a word is to a document.
By using this technique a sparse matrix is generated.By giving this to a models like Naive Bayes etc.. Then the accuracy is 

Count Vectorizer:
CountVectorizer Means Breaking Down A Sentence Or Any Text Into Words By Performing Preprocessing Tasks Like Converting All Words To Lowercase, Thus Removing Special Characters.

# Training dataset
Naive Bayes:
This classifier can also be known as a Generative Learning Model. The classification here is based on Bayes Theorem, it assumes independent predictors. In simple words, this classifier will assume that the existence of specific features in a class is not related to the existence of any other feature. If there is dependency among the features of each other or on the presence of other features, all of these will be considered as an independent contribution to the probability of the output. This classification algorithm is very much useful to large datasets and is very easy to use. 

Random Forest:
This classification algorithm are similar to ensemble learning method of classification. The regression and other tasks, work by building a group of decision trees at training data level and during the output of the class, which could be the mode of classification or prediction regression for individual trees. This classifier accuracy for decision trees practice of overfitting the training data set.

# Testing dataset
Testing of the given url through the deployed website will be predicted whether it is legitimate or not by using Naive Bayes trained model.

# Model Deployment
Inorer to deploy the model into a web browser flask technology is used.

# Result
Observations:
Accuracy Metrix is matthews-correlation Coefficient.By applying vectorization as count vectorizer and training, testing the model with naive bayes gives an accuracy of 98%. In the same way with count vectorizer and Random forest given an accuracy of 86%. With TF-IDF and Naive Bayes the accuracy is 98.1%.

# Conclusion
After training the dataset with Naive Bayes, perceptrons, Random Forest highest accuracy is obtained with Naive Bayes. To provide security to every individual sensitive information every one must know which URL is legitimate and which is not. To learn that this project is best pratice to understand.

# Input and Output Images
INPUT-1
![Screenshot (106)](https://user-images.githubusercontent.com/109868566/180846205-e36bcf98-821b-4c79-9f86-655d2f4a55bb.png)
OUTPUT-1
![Screenshot (108)](https://user-images.githubusercontent.com/109868566/180846361-d596fb19-2005-4ef9-a137-c7561bf48643.png)
INPUT-2
![Screenshot (109)](https://user-images.githubusercontent.com/109868566/180846438-ad8ba8a9-1ba7-4d4d-8d29-1de243eaf6c8.png)
OUTPUT-2
![Screenshot (110)](https://user-images.githubusercontent.com/109868566/180846548-6d9f1a72-4a79-483c-92f4-1918e993aa90.png)




