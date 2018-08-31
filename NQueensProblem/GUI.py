import pygame

def init_board_im(n, colors = [(255,255,255), (100,100,100)]):

    pygame.init()
    #colors = [(255,255,255), (100,100,100)]    # Set up colors [red, black]

    #n = len(the_board)         # This is an NxN chess board.
    surface_sz = 600           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    ball = pygame.transform.scale(pygame.image.load("120px-Chess_qlt45.svg.png"), (int(sq_sz*.75), int(sq_sz*.75)))

    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered :-)
    ball_offset = (sq_sz-ball.get_width()) // 2
    sparams = [sq_sz, ball_offset]
    return [surface,ball, sparams]

def draw_board(surface, ball, sparams, the_board, colors = [(255,255,255), (100,100,100)]):
    """ Draw a chess board with queens, as determined by the the_board. """
    n = len(the_board)         # This is an NxN chess board.
    [sq_sz, ball_offset] = sparams
    #while True:
    if True:

        # Look for an event from keyboard, mouse, etc.
        #ev = pygame.event.poll()
        #if ev.type == pygame.QUIT:
        #    break;

        # Draw a fresh background (a blank chess board)
        for row in range(n):           # Draw each row of the board.
            c_indx = row % 2           # Alternate starting color
            for col in range(n):       # Run through cols drawing squares
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # Now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # Now that squares are drawn, draw the queens.
        for (col, row) in enumerate(the_board):
          surface.blit(ball,
                   (col*sq_sz+ball_offset,row*sq_sz+ball_offset))

        #pygame.display.flip()
        pygame.display.update()


    #pygame.quit()

if __name__ == "__main__":
    [surface,ball, sparams]=init_board_im(4)
    draw_board(surface, ball, sparams,[0])    # 7 x 7 to test window size
