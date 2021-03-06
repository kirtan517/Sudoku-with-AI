import pygame

pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

BOX_SIZE=0
INNER_LINE=0
BORDER_LINE=0
WINDOW_SIZE=0

def Background(size,width_1,width_2):
    global BOX_SIZE,INNER_LINE,BORDER_LINE,WINDOW_SIZE
    BOX_SIZE=size if size  else int(input("Enter the prefered Size"))
    INNER_LINE=width_1 if width_1 else  int(input("Enter the  inner thikness"))
    BORDER_LINE =width_2 if width_2 else  int(input("Enter the  border thikness"))
    WINDOW_SIZE=BOX_SIZE*9+INNER_LINE*6+BORDER_LINE*2



Background(50,5,9)



win=pygame.display.set_mode((WINDOW_SIZE,WINDOW_SIZE))

def Crodinated_Generator(BOX_SIZE,INNER_LINE,BORDER_LINE):
    cords_black_line=[]
    cords_red_line=[]
    center_cords=[]

    curr_x=0
    curr_y=0
    for i in range(1,9):
        curr_x+=BOX_SIZE
        center_cords.append(curr_x//2)
        if not i%3 ==0:
            curr_x += INNER_LINE//2+1
            cords_black_line.append(curr_x)
            curr_x += INNER_LINE//2
        else:
            curr_x += BORDER_LINE//2+1
            cords_red_line.append(curr_x)
            curr_x += BORDER_LINE//2
    
    return cords_black_line,cords_red_line,center_cords

cords_black_line,cords_red_line,center_cords=Crodinated_Generator(BOX_SIZE, INNER_LINE, BORDER_LINE)

def draw_Background(win,Box_Size,Window_Size,Border_line,Inner_line):
    win.fill(WHITE)

    for i in cords_black_line:
        pygame.draw.line(win,BLACK,(0,i),(Window_Size,i),Inner_line)
        pygame.draw.line(win,BLACK,(i,0),(i,Window_Size),Inner_line)

    for i in cords_red_line:
        pygame.draw.line(win,RED,(0,i),(Window_Size,i),Border_line)
        pygame.draw.line(win,RED,(i,0),(i,Window_Size),Border_line)

    pygame.display.update()

draw_Background(win,BOX_SIZE,WINDOW_SIZE,BORDER_LINE,INNER_LINE)

def draw(win):
    pass


def main():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(win)


if __name__ == "__main__":
    main()
