'''Tic Tac Toe Game...'''
#Import Modules:
import pyttsx3 # --> Text to speech.

# Voice Initialization:
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

# voice[0].id --> Male Voice.
# voice[1].id --> Female Voice.

# Functions:

def speak(audio):
    '''This Function speaks the input value.'''
    engine.say(audio)
    engine.runAndWait()

def do_sum (first,second,third):
    ''' This Function sums the input values..'''
    return first+second+third

def print_board(state_x,state_tick):
    '''Board Function'''
    # Variable Declaration.
    zero = 'X' if state_x[0] else ('✓' if state_tick[0] else 0)
    one = 'X' if state_x[1] else ('✓' if state_tick[1] else 1)
    two = 'X' if state_x[2] else ('✓' if state_tick[2] else 2)
    three = 'X' if state_x[3] else ('✓' if state_tick[3] else 3)
    four = 'X' if state_x[4] else ('✓' if state_tick[4] else 4)
    five = 'X' if state_x[5] else ('✓' if state_tick[5] else 5)
    six = 'X' if state_x[6] else ('✓' if state_tick[6] else 6)
    seven = 'X' if state_x[7] else ('✓' if state_tick[7] else 7)
    eight = 'X' if state_x[8] else ('✓' if state_tick[8] else 8)

    # Print Values in the Board.
    print (f"{zero} |{one} |{two}")
    print("--|--|--")
    print (f"{three} |{four} |{five}")
    print("--|--|--")
    print (f"{six} |{seven} |{eight}")
    print("--|--|--")

def check_string():
    '''This functions check can the input value changes into int or not.'''
    while True:
        input_value = input("Please enter a value: ")
        if input_value.isnumeric():
            input_value = int(input_value)
            return input_value
        else:
            print('OOps! Invalid Input. Try between 0 - 9.')
            speak('OOps! Invalid Input. Try between 0 - 9.')

def check_winner(state_x,state_tick):
    '''This function checks who is the winner.'''

    win_condition = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in win_condition:

        if do_sum(state_x[win[0]], state_x[win[1]], state_x[win[2]]) == 3:
            print(f"Congratulations! {player1} You have won the match")
            speak(f"Congratulations! {player1} You have won the match")
            return 1

        if do_sum(state_tick[win[0]], state_tick[win[1]], state_tick[win[2]]) == 3:
            print(f"Congratulations! {player2} You have won the match")
            speak(f"Congratulations! {player2} You have won the match")
            return 0

    return -1


if __name__ == "__main__":

    cross = [0,0,0,0,0,0,0,0,0]
    tick = [0,0,0,0,0,0,0,0,0]

    # Welcome Message.
    print ('Welcome to Tic Tac Toe Game..')
    speak ('Welcome to Tic Tac Toe Game..')

    # Player Names.
    player1 = input ('Please Enter Player 1 name: ')
    player2 = input ('Please Enter Player 2 name: ')

    # Logic

    TURN = 1 # --> 1 for X 0 for ✓
    REPLAY = 'valid'

    while REPLAY == 'valid':

        while True:
            print_board(cross,tick)

            if TURN == 1:
                print(f"{player1}'s Chance")
                value = check_string()
                cross[value] = 1

            else:
                print(f"{player2}'s Chance")
                value = check_string()
                tick[value] = 1

            CHECK_WIN = check_winner(cross, tick)

            if CHECK_WIN != -1 :
                print("Match over")
                break

            TURN = 1 - TURN

        CHECK_REPLAY = 'valid'

        while CHECK_REPLAY == 'valid':
            speak('Do You wanna Play the Match Again')
            ask_replay = input ("Do You wanna Play the Match Again (y or n): ")

            if ask_replay == 'y':
                CHECK_REPLAY = "invalid"

            elif ask_replay == 'n':
                REPLAY = "invalid"
                CHECK_REPLAY = "invalid"
                print ("ThankYou! For playing this game..")
                speak ("ThankYou! For playing this game..")

            else:
                print("You Have Entered invalid value Please Try Again..")
                speak("You Have Entered invalid value Please Try Again..")
