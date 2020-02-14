import pygame
import os 
from tkinter import filedialog, Tk, messagebox
# Need to find a way to fix needing the file to save
class levelEditor:
    def __init__(self):
        self.first = True
        self.running = True
        self.loaded = False
        WIDTH = int(input("What is the width: "))
        HEIGHT = int(input("What is the height: "))
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        if os.path.exists("levels"):
            pass
        else:
            os.mkdir("levels")
    def draw_Rect(self, pos1, pos2, color= (255,255,255)):
        
        fX, fY, sX, sY = pos1[0], pos1[1], pos2[0], pos2[1]
        height = max(fY, sY) - min(fY, sY)
        width = max(fX, sX) - min(fX, sX)
        # Min is for always giving the corner
        pygame.draw.rect(self.win, color, (min(fX, sX), min(fY, sY), width, height), False)
        return min(fX, sX), min(fY, sY), width, height, color[0], color[1], color[2]
    def mainloop(self):
        self.win.fill((0, 0, 0))
        # Vars for while loop
        pygame.init()
        Level = None
        while self.running:
            pygame.display.update()

            if Level != None:
                for rect in Level.rlist:
                    pygame.draw.rect(self.win,
                                     (rect[4], rect[5], rect[6]),
                                     (rect[0], rect[1], rect[2], rect[3]), False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sure = input("Do you wish to save?(y or n): ")
                        if sure == "y" and self.loaded == False:
                            if len(self.rlist) != 0:
                                numFiles = len(os.listdir("levels"))
                                os.chdir("levels")
                                wFile = open("level%s"%str(numFiles), 'a')
                                for line in Level.rlist:
                                    wFile.write('P '+' '.join(str(value) for value in line) + '\n')
                                wFile.close()
                        pygame.quit()
                        self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        for level in os.listdir("levels"):
                            print(level)
                        Level = decoder("levels/level%s"%input("Choose a level Number: "))
                        self.loaded = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.first:
                        pos1 = pygame.mouse.get_pos()
                        self.first = False
                    else:
                        pos2 = pygame.mouse.get_pos()
                        self.first = True
                        Level.rlist.append(self.draw_Rect(pos1, pos2))
                        pygame.display.update()
                        self.loaded = False
class decoder:
    def __init__(self, lFile):
        """Takes an 'open' object and displays all of the rectangles"""
        self.rlist = []
        lfile = open(lFile)
        for line in lfile:
            if line.startswith("P"):
                self.rectangle(line)
    def rectangle(self, line):
        ituple = [int(item) for item in line.split()[1:]]
        print(ituple)
        self.rlist.append(ituple)
if __name__ == "__main__":
    app = levelEditor()
    app.mainloop()
