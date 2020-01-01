# CS-UY 1114
# Final project

import turtle
import time


userx = 0
enemies = [(300,180, "right"), (100,60, "left"), (100, -30, "right"),(100,-120,"right"), (10,150, "left"), (200, -90, "right")]
bullets = []
gameover = False

def draw_frame():
    turtle.up()#draws the player
    turtle.goto(userx,330)
    turtle.down()
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(20)
    turtle.right(120)
    for position in enemies:#draws the enemies
        turtle.up()
        turtle.goto(position[0],position[1])
        turtle.down()
        turtle.circle(10)
    for elem in range(len(bullets)):#draws the bullets
        turtle.up()
        turtle.goto(bullets[elem])
        turtle.down()
        turtle.pencolor("red")
        turtle.dot(10)
        turtle.pencolor("black") 
def key_left():
    global userx
    userx=userx-10#moves the player left if the left key is clicked
    turtle.goto(userx,330)
    if userx<-420:#limits the player from leaving the map
        userx=-420
def key_right():
    global userx
    userx=userx+10#moves the player right if the left key is clicked
    turtle.goto(userx,300)
    if userx>390:#limits the player from leaving the map
        userx=390
    
def key_space():
    cord=(userx+10,320)#adds a tuple or the coordinates to the bullets list
    bullets.append(cord)
def physics():
    global bullets#the motion of the bullet moving downwards
    global enemies
    length=len(bullets)
    for elem in range(length): 
        if bullets[elem][1]<400:#motion of bullet
            bullets_y=bullets[elem][1]-10
            bullets_x=bullets[elem][0]
            bullets[elem]=(bullets_x,bullets_y)
    for bullet in bullets:#checks if the bullet hits the enemy
        for enemy in enemies:
            if abs(bullet[0]-enemy[0])<13 and abs(bullet[1]-enemy[1])<10:
                bullet_index=bullets.index(bullet)
                enemy_index=enemies.index(enemy)
                bullets.pop(bullet_index)#removes the coordinate where the bullet and enemy collided
                enemies.pop(enemy_index)
       
def ai():
    global enemies
    global gameover
    if enemies == []:#checks if there are any enemies left
            gameover=True
            turtle.clear()
            turtle.goto(0,0)
            turtle.write("YOU SAVED THE UNIVERSE",font=("Arial",20,"normal"))
            time.sleep()
    for elem in range(len(enemies)):
        if enemies[elem][2] == "left":#moves enemies left
            new_x=enemies[elem][0]-5
            current_y=enemies[elem][1]
            enemies[elem]=(new_x,current_y,"left")
            if enemies[elem][0]<=-420:#moves enemies upwards after leaving map
                new_y=enemies[elem][1]+30
                enemies[elem]=(-420,new_y,"right")#changes it direction
        if enemies[elem][2] == "right":#moves enemies right
            new_x=enemies[elem][0]+5
            current_y=enemies[elem][1]
            enemies[elem]=(new_x,current_y,"right")
            if enemies[elem][0]>=420:#moves enemies upwards after leaving map
                    new_y=enemies[elem][1]+30
                    enemies[elem]=(420,new_y,"left")#changes it direction
        if (enemies[elem][0],enemies[elem][1])==(userx+30,300):#gameover when enemy touches player right side
            gameover=True
            turtle.clear()
            turtle.goto(0,0)
            turtle.write("GAME OVER",font=("Arial",28,"normal"))
            time.sleep()
        if (enemies[elem][0],enemies[elem][1])==(userx,300):#gameover when enemy touches player left side
            gameover=True
            turtle.clear()
            turtle.goto(0,0)
            turtle.write("GAME OVER",font=("Arial",28,"normal"))
            time.sleep()
def reset():
    global enemies
    global bullets
    global userx
    global gameover
    pass # your code here
    while gameover:
        enemies=[(300,180, "right"), (100,60, "left"), (100, -30, "right"),(100,-120,"right"), (10,150, "left"), (200, -90, "right")]
        bullets=[]
        userx=0
        gameover=False
def main():
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.listen()
    turtle.onkey(key_left, "Left")
    turtle.onkey(key_right, "Right")
    turtle.onkey(key_space, "space")
    while not gameover:
        physics()
        ai()
        turtle.clear()
        draw_frame()
        turtle.update()
        time.sleep(0.05)

main()
