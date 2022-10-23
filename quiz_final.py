import random

quest_dict = {
            "What is capital of Bahrain?" : "MANAMA",
            "What is national animal of India?" : "TIGER",
            "What is national bird of India?" : "PEACOCK",
            "What is 2 + 13?" : "15",
            "What is 22 + 20" : "42",
            "Is Bahrain an island? [Y/N]" : "Y",
            "What is national animal of Bahrain?" : "ORYX",
            "What is national bird of Bahrain?" : "BULBUL",
            "What is national sport of India?" : "HOCKEY",
            "How many states are there in India?" : "28",
            "Which city is known as pink city?" : "JAIPUR",
            "Which is the largest state of India?" : "RAJASTHAN",
            "What is the atomic number of oxygen?" : "8",
            "General name for H2O is?" : "WATER",
            "Which country is Burj Khalifa located in?" : "DUBAI",
            "Indian Ocean is named after which country?" : "INDIA"
            }
    
q_num = int(input("How many questions do you want [1-5]: "))

i = 1
score = 0
quest_list = list(quest_dict.keys())
ans_list = list(quest_dict.values())

while i <= q_num:
    questions = random.choice(quest_list)
    q = quest_list.index(questions)
    print(f"\n{questions}")

    answer = input("Enter answer : ")
    f_answer = answer.upper()

    if questions == quest_list[q]:
        if f_answer == ans_list[q]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[q]}")
    i += 1
print(f"\nYou scored {score}/{q_num}\n")