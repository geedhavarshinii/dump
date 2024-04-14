import numpy as np

feedback = [
    ("I like the AI course", "positive"),
    ("I dislike the AI course", "negative"),
    ("Good course nice assignment", "positive"),
    ("Interaction is poor", "negative"),
    ("Great examples, love the AI course", "positive")
]

def create_vocab(feedback):
    vocab = set()
    for statement, _ in feedback:
        words = statement.lower().split()
        vocab.update(words)
    return sorted(vocab)

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
    num_positive = sum(1 for _, classification in feedback if classification == "positive")
    num_negative = sum(1 for _, classification in feedback if classification == "negative")
    total = len(feedback)

    prob_positive = num_positive / total
    prob_negative = num_negative / total

    pos_word_counts = np.zeros(len(vocab))
    neg_word_counts = np.zeros(len(vocab))
    for statement, classification in feedback:
        words = statement.lower().split()
        for word in words:
            if word in vocab:
                if classification == "positive":
                    pos_word_counts[vocab.index(word)] += 1
                else:
                    neg_word_counts[vocab.index(word)] += 1

    prob_word_positive = pos_word_counts / np.sum(pos_word_counts)
    prob_word_negative = neg_word_counts / np.sum(neg_word_counts)

    return prob_positive, prob_negative, prob_word_positive, prob_word_negative

def classify_statement(statement, vocab, prob_positive, prob_negative, prob_word_positive, prob_word_negative):
    words = statement.lower().split()
    pos_prob = prob_positive
    neg_prob = prob_negative
    for word in words:
        if word in vocab:
            pos_prob *= prob_word_positive[vocab.index(word)]
            neg_prob *= prob_word_negative[vocab.index(word)]
    if pos_prob > neg_prob:
        return "positive"
    else:
        return "negative"

def main():
    vocab = create_vocab(feedback)
    feature_vectors = create_feature_vectors(feedback, vocab)
    prob_positive, prob_negative, prob_word_positive, prob_word_negative = calculate_probabilities(feedback, vocab)
    
    new_statement = "I dislike poor interaction"
    classification = classify_statement(new_statement, vocab, prob_positive, prob_negative, prob_word_positive, prob_word_negative)
    print("Classification for '{}' is: {}".format(new_statement, classification))

if __name__ == "__main__":
    main()
