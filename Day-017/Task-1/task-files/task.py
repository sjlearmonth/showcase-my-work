# Day 17 - Task 1 - The Quiz Project using OOP

# Import Question data.
from data import question_data

# Import QuizMaster class.
from quiz import QuizMaster

# Initialise quiz_master with the question_data
quiz_master = QuizMaster(question_data)

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



