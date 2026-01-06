class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows, num_cols = len(board), len(board[0])
        visited = [[False for c in range(num_cols)] for r in range(num_rows)]
        def get_neighbor(row, col):
            neighbors = []
            # i-1, j
            # i, j+1
            # i+1, j
            # i, j-1
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            for i in range(len(delta_row)):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    if not visited[neighbor_row][neighbor_col]:
                        neighbors.append((neighbor_row, neighbor_col))
            return neighbors
        
        def dfs(i, path, row, col):
            current_path_word = "".join(path)
            if i == len(word)-1 and current_path_word == word:
                return True
            
            found = False
            visited[row][col] = True
            for nei_row, nei_col in get_neighbor(row, col):
                if board[nei_row][nei_col] == word[i+1]:
                    path.append(board[nei_row][nei_col])
                    found = found or dfs(i+1, path, nei_row, nei_col)
                    path.pop()

                    if found:
                        return True
            visited[row][col] = False
            return found
        
        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] != word[0]:
                    continue
                if dfs(0, [board[r][c]], r, c):
                    return True
        return False

