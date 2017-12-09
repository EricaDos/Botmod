#Bot Rescuer************************************************************
# Author:               Erica Dos Santos
#*******************************************************************************
import csv #Allows my csv (Comma Seperated Value) to be used.
import sys #Max amount that can be used 
import time#This allows time to be used within the function so that I will be allowed to slow down the process of the outputs
from colorama import init #Allows the use of colourama
from colorama import Fore, Back, Style #Allows to use colorama to modifie background , foreground and the style
init(autoreset=True)
#*******************************************************************************
#This is the default option if the user doesn't choose to modify their robot
level = 1 #Shows what level the player is in
power = 150#Shows the begin power that bot-mod begins with
traction = 'Wheels'#Indicates what traction bot-mod will begin with
bay = 'Small'#Indicates the bay size
max_in_hold = 1 #The maximum hold the passanger bay is premitted to hold.
def exit(): #allows the player to exit resulting in the closing of the game
    print()
#*******************************************************************************
#Start menu
def start_menu():
    choice='   '
    print('Bot Mod \n')
    #The options that are going to be displayed in the start menu
    print ('1] Exit Bot-Mod Rescuer!\n') #displays first option
    print ('2] Play Bot-Mod Rescuer!\n') #displays second option
    print ('3] Modify Bot-Mod\n') #displays third option
    print ('4] Instructions\n') #displays forth option
    while (choice not in ['1','2','3','4']): #if the choices are not within the given range
        choice = input('Please choose one of the given options:\n') #instructs the user to chose within the range
    if choice == '1': #The option displayed for the player to chose from
        exit() #function to exit the game
    elif choice == '2': #The option displayed for the player to chose from
        game() #Directs player to the game board to begin to play
    elif choice == '3':#The option displayed for the player to chose from
        modifications() #Allows the player to go to the modification area
    else:
        if choice == '4':#The option displayed for the player to chose from
         instruction_game()#Direct them to instruction game
         
def instruction_game(): #instruction function
    global instructions #global function which is allowed to be used throughout the whole game
    choice= '' #empty choice area so that the player can input their choice
    print('Lets begin!') #displays a message
    time.sleep(0.5) #time delay so that the game isn't carried out to quickly and can be read carefully
    print('_________________________________________________________________________\n') #displays seperation
    time.sleep(0.5)#time delay so that the game isn't carried out to quickly and can be read carefully
    print('To make changes to your bot mod , such as tractions and your bay size.\n') #prints instructions
    time.sleep(0.5)#time delay
    print('Select the options : Modifications\n')#prints instructions
    time.sleep(0.5)#time delay
    print('To just begin the game select : Play BotMod\n')#prints instructions
    time.sleep(0.5)#time delay
    print('When playing the game to control your BotMod\n')#prints instructions
    time.sleep(0.5)#time delay
    #This will instruct the player what will be used throughout the game to be able to direct their bot mod
    print('Use the chosen keys :\n')
    print('- n for North\n')
    print('- s for South\n')
    print('- e for East\n')
    print('- w for west\n')
    time.sleep(3)#time delay
    #allows the reader to view the instructions carefully as it is organized
    print('___________________________________________________________________________\n')
    time.sleep(3)#time delay


def initialise_level_variables():#Initialise 2D 10x10 landscape (array)
    #10x10 board which is linked to the cvs to display the required colours for the different terrain
    global landscape
    landscape = [
        ['','','','','','','','','',''],
        ['','','','','','','','','',''],
        ['','','','','','','','','',''],
        ['','','','','','','','','',''],
        ['','','','','','','','','',''],
        ['','','','','','','','','',''],
        ['','','','','','','','','',''],
        ['','','','','','','','','',''],
        ['','','','','','','','','',''],
        ['','','','','','','','','','',]]

    #Indicates where bot-mod is located on the board
    #Global allows these variable to be used through out my programme
    global bm_x, bm_y
    #corrodinates of the botmod
    bm_x = 0
    bm_y = 0

    # Global allows these variable to be used through out my programme
    global p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y
    #The  corrodinates of the passengers that need rescuing
    p1_x = 2
    p1_y = 0
    p2_x = 4
    p2_y = 6
    p3_x = 7
    p3_y = 2
    p4_x = 9
    p4_y = 6

    #allows these variable names to be used throughtout the programme
    global basecamp_x, basecamp_y
    basecamp_x = 6 #The location of the basecamp on the x axis
    basecamp_y = 3#The location of the basecamp on the y axis

    #Initialise bot-mod variables
    #allows these variable names to be used throughtout the programme
    global passanger_in_basecamp, number_in_hold
    passanger_in_basecamp = 0 #the begining value of the passengers in the basecamp
    number_in_hold = 0 #the begining value of the passengers in the bay
#*******************************************************************************
#Get bot-mod modifications
def modifications():
    #the begining value of the passengers in the basecamp
    global bay, traction, max_in_hold
    choice = '  ' #empty to allow the user to assign their chosen option
    print('WELCOME TO CHANGE YOUR BOTMOD')
    print('______________________________________________________________________')
    print('Choose your traction type?\n')#Displays the question
    print(' 1] Wheels\n')#Gives the first option of which traction will be used
    print(' 2] Tracks\n')#Gives the second option of which traction could be chosen
    print(' 3] Skis\n')#Gives the third option of which traction could be chosen
    while(choice not in ['1','2','3']): #Indicates the use of a list
        print('Please choose now:')#if the response is not in the list to display 'Please choose now'
        choice = input()#Allow the input window to open
    if choice == '1': #What the user needs to input according to their decision
      traction = 'Wheels'#If the user choses choice '1' wheels will be selected
    elif choice == '2':#What the user needs to input according to their decision
        traction = 'Tracks'#If the user choses choice '2' Tracks will be selected
    else:
      if choice == '3':#What the user need to input to chose the 3rd option that hs been printed
        traction = 'Skis'#If the user choses choice '3' skis will be selected
    print ('Ok, Your traction type is -',traction) #Displays the option selected by the user
    choice = ' '#empty to allow the user to assign their chosen option
    print('\n') #creates spacing
    print('Choose the size of your passanger bay\n')
    print('1] Large\n') #the different options that are displayed to the user
    print('2] Medium\n')#each option is assigned to a value so that when selected it can be located and assigned to choice
    print('3] Small\n')
    while (choice not in ['1','2','3']): #if the given value is not within the range 1 - 3*
        print('Please select your bay - ') #*instructions to select again will be displayed
        choice = input()
    if choice == '1': #assigned variable
        bay = 'Large' #given name that is assigned to the choice number
        max_in_hold = 3 #Indicates the change of maximum hold of the passanger bay
    elif choice =='2':#assigned variable
          bay = 'Medium'#given name that is assigned to the choice number
          max_in_hold = 2 #Indicates the change of maximum hold of the passanger bay
    else:
        bay = 'Small'#given name that is assigned to the choice number
        max_in_hold = 1 #Indicates the change of maximum hold of the passanger bay

        #Shows the user what passanger bay they used
    print ('Ok!the size of your passenger bay is-',bay) #Shows what bay the user has selected to use
#*******************************************************************************
def print_landscape():
    r= 0 #Initialise row count
    c = 0 #Initialise column count

    for row in landscape: #Row at a time in the landscape
        for col in row: # Column at a time in the landscape
            my_output = ' ' #what will be displayed in the game board
            #Checks if passanger 1 is here
            if (r == p1_y) and (c == p1_x):#displayed on the board to identify the passenger
                my_output = Fore.BLACK + 'P' #given colour to be displayed on the board

            #Checks if passanger2 is here
            if (r == p2_y) and (c == p2_x):#displayed on the board to identify the passenger
                my_output = Fore.BLACK + 'P' #given colour to be displayed on the board

            #Checks if passanger2 is here
            if (r == p3_y) and (c == p3_x):#displayed on the board to identify the passenger
                my_output = Fore.BLACK + 'P'#given colour to be displayed on the board

            #Checks if passanger2 is here
            if (r == p4_y) and (c == p4_x):#displayed on the board to identify the passenger
                my_output = Fore.BLACK + 'P'#given colour to be displayed on the board

            #Checks location of basecamp
            if (r == basecamp_y) and (c == basecamp_x):
                my_output = Fore.RED + 'C' #given colour to be displayed on the board and be easily identified

            #Check if the bot-mod is here
            if (r == bm_y) and (c == bm_x):
                my_output = Fore.RED + 'B'#displayed on the board to identify the botmod
            #Output the landscape square
            if col=="grass":
                #The chosen colour for the landscape square
                sys.stdout.write(Back.GREEN+my_output),
                #The chosen colour to identifythe landscape type
            elif col==" ice ":
                sys.stdout.write(Back.WHITE+my_output),
            else:
                #The chosen colour to identifythe landscape type
                col =="rocks"
                sys.stdout.write(Back.YELLOW+my_output),
            c = c+1 #Increment column count
        r = r+1 #Increment row count
        c = 0 #Reset column count
        print()#Move to the next column
#*******************************************************************************
#Load the landscape from the CSV file
def load_landscape():
    global landscape
    #read in the file
    loaded_landscape = csv.reader(open('board_landscape.csv'),delimiter=',')
    r=0 #Initialise count of rows
    c=0 #Initialise count of columns
    for row in loaded_landscape:
        for col in row:
            if col == 'ice': #allows to be within 6 characters
                col = ' ice ' #spaces use for organisation
            landscape[r][c] = col #Put into array
            c=c+1 #Increment column count
        c=0 #Reset column count
        r=r+1 #Increment column count

#*******************************************************************************
#Outputs current statistics for the player
def output_stats():
    print('YOUR CURRENT STATISTICS\n') #to be displayed
    print('_________________________________________________________') #used for seperation and organization
    print('Your Power: ',power) #shows the value of the players power
    print('PASSENGERS IN HOLD:',number_in_hold,'/',max_in_hold)#How many passengers are to left to picked up on
    print('PASSENGERS DROPPED IN BASECAMP:',passanger_in_basecamp)#Shows the amount of passengers droppped in the basecamp
#*******************************************************************************
#The main game loop
def game():
#All the global variables that will be used within this function*
#*however have also been used throught the rest of the programme
    global bm_x, bm_y
    global p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y
    global passanger_in_basecamp, number_in_hold, power
    global level
    print_landscape() #Show initial landscape setup
    output_stats() # Show initial statistics
    while ( passanger_in_basecamp < 4) and (power > 0): #Continue while we can
        direction = '    ' #empty to be filled with the direction the user inputted
        #Get the direction the user wants to go
        while direction not in ['n','s','e','w']:
            direction = input('You may move North [n], South [s],'+
                'East [e] or West [w]')
            #Verifies if the moves are valid according to the players location
            if direction == 'w' and bm_x == 0:#does not allow the player to go out of the board
                print('Where do you think your going?')
                direction = ' '#empty so that it can be filled with the players choice
            elif direction == 'e' and bm_x == 9: #does not allow the player to go out of the board
                print('Where do you think your going?')
                direction = ' '#empty so that it can be filled with the players choice
            elif direction == 's' and bm_y == 9:#does not allow the player to go out of the board
                print('Where do you think your going?')
                direction = ' ' #empty so that it can be filled with the players choice
            elif direction == 'n' and bm_y == 0:#does not allow the player to go out of the board
                print('Where do you think your going?')
                direction = ' '#empty so that it can be filled with the players choice
#******************************************************************************
        #These Update the bot-mods's position whenever moving
        if direction == 'n': #variable to move north
            bm_y = bm_y - 1 #substituation to be able to move north
        elif direction == 's': #vairable to move south
            bm_y = bm_y + 1 #addition to be able to move south
        elif direction == 'e': #variable to move east
            bm_x = bm_x + 1#addition to be able to move east
        elif direction == 'w': #variable to move west
            bm_x = bm_x - 1#substituation to be able to move west
#******************************************************************************
        #Indicates that bot-mod is over a person
        if (bm_x == p1_x) and (bm_y == p1_y):
            # over person 1
            if number_in_hold < max_in_hold:
                p1_x = -1
                p1_y = -1
                number_in_hold = number_in_hold + 1
            else:
                print('We cant take another passenger!')

        if (bm_x == p2_x) and (bm_y == p2_y):
            # over person 2
            if number_in_hold < max_in_hold:
                p2_x = -1
                p2_y = -1
                number_in_hold = number_in_hold + 1
            else:
                print('We cant take another passenger!')

        if (bm_x == p3_x) and (bm_y == p3_y):
            # over person 3
            if number_in_hold < max_in_hold:
                p3_x = -1
                p3_y = -1
                number_in_hold = number_in_hold + 1
            else:
                print('We cant take another passenger!')

        if (bm_x == p4_x) and (bm_y == p4_y):
            # over person 4
            if number_in_hold < max_in_hold:
                p4_x = -1
                p4_y = -1
                number_in_hold = number_in_hold + 1
            else:
                print('We cant take another passenger!')
#******************************************************************************
#This will show if the bot mod is over the basecamo also*
#*this will update the statistics of the user since passengers are being dropped off
        if (bm_x == basecamp_x) and (bm_y == basecamp_y):
            #We're at the basecamp
            passanger_in_basecamp= passanger_in_basecamp + number_in_hold
            number_in_hold = 0 #begining value of the number of people in the basecamp
            print('The passanger is saved!') #message for the user when a passenger is saved
#******************************************************************************
#This will be the deductions of the wheels and if the landscape is grass
        if traction == 'Wheels':
            if landscape[bm_y][bm_x] == 'grass':
                if bay == 'Large':
                    power = power - 3
                if bay == 'Medium':
                    power = power - 2
                if bay == 'Small':
                    power = power - 1
#This will be the deductions of the wheels and if the landscape is rocks
            elif landscape [bm_y][bm_x] == 'rocks':
                if bay == 'Large':
                    power = power - 4
                if bay == 'Medium':
                    power = power - 3
                if bay == 'Small':
                    power = power - 2
#This will be the deductions of the wheels and if the landscape is ice
            else:
                if landscape [bm_y] [bm_x] == ' ice ':
                    if bay == 'Large':
                        power = power - 5
                    if bay == 'Medium':
                        power = power - 4
                    if bay == 'Small':
                        power = power - 3
#******************************************************************************
#This will be the deductions of the tracks and if the landscape is grass
        if traction == 'Tracks':
            if landscape[bm_y][bm_x] == 'grass':
                if bay == 'Large':
                    power = power - 5
                if bay == 'Medium':
                    power = power - 4
                if bay == 'Small':
                    power = power - 3
#This will be the deductions of the tracks and if the landscape is rocks
            elif landscape [bm_y][bm_x] == 'rocks':
                if bay == 'Large':
                    power = power - 5
                if bay == 'Medium':
                    power = power - 4
                if bay == 'Small':
                    power = power - 3
#This will be the deductions of the tracks and if the landscape is ice
            else:
                if landscape [bm_y] [bm_x] == ' ice ':
                    if bay == 'Large':
                        power = power - 5
                    if bay == 'Medium':
                        power = power - 4
                    if bay == 'Small':
                        power = power - 3

#******************************************************************************
#This will be the deductions of the skis and if the landscape is grass
                if traction == 'Skis':
                    if landscape[bm_y][bm_x] == 'grass':
                        if bay == 'Large':
                            power = power - 5
                if bay == 'Medium':
                    power = power - 4
                if bay == 'Small':
                    power = power - 3
#This will be the deductions of the skis and if the landscape is rocks
                elif landscape [bm_y][bm_x] == 'rocks':
                    if bay == 'Large':
                        power = power -  5
                if bay == 'Medium':
                    power = power -  4
                if bay == 'Small':
                    power = power -  3
#This will be the deductions of the skis and if the landscape is ice
                else:
                    if landscape [bm_y] [bm_x] == ' ice ':
                        if bay == 'Large':
                         power = power - 5
                    if bay == 'Medium':
                        power = power - 4
                    if bay == 'Small':
                        power = power - 3

        print_landscape()#Show the new landscape and statistics for the user
        output_stats() #displays the statistics
    if (passanger_in_basecamp == 4): #if the variable in the basecamp is '4' the player wins
        print ('You''ve won, well done!')#winners message
        level = level + 1 #moves to the next level
        print ('Move on to the next level'), level #next level introduction message
        initialise_level_variables() #executes the new level
        load_landscape()#loads the gameboard
        power = 100 - ((level-1) * 10)#adds on more power
        game()
#Player loses due to having insufficent power
    else:
        print('You are out of power! You lose!') #losers message displayed
#*******************************************************************************
#Allows a new level to be introduced
initialise_level_variables()
#loads a new landscape
load_landscape()
while True:
#directs player to main menu
    start_menu()
