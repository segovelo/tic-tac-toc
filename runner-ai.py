import pygame
import sys
import time

import tictactoe as ttt

pygame.init()
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

n = 10
x_wins = 0
o_wins = 0
ties = 0
for i in range(n):
    board = ttt.initial_state()
    game_over = ttt.terminal(board)
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)
        ai_x = ttt.X
        ai_o = ttt.O

        # Draw game board
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                    height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != ttt.EMPTY:
                    move = moveFont.render(board[i][j], True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        game_over = ttt.terminal(board)
        player = ttt.player(board)

        # Show title
        if game_over:
            winner = ttt.winner(board)
            if winner is None:
                title = f"Game Over: Tie."
                ties += 1
            else:
                title = f"Game Over: {winner} wins."
                if winner == ai_x:
                    x_wins += 1
                else:
                    o_wins += 1

        elif ai_x == player:
            title = f"AI \"X\" thinking..."
        else:
            title = f"AI \"O\" thinking..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        # Check for AI move  
        if not game_over:     
            time.sleep(0.5)
            move = ttt.minimax(board)
            board = ttt.result(board, move)   

        pygame.display.flip()

print(f"X_wins: {x_wins}") 
print(f"O_wins: {o_wins}") 
print(f"Ties: {ties}")        
screen.fill(black)
title = f"Ties: {ties}"        
title = mediumFont.render(title, True, white)
titleRect = title.get_rect()
titleRect.center = ((width / 2), 30)
screen.blit(title, titleRect)

closeButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
close = mediumFont.render("Exit", True, black)
closeRect = close.get_rect()
closeRect.center = closeButton.center
pygame.draw.rect(screen, white, closeButton)
screen.blit(close, closeRect)
click, _, _ = pygame.mouse.get_pressed()
if click == 1:
    mouse = pygame.mouse.get_pos()
    if closeButton.collidepoint(mouse):
        time.sleep(0.2)
        sys.exit()

