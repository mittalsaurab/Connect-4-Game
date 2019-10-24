import pygame 
from constants import Constants 
C = Constants()

class Screen :	

	def __init__(self):
		self.screen=pygame.display.set_mode(C.size)

	def intialize(self):
		pygame.init()
		pygame.display.set_caption("Connect-4")

	def draw_board(self, board):
		for r in range(C.ROW_COUNT):
			for c in range(C.COLUMN_COUNT):
				pygame.draw.rect(self.screen, C.BLUE, (c*C.SQUARESIZE,r*C.SQUARESIZE+C.SQUARESIZE, C.SQUARESIZE, C.SQUARESIZE))

		for r in range(C.ROW_COUNT):
			for c in range(C.COLUMN_COUNT):
				if board[r][c] == 0:
					pygame.draw.circle(self.screen, C.BLACK, (c*C.SQUARESIZE+C.RADIUS,C.height-(r*C.SQUARESIZE+C.RADIUS)),C.RADIUS-2)
				elif board[r][c] == 1:
					pygame.draw.circle(self.screen, C.RED, (c*C.SQUARESIZE+C.RADIUS,C.height-(r*C.SQUARESIZE+C.RADIUS)),C.RADIUS-2)
				elif board[r][c] == 2:
					pygame.draw.circle(self.screen, C.YELLOW, (c*C.SQUARESIZE+C.RADIUS,C.height-(r*C.SQUARESIZE+C.RADIUS)),C.RADIUS-2)
		pygame.display.update()		

	def winScreen(self,player):
	    # gameDisplay = pygame.display.set_mode((w, h))
	    pygame.display.set_caption("You Win! This level atleast.")
	    font = pygame.font.Font('freesansbold.ttf', 32)
	    text = font.render('Congratulations '+player+'! Go Party now!', True, (0, 255, 0), (0, 0, 255))
	    textRect = text.get_rect()
	    textRect.center = (C.width//2, C.height//2)
	    while True:
	        for event in pygame.event.get():
	            if event.type == pygame.QUIT:
	                pygame.quit()
	                quit()
	        self.screen.fill((0, 0, 255))
	        self.screen.blit(text, textRect)
	        pygame.display.update()
	def loseScreen(self):
	    pygame.display.set_caption("You Lose! This level atleast.")
	    font = pygame.font.Font('freesansbold.ttf', 32)
	    text = font.render('Better Luck For Next Time', True, (0, 255, 0), (0, 0, 255))
	    textRect = text.get_rect()
	    textRect.center = (width//2, height//2)
	    while True:
	        for event in pygame.event.get():
	            if event.type == pygame.QUIT:
	                pygame.quit()
	                quit()
	        self.screen.fill((0, 0, 255))
	        self.screen.blit(text, textRect)
	        pygame.display.update()


if __name__ =='__main__':
	pygame.init()
	s=Screen()
	s.winScreen('Saurabh')