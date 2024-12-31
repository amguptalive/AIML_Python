# Assuming Question is a class with attributes 'question_text' and 'answer'
class Question:
    def __init__(self, question_text, answer):
        self.question_text = question_text
        self.answer = answer

# Assuming question_data is a dictionary where each key-value pair represents a question and its answer
question_data = {"What is 2+2?": "4", "What is the capital of France?": "Paris"}

# Create an empty list for your question bank
question_bank = []

# Use a for loop to append desired values from Question objects to your question bank
for question_text, answer in question_data.items():
    question = Question(question_text, answer)
    question_bank.append((question.question_text, question.answer))

# Now, question_bank is a list of tuples, where each tuple contains a question and its answer
print(question_bank)
