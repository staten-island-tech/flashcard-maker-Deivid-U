import json

class Teacher:
    def make_cards():
        finished = False
        cards = {}
        while finished == False:
            if input("type 'YES' if you would like to make a card") == 'YES':
                cards[input('Type in a question: ')] = input('Type in the answer: ')
            else:
                finished = True
        with open(FlashCards.json) as file:
            json.dump(Ydfjisdoisjfhadjaiojf)


class Student:
    def answer_questions():
        streak = 0
        points = 0
        with open(FlashCards.json) as file:
            for card in file:
                print(f'{card.key()}')
                answer = input('What is the answer?')
                if answer == card.value():
                    streak += 1
                    points += (10 + streak)
                    print(f'CORRECT! You now have {points} points and a streak of {streak}!')
                else:
                    streak = 0
                    print(f'INCORRECT! The correct answer was "{card.value()}. Your streak has been reset to 0.')
                print(f'You have answered every index card. Your final score was: {points}')

roledecided = False

while roledecided == False:
    input('Type 1 if you are a Teacher, Type 2 if you are a student.')