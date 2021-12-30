from pieces import *

class Board:

    def __init__(self):
        self.board= {}
        self.placePieces()


    def placePieces(self):

        pieceslst=[]

        for i in ['B','G']:
            for j in range (1,9):
                if i=='B':
                    blackpawn=Pawn("Black",self,('B',j))
                    pieceslst.append(blackpawn)
                if i=="G":
                    whitepawn=Pawn("White",self,('G',j))
                    pieceslst.append(whitepawn)




        for i in range(1,9):
            for j in ['A','H']:
                if j=='A' and (i ==1 or i ==8):
                    blackrook=Rook("Black",self,('A',i))
                    pieceslst.append(blackrook)
                elif  i ==1 or i ==8:
                    whiterook = Rook("White", self, ('H', i))
                    pieceslst.append(whiterook)

                if j == 'A' and (i == 2 or i == 7):
                    blackknight = Knight("Black", self, ('A', i))
                    pieceslst.append(blackknight)
                elif i == 2 or i == 7:
                    whiteknight = Knight("White", self, ('H', i))
                    pieceslst.append(whiteknight)

                if j == 'A' and (i == 3 or i == 6):
                    blackbishop = Bishop("Black", self, ('A', i))
                    pieceslst.append(blackbishop)
                elif i == 3 or i == 6:
                    whitebishop = Bishop("White", self, ('H', i))
                    pieceslst.append(whitebishop)

                if j == 'A' and i == 5 :
                    blackking= King("Black", self, ('A', i))
                    pieceslst.append(blackking)
                elif i == 5:
                    whitequeen = King("White", self, ('H', i))
                    pieceslst.append(whitequeen)

                if j == 'A' and i == 4 :
                    blackqueen = Queen ("Black", self, ('A', i))
                    pieceslst.append(blackqueen)
                elif i == 4:
                    whitekqueen = Queen ("White", self, ('H', i))
                    pieceslst.append(whitekqueen)
        positionlst=[]
        for i in pieceslst:
            positionlst.append(i.position)

        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G','H']:
            for j in range(1, 9):
                for k in pieceslst:
                    if (i, j) == k.position:
                        self.board[(i, j)]=k

                    self.squares(i,j,positionlst)

    def squares(self, i, j, positionlst):
        if ((i, j) not in positionlst) and (
                (i == 'H' and j % 2 != 0) or (i == 'G' and j % 2 == 0) or (i == 'F' and j % 2 != 0) or (
                i == 'E' and j % 2 == 0) or (i == 'D' and j % 2 != 0) or (i == 'C' and j % 2 == 0) or (
                        i == 'B' and j % 2 != 0) or (i == 'A' and j % 2 == 0)):
            self.board[(i, j)] = NoPIce("Blck", self, (i, j))
        if ((i, j) not in positionlst) and not (
                (i == 'H' and j % 2 != 0) or (i == 'G' and j % 2 == 0) or (i == 'F' and j % 2 != 0) or (
                i == 'E' and j % 2 == 0) or (i == 'D' and j % 2 != 0) or (i == 'C' and j % 2 == 0) or (
                        i == 'B' and j % 2 != 0) or (i == 'A' and j % 2 == 0)):
            self.board[(i, j)] = NoPIce("Wite", self, (i, j))

    def setPiece(self, position, piece):
        self.board[position] = piece



    def getPiece(self, position):
        return self.board[position]

    def makeMove(self, startPosition, endPosition, player):
        if player.checkMove(endPosition) and player.color==self.board[startPosition].color and player.getName()==self.board[startPosition].getName() and  player.position==self.board[startPosition].position:
            self.board[endPosition] = player
            positionslst = []
            for i in self.board:
                if self.board[i].getName() != "NoPIce" and i != startPosition:
                    positionslst.append(i)
            self.squares(startPosition[0],startPosition[1],positionslst)

    def displayBoard(self):
        for i in range(1, 9):
            print('  {}  '.format(i),end="")
        print("")


        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            print(i, end=" ")
            for j in range(1, 9):
                for k in self.board:

                    if (i, j) == k:
                        print("[{}]".format((self.board[k]).getIcon()), end=" ")

            print("")



