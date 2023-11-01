#CS175
#Sashank Vaddiparty
#Average and Grade Assignment

#New Comment System : understanding the program based on what we input and what we what for output#

#grade_ranges: This is a list that matches scores with letter grades. For example, if a score is between 90 and 100, it gets an "A".
grade_ranges = [ 
    (90, 100, "A"),
    (80, 89, "B"),
    (70, 79, "C"),
    (60, 69, "D"),
    (0, 59, "F")
]

#determine_grade(score) Function:
#Input: A score
#Output: The letter grade for that score.
#How it works: It looks up the score in the grade_ranges list and finds out its letter grade.
def determine_grade(score):
    for low, high, grade in grade_ranges: # the list has 2 inputs ex : 90, 100 so we can use low and high to match the list.
        if low <= score <= high:
            return grade

#enter_scores() Function:
#Asks the user to input 5 scores (one by one).
#For each score, it finds out its letter grade.
#Returns two lists: One with the scores and another with the grades.
def enter_scores():
    scores = [] 
    grades = []
    for i in range(5):
        try:
            score = int(input(f'Enter score {i + 1}: '))
            scores.append(score)
            grades.append(determine_grade(score))
        except ValueError:
            print("Please enter a valid number.")
    return scores, grades

#display_scores(scores, grades) Function:

#Input: Lists of scores and grades.
#Output: Nicely displays the scores, their numeric value, and their letter grade. Then, it calculates and shows the average.


'''
zip(scores, grades): The zip() function takes two or more lists and returns an iterator that generates tuples containing elements from the input lists, taken pairwise.
#For example:
scores = [90, 80]
grades = ["A", "B"]
zipped = list(zip(scores, grades))
# zipped now contains: [(90, "A"), (80, "B")]
enumerate(zip(scores, grades)): enumerate() is a function that takes an iterator (like the one zip() returns) and
returns another iterator that generates pairs of the form (index, element). The index starts from 0 by default.

enumerated = list(enumerate(zipped))
# enumerated now contains: [(0, (90, "A")), (1, (80, "B"))]
'''
def display_scores(scores, grades):
    print("\nScore\t\tNumeric Grade\tLetter Grade")
    print("----------------------------------------------------")
    for i, (score, grade) in enumerate(zip(scores, grades)):
        print(f'score {i+1}:\t{score}.0\t\t{grade}')
    avg = sum(scores) / len(scores)
    print(f"Average score:\t{avg:.1f}\t{determine_grade(avg)}\n")

#repeat() Function:

#Continuously asks the user to input scores, displays them, then asks if they want to do it again.
def repeat():
    while True:
        scores, grades = enter_scores()
        display_scores(scores, grades)
        cont = input("Enter 'yes' if you would like to do another calculation: ")
        if cont.lower() != 'yes':
            break

# Extra credit#


#my_random(low, high) Function:

#Input: Two numbers defining a range.
#Output: A random number within that range.

def my_random(low, high):
    import random
    return random.randint(low, high)


#enter_random_scores() Function:
#Generates 5 random scores.
#For each random score, it determines its letter grade.
#Returns two lists: One with the random scores and another with the grades
def enter_random_scores():
    scores = []
    grades = []
    for i in range(5):
        score = my_random(1, 100)
        scores.append(score)
        grades.append(determine_grade(score))
    return scores, grades

#repeat_random_scores() Function:
#Continuously generates random scores, displays them, then asks if the user wants to do it again.
def repeat_random_scores():
    while True:
        scores, grades = enter_random_scores()
        display_scores(scores, grades)
        cont = input("Enter 'yes' if you would like to do another calculation: ")
        if cont.lower() != 'yes':
            break

# Uncomment the function you want to run
# repeat()
repeat_random_scores()
