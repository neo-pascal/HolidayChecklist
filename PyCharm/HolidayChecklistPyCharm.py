#  File:       HolidayChecklist.py 
#  IDE:        PyCharm Edu 2018.1.3
#  Python:     Version 3.7.0
#  Purpose:    Write a program that allows the user to create and store a checklist for a holiday
#  Programmer: Neo-Pascal Ayestaran
#  Course:     Python Challenge 29
#  Date:       Sunday 5th August 2018, 11:15 BST
#  Notes:      ANSI escape codes appear not to be natively supported by IDLE

#Number validation function
def inputNumber(message):
    #Loop if not a valid number
    while True:
        try:
            #Try and assign the passed through value to the variable userInput
            userInput = int(input(message))
        except ValueError:
            #If not a valid number then prompt the user to enter a valid number by echoing a red error message
            print("\033[1;31;48mNot a valid number! Please try again.")
            continue
        else:
            #If a valid number then return value back to original call
            return userInput

# Echo blue checklist title
programTitle = '\n\033[1;34;48mHoliday Checklist\n=================\n'
print(programTitle)

# Ask the user to enter a holiday destination and store the result to the variable <destination>
destination = input('\033[1;30;48mPlease enter the holiday destination? ')
# Ask the user to enter how many items they need to pack then validate and store the result to the variable <itemTotal>
itemTotal = inputNumber('\033[1;30;48mPlease enter how many items you need to pack for your holiday to ' + destination + '? ')
# Ask the user to enter the number of tasks needed to complete then validate and store the result to the variable <taskTotal>
taskTotal = inputNumber('\033[1;30;48mPlease enter the number of tasks you need to complete to prepare? ')

# Preload the checklist with already entered user data
checklist = [destination, itemTotal, taskTotal]
checklistIndex = 3
item = ''

# Echo purple item list title
checklistTitle = '\n\033[1;35;48mItem List\n---------\n'
print(checklistTitle)

# Loop through item index in order to retrieve each user defined item
for itemIndex in range(1, itemTotal + 1):
    item = input('\033[1;30;48mPlease enter description for item ' + str(itemIndex) + '/' + str(itemTotal) + '? ')
    # Add the user input to the end of the checklist
    checklist.append(item)
    # Increment checklist index
    checklistIndex = checklistIndex + 1

# Echo purple task list title
checklistTitle = '\n\033[1;35;48mTask List\n---------\n'
print(checklistTitle)
task = ''

# Loop through task index in order to retrieve each user defined task
for taskIndex in range(1, taskTotal + 1):
    task = input('\033[1;30;48mPlease enter description for task ' + str(taskIndex) + '/' + str(taskTotal) + '? ')
    # Add the user input to the end of the checklist
    checklist.append(task)
    # Increment checklist index
    checklistIndex = checklistIndex + 1

# Define checklist filename
filename = 'HolidayChecklist.dat'

# Save checklist to filesystem
with open(filename, 'w') as filehandle:
    filehandle.writelines("%s\n" % place for place in checklist)

# Echo the checklist filename
exportDescription = ('\nChecklist has been saved to <' + filename + '> comprising of ' + str(checklistIndex) + ' values')
print(exportDescription)

# Clear the checklist ready for loading the previously saved data.
checklist.clear()

# Load checklist from filesystem
with open(filename, 'r') as filehandle:
    filecontents = filehandle.readlines()

    for line in filecontents:
        # Remove the linebreak which is the last character of the string
        current_place = line[:-1]
        # Add item to the list
        checklist.append(current_place)

# Echo checklist
print("\nchecklist = " + str(checklist))
