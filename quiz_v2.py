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

j = 0
score = 0

quest_list = list(quest_dict.keys())
ans_list = list(quest_dict.values())

for questions in quest_dict:
    print(questions)
    answer = input("Enter answer : ")
    ans = answer.upper()
    if questions == quest_list[j]:
        if ans == ans_list[j]:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            print(f"Correct answer is {ans_list[j]}")
    j += 1
    
print(f"Your final score is {score}/{len(quest_list)}")