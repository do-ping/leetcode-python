from typing import List, Generator


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # if rowIndex == 0:
        #     return [1]
        # elif rowIndex == 1:
        #     return [1, 1]
        #
        # previous: List[int] = [1, 1]
        # for row_number in range(2, rowIndex + 2):
        #     row = []
        #     for j in range(row_number):
        #         if j == 0 or j == row_number - 1:
        #             row.append(1)
        #         else:
        #             row.append(previous[j - 1] + previous[j])
        #
        #     previous = row
        #
        # return previous
        row = [1]
        for k in range(1, rowIndex + 1):
            row.append(int(row[-1] * (rowIndex - k + 1) / k))
        return row


if __name__ == "__main__":
    s = Solution()
    for data in [(4, [1, 4, 6, 4, 1]), (1, [1, 1]), (0, [1]), (3, [1, 3, 3, 1])]:
        row_index = data[0]
        want = data[1]
        got = s.getRow(row_index)

        assert want == got, f"\nrow_index={row_index}\nwant={want}\ngot={got}\n"
