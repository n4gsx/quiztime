#!/usr/bin/env python

"""
Quiztime version 1.0

Main() mostly pulled from: 
http://codereview.stackexchange.com/questions/14838/multiple-choice-quiz-with-stat-tracking
The rest created by: 
Brian Markham

Description:
This script categorically quizzes the user based on a question bank imported from csv.
The CSV is parsed to a nested dict and should contain the following 3 field format:

category,question,answer

This script also tracks some statistics during runtime.
"""

import random
import csv
import os

# Creates the test bank
def createTestBank():
	testBank = {} #create an empty dictionary
	with open("questions.csv", "rU") as csvfile: # open the file readable with universal encoding
		questions = csv.reader(csvfile)
		for row in questions:
			if row[0] not in testBank: #add the category if it doesn't exist
				testBank[row[0]] = {}
			testBank[row[0]][row[2]] = row[1] #now add the Q's and A's to the category, which are swapped for dict logic during quiz time
	return testBank

# Selects the category to be quizzed on
def selectCategory(testBank):
	os.system('cls' if os.name=='nt' else 'clear')
	inc = 1
	print "Select a category to be quizzed on:"
	for k in testBank: #print all categories
		print str(inc) + ") " + k
		inc += 1
	selection = raw_input("> ")
	selection = int(selection)
	selection < inc and selection > 0
	inc = 1
	for category in testBank:
		if inc == selection:
			return category
		else:
			inc += 1

# Stat tracking
def print_stats(right_answer_total, wrong_answer_total, percentage):
    os.system('cls' if os.name=='nt' else 'clear') 
    print "-" * 37
    print "|         Stat Tracking             |"
    print "-" * 37
    print "| Correct | Incorrect |  Percentage |"
    print "-" * 37
    print "|    %d    |     %d     |     %d %%     |" % (right_answer_total, wrong_answer_total, percentage)
    print "-" * 37
    print "\n\n\n"
	
# Main portion of the program
def main():
    right_answer_total = 0
    wrong_answer_total = 0
    percentage = 0.0
    testBank = createTestBank()
    category = selectCategory(testBank)

    print "You picked the category '%s'." % (category)

    while True:
        print_stats(right_answer_total, wrong_answer_total, percentage)

        possible_answers = random.sample(testBank[category], 3)
        # User is presented with a question. A value from the previous randomly selected possible_answers is selected as the 'correct_answer'
        correct_answer = random.choice(possible_answers)
        question = testBank[category][correct_answer]
        print "Select an answer, (q) to quit, or (n) for a new category."
	print "\n\nQuestion: ", question
        print "\n\n(a)%s   (b)%s   (c)%s" % tuple(possible_answers)

        selection = raw_input("> ")
        if selection not in ('a', 'b', 'c', 'n', 'q'):
	    os.system('cls' if os.name=='nt' else 'clear')
            print "That is not a valid selection."
            break
	elif ord(selection) == ord('q'):
	    os.system('cls' if os.name=='nt' else 'clear')
	    break
	elif ord(selection) == ord('n'):
	    category = selectCategory(testBank)
	    continue

        answer = possible_answers[ord(selection) - ord('a')]
        
	if answer == correct_answer:
            print "That's correct!"
            right_answer_total += 1
        else:
            print "I'm sorry, that is incorrect..."
            wrong_answer_total += 1

        percentage = 100 * right_answer_total / float(right_answer_total + wrong_answer_total)

if __name__ == '__main__':
    main()

