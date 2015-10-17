import pygame
class Board:
    '''I create an instance of a chessboard for the N-queens problem.
       
       Author    : Subimal Deb (subimal.deb@gmail.com)
       Date      : 3rd January, 2013

       Note:    This code is to be reproduced only with the author's permission. 
                If used, cite it as the author's work for implementation of the 
                backtracking algorithm.
    '''
    #------------------------------------------------------------------------------#
    def __init__(self,N):
        '''
        I initialize the attributes:
            size        (int)   size of the board
            queen       (list)  columns where the queens are placed. 
                                None if the queen is not placed.
                                n-th element corresponds to the n-th queen.
            freecols    (list)  available columns for the queens. 
                                The available columns for the n-th queen
                                depends on the location of the (n-1)-th queen.
            sols        (list)  The list of solutions. It is populated as the 
                                problem is solved. 
                                The i-th solution is a list of integers. The j-th 
                                element in this list is the column where the queen 
                                in the j-th row is placed.
        '''
        #--------------------------------------------------------------------------#
        self.size=N
        self.queen=[None]*N 
        self.freecols=[[]]*N #map(lambda x: [], range(N))
        self.sols=[]
    #------------------------------------------------------------------------------#
    
    #------------------------------------------------------------------------------#
    def Queen_free(self,qno):
        '''
            I find the available positions of the queen in row qno and
            update the attribute freecols.

            Input: 
            qno     (int)   The row where a queen is to be placed.

            Output:         Nothing.
        '''
        #--------------------------------------------------------------------------#
        queensat=[]
        self.freecols[qno]=[]
        for i in range(self.size):
            if self.queen[i]!=None:
                queensat.append( (self.queen[i],i) )
        rowcoords=zip( range(self.size), [qno]*self.size )
        for xi,yi in rowcoords:
            attacked=None
            for xj,yj in queensat:
                slopeinv=abs(float(xi-xj)/float(yi-yj))
                if slopeinv==0.0 or slopeinv==1.0:
                    attacked=True
            if attacked==None:
                self.freecols[qno].append(xi)
    #------------------------------------------------------------------------------#

    #------------------------------------------------------------------------------#
    def PutQueen(self, qno):
        '''
            I put the queen in an available column in row qno.
            If such a column is available, I put the next 
            queen till all queens are placed.
            If no column is available, I backtrack to the 
            last movable queen and continue to place the
            remaining queens.

            Input: 
            qno     (int)   The row where a queen is to be placed.

            Output:
            True            When a solution is found or when all 
                            possibilities are exhausted.

            This is the heart of this code. Backtracking is done 
            here only when a solution cannot be found.
            Remember:   The n-th queen lives on the n-th row. 
                        She can only move along that row or leave 
                        the battlefield.
        '''
        #--------------------------------------------------------------------------#
        if self.queen[qno]!=None:
            # If this queen exists on the board, I came here backtracking.
            #   I will move this queen to the next available position. 
	    # All the queens that were placed after this queen will be
	    # removed.
            for i in range(qno+1,self.size):
                self.queen[i]=None
                self.freecols[i]=[]
        else:
            # This queen was never here. Let's find out where she can stay.
            self.Queen_free(qno)

        if len(self.freecols[qno])>0:
            #   This queen has at least one place on the board. 
	    # She goes to the first available position and the 
	    # remaining ones are listed as her freecols
            self.queen[qno]=self.freecols[qno][0]
            del self.freecols[qno][0]

            if self.queen.count(None)>0:
                # More queens to come. Fetch them.
                qno=qno+1
                self.PutQueen(qno)

            if self.queen.count(None)==0:
		# No more queens to come. We found a solution. 
		#sol= map(lambda x: self.queen[x], range(self.size))
                sol=[]
                for each in range(self.size):
                    sol.append(self.queen[each])

                if sol not in self.sols:
                    # We add it to the list of solutions if we did 
		    # not have this earlier.
                    self.sols.append(sol)

        elif len(self.freecols[qno])==0 and self.queen[qno]!=None:
            # This queen has nowhere else to go but she has to move. 
	    # Remove her from her current location.
            self.queen[qno]=None

            if self.freecols[0]==[]:
                # If this queen was the first one to arrive and has 
		# no other place to go, we have exhausted all the 
		# solutions.
                return True
            elif qno==0:
                # This queen was the first to occupy a place on the 
		# board and can shift. Move her.
                self.PutQueen(qno)
            if qno>0:
                # This is not the oldest queen in the battlefield. 
		# She has no place to go to. Her predecessor must 
		# move to let her shift.
                qno=qno-1
                self.PutQueen(qno)
    #------------------------------------------------------------------------------#

def Progress(board):
    '''
    I'll show the progress of the computation if you choose to.
    '''
    #--------------------------------------------------------------------------#
    from sys import stdout
    stdout.flush()
    print ("%6d")%(len(board.sols)), "solutions found for ", \
        ("%2d-Queens problem.")%(board.size),'\r',
#------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
def SolveNQueens(size, ShowProgress=False):
    '''
        I find all possible solutions for a board of given size.

        Input: 
        size            (int)       The size of the board.
        ShowProgress    (boolean)   [optional] False by default.
                                    I'll show the progress of my 
				    computation if you choose to 
				    set it to True.

        Output:
        board           (class)     The board instance with all the 
	                            available solutions in its sols 
				    attribute.

        Steps:
        1.  I initialize an instance of the board.
        2.  I place a queen and thereby find a solution. 
            (If it is the first time, I place a queen 
            on the first column.)
        3.  When a solution is found, I look for further solutions by 
            shifting a queen to another available position. The 
            queen is chosen starting from the last queen placed.
            If such a queen is found, I go to step 2.
        4.  I will not find a queen in step 3 if the first queen I 
            placed on the board has moved to the last column and no 
            more solutions can be found.
    '''
    #------------------------------------------------------------------------------#
    #from nqgui import init_board_im, draw_board
    board=Board(size)
    board.PutQueen(0)
    #if ShowProgress: 
    #    [surface, ball, sparams] = init_board_im(board.size)
    if size==1:
        if ShowProgress: Progress(board)
    lastmovable=board.size-1
    while board.freecols.count([])<len(board.freecols):
        lastmovable=board.size-1
        while board.freecols[lastmovable]==[]:
            lastmovable=lastmovable-1
        board.PutQueen(lastmovable)
        if ShowProgress: 
	    Progress(board)
            #if len(board.sols)>=1: draw_board(surface, ball, sparams, board.sols[-1])
    if ShowProgress: print
    return board
    #------------------------------------------------------------------------------#
def PrintBoards(board):
    sols=board.sols
    print
    print r"\chapter{"+str(board.size)+" Queens}"
    for each in sols:
        print r"Solution "+str(sols.index(each)+1)
        print r"\begin{verbatim}"
        print "-"*(2*len(each)+1)
        for qp in each:
            r=["0"]*len(each)
            r[qp]="1"
            r='|'.join(r)
            print "|"+r+"|"
        print "-"*(2*len(each)+1)
        print r"\end{verbatim}"
    print
		
#----------------------------------------------------------------------------------#
#       The end-user code                                                          #
#----------------------------------------------------------------------------------#
for N in range(1,12):
    b=SolveNQueens(N, ShowProgress=False)
    Progress(b)
    print
    #if sp: pygame.quit()
    #PrintBoards(b)
    #print ("%6d")%(len(b.sols)), "solutions found for ", \
    #  ("%2d-Queens problem.")%(b.size)
