import random

q_num = int(input("How many questions do you want? [1-5] : "))

i = 1
score = 0

quest_list = [
            "What is capital of Bahrain?",
            "What is national animal of India?",
            "What is national bird of India?",
            "What is 2 + 13?",
            "What is 22 + 20",
            "Is Bahrain an island? [Y/N]",
            "What is national animal of Bahrain?",
            "What is national bird of Bahrain?",
            "What is national sport of India?",
            "How many states are there in India?",
            "Which city is known as pink city?",
            "Which is the largest state of India?",
            "What is the atomic number of oxygen?",
            "General name for H2O is?",
            "Which country is Burj Khalifa located in?",
            "Indian Ocean is named after which country?"
            ]

ans_list = ["MANAMA", "TIGER", "PEACOCK", "15", "42", "Y", "ORYX", "BULBUL", "HOCKEY", "28", "JAIPUR",
            "RAJASTHAN", "8", "WATER", "DUBAI", "INDIA"]

while i <= q_num:
    questions = random.choice(quest_list)
    print(f"\n{questions}")
    answer = input("Enter answer : ")
    f_answer = answer.upper()

    if questions == quest_list[0]:
        if f_answer == ans_list[0]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[0]}")

    elif questions == quest_list[1]:
        if f_answer == ans_list[1]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[1]}")

    elif questions == quest_list[2]:
        if f_answer == ans_list[2]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[2]}")

    elif questions == quest_list[3]:
        if f_answer == ans_list[3]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[3]}")
    
    elif questions == quest_list[4]:
        if f_answer == ans_list[4]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[4]}")

    elif questions == quest_list[5]:
        if f_answer == ans_list[5]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[5]}")
    
    elif questions == quest_list[6]:
        if f_answer == ans_list[6]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[6]}")
    
    elif questions == quest_list[7]:
        if f_answer == ans_list[7]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[7]}")
    
    elif questions == quest_list[8]:
        if f_answer == ans_list[8]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[8]}")
    
    elif questions == quest_list[9]:
        if f_answer == ans_list[9]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[9]}")

    elif questions == quest_list[10]:
        if f_answer == ans_list[10]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[10]}")

    elif questions == quest_list[11]:
        if f_answer == ans_list[11]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[11]}")
    
    elif questions == quest_list[12]:
        if f_answer == ans_list[12]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[12]}")
    
    elif questions == quest_list[13]:
        if f_answer == ans_list[13]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[13]}")
    
    elif questions == quest_list[14]:
        if f_answer == ans_list[14]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[14]}")

    elif questions == quest_list[15]:
        if f_answer == ans_list[15]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[15]}")

    i += 1

print(f"\nYou got {score}/{q_num}")