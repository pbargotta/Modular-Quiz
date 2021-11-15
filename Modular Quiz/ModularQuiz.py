import random


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class Quiz:
    score = 0
    question_counter = 1

    def __init__(self):
        self.questions = []
        self.answers = []
        self.quiz_questions = self.create_quiz()

    def getquestions(self):
        # opens 'Quiz Questions' text file as read-only and returns each line of the file in a list then closes the file
        # to save memory
        questions_file = open("Quiz Questions.txt", "r")
        all_questions = questions_file.readlines()
        questions_file.close()

        question_components = []
        # iterates through all of the lines in the files and saves all components of the question into a list
        # and then joins it together once the end of the question is reached - end of question indicated by a new line
        for line in range(len(all_questions)):
            question_line = all_questions[line]
            if question_line == "\n":
                self.questions.append(" ".join(question_components))
                question_components.clear()
            else:
                question_components.append(question_line)
        return self.questions

    def getanswers(self):
        # opens 'Quiz Answers' text file as read-only and returns each line of the file in a list then closes the file
        # to save memory
        answers_file = open("Quiz Answers.txt", "r")
        all_answers = answers_file.readlines()
        answers_file.close()

        answer_components = []
        # iterates through all of the lines in the files and saves all components of the question into a list
        # and then joins it together once the end of the question is reached - end of question indicated by a new line
        for line in range(len(all_answers)):
            answer_line = all_answers[line]
            if answer_line == "\n":
                self.answers.append(" ".join(answer_components))
                answer_components.clear()
            else:
                answer_components.append(answer_line.strip())
        return self.answers

    # puts each question and answer into the question object and puts them into the 'quiz_questions' list
    def create_quiz(self):
        self.getquestions()
        self.getanswers()

        quiz_questions = []
        for i in range(len(self.questions)):
            quiz_questions.append(Question(self.questions[i], self.answers[i]))
        return quiz_questions

    def run_quiz(self):
        random.shuffle(self.quiz_questions)

        for question in self.quiz_questions:
            print(f"QUESTION {self.question_counter}")
            self.question_counter += 1

            user_answer = input(question.question)
            if user_answer.lower() == question.answer:
                print("Correct!\n")
                Quiz.score += 1
            else:
                print(f"Incorrect. The correct answer is {question.answer}\n")
        print(f"You got {Quiz.score} out of {len(self.quiz_questions)}!")


print("Welcome to THE BEST Quiz!")
quiz = Quiz()
quiz.run_quiz()
