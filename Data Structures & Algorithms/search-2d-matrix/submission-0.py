class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1

        while t <= b:
            i = (t + b) // 2

            if matrix[i][-1] < target:
                t = i + 1
            elif matrix[i][0] > target:
                b = i - 1
            else:
                break
        else:
            return False

        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            j = (l + r) // 2

            if matrix[i][j] == target:
                return True

            if matrix[i][j] > target:
                r = j - 1
            else:
                l = j + 1

        return False