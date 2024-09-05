from collections import Counter
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_diversity(qa_pairs):
    questions = [pair['question'] for pair in qa_pairs]
    answers = [pair['answer'] for pair in qa_pairs]
    
    # Lexical diversity
    question_words = ' '.join(questions).split()
    answer_words = ' '.join(answers).split()
    question_diversity = len(set(question_words)) / len(question_words)
    answer_diversity = len(set(answer_words)) / len(answer_words)
    
    # Question type diversity
    question_types = Counter([q.split()[0].lower() for q in questions])
    question_type_diversity = len(question_types) / len(questions)
    
    # Semantic diversity using TF-IDF and cosine similarity
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(questions + answers)
    cosine_similarities = cosine_similarity(tfidf_matrix)
    semantic_diversity = 1 - np.mean(cosine_similarities)
    
    return {
        'question_lexical_diversity': question_diversity,
        'answer_lexical_diversity': answer_diversity,
        'question_type_diversity': question_type_diversity,
        'semantic_diversity': semantic_diversity
    }

def assess_quality(qa_pairs):
    # This is a simplified quality assessment
    # In a real-world scenario, you might want to use more sophisticated methods
    # or even human evaluation for a subset of the data
    
    avg_question_length = np.mean([len(pair['question'].split()) for pair in qa_pairs])
    avg_answer_length = np.mean([len(pair['answer'].split()) for pair in qa_pairs])
    
    return {
        'avg_question_length': avg_question_length,
        'avg_answer_length': avg_answer_length
    }

def evaluate_dataset(qa_pairs):
    diversity_metrics = calculate_diversity(qa_pairs)
    quality_metrics = assess_quality(qa_pairs)
    
    return {**diversity_metrics, **quality_metrics}