from constants import Constants 
from screen import Screen 
from computation import Computation
# from minimax import MiniMax
C = Constants()
S = Screen()
Com = Computation()
# M = MiniMax()

import numpy as np
import pygame
import math
import random


class Board:

	def __init__(self):
		pass
	def create_board(self):
		return np.zeros((C.ROW_COUNT,C.COLUMN_COUNT))

	def is_valid_move(self,col,board):
		return board[C.ROW_COUNT-1][col] == 0

	def next_empty_pos(self,col,board):
		for i in range(C.ROW_COUNT):
			if board[i][col] == 0:
				return i

	def drop_piece(self,row,col,piece,board):
		board[row][col] = piece	

	def is_not_full(self,board):
		for i in range(C.COLUMN_COUNT):
			if board[C.ROW_COUNT-1][i] == 0:
				return True
		return False		

	def print_board(self,board):
		print(np.flip(board,0))

	def is_terminal(self,board):
		return Com.check_win(board,C.AI_PIECE) or Com.check_win(board, C.PLAYER_PIECE) or not self.is_not_full(board)

	def get_valid_locations(self,board):
		valid_locations = []
		for c in range(C.COLUMN_COUNT):
			if self.is_valid_move(c,board):
				valid_locations.append(c)
		return valid_locations		

	def minimax(self,board, depth, alpha,beta,maximisePlayer):
		locations = self.get_valid_locations(board)
		if depth == 0 or self.is_terminal(board):
			if self.is_terminal(board):
				if Com.check_win(board,C.AI_PIECE):
					return (None,100000000)
				elif Com.check_win(board,C.PLAYER_PIECE):
					return (None,-100000000)
				else:
					return (None,0)
			else:
				return (None,Com.get_score(board,C.AI_PIECE))

		if maximisePlayer :
			score= -math.inf	
			column = random.choice(locations)
			for col in locations:
				row = self.next_empty_pos(col, board)
				temp_board=board.copy()
				self.drop_piece(row,col,C.AI_PIECE,temp_board)
				new_score = self.minimax(temp_board,depth-1,alpha,beta,False)[1]
				if new_score > score:
					score=new_score
					column=col
				alpha =max(alpha,score)
				if alpha >= beta: 
					break	
			return (column,score)
		
		else:
			score= math.inf	
			column = random.choice(locations)
			for col in locations:
				row = self.next_empty_pos(col, board)
				temp_board=board.copy()
				self.drop_piece(row,col,C.PLAYER_PIECE,temp_board)
				new_score = self.minimax(temp_board, depth-1,alpha,beta,True)[1]
				if new_score < score:
					score=new_score
					column=col
				beta =min(beta,score)
				if alpha >= beta :
					break	
			return (column,score)	
	


	def play(self):

		board = self.create_board()
		
		gameWon, player = False,0
		
		turn = random.randint(C.PLAYER, C.AI)

		S.intialize()
		
		S.draw_board(board)
		
		while self.is_not_full(board) and not gameWon:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.MOUSEMOTION:
					pygame.draw.rect(S.screen,C.BLACK,(0,0,C.width,C.SQUARESIZE))
					posx=event.pos[0]
					pygame.draw.circle(S.screen,C.RED,(posx,C.RADIUS),C.RADIUS)
					pygame.display.update()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if turn == C.PLAYER:
						posx = event.pos[0]	
						col=int(math.floor(posx/C.SQUARESIZE))
						if not self.is_valid_move(col,board):
							continue
						if self.is_valid_move(col,board):
							row = self.next_empty_pos(col,board)
							self.drop_piece(row,col,C.PLAYER_PIECE,board)
							# self.print_board(board)
							S.draw_board(board)
							if Com.check_win(board,turn+1):
								gameWon, player = True, turn+1	
								break
						turn = C.AI

					if turn == C.AI and not gameWon and self.is_not_full(board):
						alpha = -math.inf
						beta = math.inf

						LEVEL = 4 #CONTROL GAME FROM HERE
 
						col = self.minimax(board,LEVEL,alpha,beta,True)[0]

						if self.is_valid_move(col,board):
							r=self.next_empty_pos(col,board)
							self.drop_piece(r, col, C.AI_PIECE, board)
							S.draw_board(board)
							if Com.check_win(board,C.AI_PIECE):
								gameWon, player = True, C.AI_PIECE	
								break
					turn = C.PLAYER

		self.print_board(board)			

		if not player:
			print("DRAW")
		elif player == 1:
			print("Player 1 WON")		
			S.winScreen("Player 1")
		elif player == 2:
			print("Player 2 WON")
			S.winScreen("Player 2")

if __name__ == '__main__' :
	B = Board()
	B.play()		