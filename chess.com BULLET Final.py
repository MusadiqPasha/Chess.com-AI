from stockfish import Stockfish
import chess
import time
import pyautogui as pp
import chess.engine
import keyboard
import tensorflow_chessbot as ttt
from datetime import datetime
global fen_play
pp.FAILSAFE = True
global chessboard
global my_fen
global k
# brave 100% theater mode

# stockfish = Stoqckfish(path=r"C:\stockfish-windows-x86-64-modern\stockfish\stockfish-windows-x86-64-modern.exe")
stockfish = Stockfish(path=r"C:\stockfish-windows-x86-64-avx2\stockfish\stockfish-windows-x86-64-avx2.exe")
stockfish.reset_engine_parameters()
stockfish.set_skill_level(9)
stockfish.set_depth(7)
#stockfish.set_elo_rating(1300)

print("StockFish READYY!!!!")

def get_SS():
    pp.screenshot(r"D:\CODEE\Hackathon\#PASHA CHESS\tensorflow_chessbot-chessfenbot\input.png",
                  region=(300, 150, 810, 800))

    return ttt.mymain()  # find fen of the board


def flip():
    time.sleep(0.1)
    pp.click(1130, 234)


def get_all_the_pos():
    xx = 353
    yy = 153
    global chessboard
    chessboard = {}
    positions = []
    # defining keys
    for n in range(1, 9):
        for alpha in "abcdefgh":
            keyy = alpha + str(n)
            chessboard[keyy] = (0, 0)

    # defining x y pos
    for i in range(8):
        xx = 353
        for j in range(8):
            # row
            positions.append((xx, yy))
            # time.sleep(0.2)
            xx += 106
        yy += 106

    #time.sleep(0.1)

    # map all the loc to keys

    loc = 0
    for n in range(8, 0, -1):
        for alpha in "abcdefgh":
            keyy = alpha + str(n)
            chessboard[keyy] = positions[loc]
            loc += 1

    # down withe a8 , b8 ..
    # X:  361 Y:  898 RGB: (248, 248, 248)

    if pp.pixel(361, 901)[1] == 255:
        print("DOWN WHITE")
        global fen_play
        fen_play = 'w'
        loc = 0
        for n in range(8, 0, -1):
            for alpha in "abcdefgh":
                keyy = alpha + str(n)
                chessboard[keyy] = positions[loc]
                loc += 1

    # down_black  h1 , g1 ...
    # X:  364 Y:  901 RGB: ( 86,  83,  82)
    if pp.pixel(361, 901)[1] == 0:
        loc = 0
        print("DOWN BLACK so flipping !! ")
        # X: 1130 Y: 234
        flip()

        fen_play = "b"

    return chessboard


def move_on_chess(move):
    global k
    k += 1
    a = move[0:2]
    b = move[2:4]

    if (a not in chessboard.keys()) or (b not in chessboard.keys()):
        pp.alert(a + " to " + b + "\n You only move")
    else:
        pp.click(chessboard[a])
        pp.sleep(0.2)
        pp.click(chessboard[b])

        print(f"MOVED :  {a} ---> {b}")

    # if(k%3!=0):
    #     if (a not in chessboard.keys()) or (b not in chessboard.keys()):
    #         pp.alert(a + " to " + b + "\n You only move")
    #     else:
    #         pp.click(chessboard[a])
    #         pp.sleep(0.2)
    #         pp.click(chessboard[b])
    #
    #         print(f"MOVED :  {a} ---> {b}")
    # else:
    #     pp.alert(a + " to " + b + "\n is the BEST MOVE")


def find_best_move():
    global k
    k += 1
    #board = chess.Board(my_fen)
    #print(board)
    stockfish.set_fen_position(my_fen)

    if(k%5==0):
        # top 5 movess
        five_top_moves = stockfish.get_top_moves(3)
        bm = [x['Move'] for x in five_top_moves][2]

    else:
        bm = str(stockfish.get_best_move())

    print(bm)
    return bm

def whiteorblack():
    if pp.pixel(361, 901)[2] == 255:  # white
        return 255
    if pp.pixel(361, 901)[2] == 0:  # black
        return 255


# ------------------------MAIN----------------------------

pp.alert("Proceeddd??")
location_ka_board = get_all_the_pos()  # get all locations once

global fen_play
print(f"fen play == {fen_play}")

option = "OK"
while True:
    if option == "OK":
        global k
        k = 0
        if fen_play == 'b':
            colour = 36
            while not keyboard.is_pressed('q'):
                # X:  100 Y:  490 RGB: ( 43,  41,  38) - off ours black when witched
                # X:  101 Y:  486 RGB: ( 38,  36,  33) - ours onn
                # (173,  31,  36) - red colour last 1 min
                if pp.pixel(63, 463)[1] in range(colour-3 , colour+3) or pp.pixel(63,463)[0] in range(170,176):  # TIMER
                    time.sleep(0.2)

                    my_fen = str(get_SS())  # take ss and get FEN
                    print(f"fen play is {fen_play}")
                    my_fen = my_fen.replace('w', 'b')
                    print(f"GOT FEN! {my_fen}")
                    best_move = find_best_move()  # find best move
                    move_on_chess(best_move)  # move that shitt
                    print("---------------------------------------------------")

        if fen_play == 'w':

            colour = 255
            #time.sleep(1)
            my_fen = str(get_SS())  # take ss and get FEN
            my_fen = my_fen.replace('w', fen_play)
            print(f"GOT FEN!: {my_fen}")
            best_move = find_best_move()
            move_on_chess(best_move)  # move that shitt
            print("---------------------------------------------------")

            while not keyboard.is_pressed('q'):
                # X:   61 Y:  595 RGB: (255, 255, 255) - pure white
                if pp.pixel(61, 592)[1] in range(colour - 3, colour + 3) or pp.pixel(61,592)[0] in range(170,176):  # TIMER
                    time.sleep(0.2)
                    my_fen = str(get_SS())  # take ss and get FEN
                    print(f"fen play is {fen_play}")
                    my_fen = my_fen.replace('w', 'w')
                    print(f"GOT FEN! {my_fen}")
                    best_move = find_best_move()  # find best move
                    move_on_chess(best_move)  # move that shitt
                    print("---------------------------------------------------")

        print("done babyy")

    option = pp.confirm("Wanna Play Again ??")
    if option == "Cancel":
        exit()

    #time.sleep(3)
    location_ka_board = get_all_the_pos()  # get all locations once
    print("------------------------NEXT-MATCH--------------------------")
    print(location_ka_board)
    colour = whiteorblack()