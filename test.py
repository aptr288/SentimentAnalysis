from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()


def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))

sentiment_analyzer_scores("@realDonaldTrump If you had all that money for a wall WITHOUT congressional authorization, why did you shut down the government?")