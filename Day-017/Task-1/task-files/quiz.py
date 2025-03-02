# Day 17 - Task 1 - The Quiz Project using OOP

# Create the QuizMaster class.
class QuizMaster:

    def __init__(self, question_data ):

        # Define and initialize question number to 0.
        self.question_number = 0

        # Define and initialise indication if there are questions left.
        self.questions_left = True

        # Define and initialize the current score.
        self.current_score = 0

        # Define and initialize the question list.
        self.question_list = []

        # Loop through the question_data, create new Question object each time and
        # append it to question_list:
        for item in question_data:

            # Create new question object.
            question = self.Question(text=item["text"], answer=item["answer"])

            # Append the next question object to question_list.
            self.question_list.append(question)

    # Create the Question inner class.
    class Question:

        def __init__(self, text, answer):
            # Define and initialize an attribute to hold the question text of the question.
            self.text = text

            # Define and initialize an attribute to hold the answer text of the question.
            self.answer = answer

    # Define the class method to ask the next question from the list
    # and ask the user for their answer.
    def ask_next_question(self):
        """
        This Class method asks the user the next question from the question list.

        It also performs a check that the user is entering only true or false as answer.

        It returns the question answer.
        :return:
        """

        # Get the next question form the question list.
        next_question = self.question_list[self.question_number]

        # Define and initialise the question answer to an empty string.
        question_answer = ""

        # Define and initialize indication that the user answer is invalid.
        user_answer_is_invalid = True

        # Loop while the user answer in not "true" or "False".
        while user_answer_is_invalid:

            # Ask the user the next question and get their answer.
            question_answer = input(f"Q.{self.question_number + 1} : {next_question.text} Answer True or False: ").lower()

            # Has the user entered "True" or "False"?
            if not ( question_answer == "true" or question_answer == "false" ):

                # No, so print error message.
                print("Error: You have entered an invalid answer. Please try again.\n")

            # Yes.
            else:

                # Indicate that a valid user input has been made.
                user_answer_is_invalid = False

        # Return the question answer.
        return question_answer

    # Define a class method to check the user's answer against the correct answer from the
    # question list.
    def check_next_answer(self, question_answer):
        """
        This Class method checks the answer given by the user against the correct
        answer in the question list.

        It prints the appropriate message to the console depending on whether the user got
        the question correct or not.

        It increments the question number ready for the next question to be fetched from the
        question list.

        :param question_answer:
        :return:
        """

        # Fetch the current question being asked.
        question = self.question_list[self.question_number]

        # Is the user answer correct?
        if question_answer == question.answer.lower():

            # Yes, so increment the user score.
            self.current_score += 1

            # Print success message to the console.
            print("Well done! You got it right!")

            # Print the correct answer to the console.
            print(f"The answer was {question.answer}.")

        # No.
        else:

            # Print wrong-answer message to the console.
            print(f"Sorry. You got it wrong.")

            # Print the correct answer to the console.
            print(f"The correct answer is: {question.answer}.")

        # Increment the question number.
        self.question_number += 1

        # Print the user's current score to the console.
        print(f"Your current score is: {self.current_score}/{self.question_number}.\n")

        # Update is there are still questions left.
        self.questions_left = self.question_number < len(self.question_list)

        # Return
        return

    # Define a class method to print out the goodbye message to the console.
    def print_goodbye_message(self):
        """
        Prints out the goodbye message to the console and the user's final score.
        :return:
        """

        print("Thank you for playing the quiz game.")

        print(f"Your final score is: {self.current_score}/{self.question_number}.\n")

        return

