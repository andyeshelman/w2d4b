#======= Question 1 =======

# Task 1 : Capitalize keywords

reviews = [ "This product is really good. I'm impressed with its quality.",
           "The performance of this product is excellent. Highly recommended!",
           "I had a bad experience with this product. It didn't meet my expectations.",
           "Poor quality product. Wouldn't recommend it to anyone.",
           "The product was average. Nothing extraordinary about it."]

keywords = ["good", "excellent", "bad", "poor", "average"]

proc_reviews = []
for review in reviews:
    proc_review = []
    for word in review.split():
        if word.isalpha() and word.lower() in keywords:
            proc_review.append(word.upper())
        # checking for punctuation mark
        elif not word.isalpha() and word.lower()[:-1] in keywords:
            proc_review.append(word.upper())
        else:
            proc_review.append(word)
    proc_reviews.append(" ".join(proc_review))


# in one line, for fun
proc_reviews_one_line = [ " ".join([ word.upper() if 
    (word.lower() in keywords if word.isalpha() else word.lower()[:-1] in keywords)
    else word for word in review.split()]) for review in reviews]

print(proc_reviews == proc_reviews_one_line)

# Task 2 : Sentiment Tally

positive_words = ["good", "excellent", "great", "awesome",
                  "fantastic", "superb", "amazing"] 

negative_words = ["bad", "poor", "terrible", "horrible",
                  "awful", "disappointing", "subpar"]

for review in proc_reviews:
    print(review)
    pos_tally, neg_tally = 0, 0
    for word in review.split():
        if word.isalpha():
            if word.lower() in positive_words:
                pos_tally += 1
            if word.lower() in negative_words:
                neg_tally += 1
        else:
            if word.lower()[:-1] in positive_words:
                pos_tally += 1
            if word.lower()[:-1] in negative_words:
                neg_tally += 1
    print(f"{pos_tally} positve words and {neg_tally} negative words")

# Task 3 : Review Summary

review_summaries = []
for review in reviews:
    length = review.find(" ",30)
    # .find() returns -1 if it can't find,
    # e.g. if the review is < 30 char long
    length = len(review) if length == -1 else length
    review_summaries.append(review[:length] + "...")

for summary in review_summaries:
    print(summary)

#======= Question 2 =======

# Task 1 : Input length validator

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

if len(first_name) < 2:
    print("ERROR ERROR : Your first name is too short.")
if len(last_name) < 2:
    print("ERROR ERROR : Your last name is too short.")

if len(first_name) >= 2 and len(last_name) >= 2:
    print(f"{first_name} {last_name} is a mighty fine name!")