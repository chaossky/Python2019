import pygame, sys  
from pygame.locals import *  
  
pygame.init()                   # pygame 초기화  
DISPLAYSURF = pygame.display.set_mode((800, 600)) # 화면크기 설정  
pygame.display.set_caption('Hello World')         # 윈도우 타이틀 설정  
  
while True:  
    for event in pygame.event.get(): # 입력에 대한 이벤트가 있을 경우  
        if event.type == QUIT:       # 종료시 입력시  
            pygame.quit()            # pygame을 종료한 후  
            sys.exit()               # 프로그램 종료  
        pygame.display.update()      # 화면 갱신  

