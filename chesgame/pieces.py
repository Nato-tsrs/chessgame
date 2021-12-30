blackIcons = {"Pawn": "♙", "Rook": "♖", "Knight": "♘", "Bishop": "♗", "King": "♔", "Queen": "♕"}
whiteIcons = {"Pawn": "♟", "Rook": "♜", "Knight": "♞", "Bishop": "♝", "King": "♚", "Queen": "♛"}


class Piece:

    def __init__(self, color, board, position):
        self._color=color
        self._board=board
        self._position=position

    @property
    def color(self):
        return self._color

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self,pos):
        if pos[0].isalpha() and len(pos[0]) == 1 and pos[0].isupper() and pos[1] in [1,2,3,4,5,6,7,8]:
            self._position=pos


    def checkMove(self, dest):
        return False

    def move(self, dest):
        if self.checkMove(dest):

            self._board.makeMove(self.position, dest, self)
            self.position = dest
            return True
        else:
            return False


    def getName(self):
        return "Pieces"

    def getIcon(self):
        if self.color == "White":
            for i in whiteIcons:
                if i == self.getName():
                    return whiteIcons[self.getName()]
        else:
            for i in blackIcons:
                if i == self.getName():
                    return blackIcons[self.getName()]


class Knight(Piece):
    def getName(self):
        return "Knight"

    def checkMove(self, dest):
        boo=False
        if (dest[0]==chr(ord(self.position[0])-1) or dest[0]==chr(ord(self.position[0])+1)) and (dest[1]==self.position[1]+2 or dest[1]==self.position[1]-2): boo=True
        if (dest[0]==chr(ord(self.position[0])-2) or dest[0]==chr(ord(self.position[0])+2))  and (dest[1]==self.position[1]+1 or dest[1]==self.position[1]-1): boo=True
        if boo and  self.color=="White" and self._board.board[dest].color=="White": boo=False
        if boo and  self.color=="Black" and self._board.board[dest].color=="Black": boo=False
        return boo

    def move(self, dest):
        if self.checkMove(dest):

            self._board.makeMove(self.position, dest, self)
            self.position = dest
            return True
        else:
            return False

class Rook(Piece):
    def getName(self):
        return "Rook"

    def checkMove(self, dest):
        boo=False
        if self.position[0]==dest[0] and  self.position[1] != dest[1]: boo=True
        if boo and self.position[1] > dest[1]:
            for i in range(dest[1],self.position[1]):
                if self._board.board[(self.position[0],i)].getName() !="NoPIce": boo=False
        if self.position[0]==dest[0] and  self.position[1] != dest[1] and self.position[1] < dest[1]:
            for i in range( self.position[1]+1,dest[1]+1):
                if self._board.board[(self.position[0], i)].getName() != "NoPIce": boo = False

        if self.position[0]!=dest[0] and  self.position[1] == dest[1]: boo=True
        if self.position[0]!=dest[0] and  self.position[1] == dest[1]:
            if ord(self.position[0]) < ord(dest[0]):
                for i in range(ord(self.position[0])+1,ord(dest[0])+1):
                    if self._board.board[(chr(i),self.position[1])].getName() != "NoPIce": boo = False

            if ord(self.position[0]) > ord(dest[0]):
                for i in range(ord(dest[0]),ord(self.position[0])  ):
                    if self._board.board[(chr(i), self.position[1])].getName() != "NoPIce": boo = False

        if  self.color=="White"  and self._board.board[dest].color=="Black": boo=True
        if  self.color == "Black" and self._board.board[dest].color == "White": boo = True

        return boo

    def move(self, dest):
        if self.checkMove(dest):

            self._board.makeMove(self.position, dest, self)
            self.position = dest
            return True
        else:
            return False


class Bishop(Piece):
    def getName(self):
        return "Bishop"

    def checkMove(self, dest):
        boo=False
        if (ord(self.position[0])>ord (dest[0]) and self.position[1]< dest[1]) or (ord(self.position[0])<ord (dest[0]) and self.position[1]> dest[1]):
            if dest[1]==self.position[1]+(ord(self.position[0])-ord (dest[0])):
                boo=True
        if boo and  (ord(self.position[0])>ord (dest[0]) and self.position[1]< dest[1]) :
            for i in range(self.position[1]+1,dest[1]+1):
                for j in range(ord(dest[0]),ord(self.position[0])):
                    if i==self.position[1]+(ord(self.position[0])-j) and  self._board.board[chr(j),i].getName() !="NoPIce":
                        boo=False
        if  dest[1]==self.position[1]+(ord(self.position[0])-ord (dest[0])) and (ord(self.position[0])<ord (dest[0]) and self.position[1]> dest[1]):
            for i in range(dest[1],self.position[1]):
                for j in range(ord(self.position[0])+1, ord(dest[0]) + 1):
                    if i == self.position[1] + (ord(self.position[0]) - j) and self._board.board[chr(j), i].getName() != "NoPIce":
                        boo = False

        if (ord(self.position[0]) < ord(dest[0]) and self.position[1] < dest[1]) or (ord(self.position[0]) > ord(dest[0]) and self.position[1] > dest[1]):
            if dest[1]==self.position[1]-(ord(self.position[0])-ord (dest[0])):
                boo=True
        if (ord(self.position[0]) < ord(dest[0]) and self.position[1] < dest[1]) and dest[1]==self.position[1]-(ord(self.position[0])-ord (dest[0]) ):
            for i in range(self.position[1]+1,dest[1]+1):
                for j in range(ord(self.position[0])+1,ord(dest[0])+1):
                    if i == self.position[1] - (ord(self.position[0]) - j) and self._board.board[chr(j), i].getName() != "NoPIce":
                        boo = False
        if (ord(self.position[0]) > ord(dest[0]) and self.position[1] > dest[1]) and dest[1]==self.position[1]-(ord(self.position[0])-ord (dest[0])):
            for i in range(dest[1],self.position[1]):
                for j in range(ord(self.position[0]),ord(self.position[0])):
                    if i == self.position[1] - (ord(self.position[0]) - j) and self._board.board[chr(j), i].getName() != "NoPIce":
                        boo = False
        if self.color=="White" and self._board.board[dest]=="Black":boo=True
        if self.color == "Black" and self._board.board[dest] == "White": boo = True
        return boo

    def move(self, dest):
        if self.checkMove(dest):

            self._board.makeMove(self.position, dest, self)
            self.position = dest
            return True
        else:
            return False


class Queen(Piece):
    def getName(self):
        return "Queen"

    def checkMove(self, dest):
        boo = False
        if self.position[0] == dest[0] and self.position[1] != dest[1]: boo = True
        if boo and self.position[1] > dest[1]:
            for i in range(dest[1], self.position[1]):
                if self._board.board[(self.position[0], i)].getName() != "NoPIce": boo = False
        if self.position[0] == dest[0] and self.position[1] != dest[1] and self.position[1] < dest[1]:
            for i in range(self.position[1] + 1, dest[1] + 1):
                if self._board.board[(self.position[0], i)].getName() != "NoPIce": boo = False

        if self.position[0] != dest[0] and self.position[1] == dest[1]: boo = True
        if self.position[0] != dest[0] and self.position[1] == dest[1]:
            if ord(self.position[0]) < ord(dest[0]):
                for i in range(ord(self.position[0]) + 1, ord(dest[0]) + 1):
                    if self._board.board[(chr(i), self.position[1])].getName() != "NoPIce": boo = False

            if ord(self.position[0]) > ord(dest[0]):
                for i in range(ord(dest[0]), ord(self.position[0])):
                    if self._board.board[(chr(i), self.position[1])].getName() != "NoPIce": boo = False

        if  self.color == "White" and self._board.board[dest].color == "Black": boo = True
        if  self.color == "Black" and self._board.board[dest].color == "White": boo = True
        if (ord(self.position[0])>ord (dest[0]) and self.position[1]< dest[1]) or (ord(self.position[0])<ord (dest[0]) and self.position[1]> dest[1]):
            if dest[1]==self.position[1]+(ord(self.position[0])-ord (dest[0])):
                boo=True
        if boo and  (ord(self.position[0])>ord (dest[0]) and self.position[1]< dest[1]) :
            for i in range(self.position[1]+1,dest[1]+1):
                for j in range(ord(dest[0]),ord(self.position[0])):
                    if i==self.position[1]+(ord(self.position[0])-j) and  self._board.board[chr(j),i].getName() !="NoPIce":
                        boo=False
        if  dest[1]==self.position[1]+(ord(self.position[0])-ord (dest[0])) and (ord(self.position[0])<ord (dest[0]) and self.position[1]> dest[1]):
            for i in range(dest[1],self.position[1]):
                for j in range(ord(self.position[0])+1, ord(dest[0]) + 1):
                    if i == self.position[1] + (ord(self.position[0]) - j) and self._board.board[chr(j), i].getName() != "NoPIce":
                        boo = False

        if (ord(self.position[0]) < ord(dest[0]) and self.position[1] < dest[1]) or (ord(self.position[0]) > ord(dest[0]) and self.position[1] > dest[1]):
            if dest[1]==self.position[1]-(ord(self.position[0])-ord (dest[0])):
                boo=True
        if (ord(self.position[0]) < ord(dest[0]) and self.position[1] < dest[1]) and dest[1]==self.position[1]-(ord(self.position[0])-ord (dest[0]) ):
            for i in range(self.position[1]+1,dest[1]+1):
                for j in range(ord(self.position[0])+1,ord(dest[0])+1):
                    if i == self.position[1] - (ord(self.position[0]) - j) and self._board.board[chr(j), i].getName() != "NoPIce":
                        boo = False
        if (ord(self.position[0]) > ord(dest[0]) and self.position[1] > dest[1]) and dest[1]==self.position[1]-(ord(self.position[0])-ord (dest[0])):
            for i in range(dest[1],self.position[1]):
                for j in range(ord(self.position[0]),ord(self.position[0])):
                    if i == self.position[1] - (ord(self.position[0]) - j) and self._board.board[chr(j), i].getName() != "NoPIce":
                        boo = False
        if self.color=="White" and self._board.board[dest]=="Black":boo=True
        if self.color == "Black" and self._board.board[dest] == "White": boo = True

        return boo

    def move(self, dest):
        if self.checkMove(dest):

            self._board.makeMove(self.position, dest, self)
            self.position = dest
            return True
        else:
            return False

class King(Piece):
    def getName(self):
        return "King"

    def checkMove(self,dest):
            boo=False
            if (dest[0]==self.position[0] or dest[0]== chr(ord(self.position[0])-1) or dest[0]== chr(ord(self.position[0])+1)) and (dest[1]== self.position[1]+1 or dest[1]== self.position[1]-1 or dest[1]==self.position[1]) and dest!=self.position:boo=True
            if boo==True and self.color=="White" and  self._board.board[dest].color=="White": boo=False
            if boo==True and self.color=="Black" and self._board.board[dest].color=="Black":boo=False

            return boo

    def move(self, dest):
        if self.checkMove(dest):

            self._board.makeMove(self.position, dest, self)
            self.position = dest
            return True
        else:
            return False






class Pawn(Piece):
    def getName(self):
        return "Pawn"

    def checkMove(self, dest):
        boo=False
        if ((self.position[0]=='G' and dest[0] in 'E') or (self.position[0]=='B' and dest[0] in 'D')) and self.position[1]==dest[1]: boo= True
        if self.color=="White" and dest[0] ==chr(ord(self.position[0])-1) and dest[1]==self.position[1]: boo=True
        if self.color == "Black" and dest[0] == chr(ord(self.position[0])+1) and dest[1] == self.position[1]: boo = True
        if self.color == "White" and dest[0]==chr(ord(self.position[0])-1) and (dest[1]==self.position[1]+1 or  dest[1]==self.position[1]-1 ) and self._board.board[dest].color=="Black":
            boo=True
        if self.color == "Black" and dest[0] == chr(ord(self.position[0]) +1) and (dest[1] == self.position[1] + 1 or dest[1] == self.position[1] - 1) and self._board.board[dest].color == "White":
            boo=True
        return boo

    def move(self, dest):
        if self.checkMove(dest):

            self._board.makeMove(self.position, dest, self)
            self.position = dest
            return True
        else:
            return False


    def mySelf(self):
        return self

# I added NoPIce as a helper class which I used to denote empty units (Hope that wasn't too much addition)

class NoPIce(Piece):
    def getName(self):
        return "NoPIce"
    def getIcon(self):
        if self.color=="Wite":
            return "⬛"
        else: return "⬜"

    def checkMove(self, dest):
        return True


