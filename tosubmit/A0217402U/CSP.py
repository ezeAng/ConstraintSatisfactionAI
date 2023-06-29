
import cProfile

import sys
import copy

# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
######## Piece
#############################################################################
class Piece:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    
class King(Piece):
    name = "King"
    icon = "♔"

    def __init__(self, x, y):
        super().__init__(x,y,self.name)

    def get_actions(x, y, grid, rows, cols):
        acts = []
        #Gets possible locations, given the board limits and obstacles 
        #(Does not remove locations with pieces or threatened locations)

        #NorthWest
        if x-1 >= 0 and y-1 >= 0: #e.g this checks board limits
            if grid[x-1][y-1] >= 0: #this checks if its not an obstacle 
                acts.append((x-1,y-1))

        #North
        if x-1 >= 0:
            if grid[x-1][y] >= 0:
                acts.append((x-1, y))

        #NorthEast
        if x-1 >= 0 and y+1 < cols:
            if grid[x-1][y+1] >= 0:
                acts.append((x-1, y+1))

        #West
        if y-1 >= 0:
            if grid[x][y-1] >= 0:
                acts.append((x, y-1))

        #East
        if y+1 < cols:
            if grid[x][y+1] >= 0:
                acts.append((x, y+1))
                
        #SouthWest
        if x+1 < rows and y-1 >= 0:
            if grid[x+1][y-1] >= 0:
                acts.append((x+1, y-1))

        #South
        if x+1 < rows:
            if grid[x+1][y] >= 0:
                acts.append((x+1, y))

        #SouthEast
        if x+1 < rows and y+1 < cols:
            if grid[x+1][y+1] >= 0:
                acts.append((x+1,y+1))
        
        return acts
    
    '''
    Takes in a board state or config, checks the possible threats the King can make
    and checks if the coordinate at that grid is walkable ( >0 )
    Then returns list possible action outcomes (x,y) from this state
    @Returns list of tuple of numbers (x,y)
    '''
    def actions(self, grid, rows, cols):
        acts = set()
        x = self.x
        y = self.y
        
        #Gets possible locations, given the board limits and obstacles 
        #(Does not remove locations with pieces or threatened locations)
        #NorthWest
        if x-1 >= 0 and y-1 >= 0: #e.g this checks board limits
            if grid[x-1][y-1] >= 0: #this checks if its not an obstacle 
                acts.add((x-1,y-1))

        #North
        if x-1 >= 0:
            if grid[x-1][y] >= 0:
                acts.add((x-1, y))

        #NorthEast
        if x-1 >= 0 and y+1 < cols:
            if grid[x-1][y+1] >= 0:
                acts.add((x-1, y+1))

        #West
        if y-1 >= 0:
            if grid[x][y-1] >= 0:
                acts.add((x, y-1))

        #East
        if y+1 < cols:
            if grid[x][y+1] >= 0:
                acts.add((x, y+1))
                
        #SouthWest
        if x+1 < rows and y-1 >= 0:
            if grid[x+1][y-1] >= 0:
                acts.add((x+1, y-1))

        #South
        if x+1 < rows:
            if grid[x+1][y] >= 0:
                acts.add((x+1, y))

        #SouthEast
        if x+1 < rows and y+1 < cols:
            if grid[x+1][y+1] >= 0:
                acts.add((x+1,y+1))
        
        return acts
        
class Knight(Piece):
    name = "Knight"
    icon = "♘"

    def __init__(self, x, y):
        super().__init__(x,y ,self.name)

    def get_actions(x, y, grid, rows, cols):
        acts = []

        #|-
        #|
        if y+1 < cols and x-2 >= 0:
            if grid[x-2][y+1] >= 0:
                acts.append((x-2, y+1))
            

        #---
        #|
        if y+2 < cols and x-1 >= 0:
            if grid[x-1][y+2] >= 0:
                acts.append((x-1, y+2))

        #|
        #---
        
        if y+2 < cols and x+1 < rows:
            if grid[x+1][y+2] >= 0:
                acts.append((x+1, y+2))


        #|
        #|-
        if y+1 < cols and x+2 < rows:
            if grid[x+2][y+1] >= 0:
                acts.append((x+2, y+1))

        # |
        #-|
        if y-1 >= 0 and x+2 < rows:
            if grid[x+2][y-1] >= 0:
                acts.append((x+2, y-1))

        #   |
        #---
        if y-2 >= 0 and x+1 < rows:
            if grid[x+1][y-2] >= 0:
                acts.append((x+1, y-2))


        #-|
        # |
        if y-1 >= 0 and x-2 >= 0:
            if grid[x-2][y-1] >= 0:
                acts.append((x-2, y-1))
            

        #---
        #|
        if y-2 >= 0 and x-1 >= 0:
            if grid[x-1][y-2] >= 0:
                acts.append((x-1, y-2))


        return acts

    '''
    Returns a list of action locations, which the knight can move to from its current location,
    that is not an obstacle and on the grid
    '''
    def actions(self, grid, rows, cols):
        acts = set()
        x = self.x
        y = self.y

        #|-
        #|
        if y+1 < cols and x-2 >= 0:
            if grid[x-2][y+1] >= 0:
                acts.add((x-2, y+1))
            

        #---
        #|
        if y+2 < cols and x-1 >= 0:
            if grid[x-1][y+2] >= 0:
                acts.add((x-1, y+2))

        #|
        #---
        
        if y+2 < cols and x+1 < rows:
            if grid[x+1][y+2] >= 0:
                acts.add((x+1, y+2))


        #|
        #|-
        if y+1 < cols and x+2 < rows:
            if grid[x+2][y+1] >= 0:
                acts.add((x+2, y+1))

        # |
        #-|
        if y-1 >= 0 and x+2 < rows:
            if grid[x+2][y-1] >= 0:
                acts.add((x+2, y-1))

        #   |
        #---
        if y-2 >= 0 and x+1 < rows:
            if grid[x+1][y-2] >= 0:
                acts.add((x+1, y-2))


        #-|
        # |
        if y-1 >= 0 and x-2 >= 0:
            if grid[x-2][y-1] >= 0:
                acts.add((x-2, y-1))
            

        #---
        #|
        if y-2 >= 0 and x-1 >= 0:
            if grid[x-1][y-2] >= 0:
                acts.add((x-1, y-2))


        return acts

class Rook(Piece):
    name = "Rook"
    icon = "♖"
    #Lists the possible moves, specifically changes in the x,y directions (reference pt top left of board)
    # the numbers correspond to the limit of how much the direction val can be changed
    #e.g queen will then be able to move the entire board

    #Rook movement
    #       ^
    #       |
    #  <--- R --->
    #       |
    #       v


    def __init__(self, x, y):
        super().__init__(x,y ,self.name)


    def get_actions(x, y, grid, rows, cols):
        acts = []

        #North
        x_avail = x
        for i in range(1, x_avail+1):
            if grid[x-i][y] >= 0:
                #if the spot is movable -> no obstacle and no piece blocking
                acts.append((x-i,y))
            else: 
                #we have to break here due to obstacle
                break

        #East
        y_avail = cols - y - 1
        for i in range(1, y_avail+1):
            
            if grid[x][y+i] >= 0:
                #if the spot is movable -> no obstacle and no piece blocking
                acts.append((x,y+i))
            else:   
                #we have to break here due to obstacle
                break

        #South
        x_avail = rows - x - 1
        for i in range(1, x_avail+1):
            if grid[x+i][y] >= 0:
                #if the spot is movable -> no obstacle and no piece blocking
                acts.append((x+i,y))
            
            else:
                #we have to break here due to obstacle or piece block
                break


        #West
        y_avail = y
        for i in range(1, y_avail+1):
            if grid[x][y-i] >= 0:
                #if the spot is movable -> no obstacle and no piece blocking
                acts.append((x,y-i))
            
            else:   
                #we have to break here due to obstacle or piece block
                break
        
        return acts



    '''
    Takes in a State object, checks the possible moves the King can take
    and checks if the coordinate at that grid is walkable ( >0 )
    Then returns list possible action outcomes (x,y) from this state
    @Returns list of tuple of numbers (x,y)

    '''
    def actions(self, grid, rows, cols):
        acts = set()
        x = self.x
        y = self.y

        #North
        x_avail = x
        for i in range(1, x_avail+1):
            if grid[x-i][y] >= 0:
                #if the spot is movable -> no obstacle and no piece blocking
                acts.add((x-i,y))
            else: 
                #we have to break here due to obstacle
                break

        #East
        y_avail = cols - y - 1
        for i in range(1, y_avail+1):
            
            if grid[x][y+i] >= 0:
                #if the spot is movable -> no obstacle and no piece blocking
                acts.add((x,y+i))
            else:   
                #we have to break here due to obstacle
                break

        #South
        x_avail = rows - x - 1
        for i in range(1, x_avail+1):
            if grid[x+i][y] >= 0:
                #if the spot is movable -> no obstacle and no piece blocking
                acts.add((x+i,y))
            
            else:
                #we have to break here due to obstacle or piece block
                break


        #West
        y_avail = y
        for i in range(1, y_avail+1):
            if grid[x][y-i] >= 0:
                #if the spot is movable -> no obstacle and no piece blocking
                acts.add((x,y-i))
            
            else:   
                #we have to break here due to obstacle or piece block
                break

        
        return acts

class Bishop(Piece):
    name = "Bishop"
    icon = "♗"

    #Lists the possible moves, specifically changes in the x,y directions (reference pt top left of board)
    # the numbers correspond to the limit of how much the direction val can be changed
    #e.g queen will then be able to move the entire board

    #Bishop movement
    #   ^       ^
    #    \     /
    #       R
    #    /     \
    #   v       v


    def __init__(self, x, y):
        super().__init__(x,y,self.name)


    def get_actions(x, y, grid, rows, cols):
        acts = []

        #NorthWest
        x_avail = x
        y_avail = y
        while x_avail - 1 >= 0 and y_avail - 1 >= 0:
            if grid[x_avail-1][y_avail-1] >= 0:
                #if the spot is movable -> no obstacle 
                
                acts.append((x_avail-1, y_avail-1))
                x_avail -= 1
                y_avail -= 1
            
            else:
                
                break

        
        #NorthEast
        x_avail = x
        y_avail = y
        while x_avail - 1 >= 0 and y_avail + 1 < cols:
            if grid[x_avail-1][y_avail+1] >= 0:
                #if the spot is movable -> no obstacle and no piece blocking
                
                acts.append((x_avail-1, y_avail+1))
                x_avail -= 1
                y_avail += 1

            else:         
                break


        #SouthEast
        x_avail = x
        y_avail = y
        while x_avail + 1 < rows and y_avail + 1 < cols:
            if grid[x_avail+1][y_avail+1] >= 0:
                #if the spot is movable -> no obstacle
                acts.append((x_avail+1,y_avail+1))
                x_avail += 1
                y_avail += 1

            else:
                break

        
        #SouthWest
        x_avail = x
        y_avail = y
        while x_avail + 1 < rows and y_avail - 1 >= 0:
            if grid[x_avail+1][y_avail-1] >= 0:
                #if the spot is movable -> no obstacle and no piece blocking
                acts.append((x_avail+1, y_avail-1))
                x_avail += 1
                y_avail -= 1
            
            else: 
                break

        return acts

    '''
    Takes in a State object, checks the possible moves the King can take
    and checks if the coordinate at that grid is walkable ( >0 )
    Then returns list possible action outcomes (x,y) from this state
    @Returns list of tuple of numbers (x,y)

    '''
    def actions(self, grid, rows, cols):
        
        acts = set()
        x = self.x
        y = self.y
        
        #NorthWest
        x_avail = x
        y_avail = y
        while x_avail - 1 >= 0 and y_avail - 1 >= 0:
            if grid[x_avail-1][y_avail-1] >= 0:
                #if the spot is movable -> no obstacle 
                acts.add((x_avail-1, y_avail-1))
                x_avail -= 1
                y_avail -= 1
            
            else:
                
                break

        
        #NorthEast
        x_avail = x
        y_avail = y
        while x_avail - 1 >= 0 and y_avail + 1 < cols:
            if grid[x_avail-1][y_avail+1] >= 0:
                #if the spot is movable -> no obstacle            
                acts.add((x_avail-1, y_avail+1))
                x_avail -= 1
                y_avail += 1

            else:         
                break


        #SouthEast
        x_avail = x
        y_avail = y
        while x_avail + 1 < rows and y_avail + 1 < cols:
            if grid[x_avail+1][y_avail+1] >= 0:
                #if the spot is movable -> no obstacle
                acts.add((x_avail+1,y_avail+1))
                x_avail += 1
                y_avail += 1

            else:
                break

        
        #SouthWest
        x_avail = x
        y_avail = y
        while x_avail + 1 < rows and y_avail - 1 >= 0:
            if grid[x_avail+1][y_avail-1] >= 0:
                #if the spot is movable -> no obstacle and no piece blocking
                acts.add((x_avail+1, y_avail-1))
                x_avail += 1
                y_avail -= 1
            
            else: 
                break

        
        return acts

class Queen(Piece):
    name = "Queen"
    icon = "♕"

    def __init__(self, x, y):
        super().__init__(x,y,self.name)
        self.bishop_part = Bishop(x,y)
        self.rook_part = Rook(x,y)
    
    def get_actions(x, y, grid, rows, cols):
        acts = []
        acts.extend(Bishop.get_actions(x, y, grid, rows, cols))
        acts.extend(Rook.get_actions(x, y, grid, rows, cols))
        return acts

    def actions(self, grid, rows, cols):
        
        acts = set()
        acts.update(self.bishop_part.actions(grid, rows, cols))
        acts.update(self.rook_part.actions(grid, rows, cols))
        
        return acts

class Ferz(Piece):
    name = "Ferz"
    icon = "F"
    def __init__(self, x, y):
        super().__init__(x,y,self.name)

    def get_actions(x, y, grid, rows, cols):
        acts = []
        #NorthWest
        if x-1 >= 0 and y-1 >= 0:
            if grid[x-1][y-1] >= 0:
                acts.append((x-1,y-1))

        

        #NorthEast
        if x-1 >= 0 and y+1 < cols:
            if grid[x-1][y+1] >= 0:
                acts.append((x-1, y+1))

            
        #SouthWest
        if x+1 < rows and y-1 >= 0:
            if grid[x+1][y-1] >= 0:
                acts.append((x+1, y-1))


        #SouthEast
        if x+1 < rows and y+1 < cols:
            if grid[x+1][y+1] >= 0:
                acts.append((x+1,y+1))

        return acts


    '''
    Takes in a State object, checks the possible moves the King can take
    and checks if the coordinate at that grid is walkable ( >0 )
    Then returns list possible action outcomes (x,y) from this state
    @Returns list of tuple of numbers (x,y)

    '''
    def actions(self, grid, rows, cols):
        acts = set()
        x = self.x
        y = self.y

        
        #NorthWest
        if x-1 >= 0 and y-1 >= 0:
            if grid[x-1][y-1] >= 0:
                acts.add((x-1,y-1))

        #NorthEast
        if x-1 >= 0 and y+1 < cols:
            if grid[x-1][y+1] >= 0:
                acts.add((x-1, y+1))

        
        #SouthWest
        if x+1 < rows and y-1 >= 0:
            if grid[x+1][y-1] >= 0:
                acts.add((x+1, y-1))


        #SouthEast
        if x+1 < rows and y+1 < cols:
            if grid[x+1][y+1] >= 0:
                acts.add((x+1,y+1))
        
        return acts

class Princess(Piece):
    name = "Princess"
    icon = "P"
    def __init__(self, x, y):
        super().__init__(x,y,self.name)
        self.bishop_part = Bishop(x,y)
        self.knight_part = Knight(x,y)


    def get_actions(x, y, grid, rows, cols):
        acts = []
        acts.extend(Bishop.get_actions(x, y, grid, rows, cols))
        acts.extend(Knight.get_actions(x, y, grid, rows, cols))
        return acts


    def actions(self, grid, rows, cols):
        acts = set()
        acts.update(self.bishop_part.actions(grid, rows, cols))
        acts.update(self.knight_part.actions(grid, rows, cols))
        return acts

class Empress(Piece):
    name = "Empress"
    icon = "E"
    def __init__(self, x, y):
        super().__init__(x,y,self.name)
        self.rook_part = Rook(x,y)
        self.knight_part = Knight(x,y)

    def get_actions(x, y, grid, rows, cols):
        acts = []
        acts.extend(Rook.get_actions(x, y, grid, rows, cols))
        acts.extend(Knight.get_actions(x, y, grid, rows, cols))
        return acts

    def actions(self, grid, rows, cols):
        acts = set()
        acts.update(self.rook_part.actions(grid, rows, cols))
        acts.update(self.knight_part.actions(grid, rows, cols))
        return acts








'''
Creates an instance of a piece and returns it. 
Returns None if no such piece fits the description
'''
def create_piece(piece_desc, location):

    if piece_desc == "King":
        return King(x = location[0], y = location[1])
    elif piece_desc == "Rook":
        return Rook(x = location[0], y = location[1])
    elif piece_desc == "Bishop":
        return Bishop(x = location[0], y = location[1])
    elif piece_desc == "Queen":
        return Queen(x = location[0], y = location[1])
    elif piece_desc == "Knight":
        return Knight(x = location[0], y = location[1])
    elif piece_desc == "Ferz":
        return Ferz(x = location[0], y = location[1])
    elif piece_desc == "Princess":
        return Princess(x = location[0], y = location[1])
    elif piece_desc == "Empress":
        return Empress(x = location[0], y = location[1])   
    else:
        return None


'''
Returns String of x val, i.e the column label of a x-axis index
'''
def col_to_txt(x):
    return str(chr(ord("a") + x))



#############################################################################
######## Board
#############################################################################
class Board:
    def __init__(self, grid, rows, cols, pieces):
        self.rows = rows
        self.cols = cols
        self.grid = grid
        self.pieces = pieces #dictionary {loc: piece} loc is in r,c!!
        self.piece_locations = [] # in (r,c) format
        
        # # #Add and create initial pieces (object) to board
        for piece in self.pieces:
            self.piece_locations.append((piece.x,piece.y))
        


    # def print_board(self):
    #     top_bot_line = " "
    #     x_axis = "   "
    #     for i in range(self.cols+1):
    #         top_bot_line += "__"
            
    #     for i in range(self.cols):
            
    #         x_axis += chr(i + 97)
    #         x_axis += " "
    #     print(top_bot_line)
    #     string = ""
    #     for i in range(self.rows):
    #         string += str(i)
    #         string += " |"
    #         row = self.grid[i]
    #         for j in range(self.cols):
                
    #             col_item = row[j]
    #             if col_item < 0:
    #                 to_add = 'X'
    #                 string += to_add
    #             else:
    #                 if (i,j) in self.piece_locations:
    #                     for piece in self.pieces:
    #                         if piece.x == i and piece.y == j:
    #                             string += piece.icon
    #                 else:
    #                     string += str("_")
    #             string += "|"
    #         if i == self.rows - 1:
    #             break
    #         string += "\n"
            
        
    #     print(string)
    #     print(x_axis)




#############################################################################
######## State
#############################################################################
class State:

    def __init__(self, assignments, domains, grid, rows, cols, num_pieces):
        #Create domains for each piece?
        #vars
        #csp-domains for each piece
        self.grid = grid
        self.rows = rows
        self.cols = cols

        self.assignments = assignments

        self.current_domains = domains

        self.threat_locations = set()
        self.num_pieces = num_pieces

        self.unassigned_vars = {
            "King": self.num_pieces[0],
            "Queen": self.num_pieces[1],
            "Bishop": self.num_pieces[2],
            "Rook": self.num_pieces[3],
            "Knight": self.num_pieces[4],
            "Ferz": self.num_pieces[5],
            "Princess": self.num_pieces[6],
            "Empress": self.num_pieces[7]
        }


    # def print_board_state(self, grid, rows, cols):
    #     pieces = [ ]

    #     for loc, piece_name in self.assignments.items():
    #         piece = create_piece(piece_name, loc)
    #         pieces.append(piece)
    #     Board(grid, rows, cols, pieces).print_board()
        

    #Check if assignment is complete 
    def is_complete(self):
        for count in self.unassigned_vars.values():
            if count > 0:
                return False
        return True
    
        


'''
Goes through all unassigned variables in the state and chooses by priority
returns a string
'''
def select_unassigned_variable(state):
    unassigned_vars_ = set()
    for piece_name, count in state.unassigned_vars.items():
        if count > 0:
            unassigned_vars_.add(piece_name)
    
    #Going down the list, we always return most constraining piece
    if "Queen" in unassigned_vars_:
        return "Queen"
    elif "Empress" in unassigned_vars_:
        return "Empress"
    elif "Princess" in unassigned_vars_:
        return "Princess"
    elif "Bishop" in unassigned_vars_:
        return "Bishop"
    elif "Rook" in unassigned_vars_:
        return "Rook"
    elif "Knight" in unassigned_vars_:
        return "Knight"
    elif "King" in unassigned_vars_:
        return "King"
    elif "Ferz" in unassigned_vars_:
        return "Ferz"
        

    

def order_domain_values(state, var, grid, rows, cols):
    #select the value which is least constraining
    # i.e, out of all the locations available in the domain, which location, 
    # when said piece is added, will lead to least threatened locations
    
    ordered_values = []
    
    for loc in state.current_domains[var]:
        actions = create_piece(var, loc).actions(grid, rows, cols) #try changing this to without creating piece
        order_val = {
            "location": loc,
            "threats": actions,
            "length": len(actions)
        }
        ordered_values.append(order_val)
    
    ordered_values.sort(key=lambda t:t["length"])
    
    return ordered_values
 
'''
Checks if value to be assigned can be consistent with assignment
i.e does the location lie in a threatened location and do the actions threaten any current piece locations
'''
def consistent(location, actions, state):
    
    #check if location is in threatened locations
    if location in state.threat_locations:
        return False
    
    #check if threatens positions of other pieces
    for each_loc in state.assignments.keys():
        if each_loc in actions:
            return False

    return True

'''
variable to add will choose a object with that variable name, and does not yet have location assigned
'''
def add_to_assignment(variable_to_change, value, actions, state):
    # print(variable_to_change, value, state.assignments)

    #Add to assignments
    state.assignments[value] = variable_to_change

    #reflect addition of pieces and threatened locations
    state.threat_locations.update(actions)


    state.unassigned_vars[variable_to_change] -= 1





#############################################################################
######## Implement Search Algorithm
#############################################################################
def search(rows, cols, grid, num_pieces):
    
    piece_types = ["King", "Queen", "Bishop", "Rook", "Knight", "Ferz", "Princess", "Empress"]
    
    piece_assignments = {

    }

    piece_domains = {
        
    }

    #Initialising Initial State
    for i in range(len(num_pieces)):
        if num_pieces[i] > 0:
            piece_domains[piece_types[i]] = set()
        
    
    #Initialising initial domains to be any location on the grid except obstacles
    for i in range(rows):
        for j in range(cols):
            for val in piece_domains.values():
                if grid[i][j] == -1:
                    continue
                else:
                    val.add((i,j))

    #---- ---- ---- Created initial assignments and initial domains
    #Initial state
    
    
    initial_state = State(piece_assignments, piece_domains, grid, rows, cols, num_pieces)

    

    
    res_state = backtrack(initial_state, grid, rows, cols)
    # res_state.print_board_state(grid, rows, cols)
    

    res_assignment = {

    }
    for loc, piece_name in res_state.assignments.items():
        x = col_to_txt(loc[1])
        y = loc[0]
        res_assignment[(x,y)] = piece_name
    return res_assignment
    





#Define backtracking algo
def backtrack(state, grid, rows, cols):
    if state.is_complete():
        return state
    
    var = select_unassigned_variable(state) #contains domain and assignment
    
    for each_value in order_domain_values(state, var, grid, rows, cols):
        #each_value is in the form (len(actions), loc, actions)
        loc = each_value["location"]
        actions = each_value["threats"]
        if consistent(loc, actions, state): #<-- check if value will result in being threatened or threaten others
            
            #add to assignment, updates threat locations and unassigned variables tracker
            add_to_assignment(var, loc, actions, state)

            #Inferences, check if domain is legal, remove all locations where pieces cannot be placed
            #Cannot place on obstacles(done as pre-process), cannot place at threatened locations
            # 
            # a copy of the domains, reduce domain size by deleting the threatened locations from all the domains 
            # + for every piece, populate threats from the location, those also have to be removed

            test_domains = copy.deepcopy(state.current_domains)
            
            prev_domains = state.current_domains

            proceed = True
            for piece_name, domain in test_domains.items():
                #remove current occupied position
                domain.discard(loc)
                
                #remove threatened locations that came from this assignment from all domains
                domain.difference_update(actions)

                #remove locations which will threaten this piece
                domain.difference_update(create_piece(piece_name, loc).actions(grid, rows, cols))

                #Check domains if the unassigned vars no longer have available actions
                if state.unassigned_vars[piece_name] > 0 and len(domain) == 0:
                    # print("Domain is empty for ", piece_type)
                    proceed = False
                    break

            if proceed: # if inferences not failure
                #Ad those inferences to CSP -> formalise the use of domains -> if ok then use the new copy as the domains, else discard
                state.current_domains = test_domains
                
                result = backtrack(state, grid, rows, cols)
                
                if result: #<-- check if return is none, if not none, check state consistent and constraint satisfied
                    return result
                
                #remove inferences from CSP????
                state.current_domains = prev_domains
                
            
            #Unassign the variable, delete the assignment from state, remove the threats
            
            state.unassigned_vars[var] += 1
            del state.assignments[loc]
            state.threat_locations.difference_update(actions)
            
    
    return None
            




#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
def parse(testcase):
    handle = open(testcase, "r")

    get_par = lambda x: x.split(":")[1]
    rows = int(get_par(handle.readline()))
    cols = int(get_par(handle.readline()))
    grid = [[0 for j in range(cols)] for i in range(rows)]

    num_obstacles = int(get_par(handle.readline()))
    if num_obstacles > 0:
        for ch_coord in get_par(handle.readline()).split():  # Init obstacles
            r, c = from_chess_coord(ch_coord)
            grid[r][c] = -1
    else:
        handle.readline()
    
    piece_nums = get_par(handle.readline()).split()
    num_pieces = [int(x) for x in piece_nums] #List in the order of King, Queen, Bishop, Rook, Knight

    return rows, cols, grid, num_pieces

def add_piece( comma_seperated):
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [(r,c), piece]

#Returns row and col index in integers respectively
def from_chess_coord( ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)

### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# To return: Goal State which is a dictionary containing a mapping of the position of the grid to the chess piece type.
# Chess Pieces (String): King, Queen, Knight, Bishop, Rook (First letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Goal State to return example: {('a', 0) : Queen, ('d', 10) : Knight, ('g', 25) : Rook}
def run_CSP():
    testcase = sys.argv[1] #Do not remove. This is your input testfile.
    rows, cols, grid, num_pieces = parse(testcase)
    goalstate = search(rows, cols, grid, num_pieces)
    return goalstate #Format to be returned

# rows, cols, grid, num_pieces = parse("CSP2.txt")
# goalstate = search(rows, cols, grid, num_pieces)
# # cProfile.run("search(rows, cols, grid, num_pieces)")
# print(goalstate)