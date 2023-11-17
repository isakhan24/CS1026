"""
CS1026a 2023
Assingment 3 - Sentiment Analysis
Isa Khan
251337547
ikhan97
11/15/2023

This file contains functions that carry out the tweet analysis.
The functions do the following: read keywords, read tweets,
calculate sentiment, classify the sentiment,
make report and write the end report.
"""

# This function reads in the keywords file and returns each keyword and its score in a dictionary
# It checks for IO errors

def read_keywords(keyword_file_name):
    keywords = {}
    try:   
        input_file = open(keyword_file_name, "r")
        line = input_file.readline()
        # Checking for empty line
        while line != "":
            # Removing unwanted elements of the file, saving to dictionary
            line = line.strip("\n")
            lst = line.split("\t")
            keywords[lst[0]] = int(lst[1])
            line = input_file.readline()
        return keywords
    #Excepting error
    except IOError:
        print(f"Could not open file {keyword_file_name}!")
        return keywords

# This function takes in the raw text of a tweet and returns a "clean" string that does not contain special characters or numbers with all lowercase letters
def clean_tweet_text(tweet_text):
    # Removing all special characters
    clean_tweet = "".join(char for char in tweet_text if char.isalnum() or char == " ") 
    # Removing all digits
    cleaner_tweet = "".join(char for char in clean_tweet if not char.isdigit())
    clean_text = cleaner_tweet.lower()
    return clean_text

# This funcion calculates the sentiment by comparing the words in the tweet to those found in the keywords file and scoring the tweet accordingly
def calc_sentiment(tweet_text, keyword_dict):
    count = 0
    splitString = tweet_text.split()
    for element in splitString:
        if element in keyword_dict:
            count += keyword_dict[element]
    return count

# This funcition takes a numerical score and returns a string value representing that score
def classify(score):
    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"

# This function reads in the tweets file and returns each tweet as a dictionary in a list
# It checks for IO errors
def read_tweets(tweet_file_name):
    tweets = []
    try:   
        inputFile = open(tweet_file_name, "r")
        line = inputFile.readline()
        while line != "":
            currentTweet = {}  
            # Removing unwanted values from tweet
            line = line.strip("\n")
            lst = line.split(",")   
            # Assigning each tweet characteristic to its proper key in dictionary
            currentTweet['date'] = lst[0]
            # Cleaning text before adding it to the dictionary
            currentTweet['text'] = clean_tweet_text(lst[1])
            currentTweet['user'] = lst[2]
            currentTweet['retweet'] = int(lst[3])
            currentTweet['favorite'] = int(lst[4])
            currentTweet['lang'] = lst[5]
            currentTweet['country'] = lst[6]
            currentTweet['state'] = lst[7]
            currentTweet['city'] = lst[8] 
            currentTweet['lat'] = lst[9]
            # Checking to see whether float or string value should be added to the dictionary
            if currentTweet['lat'] != "NULL":
                currentTweet['lat'] = float(lst[9])
            currentTweet['lon'] = lst[10]
            if currentTweet['lon'] != "NULL":
                currentTweet['lon'] = float(lst[10])
            # Appending the current tweet as a dictionary to the list of tweets
            tweets.append(currentTweet)
            line = inputFile.readline()
        return tweets
    # Excepting IOError
    except IOError:
        print(f"Could not open file {tweet_file_name}")
        return tweets
   
# This function makes the report of all the calculations made based on the tweets and keyword dictionary
def make_report(tweet_list, keyword_dict):

    avg_favorite = "NAN"
    avg_retweet = "NAN"
    avg_sentiment = "NAN"
    report = {}

    num_favorite = 0
    avg_favorite_score = 0
    num_retweet = 0
    avg_retweet_score = 0
    num_negative = 0
    num_neutral = 0
    num_positive = 0
    avg_sentiment_score = 0
    country_scores = {}
    countries = []
    # Looping through each element of the list
    for element in tweet_list:
        # Calculating sentiment
        element["sentiment"] = calc_sentiment(element["text"], keyword_dict) 

        if element["favorite"] > 0:
            num_favorite += 1
            avg_favorite_score += element["sentiment"]

        if element["retweet"] > 0:
            num_retweet += 1
            avg_retweet_score += element["sentiment"]
        
        classification = classify(element["sentiment"])
        # Classifying the tweet with a string value based on the sentiment value
        if classification == "positive":
            num_positive += 1
            avg_sentiment_score += element["sentiment"]
        if classification == "negative":
            num_negative += 1
            avg_sentiment_score += element["sentiment"]
        if classification == "neutral":
            num_neutral += 1
            avg_sentiment_score += element["sentiment"]
        
        # Recording countries and keeping track of scores for each country
        if element['country'] not in country_scores and element["country"] != "NULL":
            country_scores[element["country"]] = [element["sentiment"], 1]
            countries.append(element["country"])
        elif element["country"] != "NULL":
            country_scores[element["country"]][0] += element["sentiment"]
            country_scores[element["country"]][1] += 1

    # Properly sorting the coutries into the proper order and placing the top 5 into a string 
    for element in countries:
        country_scores[element] = round(country_scores[element][0] / country_scores[element][1], 2)
    sorted_country_scores = sorted(country_scores.items(), key=lambda x:x[1], reverse=True)[:5]
    converted_dict = dict(sorted_country_scores)
    str_top_5_countries = ", ".join(converted_dict)

    # Calculating the averages if applicable
    if num_favorite != 0:
        avg_favorite = round(avg_favorite_score / num_favorite, 2)
    if num_retweet != 0:
        avg_retweet = round(avg_retweet_score / num_retweet, 2)
    if len(tweet_list) > 0:
        avg_sentiment = round(avg_sentiment_score / len(tweet_list), 2)

    # Adding all the calculations to dictionary and returning it to main
    report["avg_favorite"] = avg_favorite
    report["avg_retweet"] = avg_retweet
    report["avg_sentiment"] = avg_sentiment
    report["num_favorite"] = num_favorite
    report["num_negative"] = num_negative
    report["num_neutral"] = num_neutral
    report["num_positive"] = num_positive
    report["num_retweet"] = num_retweet
    report["num_tweets"] = len(tweet_list)
    report["top_five"] = str_top_5_countries

    return report
    
# This function write the report to a text file
# It checks for IO errors
def write_report(report, output_file):
    try:
        outputFile = open(output_file, "w")
        # Writing calculations out to the text file
        outputFile.write(
f"""Average sentiment of all tweets: {report["avg_sentiment"]}
Total number of tweets: {report["num_tweets"]} 
Number of positive tweets: {report["num_positive"]} 
Number of negative tweets: {report["num_negative"]} 
Number of neutral tweets: {report["num_neutral"]} 
Number of favorited tweets: {report["num_favorite"]} 
Average sentiment of favorited tweets: {report["avg_favorite"]} 
Number of retweeted tweets: {report["num_retweet"]} 
Average sentiment of retweeted tweets: {report["avg_retweet"]}
Top five countries by average sentiment: {report["top_five"]}""")
        print(f"Wrote report to {output_file}")
    except IOError: # Excepting IO Error
        print(f"Could not open file {output_file}")
2