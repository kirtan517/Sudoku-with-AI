import pygame
import math

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
FONT_SIZE=50

font = pygame.font.SysFont('Sans', FONT_SIZE)

def Background(size,width_1,width_2):
    global BOX_SIZE,INNER_LINE,BORDER_LINE,WINDOW_SIZE
    BOX_SIZE=size if size  else int(input("Enter the prefered Size"))
    INNER_LINE=width_1 if width_1 else  int(input("Enter the  inner thikness"))
    BORDER_LINE =width_2 if width_2 else  int(input("Enter the  border thikness"))
    WINDOW_SIZE=BOX_SIZE*9+INNER_LINE*6+BORDER_LINE*2



Background(100,5,9)



win=pygame.display.set_mode((WINDOW_SIZE,WINDOW_SIZE))

def Crodinated_Generator(BOX_SIZE,INNER_LINE,BORDER_LINE):
    cords_black_line=[]
    cords_red_line=[]
    center_cords=[]
    center=[]
    curr_x=0
    curr_y=0
    for i in range(1,9):
        curr_x+=BOX_SIZE
        center_cords.append(curr_x-BOX_SIZE//2)
        if not i%3 ==0:
            curr_x += INNER_LINE//2+1
            cords_black_line.append(curr_x)
            curr_x += INNER_LINE//2
        else:
            curr_x += BORDER_LINE//2+1
            cords_red_line.append(curr_x)
            curr_x += BORDER_LINE//2
    curr_x += BOX_SIZE
    center_cords.append(curr_x-BOX_SIZE//2)
    for i in center_cords:
        for j in center_cords:
            center.append((i,j))

    return cords_black_line,cords_red_line,center

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


class Digit:

    def __init__(self,xpos,ypos,digit):
        self.x=xpos
        self.y=ypos
        self.digit=digit

    def possible(self,number):
        pass

    def value(self):
        return self.digit


    def draw(self,win):
        self.img = font.render(str(self.digit), True, BLACK)
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        win.blit(self.img,(self.x-self.width//2,self.y-self.height//2))

    def erase(self,win):
        surface=pygame.Surface((self.width,self.height))
        surface.fill(WHITE)
        win.blit(surface, (self.x-self.width//2, self.y-self.height//2))

def position(xpos, ypos):
    for x,y in center_cords:
        if (x-BOX_SIZE//2<xpos and x+BOX_SIZE//2>xpos and y-BOX_SIZE//2<ypos and y+BOX_SIZE//2>ypos):
            return x,y

def checkRepeat(digit_typed):
    for (x,y) in digit_typed:
        for (m,n) in digit_typed:
            if m==x and not (y==n):
                if digit_typed[(x,y)].value()==digit_typed[(m,n)].value():
                    print("repeatx")
            if y == n and not (x == m):
                if digit_typed[(x, y)].value() == digit_typed[(m, n)].value():
                    print("repeaty")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")






def draw(win,digit_typed):
    for i in digit_typed:
        digit_typed[i].draw(win)
    pygame.display.update()

def main():
    run=True
    digit_typed={}
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    xpos, ypos = pygame.mouse.get_pos()
                    xpos, ypos = position(xpos, ypos)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pass
            if event.type == pygame.KEYDOWN:
                if ((xpos,ypos) in digit_typed):
                    digit_typed[(xpos,ypos)].erase(win)
                    digit_typed.pop((xpos,ypos))
                if not ((xpos, ypos) in digit_typed):
                    if pygame.K_1 == event.key:
                        digit_typed[(xpos, ypos)] = (Digit(xpos, ypos, 1))
                    if pygame.K_2 == event.key:
                        digit_typed[(xpos, ypos)] = (Digit(xpos, ypos, 2))
                    if pygame.K_3 == event.key:
                        digit_typed[(xpos, ypos)] = (Digit(xpos, ypos, 3))
                    if pygame.K_4 == event.key:
                        digit_typed[(xpos, ypos)] = (Digit(xpos, ypos, 4))
                    if pygame.K_5 == event.key:
                        digit_typed[(xpos, ypos)] = (Digit(xpos, ypos, 5))
                    if pygame.K_6 == event.key:
                        digit_typed[(xpos, ypos)] = (Digit(xpos, ypos, 6))
                    if pygame.K_7 == event.key:
                        digit_typed[(xpos, ypos)] = (Digit(xpos, ypos, 7))
                    if pygame.K_8 == event.key:
                        digit_typed[(xpos, ypos)] = (Digit(xpos, ypos, 8))
                    if pygame.K_9 == event.key:              
                        digit_typed[(xpos, ypos)] = (Digit(xpos, ypos, 9))
                    checkRepeat(digit_typed)
        draw(win, digit_typed)


if __name__ == "__main__":

    main()
