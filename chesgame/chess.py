from board import Board
from pieces import *


class Chess:
    def __init__(self):
        self.board=Board()
        self.currentPlayer="White"


    def swapPlayers(self):
        if self.currentPlayer=="Black":
            self.currentPlayer="White"
            return
        if self.currentPlayer=="White":
            self.currentPlayer="Black"
            return


    def isStringValidMove(self,moveStr):
        if moveStr[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] and moveStr[3] in ['A', 'B', 'C', 'D', 'E', 'F', 'G','H'] and int(moveStr[1]) in [1, 2,3, 4,5, 6,7,8] and \
                int(moveStr[4]) in [1, 2, 3, 4, 5, 6, 7, 8] and moveStr[2] == " " and isinstance(moveStr, str) and len(moveStr) == 5:
            return True
        else:
            return False

    def play(self):
        while (True):
            self.board.displayBoard()
            print("{}'s turn. Enter a move:".format(self.currentPlayer))
            move = input()
            if move == "EXIT":
                break
            while (self.isStringValidMove(move) == False):
                print("INVALID MOVE")
                print("{}'s turn. Enter a move:".format(self.currentPlayer))
                move=input()
                if move == "EXIT":
                    break

            if self.board.board[(move[0],int(move[1]))].color!=self.currentPlayer:
                    print("INVALID move. Piece should be {}!".format(self.currentPlayer.lower()))
                    while (self.board.board[(move[0],int(move[1]))].color!=self.currentPlayer):

                        print("{}'s turn. Enter a move again :".format(self.currentPlayer))
                        move = input()
                        if move == "EXIT":
                            break

            if self.board.board[(move[0], int(move[1]))].checkMove((move[3], int(move[4]))) == False:
                print("INVALID move. Path is blocked!")
                continue
            if self.board.board[(move[0], int(move[1]))].getName=="Pawn" and  move[3]+move[4] in ['A1','A3','A4','A5',"A6",'A7','A8','H1','H3','H4','H5',"H6",'H7','H8'] :
                changePiece=input("The Pawn is prompted. \n Enter the piece name  you whant to substitude with: ")
                if changePiece=="Queen":
                    self.board.setPiece((move[0], int(move[1])),Queen(self.currentPlayer, self.board, (move[0], int(move[1]))))
                if changePiece == "Rook":
                    self.board.setPiece((move[0], int(move[1])),Rook(self.currentPlayer, self.board, (move[0], int(move[1]))))
                if changePiece == "Knight":
                    self.board.setPiece((move[0], int(move[1])),Knight(self.currentPlayer, self.board, (move[0], int(move[1]))))
                if changePiece == "Bishop":
                    self.board.setPiece((move[0], int(move[1])),Bishop(self.currentPlayer, self.board, (move[0], int(move[1]))))



                while(changePiece not in ['Queen','Bishop','Rook','Knight']) :
                    print('pawn chould be sibstituted with Queen,Bishop,Rook and  Knight')
                    changePiece = input("The Pawn is prompted. \n Enter the piece name  you whant to substitude with: ")
                    if changePiece == "Queen":
                        self.board.setPiece((move[0], int(move[1])),
                                            Queen(self.currentPlayer, self.board, (move[0], int(move[1]))))
                    if changePiece == "Rook":
                        self.board.setPiece((move[0], int(move[1])),
                                            Rook(self.currentPlayer, self.board, (move[0], int(move[1]))))
                    if changePiece == "Knight":
                        self.board.setPiece((move[0], int(move[1])),
                                            Knight(self.currentPlayer, self.board, (move[0], int(move[1]))))
                    if changePiece == "Bishop":
                        self.board.setPiece((move[0], int(move[1])),
                                            Bishop(self.currentPlayer, self.board, (move[0], int(move[1]))))

            self.board.board[(move[0],int(move[1]))].move((move[3],int(move[4])))

            self.swapPlayers()



if __name__ == "__main__":
    game = Chess()
    game.play()

