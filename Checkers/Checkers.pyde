gamepieces = [ [1,0,1,0,1,0,1,0],  # 1's represent blue checkers, 2's represent red checkers, variable stores checker locations
               [0,1,0,1,0,1,0,1], 
               [1,0,1,0,1,0,1,0], 
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,2,0,2,0,2,0,2],
               [2,0,2,0,2,0,2,0], 
               [0,2,0,2,0,2,0,2]]

board  =     [ [1,0,1,0,1,0,1,0], # 0's represent black tiles, 1's represents white tiles, variable stores color of the tile on the board
               [0,1,0,1,0,1,0,1], 
               [1,0,1,0,1,0,1,0], 
               [0,1,0,1,0,1,0,1],
               [1,0,1,0,1,0,1,0],
               [0,1,0,1,0,1,0,1],
               [1,0,1,0,1,0,1,0], 
               [0,1,0,1,0,1,0,1]]

upper_left_check = True #used in king detection to see if king can jump forward and to the left 
upper_right_check = True #used in king detection to see if king can jump forward and to the right
lower_left_check = True #used in king detection to see if king can jump backward and to the left
lower_right_check = True #used in king detection to see if king can jump backward and to the right

total_check = False #checks if there are jumpable pieces on board

clearedpieces = {} #stores the location of the pieces a normal checker can take
redspots = {} #stores the location of the spots a normal checker can jump to
oldcol = 0 # stores old location of checker so it can be removed after turn with jumping
oldrow = 0 # stores old location of checker so it can be removed after turn with jumping

safe1 = True #var used to make sure that when the king jumps it does not go back to the same open spot before
safe2 = True
safe3 = True
safe4 = True

new_row = 0 #used to record location of old gamepiece
new_col = 0 #used to record location of old gamepiece

w = 87.5 #lenght of each tile or distance between each checker
c = w/2 #centre of tile to place checkers

run = False #resets board (available postitions) if checker is moved

turn_count = 0 #checks whos turn it is

standard_col = -1 #used while looping through the array to calculate index of pieces
standard_row = -1 #used while looping through the array to calculate index of pieces

left_col = -1 #used as left detection for jumping 
right_col = -1 #used as right detection for jumping 

left_row = -1 #used as left detection for jumping 
right_row = -1 #used as right detection for jumping

screen = 0 #used to control which screen is shown to user

redscore = 0 # red player's score
blackscore = 0 # black players's score

rowredspots = [] #empty list to append row location of possible jumps for king
colredspots = [] #empty list to append col location of possible jumps for king

rowclearedpieces = [] #empty list to append row location of possible pieces a king can take
colclearedpieces = [] # empty list to append col location of possible pieces a king can take

def game_reset(): #resets game if player clicks home screen button or game is finished and user restarts
    global gamepieces, redscore, blackscore, turn_count, total_check
    gamepieces = [[1,0,1,0,1,0,1,0],  # returns all piece locations to normal on the board
                  [0,1,0,1,0,1,0,1], 
                  [1,0,1,0,1,0,1,0], 
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,2,0,2,0,2,0,2],
                  [2,0,2,0,2,0,2,0], 
                  [0,2,0,2,0,2,0,2]]
    redscore = 0 #resets scores
    blackscore = 0
    turn_count = 0 #makes red turn first
    total_check = False  #makes jumping boolean false


def reset(): #resets all the red spots on the board to normal checkered board
    global board
    board  =  [[1,0,1,0,1,0,1,0], # resets gameboard to black and white checkers
               [0,1,0,1,0,1,0,1], 
               [1,0,1,0,1,0,1,0], 
               [0,1,0,1,0,1,0,1],
               [1,0,1,0,1,0,1,0],
               [0,1,0,1,0,1,0,1],
               [1,0,1,0,1,0,1,0], 
               [0,1,0,1,0,1,0,1]]
    
def sound(): #plays noise for checker moving
    add_library("minim")
    minim=Minim(this)
    sound = minim.loadFile("CheckerMove.mp3")
    sound.play()   #plays once only instead of loop

def menu():  #menu screen for game
    imageMode(CORNER) #all images start being drawn from corner
    
    homescreen = loadImage("menubackground.png") #loads in blurred checker board
    image(homescreen, 0,0,700,700)
    
    wood = loadImage("woodgrain.png") #loads  in wood on side of board
    image(wood, 700,0,200,700)
    
    redchecker = loadImage("redhomechecker.png") #redchecker design on menu
    image(redchecker, 200,225, 205, 205)
    
    blackchecker = loadImage("blackhomechecker.png") #blackchecker design on menu
    image(blackchecker, 290,260, 205, 205)
    
    game = loadImage("play.png") #playing controller
    image(game, 760,180, 75,75)
    
    instructions = loadImage("instructions.png") #instruction design
    image(instructions, 775, 570, 50,50)
    
    homeFont = createFont("menufont.ttf",60) #Loads custom font and prints text onto screen
    textFont(homeFont)
    
    fill(255)
    textSize(105)
    text("CHECKERS",15,250) #title
        
    textSize(25)
    text("Created by Omer Adeel", 210, 460) #name
   
    stroke(184,145,100) #creates boarder design for wooden board on side
    strokeWeight(6)
    line(700,350, 900,350)
    line(700,0,700,700)
    if mouseX > 700 and mouseX < 900 and mouseY < 350 and mouseY > 0:   #makes text become white if hovering over button
        fill(255)
    else:
        fill(0)
    textSize(25)
    text("Press to Play", 713, 175)
    if mouseX > 700 and mouseX < 900 and mouseY >350 and mouseY < 700: # makes instruction text white if hovering over button
        fill(255)
    else:
        fill(0)
    text(" Press for\nInstructions", 725, 525)                       

def instructions(): #function to play instructions
    background(192)  #Prints all the instructions onto the screen 
    
    wood = loadImage("woodgrain.png") #loads wood design on side
    image(wood, 700,0,200,700)
    
    game = loadImage("play.png") #loads playing design on board
    image(game, 760,180, 75,75)
    
    menu = loadImage("home.png") #loads picture to go home
    image(menu, 775, 570, 50,50)
    
    question = loadImage("question mark.png") #loads question mark design
    image(question, 360,350, 350,350)
    
    instructions= createFont("instruction font.ttf",60) #Loads custom font and prints text onto screen    
    
    homeFont = createFont("menufont.ttf",60) #Loads custom font and prints text onto screen
    
    imageMode(CORNER)

    fill(0)   #ALl headings
    textFont(homeFont)
    textSize(28)
    text("How to Play",18,53)
    text("Movement Rules", 18, 180)
    text("Capturing an Opponent's Checker", 18, 385)
    text("Becoming a 'king'", 18, 475)
    text("How to Win", 18, 580)
    
    fill(255) #ALl instructions
    textFont(instructions)
    textSize(17)
    text(" Choose a player to go first. On your turn, move any one of your\n checkers by the movement rules described below. After you move\n one checker, your turn is over. The game continues with players\n alternating turns.",18,80)
    text("- Always move your checker diagonally forward, toward your oppenent's\nside of the gameboard", 18, 205)       
    text("- Move your checker one space diagonally, to an open adjecent square;\nor jump one or more checkers diagonally to an open square adjecent\nto the checker you jumped.", 18, 255)
    text("- If all squares adjacent to your checker are occupied, your checker is\nblocked and cannot move.", 18, 325)
    text("If you jump an oppenent's checker, you capture it. It gets removed\nfrom the gameboard. 12 checkers in total must be jumped.", 18, 415)
    text("As soon as one of your checkers reaches the first row on your\nopponent's side of the gameboard, it becomes King. Now this\nchecker can move forward or backward on the gameboard.", 18, 500)
    text("The first player to capture all opposing checkers from the gameboard wins\nthe game!", 18, 610)
    
    stroke(184,145,100)
    strokeWeight(6)
    line(700,350, 900,350) #creates border design on wooden board
    line(700,0,700,700)
    textFont(homeFont)
        
    if mouseX > 700 and mouseX < 900 and mouseY < 350 and mouseY > 0: #text turns white if hovering over button
        fill(255)
    else:
        fill(0)
    textSize(25)
    text("Press to Play", 713, 175)
    if mouseX > 700 and mouseX < 900 and mouseY >350 and mouseY < 700:
        fill(255)
    else:
        fill(0)
    text(" Press for\nMain Menu", 725, 525)
    
def win(): #winning screen when player reaches 12 captured checkers
    global redscore, blackscore
    homeFont = createFont("menufont.ttf",60) #Loads custom font and prints text onto screen
    redchecker = loadImage("redhomechecker.png") #loads checker design based on who wins
    blackchecker = loadImage("blackhomechecker.png")
    
    if redscore == 12: #if red wins
        background(0)
        imageMode(CORNER)
        image(redchecker, 50,-90, 800,800)   #checker design shows up 
        textFont(homeFont)
        textSize(50)
        text("Player 1 Wins!", 270,610)      #player 1 wins
    if blackscore == 12: #if black wins
        background(220,20,60)
        imageMode(CORNER)
        image(blackchecker, 50, -90, 800,800) #checker design shows up
        textSize(50)
        textFont(homeFont)
        text("Player 2 Wins!", 220, 615) #player 2 wins
    
    instructions= createFont("instruction font.ttf",60) #Loads custom font and prints text onto screen    
    textFont(instructions)
    textSize(30)
    text("Click to Play Again", 320,670)    #playing again
        

def gameboard(): #draws gameboard out (checkered tiles)  
    global turn_count, blackscore, redscore
    imageMode(CORNER)  
  
    wood = loadImage("woodgrain.png") #loads in wood on side design
    image(wood, 700,0,200,700)
    
    menu = loadImage("home.png") #loads in home button on wood board
    image(menu, 710, 647, 50,50)
    
    instruction = loadImage("instructions.png") #instruction button on wood board
    image(instruction, 845, 647, 45,45)
    
    instructions= createFont("instruction font.ttf",60) #Loads custom font and prints text onto screen
    
    homeFont = createFont("menufont.ttf",60) #Loads custom font and prints text onto screen    
    
    redchecker = loadImage("redhomechecker.png") #shows red checker design above score
    image(redchecker,790,60,120,120)  
    
    blackchecker = loadImage("blackhomechecker.png") #shows black checker design above score
    image(blackchecker,690,60,120,120)     
    
    if turn_count%2 == 0:
        fill(255,0,0)
        textSize(30)
        text("Red Turn", 720, 70) #shows text based on turn for red
    if turn_count%2 == 1:
        fill(0)
        textSize(30)
        text("Black Turn", 715, 70) #shows text based on turn for black

    textSize(35)
    fill(255)
    textFont(instructions) #displays score for both players
    if blackscore < 10:
        text(blackscore, 732, 210) #score may show up differently if double digits so it is moved slightly to show it formatted properly
    if blackscore >= 10:
        text(blackscore, 715, 210) 
    if redscore < 10:
        text(redscore, 832, 210)
    if redscore >= 10: 
        text(redscore, 815, 210)
    
    textFont(homeFont)
            
    x = 0 #sets starting point of x-coordinate
    y = 0 #sets starting point of y-coordinate
    for row in board:
        for col in row: #loops through board array to see where black and white tiles
            if col == 0: # draws a black tile 
                stroke(0)
                strokeWeight(3)
                fill(0)
                square(x,y,w)
            if col == 1: #draws a white tile 
                stroke(0)
                strokeWeight(3)
                fill(255)
                square(x,y,w)
            if col == 2: #draws a green tile for open options
                stroke(0)
                strokeWeight(3)
                fill(0,255,127)
                square(x,y,w)
            if col == 3: #draws a red tile for jumping
                stroke(0)
                strokeWeight(3)
                fill(203,47,77)
                square(x,y,w)
            x = x + w #moves to the left to draw next tile
        y = y + w #after row is done it moves down one row
        x = 0 #resets x coord to 0
        
    stroke(184,145,100)
    strokeWeight(4) #draws boarder design on board
    line(700,0,700,700)
    
    redclip = loadImage("redclipart.png") 
    
    for n in range(0,blackscore,1):
        image(redclip, 715, (500-(n*25)), 75,50) #draws stacked checkers based on how many pieces black has taken
        
    blackclip = loadImage("blackclipart.png")
    
    for n in range(0,redscore,1):
        image(blackclip, 810, (500-(n*25)), 75,50) #draws stacked checkers based on how many pieces red has taken 
    
    

def gamepiece(): #draws out checkers
    x = c #starting point of first checker
    y = c #starting point of first checker 
    for row in gamepieces: #loops through gamepieces array
        for col in row: 
            if col == 1: #draws a black checker
                imageMode(CENTER)
                blackchecker = loadImage("blackchecker.png")
                image(blackchecker,x+4,y,82,82)        
            if col == 2: #draws a red checker 
                imageMode(CENTER)
                redchecker = loadImage("redchecker.png")
                image(redchecker,x+1.5,y,82,82)        
            if col == 3: #draws a black king checker
                imageMode(CENTER)
                blackking = loadImage("blackking.png")
                image(blackking,x+4,y,82,82)
            if col == 4: #draws a red king checker
                imageMode(CENTER)
                redking = loadImage("redking.png")
                image(redking,x,y+1,82,82)
            if col == 5: #draws a black checker with yellow highlight
                imageMode(CENTER)
                stroke(255,255,51)
                strokeWeight(9)
                ellipse(x,y,73,73) 
                strokeWeight(1)
                stroke(0)
                blackchecker = loadImage("blackchecker.png")
                image(blackchecker,x+4,y+1,82,82) 
            if col == 6: #draws a red checker with yellow highlight
                imageMode(CENTER)
                stroke(255,255,51)
                strokeWeight(9)
                ellipse(x-1,y+1,73,73) 
                strokeWeight(1)
                stroke(0)
                redchecker = loadImage("redchecker.png")
                image(redchecker,x+1,y+2,82,82) 
            if col == 7: #draws a black king checker with yellow highlight
                imageMode(CENTER)
                stroke(255,255,51)
                strokeWeight(9)
                ellipse(x-1,y+1,73,73) 
                strokeWeight(1)
                stroke(0)
                blackking = loadImage("blackking.png")
                image(blackking,x+2.25,y+2,82,82)
            if col == 8: #draws a red king checker with yellow highlight
                imageMode(CENTER)
                stroke(255,255,51)
                strokeWeight(9)
                ellipse(x,y+1,73,73) 
                strokeWeight(1)
                stroke(0)
                redking = loadImage("redking.png")
                image(redking,x+1,y+2,82,82)
            x = x + w #moves next checker to the left
        y = y + w # moves down row
        x = c #resets x coord to starting point


def black_movement(): #normal diagonal movement of checker piece
    global row, col, new_col, new_row, run
    reset();
    if gamepieces[row][col] == 1 and col != 0 and col!= 7 and row!= 7: #checks if you clicked on a blue piece and not in column 7 or 0 and it is not row 7
        new_col = col #records location of previous piece
        new_row = row  #records location of previous piece
        if gamepieces[row+1][col+1] == 0:
            board[row+1][col+1] = 2  
        if gamepieces[row+1][col-1] == 0: 
            board[row+1][col-1] = 2 
            
    if gamepieces[row][col] == 1 and col == 0 and row!=7 : #if bluepiece is on first column and it is not on row 7
        new_col = col #records location of previous piece
        new_row = row  #records location of previous piece
        if gamepieces[row+1][col+1] == 0: #checks if spot forward & right is open
            board[row+1][col+1] = 2  
    
    if gamepieces[row][col] == 1 and col == 7 and row != 7: #if bluepiece is on last column and it is not on row 7
        new_col = col #records location of previous piece
        new_row = row  #records location of previous piece
        if gamepieces[row+1][col-1] == 0: #checks if spot forward & left is open
            board[row+1][col-1] = 2 
            
    if gamepieces[row][col] == 3 and col != 0 and col != 7 and row != 0: #checks if you clicked on a black piece and it's not in the first or last column and makes sure it is not in the first row
        new_col = col #records location of previous piece
        new_row = row  #records location of previous piece
        if gamepieces[row-1][col+1] == 0: #checks if spot forward & right is open
            board[row-1][col+1] = 2
        if gamepieces[row-1][col-1] == 0: #checks if spot forward & left is open
            board[row-1][col-1] = 2 
    
    if gamepieces[row][col] == 3 and col == 0 and row != 0: #if redpiece is on first column
        new_col = col #records location of previous piece
        new_row = row  #records location of previous piece
        if gamepieces[row-1][col+1] == 0: #checks if spot forward & right is open
            board[row-1][col+1] = 2  
            
    if gamepieces[row][col] == 3 and col == 7 and row!= 0: #if redpiece is on last column and makes sure it is not on the first row because it cannot go forward
         new_col = col #records location of previous piece
         new_row = row  #records location of previous piece
         if gamepieces[row-1][col-1] == 0: #checks if spot forward & left is open
            board[row-1][col-1] = 2 

    if gamepieces[row][col] == 3 and col != 0 and col!= 7 and row!= 7: #checks if you clicked on a blue piece and not in column 7 or 0 and it is not row 7
        new_col = col #records location of previous piece
        new_row = row  #records location of previous piece
        if gamepieces[row+1][col+1] == 0:
            board[row+1][col+1] = 2  
        if gamepieces[row+1][col-1] == 0: 
            board[row+1][col-1] = 2 
            
    if gamepieces[row][col] == 3 and col == 0 and row!=7 : #if bluepiece is on first column and it is not on row 7
        new_col = col #records location of previous piece
        new_row = row  #records location of previous piece
        if gamepieces[row+1][col+1] == 0: #checks if spot forward & right is open
            board[row+1][col+1] = 2  
    
    if gamepieces[row][col] == 3 and col == 7 and row != 7: #if bluepiece is on last column and it is not on row 7
        new_col = col #records location of previous piece
        new_row = row  #records location of previous piece
        if gamepieces[row+1][col-1] == 0: #checks if spot forward & left is open
            board[row+1][col-1] = 2 
            
    if run: #since function is played after place function. If place function has occured reset the board
        reset();
        run = False #makes reset function disabled so that it won't clear board again
        
def black_placement(): #moves black piece
    global row, col, run, new_row, new_col, turn_count
    if board[row][col] == 2 and gamepieces[new_row][new_col] == 1: #where green tile marker is 
        gamepieces[row][col] = 1 #place turns into counter
        gamepieces[new_row][new_col] = 0
        reset();
        turn_count+= 1 #switches turn 
        run = True
        sound();

    if board[row][col] == 2 and gamepieces[new_row][new_col] == 3: #where green tile marker is 
        gamepieces[row][col] = 3 #place turns into counter
        gamepieces[new_row][new_col] = 0
        reset();
        turn_count+= 1 #switches turn 
        run = True
        sound();
        
def new_black(): #used to see which black checkers can go and makes them highlighted in yellow 
    global total_check
    standard_row = -1
    standard_col = -1
    check = False
         
    for row in gamepieces: #loops through lists in array
       standard_row +=1  #increments to record index
       for col in row: #loops through lists for elements
          standard_col += 1 #increments to record index
          if col == 1: #if element is a blue piece
             if standard_col != 6 and standard_col != 7 and standard_row != 6 and standard_row != 7:  #right detection: if not on last two rows or last two columns so it does not go off page
                 if (gamepieces[standard_row+1][standard_col+1] == 2 or gamepieces[standard_row+1][standard_col+1] == 4) and gamepieces[standard_row+2][standard_col+2] == 0: #checks if piece forward and diagonal right is red and space is open in front 
                    gamepieces[standard_row][standard_col] = 5 #becomes highlighted piece
                    check = True #shows that a piece can go
                    
             if standard_col != 0 and standard_col != 1 and standard_row != 7 and standard_row != 6: #left detection: if not on last two rows or first two columns so it does not go off page
                  if (gamepieces[standard_row+1][standard_col-1] == 2 or gamepieces[standard_row+1][standard_col-1] == 4) and gamepieces[standard_row+2][standard_col-2] == 0: #checks if piece forward and diagonal left is red and if place in front is open
                    gamepieces[standard_row][standard_col] = 5
                    check = True
          if standard_row == 7 and standard_col == 7 and check: #once board has gone through all pieces and someone can go it makes the jumping actigcated
            total_check = True #activates jumping
       standard_col = -1
    standard_row = -1
    
def black_jumping(): #checks which black checkers can jump to and which pieces it can take
    global oldcol, oldrow, clearedpieces, redspots, col ,row, blackscore, turn_count, check , total_check
    combo_count = 0 #used to count how many times the open spot dictionary is looped through
    countv = 0 #another counter to make sure that it loops through the clearedpieces dictionary the same amount
    
    if gamepieces[row][col] != 5 and board[row][col] !=3 and gamepieces[row][col] != 7: #if the player clicks on no spots and b
        redspots = {}
        clearedpieces = {}
        reset();
    
    if gamepieces[row][col] == 5: #if player clicks on black piece
        reset(); #resets all the redspots from previously clicked spots
        redspots = {} #makes dict empty for storing empty spaces
        clearedpieces = {} #makes dict empty for storing empty spaces
        oldcol = col #stores old location of checker to remove later
        oldrow = row #stores old location of checker to remove later
        left_check = True #left detection activated
        right_check = True #right detection activated
        left_row = row #all set to old location for left and right detection
        left_col = col
        right_row = row
        right_col = col 
        while left_check or right_check: #if the left and right detection are activated
            left_check = True 
            right_check = True
            if right_col != 6 and right_col != 7 and right_row != 6 and right_row != 7: #LEFT DETECTION: the piece must not be in the last two columns or last two rows or else it will go off screen or there will be an index error
                if (gamepieces[right_row+1][right_col+1] == 2 or gamepieces[right_row+1][right_col+1] == 4) and gamepieces[right_row+2][right_col+2] == 0: 
                    clearedpieces[right_row+1] = right_col +1 
                    redspots[right_row+2] = right_col + 2 
                    right_row = right_row + 2 #the right detection becomes the new array location
                    right_col = right_col + 2
                    board[right_row][right_col] = 3
                else:
                  right_col = left_col 
                  right_row = left_row
                  right_check = False
            else:
              right_col = left_col 
              right_row = left_row
              right_check = False
            if left_col != 0 and left_col != 1 and left_row != 7 and left_row != 6: #must not be in the first two columns and last two rows or else it will go off screen
               if (gamepieces[left_row+1][left_col-1] == 2 or gamepieces[left_row+1][left_col-1] == 4) and gamepieces[left_row+2][left_col-2] == 0:  
                 clearedpieces[left_row+1] = left_col - 1 
                 redspots[left_row+2] = left_col - 2 
                 left_row = left_row + 2 #detection moves to the new location
                 left_col = left_col - 2 
                 board[left_row][left_col] = 3
               else:
                 left_col = right_col #left check becomes unactivated if not meeting requirements
                 left_row = right_row
                 left_check = False
            else:
             left_col = right_col
             left_row = right_row
             left_check = False
             
    if board[row][col] == 3: #if clicked on an empty red space for jumping
        for elem in redspots: #loops through open spots 
            combo_count += 1 #increments until the spot selected by the player is met
            if row == elem and col == redspots[elem]: 
                break #breaks function to make sure the count does not increase
        if combo_count > 0:
            for elem in clearedpieces: #loops through the clearedpieces
                countv +=1 #increments until it becomes the same as the spots count so that the same number of pieces is removed
                if countv <= combo_count: 
                    gamepieces[elem][clearedpieces[elem]] = 0 #makes every piece 0
                    gamepieces[oldrow][oldcol] = 0 #makes the original piece removed
                    gamepieces[row][col] = 1 #turns clicked spot into piece
                    sound();
            blackscore += combo_count    
            turn_count+= 1 #turn changes
            combo_count = 0
            countv = 0            #resets all variables for next time it will be used in function
            clearedpieces = {}
            redspots = {}
            oldrow = 0
            oldcol = 0
            check = False
            total_check = False
            reset_black();
            reset_blackking();
                    
def reset_black(): # all the black checkers with the highlighted border is reset to its normal state
    reset();
    standard_col = -1
    standard_row = -1
    for row in gamepieces:
        standard_row += 1 
        for col in row:
            standard_col += 1
            if col == 5: #removes old highlighted piece for black checker
                gamepieces[standard_row][standard_col] = 1
        standard_col = -1
    standard_row = -1

def black_king(): #makes pieces kings once it reaches the end of the board
    s_row = -1
    s_col = -1 
    
    for row in gamepieces:
        s_row += 1 
        for col in row:
            s_col += 1
            if col == 1: #if it is a black checker
                if s_row == 7: #if in the last row of the board
                    gamepieces[s_row][s_col] = 3
        s_col = -1
    s_row = -1
    

def new_blackking(): #makes jumpable pieces a yellow highlight border
    global total_check
    check = False
    standard_row = -1
    standard_col = -1
         
    for row in gamepieces: #loops through lists in array
       standard_row +=1  #increments to record index
       for col in row: #loops through lists for elements
          standard_col += 1 #increments to record index
          if col == 3: #if element is a blue piece
              if standard_col != 6 and standard_col != 7 and standard_row != 6 and standard_row != 7: #if piece is not in the last two columns or last two rows or else it will go off screen
                  if (gamepieces[standard_row+1][standard_col+1] == 2 or gamepieces[standard_row+1][standard_col+1] == 4) and gamepieces[standard_row+2][standard_col+2] == 0:
                    gamepieces[standard_row][standard_col] = 7
                    check = True
                    
              if standard_col != 0 and standard_col != 1 and standard_row != 7 and standard_row != 6: #the piece should not be on the first or second column and the second last or last row or else it will go off screen
                  if (gamepieces[standard_row+1][standard_col-1] == 2 or gamepieces[standard_row+1][standard_col-1] == 4) and gamepieces[standard_row+2][standard_col-2] == 0:
                    gamepieces[standard_row][standard_col] = 7
                    check = True
            
              if standard_col != 6 and standard_col != 7 and standard_row != 0 and standard_row != 1: #if piece is not in the last two columns or last two rows or else it will go off screen
                  if (gamepieces[standard_row-1][standard_col+1] == 2 or gamepieces[standard_row-1][standard_col+1] == 4) and gamepieces[standard_row-2][standard_col+2] == 0:
                    gamepieces[standard_row][standard_col] = 7
                    check = True
              if standard_col != 0 and standard_col != 1 and standard_row != 0 and standard_row != 1: #the piece should not be on the first or second column and the second last or last row or else it will go off screen
                  if (gamepieces[standard_row-1][standard_col-1] == 2 or gamepieces[standard_row-1][standard_col-1] == 4)and gamepieces[standard_row-2][standard_col-2] == 0:
                      gamepieces[standard_row][standard_col] = 7
                      check = True
          if standard_row == 7 and standard_col == 7 and check:
            total_check = True
       standard_col = -1
    standard_row = -1
    
def blackking_jumping(): #allows black king to jump
    global safe1, safe2, safe3, safe4, lower_left_check, lower_right_check, upper_right_check, upper_left_check
    global rowredspots, colredspots, rowclearedpieces, colclearedpieces, oldcol, oldrow, clearedpieces, redspots, col ,row, blackscore, turn_count, check , total_check
    standard_row = -1
    standard_col = -1  
    combo_count = 0
    countv = 0
   
    if gamepieces[row][col] != 5 and gamepieces[row][col] != 7 and board[row][col] !=3: #if nothing is clicked
        rowredspots = [] 
        colredspots = [] #resets all data storing vars
        rowclearedpieces = []
        colclearedpieces = []
        reset();
    
    if gamepieces[row][col] == 7: #if highlighted piece is clicked for black king ckecker
        reset();
        rowredspots = [] #resets all data storing vars
        colredspots = []
        rowclearedpieces = []
        colclearedpieces = []
        oldcol = col
        oldrow = row
        upper_left_check = True
        upper_right_check = True
        lower_left_check = True
        lower_right_check = True
        left_row = row
        left_col = col
        right_row = row
        right_col = col 
        upper_right_col = col #right detection becomes index for columns
        upper_right_row = row #right detection becomes index for rows
        upper_left_col = col #left detection becomes index for columns
        upper_left_row = row #left detection becomes index for columns
        lower_right_col = col #right detection becomes index for columns
        lower_right_row = row #right detection becomes index for rows
        lower_left_col = col #left detection becomes index for columns
        lower_left_row = row #left detection becomes index for columns
        while lower_left_check or lower_right_check or upper_left_check or upper_right_check: #if either left or right detection functions the loop runs. If both no longer functions then the loop breaks
         upper_left_check = True #loop resets the two conditions because there could be new possibilities for the new jump
         upper_right_check = True
         lower_left_check = True
         lower_right_check = True
         if safe1:
          if lower_right_col != 6 and lower_right_col != 7 and lower_right_row != 6 and lower_right_row != 7:
            if (gamepieces[lower_right_row+1][lower_right_col+1] == 2 or gamepieces[lower_right_row+1][lower_right_col+1] == 4) and gamepieces[lower_right_row+2][lower_right_col+2] == 0: #the piece diagonal right must be a red piece and two two diagonals right must be open
                rowclearedpieces.append(lower_right_row+1)
                colclearedpieces.append(lower_right_col+1) #appended to the dictionary for the first jumping combo for piece that can be taken
                rowredspots.append(lower_right_row+2) # appended to the dictionary for the first jumping combo for the possible places the piece can jump for the combo
                colredspots.append(lower_right_col+2)
                lower_right_row = lower_right_row + 2 #the right detection becomes the new array location
                lower_right_col = lower_right_col + 2 
                board[lower_right_row][lower_right_col] = 3 #spot becomes red
            else:
              lower_right_check = False
          else:
               lower_right_check = False
         else:
            lower_right_check = False
            safe1 = True

         if safe2:
           if lower_left_row != 7 and lower_left_row != 6 and lower_left_col != 0 and lower_left_col !=1: #must not be in the first two columns and last two rows or else it will go off screen
            if (gamepieces[lower_left_row+1][lower_left_col-1] == 2 or gamepieces[lower_left_row+1][lower_left_col-1] == 4) and gamepieces[lower_left_row+2][lower_left_col-2] == 0: #if the piece diagonal left is red and the place diagonal left two places is open 
                 rowclearedpieces.append(lower_left_row+1)
                 colclearedpieces.append(lower_left_col-1) #appended to the dictionary for the first jumping combo for piece that can be taken
                 rowredspots.append(lower_left_row+2) # appended to the dictionary for the first jumping combo for the possible places the piece can jump for the combo
                 colredspots.append(lower_left_col-2)
                 lower_left_row = lower_left_row + 2 #detection moves to the new location
                 lower_left_col = lower_left_col - 2 
                 board[lower_left_row][lower_left_col] = 3
            else:
              lower_left_check = False
           else:
                lower_left_check = False
         else:
             lower_left_check = False
             safe2 = True
                
         if safe3:       
          if upper_right_col != 6 and upper_right_col != 7 and upper_right_row != 0 and upper_right_row != 1: #LEFT DETECTION: the piece must not be in the last two columns or last two rows or else it will go off screen or there will be an index error
            if (gamepieces[upper_right_row-1][upper_right_col+1] == 2 or gamepieces[upper_right_row-1][upper_right_col+1] == 4) and gamepieces[upper_right_row-2][upper_right_col+2] == 0: #the piece diagonal right must be a red piece and two two diagonals right must be ope
                rowclearedpieces.append(upper_right_row-1)
                colclearedpieces.append(upper_right_col+1) #appended to the dictionary for the first jumping combo for piece that can be taken
                rowredspots.append(upper_right_row-2) # appended to the dictionary for the first jumping combo for the possible places the piece can jump for the combo
                colredspots.append(upper_right_col+2)
                upper_right_row = upper_right_row - 2 #the right detection becomes the new array location
                upper_right_col = upper_right_col + 2 
                board[upper_right_row][upper_right_col] = 3
            else:
              upper_right_check = False #if the conditions above are not true right detection beceomes turned off
          else:
            upper_right_check = False
         else:
            upper_right_check = False
            safe3 = True
          
         if safe4:
           if upper_left_col != 0 and upper_left_col != 1 and upper_left_row != 0 and upper_left_row != 1: #must not be in the first two columns and last two rows or else it will go off screen
            if (gamepieces[upper_left_row-1][upper_left_col-1] == 2 or gamepieces[upper_left_row-1][upper_left_col-1] == 4) and gamepieces[upper_left_row-2][upper_left_col-2] == 0: #if the piece diagonal left is red and the place diagonal left two places is open 
                rowclearedpieces.append(upper_left_row-1)
                colclearedpieces.append(upper_left_col-1) #appended to the dictionary for the first jumping combo for piece that can be taken
                rowredspots.append(upper_left_row-2) # appended to the dictionary for the first jumping combo for the possible places the piece can jump for the combo
                colredspots.append(upper_left_col-2)
                upper_left_row = upper_left_row - 2 #detection moves to the new location
                upper_left_col = upper_left_col - 2 
                board[upper_left_row][upper_left_col] = 3 #spot becomes red
    
            else:
                upper_left_check = False
           else:
            upper_left_check = False
         else:
            upper_left_check = False
            safe4 = True
       
         if lower_right_check: #if backward and to the right is open 
            safe4 = False #makes position unjumpable afterwards
            lower_left_col = lower_right_col #makes all detection vars equal to one that ran
            lower_left_row = lower_right_row
            upper_left_col = lower_right_col
            upper_left_row = lower_right_row
            upper_right_col = lower_right_col
            upper_right_row = lower_right_row
            
         if lower_left_check: #if backward and to the left is open
            safe3 = False #makes position unjumpable afterwards
            lower_right_col = lower_left_col #makes all dectection vars equal to the one that ran
            lower_right_row = lower_left_row
            upper_right_col = lower_left_col
            upper_right_row = lower_left_row
            upper_left_col = lower_left_col
            upper_left_row = lower_left_row

         if upper_right_check: #if forward and to the right is open
            safe2 = False #makes postion unjumpable afterwards 
            lower_right_col = upper_right_col #makes all dectection vars equal to the one that ran
            lower_right_row = upper_right_row
            upper_left_col = upper_right_col
            upper_left_row = upper_right_row
            lower_left_col = upper_right_col
            lower_left_row = upper_right_row
         
         if upper_left_check: #if forward and to the left is open
             safe1 = False #makes postion unjumpable afterwards       
             lower_right_col = upper_left_col #makes all dectection vars equal to the one that ran
             lower_right_row = upper_left_row
             upper_right_col = upper_left_col
             upper_right_row = upper_left_row          
             lower_left_col = upper_left_col
             lower_left_row = upper_left_row    
   
    if board[row][col] == 3:
        for elem, elem1 in zip(rowredspots, colredspots): #loops through open spots 
            combo_count += 1 #increments until the spot selected by the player is met
            if row == elem and col == elem1: 
                break #breaks function to make sure the count does not increase
        if combo_count > 0:
            for elem2, elem3 in zip(rowclearedpieces, colclearedpieces): #loops through the clearedpieces
                countv +=1 #increments until it becomes the same as the spots count so that the same number of pieces is removed
                if countv <= combo_count:
                    gamepieces[elem2][elem3] = 0 #makes every piece 0
                    gamepieces[oldrow][oldcol] = 0 #makes the original piece removed
                    gamepieces[row][col] = 3 #turns clicked spot into piece
                    sound();
            blackscore += combo_count    
            turn_count+= 1 #turn changes
            combo_count = 0
            countv = 0
            rowredspots = [] #resets all data storing vars 
            colredspots = []
            rowclearedpieces = []
            colclearedpieces = []
            oldrow = 0
            oldcol = 0
            check = False
            total_check = False
            reset_black();
            reset_blackking();    
            
def reset_blackking(): #resets unused black kings which can jump to normal state
    reset();
    standard_col = -1
    standard_row = -1
    for row in gamepieces:
        standard_row += 1 
        for col in row:
            standard_col += 1
            if col == 7:
                gamepieces[standard_row][standard_col] = 3
        standard_col = -1
    standard_row = -1
   
def red_movement(): #normal diagonal movement of red checker piece
    global row, col, new_row, new_col, run 
    reset();
    if gamepieces[row][col] == 2 and col != 0 and col != 7 and row != 0: #checks if you clicked on a red piece and it's not in the first or last column and makes sure it is not in the first row
        new_col = col #records location of previous piece
        new_row = row  #records location of previous piece
        if gamepieces[row-1][col+1] == 0: #checks if spot forward & right is open
            board[row-1][col+1] = 2 
        if gamepieces[row-1][col-1] == 0: #checks if spot forward & left is open
            board[row-1][col-1] = 2 
     
    if gamepieces[row][col] == 2 and col == 0 and row != 0: #if redpiece is on first column
        new_col = col #records location of previous piece
        new_row = row  #records location of previous piece
        if gamepieces[row-1][col+1] == 0: #checks if spot forward & right is open
            board[row-1][col+1] = 2  
            
    if gamepieces[row][col] == 2 and col == 7 and row!= 0: #if redpiece is on last column and makes sure it is not on the first row because it cannot go forward
         new_col = col #records location of previous piece
         new_row = row  #records location of previous piece
         if gamepieces[row-1][col-1] == 0: #checks if spot forward & left is open
            board[row-1][col-1] = 2 

    if gamepieces[row][col] == 4 and col != 0 and col != 7 and row != 0: #checks if you clicked on a red piece and it's not in the first or last column and makes sure it is not in the first row
        new_col = col #records location of previous piece
        new_row = row  #records location of previous piece
        if gamepieces[row-1][col+1] == 0: #checks if spot forward & right is open
            board[row-1][col+1] = 2
        if gamepieces[row-1][col-1] == 0: #checks if spot forward & left is open
            board[row-1][col-1] = 2 
    
    if gamepieces[row][col] == 4 and col == 0 and row != 0: #if redpiece is on first column
        new_col = col #records location of previous piece
        new_row = row  #records location of previous piece
        if gamepieces[row-1][col+1] == 0: #checks if spot forward & right is open
            board[row-1][col+1] = 2  
            
    if gamepieces[row][col] == 4 and col == 7 and row!= 0: #if redpiece is on last column and makes sure it is not on the first row because it cannot go forward
         new_col = col #records location of previous piece
         new_row = row  #records location of previous piece
         if gamepieces[row-1][col-1] == 0: #checks if spot forward & left is open
            board[row-1][col-1] = 2 

    if gamepieces[row][col] == 4 and col != 0 and col!= 7 and row!= 7: #checks if you clicked on a blue piece and not in column 7 or 0 and it is not row 7
        new_col = col #records location of previous piece
        new_row = row  #records location of previous piece
        if gamepieces[row+1][col+1] == 0:
            board[row+1][col+1] = 2  
        if gamepieces[row+1][col-1] == 0: 
            board[row+1][col-1] = 2 
            
    if gamepieces[row][col] == 4 and col == 0 and row!=7 : #if bluepiece is on first column and it is not on row 7
        new_col = col #records location of previous piece
        new_row = row  #records location of previous piece
        if gamepieces[row+1][col+1] == 0: #checks if spot forward & right is open
            board[row+1][col+1] = 2  
    
    if gamepieces[row][col] == 4 and col == 7 and row != 7: #if bluepiece is on last column and it is not on row 7
        new_col = col #records location of previous piece
        new_row = row  #records location of previous piece
        if gamepieces[row+1][col-1] == 0: #checks if spot forward & left is open
            board[row+1][col-1] = 2 
            
    if run: #since function is played after place function. If place function has occured reset the board
        reset();
        run = False #makes reset function disabled so that it won't clear board again
    
def red_placement(): #moves places down red piece
    global row, col, new_row, new_col, turn_count, run
    if board[row][col] == 2 and gamepieces[new_row][new_col] == 2: #where green tile marker is 
        gamepieces[row][col] = 2 #place turns into counter
        gamepieces[new_row][new_col] = 0
        reset();
        turn_count+= 1 #switches turn 
        run = True
        sound();
    
    if board[row][col] == 2 and gamepieces[new_row][new_col] == 4: #where green tile marker is 
        gamepieces[row][col] = 4 #place turns into counter
        gamepieces[new_row][new_col] = 0
        reset();
        turn_count+= 1 #switches turn 
        run = True 
        sound(); 

def new_red():
    global total_check
    standard_row = -1
    standard_col = -1
    check = False
         
    for row in gamepieces: #loops through lists in array
       standard_row +=1  #increments to record index
       for col in row: #loops through lists for elements
          standard_col += 1 #increments to record index
          if col == 2: #if element is a blue piece
             if standard_col != 6 and standard_col != 7 and standard_row != 1 and standard_row != 0: 
                 if (gamepieces[standard_row-1][standard_col+1] == 1 or gamepieces[standard_row-1][standard_col+1] == 3) and gamepieces[standard_row-2][standard_col+2] == 0:
                    gamepieces[standard_row][standard_col] = 6
                    check = True
                    
             if standard_col != 0 and standard_col != 1 and standard_row != 1 and standard_row != 0: 
                  if (gamepieces[standard_row-1][standard_col-1] == 1 or gamepieces[standard_row-1][standard_col-1] == 3) and gamepieces[standard_row-2][standard_col-2] == 0:
                    gamepieces[standard_row][standard_col] = 6
                    check = True
                    
          if standard_row == 7 and standard_col == 7 and check == True:
             total_check = True
       standard_col = -1
    standard_row = -1
    
def red_jumping():
    global oldcol, oldrow, clearedpieces, redspots, col ,row, redscore, turn_count, check , total_check
    combo_count = 0
    countv = 0
    standard_col = -1
    standard_row = -1
    
    if gamepieces[row][col] != 6 and gamepieces[row][col] != 8 and board[row][col] !=3:
        redspots = {}
        clearedpieces = {} #resets all datastoring vars
        reset();
    
    if gamepieces[row][col] == 6:
        reset();
        redspots = {} #resets all datastoring vars
        clearedpieces = {}
        oldcol = col
        oldrow = row
        left_check = True
        right_check = True
        left_row = row
        left_col = col
        right_row = row
        right_col = col 
        while left_check or right_check: #if left and right detection functioning correclty
            left_check = True 
            right_check = True
            if right_col != 6 and right_col != 7 and right_row != 0 and right_row != 1: #LEFT DETECTION: the piece must not be in the last two columns or last two rows or else it will go off screen or there will be an index error
                if (gamepieces[right_row-1][right_col+1] == 1 or gamepieces[right_row-1][right_col+1] == 3) and gamepieces[right_row-2][right_col+2] == 0: 
                    clearedpieces[right_row-1] = right_col +1 
                    redspots[right_row-2] = right_col + 2 
                    right_row = right_row - 2 #the right detection becomes the new array location
                    right_col = right_col + 2
                    board[right_row][right_col] = 3 #spot becomes red
                else:
                  right_col = left_col 
                  right_row = left_row
                  right_check = False
            else:
              right_col = left_col 
              right_row = left_row
              right_check = False
            if left_col != 0 and left_col != 1 and left_row != 0 and left_row != 1: #must not be in the first two columns and last two rows or else it will go off screen
               if (gamepieces[left_row-1][left_col-1] == 1 or gamepieces[left_row-1][left_col-1] == 3) and gamepieces[left_row-2][left_col-2] == 0:  
                 clearedpieces[left_row-1] = left_col - 1 
                 redspots[left_row-2] = left_col - 2 
                 left_row = left_row - 2 #detection moves to the new location
                 left_col = left_col - 2 
                 board[left_row][left_col] = 3 #spot becomes red
               else:
                 left_col = right_col
                 left_row = right_row
                 left_check = False
            else:
             left_col = right_col
             left_row = right_row
             left_check = False
             
    if board[row][col] == 3:
        for elem in sorted(redspots, reverse = True): #loops through open spots 
            combo_count += 1 #increments until the spot selected by the player is met
            if row == elem and col == redspots[elem]: 
                break #breaks function to make sure the count does not increase
     
        if combo_count > 0:
            for elem in sorted(clearedpieces, reverse = True): #loops through the clearedpieces
                countv +=1 #increments until it becomes the same as the spots count so that the same number of pieces is removed
                if countv <= combo_count: 
                    gamepieces[elem][clearedpieces[elem]] = 0 #makes every piece 0
                    gamepieces[oldrow][oldcol] = 0 #makes the original piece removed
                    gamepieces[row][col] = 2 #turns clicked spot into piece
                    sound();
            redscore += combo_count    
            turn_count+= 1 #turn changes
            combo_count = 0 #resets all data storing vars
            countv = 0 
            clearedpieces = {}
            redspots = {}
            oldrow = 0
            oldcol = 0
            check = False
            total_check = False
            reset_red();
            reset_redking();
                    
def reset_red(): #once turn has gone it resets all highlighted pieces back to normal
    reset();
    standard_col = -1
    standard_row = -1
    for row in gamepieces:
        standard_row += 1 
        for col in row:
            standard_col += 1
            if col == 6:
                gamepieces[standard_row][standard_col] = 2
        standard_col = -1
    standard_row = -1    

def red_king(): #if redchecker reaches first row it becomes a king
    s_row = -1
    s_col = -1 
    
    for row in gamepieces:
        s_row += 1 
        for col in row:
            s_col += 1
            if col == 2:
                if s_row == 0:
                    gamepieces[s_row][s_col] = 4
        s_col = -1
    s_row = -1

def new_redking(): #makes redking highlighted for jumping
    global total_check
    check = False
    standard_row = -1
    standard_col = -1
         
    for row in gamepieces: #loops through lists in array
       standard_row +=1  #increments to record index
       for col in row: #loops through lists for elements
          standard_col += 1 #increments to record index
          if col == 4: #if element is a blue piece
              if standard_col != 6 and standard_col != 7 and standard_row != 6 and standard_row != 7: #if piece is not in the last two columns or last two rows or else it will go off screen
                  if (gamepieces[standard_row+1][standard_col+1] == 1 or gamepieces[standard_row+1][standard_col+1] == 3) and gamepieces[standard_row+2][standard_col+2] == 0:
                    gamepieces[standard_row][standard_col] = 8
                    check = True
                    
              if standard_col != 0 and standard_col != 1 and standard_row != 7 and standard_row != 6: #the piece should not be on the first or second column and the second last or last row or else it will go off screen
                  if (gamepieces[standard_row+1][standard_col-1] == 1 or gamepieces[standard_row+1][standard_col-1] == 3) and gamepieces[standard_row+2][standard_col-2] == 0:
                    gamepieces[standard_row][standard_col] = 8
                    check = True
            
              if standard_col != 6 and standard_col != 7 and standard_row != 0 and standard_row != 1: #if piece is not in the last two columns or last two rows or else it will go off screen
                  if (gamepieces[standard_row-1][standard_col+1] == 1 or gamepieces[standard_row-1][standard_col+1] == 3) and gamepieces[standard_row-2][standard_col+2] == 0:
                    gamepieces[standard_row][standard_col] = 8
                    check = True
              if standard_col != 0 and standard_col != 1 and standard_row != 0 and standard_row != 1: #the piece should not be on the first or second column and the second last or last row or else it will go off screen
                  if (gamepieces[standard_row-1][standard_col-1] == 1 or gamepieces[standard_row-1][standard_col-1] == 3)and gamepieces[standard_row-2][standard_col-2] == 0:
                      gamepieces[standard_row][standard_col] = 8
                      check = True
          if standard_row == 7 and standard_col == 7 and check:
            total_check = True
       standard_col = -1
    standard_row = -1
    
def redking_jumping():
    global safe1, safe2, safe3, safe4, lower_left_check, lower_right_check, upper_right_check, upper_left_check
    global rowredspots, colredspots, rowclearedpieces, colclearedpieces, oldcol, oldrow, clearedpieces, redspots, col ,row, redscore, turn_count, check , total_check
    combo_count = 0
    countv = 0
    standard_col = -1
    standard_row = -1
   
    if gamepieces[row][col] != 6 and gamepieces[row][col] != 8 and board[row][col] !=3:
        rowredspots = []
        colredspots = []
        rowclearedpieces = [] #resets all data storing vars
        colclearedpieces = []
        reset();
    
    if gamepieces[row][col] == 8:
        reset();
        rowredspots = [] #resets all data storing vars
        colredspots = []
        rowclearedpieces = []
        colclearedpieces = []
        oldcol = col
        oldrow = row
        upper_left_check = True
        upper_right_check = True
        lower_left_check = True
        lower_right_check = True
        left_row = row
        left_col = col
        right_row = row
        right_col = col 
        upper_right_col = col #right detection becomes index for columns
        upper_right_row = row #right detection becomes index for rows
        upper_left_col = col #left detection becomes index for columns
        upper_left_row = row #left detection becomes index for columns
        lower_right_col = col #right detection becomes index for columns
        lower_right_row = row #right detection becomes index for rows
        lower_left_col = col #left detection becomes index for columns
        lower_left_row = row #left detection becomes index for columns
        while lower_left_check or lower_right_check or upper_left_check or upper_right_check: #if either left or right detection functions the loop runs. If both no longer functions then the loop breaks
         upper_left_check = True #loop resets the two conditions because there could be new possibilities for the new jump
         upper_right_check = True
         lower_left_check = True
         lower_right_check = True
         if safe1:
          if lower_right_col != 6 and lower_right_col != 7 and lower_right_row != 6 and lower_right_row != 7: #must not be in last two rows or last two columns
            if (gamepieces[lower_right_row+1][lower_right_col+1] == 1 or gamepieces[lower_right_row+1][lower_right_col+1] == 3) and gamepieces[lower_right_row+2][lower_right_col+2] == 0: #the piece diagonal right must be a red piece and two two diagonals right must be open
                rowclearedpieces.append(lower_right_row+1)
                colclearedpieces.append(lower_right_col+1) #appended to the dictionary for the first jumping combo for piece that can be taken
                rowredspots.append(lower_right_row+2) # appended to the dictionary for the first jumping combo for the possible places the piece can jump for the combo
                colredspots.append(lower_right_col+2)
                lower_right_row = lower_right_row + 2 #the right detection becomes the new array location
                lower_right_col = lower_right_col + 2 
                board[lower_right_row][lower_right_col] = 3 #makes spot red
            else:
              lower_right_check = False
          else:
               lower_right_check = False
         else:
            lower_right_check = False
            safe1 = True

         if safe2:
           if lower_left_row != 7 and lower_left_row != 6 and lower_left_col != 0 and lower_left_col !=1: #must not be in the first two columns and last two rows or else it will go off screen
            if (gamepieces[lower_left_row+1][lower_left_col-1] == 1 or gamepieces[lower_left_row+1][lower_left_col-1] == 3) and gamepieces[lower_left_row+2][lower_left_col-2] == 0: #if the piece diagonal left is red and the place diagonal left two places is open 
                 rowclearedpieces.append(lower_left_row+1)
                 colclearedpieces.append(lower_left_col-1) #appended to the dictionary for the first jumping combo for piece that can be taken
                 rowredspots.append(lower_left_row+2) # appended to the dictionary for the first jumping combo for the possible places the piece can jump for the combo
                 colredspots.append(lower_left_col-2)
                 lower_left_row = lower_left_row + 2 #detection moves to the new location
                 lower_left_col = lower_left_col - 2 
                 board[lower_left_row][lower_left_col] = 3 #makes spot red
            else:
              lower_left_check = False
           else:
                lower_left_check = False
         else:
             lower_left_check = False
             safe2 = True
                
         if safe3:       
          if upper_right_col != 6 and upper_right_col != 7 and upper_right_row != 0 and upper_right_row != 1: #LEFT DETECTION: the piece must not be in the last two columns or last two rows or else it will go off screen or there will be an index error
            if (gamepieces[upper_right_row-1][upper_right_col+1] == 1 or gamepieces[upper_right_row-1][upper_right_col+1] == 3) and gamepieces[upper_right_row-2][upper_right_col+2] == 0: #the piece diagonal right must be a red piece and two two diagonals right must be ope
                rowclearedpieces.append(upper_right_row-1)
                colclearedpieces.append(upper_right_col+1) #appended to the dictionary for the first jumping combo for piece that can be taken
                rowredspots.append(upper_right_row-2) # appended to the dictionary for the first jumping combo for the possible places the piece can jump for the combo
                colredspots.append(upper_right_col+2)
                upper_right_row = upper_right_row - 2 #the right detection becomes the new array location
                upper_right_col = upper_right_col + 2 
                board[upper_right_row][upper_right_col] = 3 #makes spot red 
            else:
              upper_right_check = False #if the conditions above are not true right detection beceomes turned off
          else:
            upper_right_check = False
         else:
            upper_right_check = False
            safe3 = True
          
         if safe4:
           if upper_left_col != 0 and upper_left_col != 1 and upper_left_row != 0 and upper_left_row != 1: #must not be in the first two columns and last two rows or else it will go off screen
            if (gamepieces[upper_left_row-1][upper_left_col-1] == 1 or gamepieces[upper_left_row-1][upper_left_col-1] == 3) and gamepieces[upper_left_row-2][upper_left_col-2] == 0: #if the piece diagonal left is red and the place diagonal left two places is open 
                rowclearedpieces.append(upper_left_row-1)
                colclearedpieces.append(upper_left_col-1) #appended to the dictionary for the first jumping combo for piece that can be taken
                rowredspots.append(upper_left_row-2) # appended to the dictionary for the first jumping combo for the possible places the piece can jump for the combo
                colredspots.append(upper_left_col-2)
                upper_left_row = upper_left_row - 2 #detection moves to the new location
                upper_left_col = upper_left_col - 2 
                board[upper_left_row][upper_left_col] = 3 #makes spot red
    
            else:
                upper_left_check = False
           else:
            upper_left_check = False
         else:
            upper_left_check = False
            safe4 = True
       
         if lower_right_check: #if the redchecker can jump backward and left
            safe4 = False # makes it not go back in same direction
            lower_left_col = lower_right_col #all other detection is set to the succesful detection
            lower_left_row = lower_right_row
            upper_left_col = lower_right_col
            upper_left_row = lower_right_row
            upper_right_col = lower_right_col
            upper_right_row = lower_right_row
            
         if lower_left_check: #if the redchecker can jump backward and left
            safe3 = False # makes it not go back in same direction
            lower_right_col = lower_left_col#all other detection is set to the succesful detection
            lower_right_row = lower_left_row
            upper_right_col = lower_left_col
            upper_right_row = lower_left_row
            upper_left_col = lower_left_col
            upper_left_row = lower_left_row

         if upper_right_check: #if the redchecker can jump forward and right
            safe2 = False # makes it not go back in same direction
            lower_right_col = upper_right_col #all other detection is set to the succesful detection
            lower_right_row = upper_right_row
            upper_left_col = upper_right_col
            upper_left_row = upper_right_row
            lower_left_col = upper_right_col
            lower_left_row = upper_right_row
         
         if upper_left_check: #if the redchecker can jump forward and left
             safe1 = False  # makes it not go back in same direction
             lower_right_col = upper_left_col #all other detection is set to the succesful detection
             lower_right_row = upper_left_row
             upper_right_col = upper_left_col
             upper_right_row = upper_left_row           
             lower_left_col = upper_left_col
             lower_left_row = upper_left_row    
   
    if board[row][col] == 3:
        for elem, elem1 in zip(rowredspots, colredspots): #loops through open spots 
            combo_count += 1 #increments until the spot selected by the player is met
            if row == elem and col == elem1: 
                break #breaks function to make sure the count does not increase
        if combo_count > 0:
            for elem2, elem3 in zip(rowclearedpieces, colclearedpieces): #loops through the clearedpieces
                countv +=1 #increments until it becomes the same as the spots count so that the same number of pieces is removed
                if countv <= combo_count:
                    gamepieces[elem2][elem3] = 0 #makes every piece 0
                    gamepieces[oldrow][oldcol] = 0 #makes the original piece removed
                    gamepieces[row][col] = 4 #turns clicked spot into piece
                    sound();
            redscore += combo_count  #increases turn
            turn_count+= 1 #turn changes
            combo_count = 0 #makes all vars used in function return to normal state for use again
            countv = 0
            rowredspots = []
            colredspots = []
            rowclearedpieces = []
            colclearedpieces = []
            oldrow = 0
            oldcol = 0
            check = False
            total_check = False
            reset_red();
            reset_redking();    
            
def reset_redking(): # resets all red kings that were not used in the turn to unhighlited form
    reset(); #resets to normal checkered board
    standard_col = -1
    standard_row = -1
    for row in gamepieces:
        standard_row += 1 
        for col in row:
            standard_col += 1
            if col == 8:
                gamepieces[standard_row][standard_col] = 4
        standard_col = -1
    standard_row = -1
    

def setup():
    size(900,700)
   
    add_library("minim") #jeapordy background music
    minim=Minim(this)
    sound = minim.loadFile("game.mp3") 
    sound.loop()

def draw():
    global screen, redscore, blackscore, turn_count, total_check
    background(0)
    if redscore == 12 or blackscore == 12: #if someone wins the screen becomes black
        screen = 3
    
    if screen == 0: #draws menu screen 
        menu();
    if screen == 1: #draws board and gamepieces
        gameboard(); 
        gamepiece();
        red_king();
        black_king();
        if turn_count%2 == 1: #black turn
            new_black();
            new_blackking();
        if turn_count%2 == 0: #red turn 
            new_red();
            new_redking();
    if screen == 2: #runs instruction function if screen 2
        instructions();
    if screen == 3: #runs win function if screen 3
        win(); 
    
def mousePressed():  #
    global row, col, turn_count, screen, total_check
    check = True
    if screen == 0: #menu screen
        if mouseX > 700 and mouseX < 900 and mouseY < 350 and mouseY > 0: #button for playing 
            screen = 1
        if mouseX > 700 and mouseX < 900 and mouseY >350 and mouseY < 700:  #button for instructions
            screen = 2
            check = False #makes it so that it does not automatically go to game screen because it is in the same location
            
    if check:
        if screen == 2: #instruction screen
            if mouseX > 700 and mouseX < 900 and mouseY < 350 and mouseY > 0: #button for playing
                screen = 1
            if mouseX > 700 and mouseX < 900 and mouseY >350 and mouseY < 700:
                screen = 0
            
    if screen == 1: #if on gamescreen
        if mouseX > 820 and mouseX < 900 and mouseY > 640 and mouseY <700: # button for instructions 
            screen = 2
        if mouseX > 700 and mouseX < 770 and mouseY >640 and mouseY < 700: #button for returning home and restarting game
            reset();
            game_reset();
            screen = 0
            
        if mouseX < 700: #makes sure it does not interput with wooden board interface on right side of board
            col = int(mouseX//87.5) #barriers for each column
            row = int(mouseY//87.5) #barriers for each row
            if turn_count%2 == 1: # black turn
                if not total_check: #if jumping not activated
                    black_placement(); #normal movement
                    black_movement();
                if total_check:
                    black_jumping(); #black jumping
                    blackking_jumping();
        
            if turn_count%2 == 0: # red turn
                if not total_check: #if jumping not activated
                    red_placement(); #normal movement
                    red_movement();
                if total_check:
                    red_jumping(); #red jumping
                    redking_jumping();
                    
    if screen == 3: #if player clicks on win screen it resets game
        reset();
        game_reset();
        screen = 1
