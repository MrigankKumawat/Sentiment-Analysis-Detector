### SENTIMENT DETECTION ANALYZER

from textblob import TextBlob

def sentiment1(text):
    blob=TextBlob(text)
    polarity=blob.sentiment.polarity
    subject=blob.sentiment.subjectivity 
    if polarity>0:
        sentiment="Positive"
    elif polarity<0:
        sentiment="Negative"
    else:
        sentiment="Neutral"

    return sentiment,polarity,subject

user=input("Enter a sentence to analyze the sentiment:")
sentiment,polarity,subject=sentiment1(user)

print("Sentiment:",sentiment)
print("Polarity:",polarity)
print("Subjectivity:",subject)






