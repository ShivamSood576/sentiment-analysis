import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
sai=SentimentIntensityAnalyzer()

Texts=[]
Number_of_text=int(input("Enter number of text :"))
for i in  range(1,Number_of_text+1):
    EText=input(f"Enter the text {i} :")
    Texts.append(EText)
print(Texts)


sai=SentimentIntensityAnalyzer()

for text in Texts:
    sentiment_score=sai.polarity_scores(text)

    if sentiment_score['compound']>=0:
     sentiment="positive text statement"

    elif sentiment_score['compound']<=0:
     sentiment="negative text statement"

    if sentiment_score['compound']==0:
     sentiment="nuetral text statement"

    print()
    print(f"text => {text}")
    print(sentiment)
    print(sentiment_score)
    print()
    