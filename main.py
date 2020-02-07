import pygame
import os 
from tkinter import filedialog, Tk, messagebox
running = True
first = True
win = pygame.display.set_mode((600, 800))
if os.path.exists(os.getcwd()+"/levels"):
    pass
else:
    os.mkdir(os.getcwd()+"/levels")
def draw_Rect(pos1, pos2, color=(255, 255, 255)):
    fX, fY, sX, sY = pos1[0], pos1[1], pos2[0], pos2[1]
    height = max(fY, sY) - min(fY, sY)
    width = max(fX, sX) - min(fX, sX)
    # Min is for always giving the corner
    pygame.draw.rect(win, color, (min(fX, sX), min(fY, sY), width, height), False)
    return min(fX, sX), min(fY, sY), width, height
def loadFile(lfile):
    """Takes an 'open' object and displays all of the rectangles"""
    for line in lfile:
        ituple = []
        for item in line.split(" "):
            num = int(item)
            ituple.append(num)
        pygame.draw.rect(win, (255,255,255), ituple, False)
    pygame.display.update()
win.fill((0, 0, 0))
# Vars for while loop
rlist = []
loaded = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            Tk().withdraw()
            if messagebox.askyesno("Save?", "Do you wish to save?") and loaded == False:
                if len(rlist) != 0:
                    numFiles = len(os.listdir(os.getcwd()+"/levels"))
                    wFile = open(os.getcwd()+"/levels/level%s"%str(numFiles+1), 'a')
                    for line in rlist:
                        wFile.write(' '.join(str(value) for value in line) + '\n')
                    wFile.close()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Tk().withdraw()
                file = filedialog.askopenfile(initialdir=os.getcwd()+"/levels")
                loadFile(file)
                loaded = True
        if event.type == pygame.MOUSEBUTTONUP:
            if first:
                pos1 = pygame.mouse.get_pos()
                first = False
            else:
                pos2 = pygame.mouse.get_pos()
                first = True
                rlist.append(draw_Rect(pos1, pos2))
                pygame.display.update()
                loaded = False

