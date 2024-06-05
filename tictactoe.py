def printboard(board):
    print("*"*20)
    for row in board:
        print("   |".join(row))
        print("-"*15)
    print("*"*20)
    
def check(board,p):
    for row in range(3):
        if board[row][0]==p and board[row][1]==p and board[row][2]==p:
            return True
    for col in range(3):
        if board[0][col]==p and board[1][col]==p and board[2][col]==p:
            return True
    if board[0][0]==p and board[1][1]==p and board[2][2]==p:
        return True
    if board[0][2]==p and board[1][1]==p and board[2][0]==p:
        return True
    else:
        return False
def isFull(board):
    for row in board:
        for col in row:
            if col == " ":
                return False
    else:
        return True
board = [[" "]*3 for i in range(3)]
print("Welcome to tic-tac-toe game")
printboard(board)
print("player - x or o")
current = 'x'
while True:
    print("current player is:",current)
    print("Enter the dimension:")
    x,y = map(int,input().split())
    if -1<x<3 and -1<y<3:
        if board[x][y]==" ":
            board[x][y] = current
            printboard(board)
        else:
            print("Dimesion is already taken")
    if check(board,current):
        print("congrats",current,"wins")
        print("thank you for playing")
        break
    if isFull(board):
        print("Draw")
        print("thank you for playing")
        break
    else:
        print("enter valid dimensions")
    if current=='x':
        current='o'
    else:
        current='x'