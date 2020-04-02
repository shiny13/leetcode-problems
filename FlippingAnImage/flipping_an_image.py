class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        output = []
        for row in A:
            _row = []
            length = len(row) - 1
            while length >= 0:
                _row.append(row[length])
                length -= 1
            length = 0
            while length < len(_row):
                if _row[length] == 0:
                    _row[length] = 1
                elif _row[length] == 1:
                    _row[length] = 0
                length += 1
            output.append(_row)
        return output