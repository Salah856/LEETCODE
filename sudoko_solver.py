class BoardState:
    def __init__(self):
        self.cells = [set() for _ in range(9)]
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
	
    def init_board(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    self.set_board(i, j, val)  
        
    def valid_step(self, i, j, val):
        cell_id = i // 3 * 3 + j // 3
        in_col = val in self.cols[j]
        in_row = val in self.rows[i]
        in_cell = val in self.cells[cell_id]
        return (in_col or in_row or in_cell) == False
        
    def set_board(self, i, j, val):
        cell_id = i // 3 * 3 + j // 3
        self.cols[j].add(val)
        self.rows[i].add(val)
        self.cells[cell_id].add(val)
            
    def clear_board(self, i, j, val):
        cell_id = i // 3 * 3 + j // 3
        self.cols[j].remove(val)
        self.rows[i].remove(val)
        self.cells[cell_id].remove(val)

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        board_state = BoardState()
        board_state.init_board(board)

        def backtracking(i, j, board_state):
            if i == len(board[0]):
                i = 0
                j += 1
            
            if j == len(board):
                return True
            
            if board[i][j] != '.':
                return backtracking(i+1, j, board_state)

            for intended in range(1, 10):
                if board_state.valid_step(i, j, intended):
                    board[i][j] = str(intended)
                    board_state.set_board(i, j, intended)
                    res = backtracking(i+1, j, board_state)
                    
                    if res:
                        return True
                    
                    board_state.clear_board(i, j, intended)
                    board[i][j] = '.'

            return False
        
        backtracking(0, 0, board_state)
        # return
