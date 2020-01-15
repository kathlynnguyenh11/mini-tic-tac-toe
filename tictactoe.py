import turtle
import random
boxnum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
human = 0
computer = 0
poslist = [[-200, 200], [0, 200], [200, 200], [-200, 0], [0, 0], [200, 0], [-200, -200], [0, -200], [200, -200]]
winbox = [[1,2,3],[1,4,7],[1,5,9],[4,5,6],[7,8,9],[2,5,8],[3,6,9],[3,5,7]]
humanbox = []
computerbox = []
isPlayerTurn = False

def forwardBack (t,pos):
    for i in range(2):
        t.fd(pos)
        t.rt(180)

def drawBoard(board):
    board.penup()
    board.setposition(-300,300)
    board.pd()
    for i in range(2):
        board.fd(200)
        board.right(90)
        forwardBack(board, 600)
        board.lt(90)
    ""board.hideturtle()
    for i in range (4):
        board.fd(600)
        board.right(90)
   
    board.setposition(-300,300)
    for i in range (2):
        board.right(90)
        board.fd(200)
        board.lt(90)
        forwardBack (board, 600)
    board.setposition(-300,300)
    board.seth(0)

def winCheck (playerBox):
    playerBox = sorted(playerBox)
    for lis1 in winbox:
        winlist = []
        for i in lis1:
            if i in playerBox:
                winlist.append(i)
        if len(winlist) == 3:
            return True
    return False

def returnBoxCoordinates (boxnum):
    num = boxnum - 1
    return (poslist[num])

def returnBoxnum (boxNum):
    num = boxnum.index(boxNum)
    return num

def drawX (turt, lis):
    currentPos = turt.position()
    turt.pu()
    turt.goto(lis)
    turt.pd()
    turt.lt(45)
    for i in range(4):
        forwardBack(turt, 100)
        turt.lt(90)
    turt.pu()
    turt.setposition(currentPos)
    turt.seth(0)

def drawO (turt, lis):
    currentpos = turt.position()
    turt.pu ()
    turt.goto(lis)
    turt.fd(90)
    turt.seth(90)
    turt.pd()
    turt.circle(90)
    turt.pu()
    turt.lt(90)
    turt.fd(90)
    turt.rt(180)
    turt.setposition(currentpos)

def setPlayer ():
    inp = input('What would you like to be? (x or o):  ')
    global human
    global computer
    global isPlayerTurn
    if inp.lower() == 'x':
        human = 1  #1 is an x
        computer = 0  #0 is an o
        isPlayerTurn = True
    elif inp.lower() == 'o':
        human = 0
        computer = 1
        isPlayerTurn = False

def firstTurn(turt):
    setPlayer()
    global isPlayerTurn
    global humanbox
    if computer == 1:
        num1 = random.randint(1, 9)
        drawX(turt, returnBoxCoordinates(num1))
        boxnum.pop(num1-1)
        computerbox.append(num1)
        isPlayerTurn = True
    else:
        inp = int(input('What box? (1-9)  '))
        drawX(turt, returnBoxCoordinates(inp))
        boxnum.remove(inp)
        humanbox.append(inp)
        isPlayerTurn = False

def mainGame ():
    global computer
    global human
    global poslist
    global humanbox
    global computerbox
    global winbox
    global boxnum
    global isPlayerTurn
    board = turtle.Turtle()
    win = turtle.Screen()
    board.speed('fastest')
    drawBoard(board)
    firstTurn(board)
    attempt = 2
    wincheck = True
    while (attempt <= 9) and wincheck:
        if winCheck(humanbox):
            wincheck = False
            break
        elif winCheck(computerbox):
            wincheck = False
            break
        elif len(boxnum) == 0:
            wincheck = False
            break
        elif attempt == 10:
            break
        while isPlayerTurn:
            inp = int(input('What box? Choose from: '+str(boxnum)+'  '))
            if human == 1:
                drawX(board, returnBoxCoordinates(inp))
            else:
                drawO(board, returnBoxCoordinates(inp))
            boxnum.remove(inp)
            humanbox.append(inp)
            isPlayerTurn = False
            if winCheck(humanbox):
                wincheck = False
                break
            if winCheck(computerbox):
                wincheck = False
                break
            break
        if winCheck(humanbox):
            wincheck = False
            break
        elif winCheck(computerbox):
            wincheck = False
            break
        while (not isPlayerTurn) and (len(boxnum) > 0):
            num = 0
            while num not in boxnum:
                num = random.randint(1,9)
            if computer == 1:
                drawX(board, returnBoxCoordinates(num))
            else:
                drawO(board, returnBoxCoordinates(num))
            computerbox.append(boxnum[returnBoxnum(num)])
            boxnum.pop(returnBoxnum(num))
            isPlayerTurn = True
            if winCheck(humanbox):
                wincheck = False
                break
            if winCheck(computerbox):
                wincheck = False
                break
            break
        attempt += 1
    if winCheck(humanbox):
        print('You beat the computer you are a genius!')
    elif winCheck(computerbox):
        print('The computer beat you even though it chose randomly! [lol]')
    else:
        print('No one won')

mainGame()
