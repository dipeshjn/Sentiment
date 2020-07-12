from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'etuXjVWafJDNSbXPWm9pfzCjG'
consumer_secret = '1v2wRtJ7s1GiH5SIfUAlFehFt2wqVFh8sWZL8noVTcJ0Igj5T8'

access_token = '780951174086168576-MsQIMhqgy1PpJxqH3bcq0BT8lPIDHmc'
access_token_secret = '2skub6nwlCknKDv1YEqvOpUnI2JHfXlHY3k5OQipgGLZX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    # t = [[]]
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})


#---------------------------------------------------------------------------


