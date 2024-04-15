#importing numpy
import numpy as np

#first we take in the feedback as a list of strings
feedback = [
    ("I like the AI course", "positive"),
    ("I dislike the AI course", "negative"),
    ("Good course nice assignment", "positive"),
    ("Interaction is poor", "negative"),
    ("Great examples, love the AI course", "positive")
]

#creating a vocabulary set with all the unique words from the feedback
def create_vocab(feedback):
    vocab = set()
    for statement, _ in feedback:
        words = statement.lower().split()
        vocab.update(words)
    return sorted(vocab)

#creating feature vectors which i need to look into
#A feature vector is a term commonly used in machine learning and data analysis. It refers to a numerical representation of a data point, often used to describe the characteristics or features of the data in a quantitative way. 
# In the context of machine learning, a feature vector typically represents an individual instance or data point, where each element in the vector corresponds to a specific feature or attribute of that instance. These features could be anything from numerical values like height or weight to categorical variables like color or type. 
# Feature vectors are fundamental to many machine learning algorithms as they provide a structured input for training models to learn patterns and make predictions based on the given data. They play a crucial role in tasks such as classification, regression, and clustering.
def create_feature_vectors(feedback, vocab):
    feature_vectors = []
    for statement, _ in feedback:
        vector = np.zeros(len(vocab))
        words = statement.lower().split()
        for word in words:
            if word in vocab:
                vector[vocab.index(word)] += 1
        feature_vectors.append(vector)
    return feature_vectors

def calculate_probabilities(feedback, vocab):
    num_positive = sum(1 for _, classification in feedback if classification=="positive")
    num_negative = sum(1 for _, classification in feedback if classification=="negative")
    total = len(feedback)

    prob_positive = num_positive/total
    prob_negative = num_negative/total

    pos_word_counts = np.zeros(len(vocab))
    neg_word_counts = np.zeros(len(vocab))
    for statement, classification in feedback:
        words = statement.lower().split()
        for word in words:
            if word in vocab:
                if classification == "positive":
                    pos_word_counts[vocab.index(word)] += 1
                else:
                    neg_word_counts[vocab.index(word)] +=1

    prob_word_positive = pos_word_counts / np.sum(pos_word_counts)
    prob_word_negative = neg_word_counts / np.sum(neg_word_counts)

    return prob_positive, prob_negative, prob_word_positive, prob_word_negative

def classify_statement(statement, vocab, prob_positive, prob_negative, prob_word_positive, prob_word_negative):
    words = statement.lower().split()
    pos_prob = prob_positive
    neg_prob = prob_negative
    for word in words:
        if word in vocab:
            pos_prob += prob_word_positive[vocab.index(word)]
            neg_prob += prob_word_negative[vocab.index(word)]
    if pos_prob > neg_prob:
        return "positive"
    else:
        return "negative"

def main():
    print("\n")
    vocab = create_vocab(feedback)
    print(vocab)
    print("\n")
    feature_vectors = create_feature_vectors(feedback, vocab)
    print(feature_vectors)
    print("\n")
    prob_positive, prob_negative, prob_word_positive, prob_word_negative = calculate_probabilities(feedback, vocab)

    new_statement = input("Enter statement to be classified: ")
    classification = classify_statement(new_statement, vocab, prob_positive, prob_negative, prob_word_positive, prob_word_negative)
    print("Classification for '{}' is {}.".format(new_statement, classification))

if __name__ == "__main__":
    main()
