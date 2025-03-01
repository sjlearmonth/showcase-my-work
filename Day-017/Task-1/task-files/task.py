# Day 17 - Task 1 - The Quiz Project using OOP

# Import Question class.
from question import Question

# Import Question data.
from data import question_data

# Import QuizMaster class.
from quiz import QuizMaster

# Define and initialize question bank.
question_bank = []

# Loop through all elements in the question bank list.
for item in question_data:

    # Create Question object.
    next_question = Question(text=item["text"], answer=item["answer"])

    # Append the next question object to the question bank List.
    question_bank.append(next_question)

# Initialise quiz_master with the quiz questions.
quiz_master = QuizMaster(question_bank)

# Loop while there are still questions to ask.
while quiz_master.questions_left:

    # Ask the next question and get an answer.
    next_answer = quiz_master.ask_next_question()

    # Check the answer.
    quiz_master.check_next_answer(next_answer)

######################
# End of while loop. #
######################

# Print goodbye message to the console.
quiz_master.print_goodbye_message()



