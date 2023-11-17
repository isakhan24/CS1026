"""

CS1026a 2023
Assingment 3 - Sentiment Analysis
Isa Khan
251337547
ikhan97
11/15/2023

This is the main file for the sentiment analysis.
It receives user input and raises exceptions if there
is improper inputs. Main then calls functions from the 
sentiment_analysis module to read the files, form the 
report and write the determined results to another file. 

"""

# Import the sentiment_analysis module
from sentiment_analysis import *


def main():
    # Grabbing user input and raising exceptions if file names are improper
    tsv_file_name = input(" Input keyword filename (.tsv file): ")
    if tsv_file_name[-4:] != ".tsv":
        raise  ("Must have tsv file extension!")
    csv_file_name = input("Input tweet filename (.csv file): ")
    if csv_file_name[-4:] != ".csv":
        raise  ("Must have csv file extension!")
    txt_file_name = input("Input filename to output report in (.txt file): ")
    if txt_file_name[-4:] != ".txt":
        raise ("Must have txt file extension!")
    
    # Calling functions to read both input files and raising exception if either was empty
    keywords = read_keywords(tsv_file_name)
    tweets = read_tweets(csv_file_name)
    if len(keywords) < 1 or len(tweets) < 1:
        raise ("Tweet list or keyword dictionary is empty!")

    # Calling functions to make and write the report
    report = make_report(tweets, keywords)
    write_report(report, txt_file_name)

main()
