print("Coded By - Abhisar Sen\n")
print("version - 1\n")
print("Date - 20 May 2021\n")
print("\t\t\t\t THE GAME OF LATRONES")
print("\n\n\t\t!!!Tie your seat belt and get ready to use your mind!!!\n\n")
print('''\t\t\t\t !!!INSTRUCTIONS!!!
To play this game follow the below instruction - 

1.  Read the instruction or question before filling up the entries, inside the game while playing it.
2.  Give valid inputs or fill out the entries carefully.
3.  In the game you would be first asked to enter the grid size of the game.
4.  For a better gameplay choose grid size 8X12 (rows = 8; column = 12).
5.  After that Player 1 would be asked to enter row and column no of the latrone he wants to go ahead with.
6.  Then he would be asked to enter whether he want to go in rows and columns, (choose one of the two option only, don’t go with any other word)
7.  Then he would be asked to enter a new row no or column where he wants to move.
8.  Then he would be asked row and column no for which he wants to check for defeating his opponent’s latrone.
9.  If that corresponding latrone is found defeated then that would be removed from the board.
10. The process from point 4 to 8 will be kept on going throughout the game for each of the players, one after the other, until the king latrone (identified as 3 for player 1 and 4 for player 2) is defeated.
11. After winning the game, the winner would be awarded 5 points and his opponent will get -1 point (if his points are greater than 0). (there is no negative point for any player.
12. The game has limited turns, each player has 26 chance to play and win. If none of them wins the game, then the match will be finished with no winner.\n\n\n''')

'''
importing numpy for making grid or matrix and to make function in it
'''
import numpy as np

while True:
    try:
        Row_size = int(input("Enter the no of rows that you want in your grid size "))
        Col_size = int(input("Enter the no of col that you want in your grid size "))
        break
    except:
        print("please inter the valid integers only")
if Row_size<Col_size:
    grid=np.array([np.zeros([Row_size,Col_size])])     
    grid_entry = grid.reshape([Row_size,Col_size])
else:
    Row_size = 8
    Col_size = 12
    grid=np.array([np.zeros([8,12])])     
    grid_entry = grid.reshape([8,12])

for i in range(Col_size):
    grid_entry[0][i] = 1        # arranging fist player latrones
    grid_entry[Row_size-1][i] = 2        # arranging second player latrones
grid_entry[1][int((Col_size/2) -1)] = 3     # king of player 1 is identified by 3
grid_entry[Row_size-2][int(Col_size/2)] = 4      # king of player 2 is identified by 4
print(grid_entry)

'''functioning for giving choice to player 1 for moving his latrone at desired position'''
def Player1_select_latrone(nth_row, nth_col):
    global turn
    while True:
        try:
            move_line = input("how do you want to move\n\t rows\n\t columns\n\n")
            break
        except:
            print("choose one of the above option only")
    while True:
        try:
            if move_line == 'columns':
                new_nth_row = int(input("P1 - enter the row no. of same column, you want to move in "))
                '''for moving normal latrones of player 1 in columns'''
                if grid_entry[new_nth_row][nth_col] == 0 and grid_entry[nth_row][nth_col] == 1:
                    grid_entry[nth_row][nth_col]= np.where(grid_entry[nth_row][nth_col]!=0, 0,grid_entry[nth_row][nth_col])
                    grid_entry[new_nth_row][nth_col] = 1
                    '''for moving king latrones of player 1 in columns'''
                elif grid_entry[new_nth_row][nth_col] == 0 and grid_entry[nth_row][nth_col] == 3:
                    grid_entry[nth_row][nth_col]= np.where(grid_entry[nth_row][nth_col]!=0, 0,grid_entry[nth_row][nth_col])
                    grid_entry[new_nth_row][nth_col] = 3
                else:
                    print("Please enter a valid move")
                    turn = turn-1
                print(grid_entry)
            elif move_line == 'rows':
                new_nth_column = int(input("P1 - enter the column no of same row, you want to move in "))
                '''for moving normal latrones of player 1 in rows'''
                if grid_entry[nth_row][new_nth_column] == 0 and grid_entry[nth_row][nth_col] == 1:
                    grid_entry[nth_row][nth_col] = np.where(grid_entry[nth_row][nth_col]!=0, 0, grid_entry[nth_row][nth_col])
                    grid_entry[nth_row][new_nth_column] = 1
                    '''for moving king latrones of player 1 in rows'''
                elif grid_entry[nth_row][new_nth_column] == 0 and grid_entry[nth_row][nth_col] == 3:
                    grid_entry[nth_row][nth_col] = np.where(grid_entry[nth_row][nth_col]!=0, 0, grid_entry[nth_row][nth_col])
                    grid_entry[nth_row][new_nth_column] = 3
                else:
                    print("Please enter a valid move")
                    turn = turn-1
                print(grid_entry)
            break
        except:
            print("Enter the valid move!!")
            turn = turn-1

'''functioning for giving choice to player 2 for moving his latrone at desired position'''
def Player2_select_latrone(nth_row, nth_col):
    global turn
    while True:
        try:
            move_line = input("how do you want to move\n\t rows\n\t columns\n\n")
            break
        except:
            print("choose one of the above option only")
    while True:
        try:
            if move_line == 'columns':
                new_nth_row = int(input("P2 - enter the row no. of same column, you want to move in "))
                '''for moving normal latrones of player 2 in columns'''
                if grid_entry[new_nth_row][nth_col] == 0 and grid_entry[nth_row][nth_col] == 2:
                    grid_entry[nth_row][nth_col]= np.where(grid_entry[nth_row][nth_col]!=0, 0,grid_entry[nth_row][nth_col])
                    grid_entry[new_nth_row][nth_col] = 2
                    '''for moving king latrones of player 2 in columns'''
                elif  grid_entry[new_nth_row][nth_col] == 0 and grid_entry[nth_row][nth_col] == 4:
                    grid_entry[nth_row][nth_col]= np.where(grid_entry[nth_row][nth_col]!=0, 0,grid_entry[nth_row][nth_col])
                    grid_entry[new_nth_row][nth_col] = 4
                else:
                    print("Please enter a valid move")
                    
                print(grid_entry)
            elif move_line == 'rows':
                new_nth_column = int(input("P2 - enter the column no of same row, you want to move in "))
                '''for moving normal latrones of player 2 in columns'''
                if grid_entry[nth_row][new_nth_column] == 0 and grid_entry[nth_row][nth_col] == 2:
                    grid_entry[nth_row][nth_col] = np.where(grid_entry[nth_row][nth_col]!=0, 0, grid_entry[nth_row][nth_col])
                    grid_entry[nth_row][new_nth_column] = 2
                    '''for moving king latrones of player 2 in columns'''
                elif grid_entry[nth_row][new_nth_column] == 0 and grid_entry[nth_row][nth_col] == 4:
                    grid_entry[nth_row][nth_col] = np.where(grid_entry[nth_row][nth_col]!=0, 0, grid_entry[nth_row][nth_col])
                    grid_entry[nth_row][new_nth_column] = 4
                else:
                    print("Please enter a valid move")
                    
                print(grid_entry)
            break
        except:
            print("Enter the valid move!!")
            turn = turn-1
'''
functioning for checking whether the input latrone position is valid for being declared defeated.
'''
def Winning_move():
    global turn     #to rectify unbound local errors
    global points_P1
    global points_P2
    try:
        print("if you want to check for defeating the latrone, fill up the entries else just give input as \n\trows = 0 \n\tcolumns = 0\n")
        nth_row = int(input("which latorone you want to check for defeat, enter its row no. "))
        nth_col = int(input("which latorone you want to check for defeat, enter its column no. "))
    except:
        print("Good move,\n\tKeep it up")
    try:
        condition1 = (grid_entry[nth_row-1][nth_col] == 1)
        condition2 = (grid_entry[nth_row+1][nth_col] == 1)
        condition3 = (grid_entry[nth_row][nth_col-1] == 1)
        condition4 = (grid_entry[nth_row][nth_col+1] == 1)
        condition5 = (grid_entry[nth_row, nth_col] == 2)
    except:
        print("input value is exceeding the grid size!!")
    if condition1 and condition2 and condition5:   #'''winning condition for normal latrone \ player 1'''
        grid_entry[nth_row][nth_col] = np.where(grid_entry[nth_row][nth_col]==2, 0, None)
        print("one of the latrone of player 2 is defeated\n", grid_entry)
    elif condition3 and condition4 and condition5:   #'''winning condition for normal latrone \ player 1'''
        grid_entry[nth_row][nth_col] = np.where(grid_entry[nth_row][nth_col]==2, 0, None)
        print("one of the latrone of player 2 is defeated\n", grid_entry)
    try:
        condition6 = (grid_entry[nth_row-1][nth_col] == 2)
        condition7 = (grid_entry[nth_row+1][nth_col] == 2)
        condition8 = (grid_entry[nth_row][nth_col-1] == 2)
        condition9 = (grid_entry[nth_row][nth_col+1] == 2)
        condition10 = (grid_entry[nth_row, nth_col] == 1)
    except:
        print("input value is exceeding the grid size!!")

    if (condition6 and condition7 and condition10) or (condition8 and condition9 and condition10):   #'''winning condition for normal latrone \ player 2'''
        grid_entry[nth_row][nth_col] = np.where(grid_entry[nth_row][nth_col]==1, 0, grid_entry[nth_row][nth_col])
        print("one of the latrone of player 1 is defeated\n", grid_entry)
        '''
        winning condition of players while defeating king
        '''
    condition11 = (grid_entry[nth_row, nth_col] == 4)
    condition12 = (grid_entry[nth_row, nth_col] == 3)
    if  condition1 and condition2 and condition3 and condition4 and condition11:   #'''winning condition for king latrone \ player 1'''
        grid_entry[nth_row][nth_col] = np.where(grid_entry[nth_row][nth_col]==4, 0, grid_entry[nth_row][nth_col])
        print("!!!player2 has lost the game \n\t player 1 is the Winner!!!\n", grid_entry)
        turn = turn-1
        points_P1 = points_P1+5
        if points_P2>0:
            points_P2 = points_P2 - 1
        print("points of player 1 -\t", points_P1,"\n points of player 2 -\t", points_P2)

    elif  condition6 and condition7 and condition8 and condition9 and condition12:   #'''winning condition for king latrone \ player 2'''
        grid_entry[nth_row][nth_col] = np.where(grid_entry[nth_row][nth_col]==3, 0, grid_entry[nth_row][nth_col])
        print("!!!player1 has lost the game \n\t player 2 is the Winner!!! \n", grid_entry)     
        points_P2=points_P2+5
        if points_P1>0:
            points_P1 = points_P1 - 1
        print("points of player 1 -\t", points_P1,"\n points of player 2 -\t", points_P2)

points_P1 = 0
points_P2 = 0
turn = 0
while True:
    if turn%2 == 0:
        row_no_P1 = int(input("P1 - Which Latrone you want to move, enter its row no."))
        col_no_P1 = int(input("P1 - Which Latrone you want to move, enter its col no."))
        Player1_select_latrone(row_no_P1, col_no_P1)
        Winning_move()
    elif turn%2 != 0:
        row_no_P2 = int(input("P2 - Which Latrone you want to move, enter its row no."))
        col_no_P2 = int(input("P2 - Which Latrone you want to move, enter its col no."))
        Player2_select_latrone(row_no_P2, col_no_P2)
        Winning_move()
    turn = turn+1
    if turn == 52:
        print("this match is over as you have reached the limit and\n therefore can't be played further")
        next_match = input("do you want to play next game, choose one of the below option\n\t yes\n\t no")
        while True:
            try:
                if next_match == 'yes':
                    turn = 0
                    break
                elif next_match == 'no':
                    break
            except:
                print("Choose between yes or no, only")