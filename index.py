name = input('Enter Your Name: ').capitalize()
print(f'Hey {name}, how can I help you?')

questions = [
    [f'1. Describe Gaurab Lohani', "Gaurab is a dedicated and skilled full stack developer with expertise in HTML, CSS, JavaScript, Django, Flask, and Python. He has a passion for crafting innovative web applications and strives to deliver high-quality solutions that meet client needs. On the front-end, he excels at creating visually appealing and interactive user interfaces using HTML, CSS, and JavaScript. He has experience in responsive web design, ensuring that applications look and perform seamlessly across various devices and screen sizes."],
    [f'2. Which school did Gaurab attend in primary level (1-8)?', 'Golden Future Academy Boarding School'],
    [f'3. Which college did Gaurab attend in secondary level (9-12)?', 'Future Star Secondary Boarding School'],
    [f'4. What is Gaurab planning to study in his bachelor program?', 'BIT'],
    [f'5. How many programming languages does he know?', 4, [f'a. Name the programming languages he knows:', '1. HTML\n2. CSS\n3. JavaScript\n4. Python']],
    [f'6. How many frameworks does he know?', 2, [f'a. Name the frameworks he knows:', '1. Flask\n2. Django']],
    [f'7. Which OS does he use?', 'Linux'],
]

def loop_question():
    for question in questions:
        print(question[0])

def question_answer_logic():
    user_input = input("Type (1-7) or 'quit' to exit: ").strip().lower()
    if user_input == 'quit':
        print("Exiting the program.")
        exit()
    
    try:
        user_input_question = int(user_input)
        if 1 <= user_input_question <= len(questions):
            user_input_question -= 1
            print(f'{questions[user_input_question][0]}\nAnswer: {questions[user_input_question][1]}\n')
            
            if len(questions[user_input_question]) > 2:
                print(questions[user_input_question][2][0])
                user_input_deep = input("Type 'a' for the detailed answer or 'mainmenu' to go back to the main menu: ").strip().lower()
                if user_input_deep == 'a':
                    print(f'{questions[user_input_question][2][0]}\nAnswer: \n{questions[user_input_question][2][1]}\n')
                elif user_input_deep == 'mainmenu':
                    when_true()
                else:
                    print('Invalid input. Please try again.')
        else:
            print('Invalid question number. Please enter a number between 1 and 7.')
    except ValueError:
        print('Invalid input. Please enter a number between 1 and 7 or type "quit" to exit.')

def when_true():
    while True:
        loop_question()
        question_answer_logic()

when_true()
