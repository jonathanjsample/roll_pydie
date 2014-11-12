#######################
# roll_pydie
# gaming dice generator
# version 1
#######################

###########################
# random module importation
###########################

import random

#############################
# instructional text for user
#############################

print '''
--------------------------------------------------
To receive a random die roll, please choose 
between 4, 6, 8, 10, 12, and 20-sided die, 
or enter "quit" to exit the program.
--------------------------------------------------
'''

#####################################
# input and conditionals to determine 
# psuedo-random numeric result
#####################################

while True:
    try:
        inp = raw_input('>Enter number of sides: ')
        if inp == 'quit':
            print '''
            ****************************
            **Thank you for the rolls.**
            ****************************
            '''
            break
        num_sides = int(inp)
        print '...'
        if num_sides % 2 == 0 and num_sides >= 4 and num_sides <= 20:
            print """You have chosen the %s-sided die. \nStandby for the result of your roll.""" % num_sides
            print '....'
            if num_sides == 4:
                result = random.randint(1, 4)
                print 'Your result: %s' % result
            elif num_sides == 6:
                result = random.randint(1, 6)
                print 'Your result: %s' % result
            elif num_sides == 8:
                result = random.randint(1, 8)
                print 'Your result: %s' % result
            elif num_sides == 10:
                result = random.randint(1, 10)
                print 'Your result: %s' % result
            elif num_sides == 12:
                result = random.randint(1, 12)
                print 'Your result: %s' % result
            elif num_sides == 20:
                result = random.randint(1, 20)
                print 'Your result: %s' % result
            else:
                print '''Please enter either 4, 6, 8, 10, 12, or 20\nfor die roll result.'''
        else:
            print '''Please enter either 4, 6, 8, 10, 12, or 20\nfor die roll result.'''
    except:
        print 'Invalid entry. Please enter a number.'
