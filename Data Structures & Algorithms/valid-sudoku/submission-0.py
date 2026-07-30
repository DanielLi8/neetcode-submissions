def validRow(row :List[str]) -> bool:
    dictRow= {}

    for num in row:
        dictRow[num] = dictRow.get(num,0) +1
        if num == '.':
            continue
        if dictRow[num]>1:
            return False
    return True


def validSubBox(box: List[List[str]])-> bool:
    dictRow= {}
    for rows in box:
        for subRow in rows:
            dictRow[subRow] = dictRow.get(subRow,0) +1
            if subRow == '.':
                continue
            if dictRow[subRow]>1:
                return False
    return True

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
        for row in range(0,len(board),3):
            if validRow(board[row]) and validRow(board[row+1])and validRow(board[row+2]) and validRow(res[row]) and validRow(res[row+1])and validRow(res[row+2]):
                for column in range(0,len(board)-3,3):
                    firstSubRow = board[row][column:column+3]
                    secondSubRow = board[row+1][column:column+3]
                    thirdSubRow = board[row+2][column:column+3]

                    subBox = [firstSubRow , secondSubRow , thirdSubRow]
                    print(subBox)
                    if not validSubBox(subBox):
                       return False
            else:
                return False
        
                
                    
        return True



