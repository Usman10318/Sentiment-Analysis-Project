from textblob import TextBlob
import matplotlib.pyplot as plt

def analyze_sentiment(tweet):
    """Analyze the sentiment of a single tweet."""
    blob = TextBlob(tweet)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, sentiment_score

def predefined_tweets_analysis():
    """Analyze a predefined set of tweets."""
    tweets = [
        "I love programming!",
        "The weather is terrible today.",
        "Python is amazing for data science.",
        "I'm so tired of waiting in traffic.",
        "Today is an average day.",
        "Exams are so stressful!",
        "This coffee is fantastic!"
    ]
    results = []
    print("\nPredefined Tweets Analysis")
    print("-" * 50)
    for tweet in tweets:
        sentiment, score = analyze_sentiment(tweet)
        print(f"Tweet: {tweet}\nSentiment: {sentiment} (Score: {score})\n")
        results.append((tweet, sentiment, score))
    return results

def user_tweets_analysis():
    """Analyze tweets provided by the user."""
    user_tweets = []
    print("\nEnter your tweets (type 'exit' to finish):")
    print("-" * 50)
    while True:
        tweet = input("Tweet: ")
        if tweet.lower() == 'exit':
            break
        sentiment, score = analyze_sentiment(tweet)
        print(f"Sentiment: {sentiment} (Score: {score})\n")
        user_tweets.append((tweet, sentiment, score))
    return user_tweets

def filter_tweets_by_keyword(tweets, keyword):
    """Filter tweets containing a specific keyword."""
    filtered_tweets = [tweet for tweet in tweets if keyword.lower() in tweet[0].lower()]
    if filtered_tweets:
        print(f"\nTweets containing the keyword '{keyword}':")
        for tweet, sentiment, score in filtered_tweets:
            print(f"Tweet: {tweet}\nSentiment: {sentiment} (Score: {score})\n")
    else:
        print(f"\nNo tweets found containing the keyword '{keyword}'.")
    return filtered_tweets

def save_results_to_file(results):
    """Save sentiment analysis results to a text file."""
    with open("sentiment_analysis_results.txt", "w") as file:
        for tweet, sentiment, score in results:
            file.write(f"Tweet: {tweet}\nSentiment: {sentiment} (Score: {score})\n")
    print("\nResults saved to 'sentiment_analysis_results.txt'.")

def plot_sentiment_distribution(results):
    """Plot the distribution of sentiments."""
    sentiments = [sentiment for _, sentiment, _ in results]
    sentiment_counts = {
        "Positive": sentiments.count("Positive"),
        "Negative": sentiments.count("Negative"),
        "Neutral": sentiments.count("Neutral"),
    }
    # Bar chart
    plt.bar(sentiment_counts.keys(), sentiment_counts.values(), color=['green', 'red', 'blue'])
    plt.title("Sentiment Distribution (Bar Chart)")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.show()

    # Pie chart
    plt.pie(sentiment_counts.values(), labels=sentiment_counts.keys(), autopct='%1.1f%%', colors=['green', 'red', 'blue'])
    plt.title("Sentiment Distribution (Pie Chart)")
    plt.show()

def display_statistics(results):
    """Display basic statistics of the sentiment analysis."""
    total_tweets = len(results)
    positive = sum(1 for _, sentiment, _ in results if sentiment == "Positive")
    negative = sum(1 for _, sentiment, _ in results if sentiment == "Negative")
    neutral = sum(1 for _, sentiment, _ in results if sentiment == "Neutral")

    print("\nStatistical Overview:")
    print("-" * 50)
    print(f"Total Tweets Analyzed: {total_tweets}")
    print(f"Positive Tweets: {positive} ({(positive / total_tweets) * 100:.2f}%)")
    print(f"Negative Tweets: {negative} ({(negative / total_tweets) * 100:.2f}%)")
    print(f"Neutral Tweets: {neutral} ({(neutral / total_tweets) * 100:.2f}%)")

def main():
    while True:
        print("\nSentiment Analysis of Tweets")
        print("-" * 50)
        print("1. Analyze Predefined Tweets")
        print("2. Enter Your Own Tweets")
        print("3. Filter Predefined Tweets by Keyword")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            results = predefined_tweets_analysis()
            save_results_to_file(results)
            plot_sentiment_distribution(results)
            display_statistics(results)
        elif choice == '2':
            results = user_tweets_analysis()
            save_results_to_file(results)
            plot_sentiment_distribution(results)
            display_statistics(results)
        elif choice == '3':
            keyword = input("\nEnter the keyword to filter tweets: ")
            predefined_results = predefined_tweets_analysis()
            filtered_results = filter_tweets_by_keyword(predefined_results, keyword)
            if filtered_results:
                plot_sentiment_distribution(filtered_results)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
