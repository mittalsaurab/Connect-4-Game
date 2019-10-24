from constants import Constants

C = Constants()

class Computation :

	def check_win(self,board,piece):
		# check for horizontal winning positons

		ROW_COUNT = C.ROW_COUNT
		COLUMN_COUNT = C.COLUMN_COUNT

		for c in range(COLUMN_COUNT-3):
			for r in range(ROW_COUNT):
				if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] == piece:
					return True

		#check for vertical positions 

		for r in range(ROW_COUNT-3):
			for c in range(COLUMN_COUNT):
				if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] == piece:
					return True

		#check for postively sloped diagonals

		for r in range(ROW_COUNT-3):
			for c in range(3,COLUMN_COUNT):
				if board[r][c] == board[r+1][c-1] ==  board[r+2][c-2] == board[r+3][c-3] == piece:
					return True			

		#check for negative slope diagonals
		
		for r in range(ROW_COUNT-3):
			for c in range(COLUMN_COUNT-3):
				if board[r][c] == board[r+1][c+1] ==  board[r+2][c+2] == board[r+3][c+3] == piece:
					return True			

		return False		

	def evaluate_window(self,window, piece):
		score = 0
		if window.count(piece) == 4:
			score += 100
		elif window.count(piece) == 3 and window.count(C.EMPTY) == 1:
			score += 5
		if window.count(3-piece) == 3 and window.count(C.EMPTY) == 1:
			score -= 50			
		return score	

	def get_score(self,board,piece):
		ROW_COUNT = C.ROW_COUNT
		COLUMN_COUNT = C.COLUMN_COUNT
		WINDOW_LENGTH = C.WINDOW_LENGTH
		score = 0
		center_arr=[int(i) for i in board[:,COLUMN_COUNT//2]]
		center_count = center_arr.count(piece)
		score += center_count*6
		#Considering horizontal positions
		for r in range(ROW_COUNT):
			row_arr=[int(i) for i in list(board[r,])]	
			for c in range(COLUMN_COUNT-3):
				col_arr = row_arr[c:c+WINDOW_LENGTH]
				score += self.evaluate_window(col_arr,piece)
		#vertical							
		for c in range(COLUMN_COUNT):
			col_arr = [int(i) for i in list(board[:,c])]	
			for r in range(ROW_COUNT-3):
				row_arr = col_arr[r:r+WINDOW_LENGTH]
				score += self.evaluate_window(row_arr,piece)

		for r in range(ROW_COUNT-3):
			for c in range(COLUMN_COUNT-3):
				window = [board[r+i][c+i] for i in range(WINDOW_LENGTH) ]			
				score+=self.evaluate_window(window,piece)

		for r in range(ROW_COUNT-3):
			for c in range(3,COLUMN_COUNT):
				window = [board[r+i][c-i] for i in range(WINDOW_LENGTH) ]			
				score += self.evaluate_window(window,piece)			
		
		return score				


		
	def get_best_move(self,board, piece):
		valid_locations = get_valid_locations(board)
		best_score = -1000
		best_move = random.choice(valid_locations)
		scores=[]
		for col in valid_locations:
			row = next_empty_pos(col,board)
			temp_board = board.copy()
			drop_piece(row, col, piece, temp_board)
			score = get_score(temp_board, piece)
			scores.append(score)
			if score > best_score:
				best_score = score
				best_move = col
		for v, s in zip(valid_locations,scores):
				 print("(",v,s,")",end = "")
		print(best_move)		
		return best_move		


# if __name__ == '__main__':
