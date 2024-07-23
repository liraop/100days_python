def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_down():
    turn_left()
    turn_left()
    
def jump():
    while wall_on_right() and not front_is_clear():
        turn_left()
    while front_is_clear() and wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
        
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
        
### uma vergonha