class Constants :
	def __init__(self):
		
		self.ROW_COUNT = 6
		self.COLUMN_COUNT = 7
		
		self.SQUARESIZE = 100
		self.RADIUS =self.SQUARESIZE//2
		
		self.width = self.COLUMN_COUNT*self.SQUARESIZE
		self.height = (self.ROW_COUNT+1)*self.SQUARESIZE
		
		self.size = (self.width,self.height)

		self.RED = (255,0,0)
		self.BLUE = (0,0,255)
		self.YELLOW = (255,255,0)
		self.BLACK = (0,0,0)

		self.WINDOW_LENGTH = 4
		self.EMPTY = 0

		self.PLAYER = 0
		self.AI = 1

		self.PLAYER_PIECE = 1
		self.AI_PIECE = 2

			
