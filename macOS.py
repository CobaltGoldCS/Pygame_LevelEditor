import pygame
import os 
from tkinter import filedialog, Tk, messagebox

class levelEditor():
    def __init__(self):
        self.first = True
        self.running = True
        self.loaded = False
        self.win = pygame.display.set_mode((600, 800))
        if os.path.exists(os.getcwd()+"\levels"):
            pass
        else:
            os.mkdir(os.getcwd()+"\levels")
    def draw_Rect(self, pos1, pos2, color=(255, 255, 255)):
        fX, fY, sX, sY = pos1[0], pos1[1], pos2[0], pos2[1]
        height = max(fY, sY) - min(fY, sY)
        width = max(fX, sX) - min(fX, sX)
        # Min is for always giving the corner
        pygame.draw.rect(self.win, color, (min(fX, sX), min(fY, sY), width, height), False)
        return min(fX, sX), min(fY, sY), width, height
    def loadFile(self, lfile):
        """Takes an 'open' object and displays all of the rectangles"""
        for line in lfile:
            ituple = []
            for item in line.split(" "):
                num = int(item)
                ituple.append(num)
            pygame.draw.rect(self.win, (255,255,255), ituple, False)
        pygame.display.update()
    def mainloop(self):
        self.win.fill((0, 0, 0))
        # Vars for while loop
        rlist = []
        pygame.init()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sure = input("Do you wish to save?(y or n): ")
                        if sure == "y" and self.loaded == False:
                            if len(rlist) != 0:
                                numFiles = len(os.listdir("levels")
                                os.chdir("levels")
                                wFile = open("level%s"%str(numFiles+1), 'a')
                                for line in rlist:
                                    wFile.write(' '.join(str(value) for value in line) + '\n')
                                wFile.close()
                        pygame.quit()
                        running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        for level in os.listdir("levels"):
                            print(level)
                        file = open(os.getcwd()+"/levels/"+input("Filepath: "))
                        self.loadFile(file)
                        self.loaded = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.first:
                        pos1 = pygame.mouse.get_pos()
                        self.first = False
                    else:
                        pos2 = pygame.mouse.get_pos()
                        self.first = True
                        rlist.append(self.draw_Rect(pos1, pos2))
                        pygame.display.update()
                        self.loaded = False

if __name__ == "__main__":
    app = levelEditor()
    app.mainloop()
