import random
import time

quiz_data={
     "General Knowledge": {
        "timeLimit": 20,
        "questions": [
            {
                "text": "What is the capital of France?",
                "choices": {"A": "Paris", "B": "London", "C": "Berlin", "D": "Madrid"},
                "answer": "A"
            },
            {
                "text": "Which planet is known as the Red Planet?",
                "choices": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Saturn"},
                "answer": "B"
            },
        ]
    },
    "Math": {
        "timeLimit": 30,
        "questions": [
            {
                "text": "What is 7 * 8?",
                "choices": {"A": "54", "B": "56", "C": "64", "D": "48"},
                "answer": "B"
            },
            {
                "text": "What is the square root of 49?",
                "choices": {"A": "7", "B": "8", "C": "9", "D": "6"},
                "answer": "A"
            },
        ]
    },
    "History": {
        "timeLimit": 25,
        "questions": [
            {
                "text": "Who was the first President of Kenya?",
                "choices": {"A": "Mwai Kibaki", "B": "Jomo Kenyatta", "C": "Daniel Moi", "D": "Uhuru Kenyatta"},
                "answer": "B"
            },
            {
                "text": "What year did Kenya gain independence?",
                "choices": {"A": "1944", "B": "1945", "C": "1946", "D": "1947"},
                "answer": "B"
            },
        ]
    }
}

def getCategoryByName(userInput, categories):
    for category in categories:
        if userInput.strip().lower() == category.lower():
            return category
    return None


def chooseCategory():
    print("Welcome!")
    print("Available categories:")
    for category in quiz_data.keys():
        print(f"- {category}")

    selectedCategory = None
    while selectedCategory is None:
        userInput = input("Input the name of category you want: ")
        selectedCategory = getCategoryByName(userInput, quiz_data.keys())
        if selectedCategory is None:
            print(" Category not found. Please try again.")
    return selectedCategory
# selectedCategory=chooseCategory()

def runQuiz(categoryName):
    categoryData=quiz_data[categoryName]
    questions=categoryData["questions"]
    timeLimit=categoryData["timeLimit"]
    random.shuffle(questions)
    
    score=0

    print(f"Starting quiz in: {categoryName}(Time per question:{timeLimit})")

    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['text']}")
        for option, value in q["choices"].items():
            print(f"  {option}. {value}")

        startTime=time.time()
        userAnswer=None

        while True:
            userAnswer=input("Your answer(A/B/C/D):").strip().upper()
            if time.time()-startTime>timeLimit:
                print("Time's up!")
                break
            if userAnswer in['A','B','C','D']:
                break
            else:
                print("Invalid option")

        if userAnswer==q["answer"]:
            print("correct!")    
            score +=1

        else:
            correctText=q["choices"][q["answer"]]
            print(f"Wrong! Correct answer:{q['answer']}.{correctText}")  
    print(f"Final Score:{score} out of {len(questions)}")   
    if score == len(questions):
        print("Excellent!")
    elif score >= len(questions) // 2:
        print("Good job!")
    else:
        print("Try Again!")     


selectedCategory = chooseCategory()
runQuiz(selectedCategory)