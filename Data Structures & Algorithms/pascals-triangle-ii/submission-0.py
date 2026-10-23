class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        before_row = [1, 1]

        while rowIndex > 1:
            new_row = [1, 1]

            for i in range(len(before_row) - 1):
                new_row.insert(-1, before_row[i] + before_row[i + 1])

            before_row = new_row
            rowIndex -= 1

        return before_row