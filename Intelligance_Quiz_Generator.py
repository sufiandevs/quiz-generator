import random
import numpy as np
import matplotlib.pyplot as plt
questions = {
    "AI Stands for?": "artificial intelligence",
    "What is Python?": "programming language",
    "Who developed Python?": "guido van rossum",
    "CPU Stands for?": "central processing unit",
    "RAM Stands For?": "random access memory",
    "OS Stands for?": "operating system",
    "HTML Stands for?": "hyper text markup language",
    "CSS Stands for?": "cascading style sheets",
    "IP Stands for?": "internet protocol",
    "DBMS Stands for?": "database management system",
    "Explain the difference between supervised and unsupervised learning.": "supervised labeled unsupervised unlabeled",
    "What does HTTP stand for?": "hypertext transfer protocol",
    "Define normalization in databases.": "organizing data reduce redundancy",
    "What is the function of the ALU in a CPU?": "arithmetic logic unit calculations logic",
    "Name the four layers of the OSI model.": "physical data link network transport",
    "What is recursion in programming?": "function calling itself",
    "What is Big O notation?": "algorithm time complexity",
    "Explain polymorphism in OOP.": "ability objects many forms",
}

# Random Question Selection
total_questions = 5
random_questions = random.sample(list(questions.keys()), total_questions)

score = 0

print("🧠 Welcome to Computer Science Online Quiz")
print("---------------------------------------")

# partial keyword match with threshold 70%, your style matching

def is_answer_correct(user_ans, correct_keywords, threshold=0.7):
    user_ans = user_ans.lower()
    keywords = correct_keywords.split()
    matched = 0
    for kw in keywords:
        if kw in user_ans:
            matched += 1
    ratio = matched / len(keywords)
    return ratio >= threshold


# Quiz Loop

for question in random_questions:
    print("\nQuestion:", question)
    user_answer = input("Write Your Answer Here: ")

    correct_answer= questions[question]

    if is_answer_correct(user_answer, correct_answer):
        score += 1


# Final Result Calculation

wrong = total_questions - score
percentage = (score / total_questions) * 100

print("\n---------------------------------------")
print("Quiz Completed")
print("Total Questions:", total_questions)
print("Correct Answers:", score)
print("Wrong Answers:", wrong)
print("Percentage:", percentage, "%")

if percentage >= 80:
    performance = "Excellent"
elif percentage >= 60:
    performance = "Good"
elif percentage >= 40:
    performance = "Average"
else:
    performance = "Poor"

print("Performance:", performance)


# NumPy arrays for scores

labels = np.array(['Correct Answers', 'Wrong Answers'])
values = np.array([score, wrong])


# Matplotlib Bar Chart

colors = ['green', 'red']
plt.bar(labels, values, color=colors)
plt.title('Quiz Performance')
plt.ylabel('Number of Questions')
plt.ylim(0, total_questions)
plt.show()
