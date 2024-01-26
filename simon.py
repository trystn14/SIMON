import board
import digitalio as dio
import time
import random

red = dio.DigitalInOut(board.D6)
red.direction = dio.Direction.OUTPUT
red.value = False

yellow = dio.DigitalInOut(board.D7)
yellow.direction = dio.Direction.OUTPUT
yellow.value = False

green = dio.DigitalInOut(board.D8)
green.direction = dio.Direction.OUTPUT
green.value = False

white = dio.DigitalInOut(board.D9)
white.direction = dio.Direction.OUTPUT
white.value = False

red_btn = dio.DigitalInOut(board.D2)
red_btn.direction = dio.Direction.INPUT

yel_btn = dio.DigitalInOut(board.D3)
yel_btn.direction = dio.Direction.INPUT

gre_btn = dio.DigitalInOut(board.D4)
gre_btn.direction = dio.Direction.INPUT

whi_btn = dio.DigitalInOut(board.D5)
whi_btn.direction = dio.Direction.INPUT

play = dio.DigitalInOut(board.D1)
play.direction = dio.Direction.INPUT

play_seq = []
user_seq = []
final_seq = []
points = 0
blink = 0.3
start_blink = 0.5
sequence_blink = 2

# this function plays a sequence with an added light each run.
def sequence():
    seq_len = 1
    for i in range(seq_len):
        light = random.randint(1, 4)
        play_seq.append(light)
        seq_len += 1
    for light in play_seq:
        if light == 1:
            red.value = True
            time.sleep(blink)
            red.value = False
            time.sleep(blink)
        elif light == 2:
            yellow.value = True
            time.sleep(blink)
            yellow.value = False
            time.sleep(blink)
        elif light == 3:
            green.value = True
            time.sleep(blink)
            green.value = False
            time.sleep(blink)
        else:
            white.value = True
            time.sleep(blink)
            white.value = False
            time.sleep(blink)

#this function allows the user to enter in their sequence.
def enter_seq():
    for light in play_seq:
        while game_on and not red_btn.value and not yel_btn.value and not gre_btn.value and not whi_btn.value: 
            pass
        if red_btn.value:
            red.value = True
            time.sleep(blink)
            red.value = False
            user_seq.append(1)
        if yel_btn.value:
            yellow.value = True
            time.sleep(blink)
            yellow.value = False
            user_seq.append(2)       
        if gre_btn.value:
            green.value = True
            time.sleep(blink)
            green.value = False
            user_seq.append(3)
        if whi_btn.value:
            white.value = True
            time.sleep(blink)
            white.value = False
            user_seq.append(4)
    final_seq.append(user_seq[-1])

"""this function decides if the user entered in the right sequence, if they did, they get points and the game continues.
    if they didnt, the game is over."""
def level_up():
    global alive, points
    if final_seq == play_seq:
        points = points + 1
    else:
        alive = False
        for i in range(sequence_blink):
            red.value = True
            yellow.value = True
            green.value = True
            white.value = True
            time.sleep(start_blink)
            red.value = False
            yellow.value = False
            green.value = False
            white.value = False
            time.sleep(start_blink)
            
game_on = True
alive = True
while True:
    #this turns the game on
    if play.value:
        game_on = True
        alive = True
    #this is the startup sequence
    if play.value and game_on:
        for i in range(sequence_blink):
            red.value = True
            yellow.value = True
            green.value = True
            white.value = True
            time.sleep(start_blink)
            red.value = False
            yellow.value = False
            green.value = False
            white.value = False
            time.sleep(start_blink)
        #this is where the game is executed
        while alive:
            sequence()
            enter_seq()
            level_up()
            time.sleep(start_blink)
        #after the user failed to enter in the sequence, they will be displayed their points.
        for i in range(points):
            green.value = True
            time.sleep(start_blink)
            green.value = False
            time.sleep(start_blink) 
