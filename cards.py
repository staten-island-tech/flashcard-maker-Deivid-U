import json

class Teacher:
    def make_cards():
        finished = False
        cards = {}
        while finished == False:
            if input("type 'YES' if you would like to make a card ") == 'YES': 
                cards[input('Type in the question: ')] = input('Type in the answer: ')
            else:
                finished = True
        with open("FlashCards.json", "w") as file:
            json.dump(cards, file, indent = 4)


class Student:
    def answer_questions():
        streak = 0
        points = 0
        with open("FlashCards.json", "r") as file:
            student_cards = json.load(file)
        for card in student_cards:
            print(f'{card}')
            answer = input('What is the answer? ')
            if answer == student_cards[card]:
                points += (10 + streak)
                streak += 1
                print(f'CORRECT! You now have {points} points and a streak of {streak}!')
            else:
                streak = 0
                print(f'INCORRECT! The correct answer was "{card.value()}. Your streak has been reset to 0.')
            print(f'You have answered every index card. Your final score was: {points}') 

while True:

    role_decided = False

    while role_decided == False:
        response = input('Type 1 if you are a Teacher, Type 2 if you are a student. ')
        if response == '1':
            Teacher.make_cards() 
            role_decided = True
        elif response == '2':
            Student.answer_questions()
            role_decided = True
        else:
            print('Input invalid')


