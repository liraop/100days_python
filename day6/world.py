def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_down():
    turn_left()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif wall_on_right():
        turn_left()