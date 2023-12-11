from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # rows_n = len(triangle)
        # if rows_n == 0:
        #     return 0
        #
        # if rows_n == 1:
        #     return triangle[0][0]
        #
        # for row_n in range(1, rows_n):
        #     for cell_n in range(row_n + 1):
        #         if cell_n == 0:
        #             triangle[row_n][cell_n] = (
        #                 triangle[row_n][cell_n] + triangle[row_n - 1][0]
        #             )
        #         elif cell_n == len(triangle[row_n]) - 1:
        #             triangle[row_n][cell_n] = (
        #                 triangle[row_n][cell_n] + triangle[row_n - 1][-1]
        #             )
        #         else:
        #             triangle[row_n][cell_n] = min(
        #                 triangle[row_n][cell_n] + triangle[row_n - 1][cell_n],
        #                 triangle[row_n][cell_n] + triangle[row_n - 1][cell_n - 1],
        #             )
        #
        # return min(triangle[-1])
        below_row = triangle[-1]
        n = len(triangle)
        for row_n in reversed(range(n - 1)):
            curr_row = []
            for col in range(row_n + 1):
                smallest = min(below_row[col], below_row[col + 1])
                curr_row.append(triangle[row_n][col] + smallest)
            below_row = curr_row
        return below_row[0]


if __name__ == "__main__":
    s = Solution()
    for data in [
        ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
        ([[-10]], -10),
        ([[-1], [2, 3], [1, -1, -3]], -1),
    ]:
        triangle = data[0]
        want = data[1]
        got = s.minimumTotal(triangle)

        assert want == got, f"\ntriangle={triangle}\nwant={want}\ngot={got}\n"
