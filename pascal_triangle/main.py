from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []

        result: List[List[int]] = []
        for row_number in range(1, numRows + 1):
            if row_number == 1:
                result.append([1])
            elif row_number == 2:
                result.append([1, 1])
            else:
                row = []
                for j in range(row_number):
                    if j == 0 or j == row_number - 1:
                        row.append(1)
                    else:
                        _sum = result[row_number - 2][j - 1] + result[row_number - 2][j]
                        row.append(_sum)

                result.append(row)

        return result


if __name__ == "__main__":
    s = Solution()
    for data in [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
    ]:
        num_rows = data[0]
        want = data[1]
        got = s.generate(num_rows)

        assert want == got, f"\nnum_rows={num_rows}\nwant={want}\ngot={got}\n"
