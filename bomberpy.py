import pygame

pygame.init() #start pygame and starts you subprocess
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Bomberpy") #name of game in window bar
clock = pygame.time.Clock()

wall = pygame.image.load('./sprites/wall.png').convert_alpha() #walls

background = pygame.image.load('./sprites/background.png').convert_alpha() #ground

player = pygame.image.load('./sprites/placeholder.png').convert_alpha() #player
player_box = player.get_rect(topleft=(50,50))

#main loop
while True:
    #game clock
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #check if close button was clicked
            pygame.quit()
            
    
    screen.blit(background,(0,0)) #background
    screen.blit(player,player_box) #player
    
    #Map Generation
    n=0
    w=105 #horizontal
    h=135 #vertical
    control = 0
    wall_rect = []
    for j in range(4):
        for i in range(6):
            wall1=wall.get_rect(topleft=(w,h))
            wall_rect.append(wall1)
            screen.blit(wall,wall1)
            i=i+1
            w=w+145
        w=105
        wall1=wall.get_rect(topleft=(w,h))
        wall_rect.append(wall1)
        screen.blit(wall,wall1)
        h=h+145
        j=j+1

    move_x = 0
    move_y = 0
    player_speed = 4.5
    #controls
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_d]):
        player_box.x+=player_speed
    
    if (keys[pygame.K_a]):
        player_box.x-=player_speed

    if (keys[pygame.K_w]):
        player_box.y-=player_speed
    
    if (keys[pygame.K_s]):
        player_box.y+=player_speed

    

    #Collisions
    # Collisions
    for wall1 in wall_rect:
        if player_box.colliderect(wall1):
            overlap_x = player_box.x + player_box.width / 2 - wall1.x - wall1.width / 2
            overlap_y = player_box.y + player_box.height / 2 - wall1.y - wall1.height / 2
            
            if abs(overlap_x) > abs(overlap_y):
                if overlap_x > 0:
                    player_box.right+=5
                else:
                    player_box.left-=5
            else:
                if overlap_y > 0:
                    player_box.bottom+=5
                else:
                    player_box.top-=5


    if player_box.left < 50:
        player_box.left = 50
    
    if player_box.right > 950:  
        player_box.right = 950

    if player_box.top < 50:
        player_box.top = 50

    if player_box.bottom > 750:
        player_box.bottom = 750    
    print(player_box.colliderect(wall1))
    pygame.display.update()
    clock.tick(60) # 60 frames per second
