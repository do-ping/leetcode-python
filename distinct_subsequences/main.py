class Solution:
    def recursion_cache(self, s: str, t: str) -> int:
        cache = {}

        def func(i: int, j: int) -> int:
            M, N = len(s), len(t)

            if i == M or j == N or M - i < N - j:
                return int(j == len(t))

            if (i, j) in cache:
                return cache[i, j]

            answer = func(i + 1, j)

            if s[i] == t[j]:
                answer += func(i + 1, j + 1)

            cache[i, j] = answer
            return answer

        return func(0, 0)

    def iterative_dynamic(self, s: str, t: str) -> int:
        M, N = len(s), len(t)

        dp: list[list[int]] = [[0 for i in range(N + 1)] for j in range(M + 1)]

        for j in range(N + 1):
            dp[M][j] = 0

        for i in range(M + 1):
            dp[i][N] = 1

        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]

                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]

    def iterative_dynamic_space_efficient(self, s: str, t: str) -> int:
        M, N = len(s), len(t)

        dp: list[int] = [0 for j in range(N)]

        for i in range(M - 1, -1, -1):
            prev = 1

            for j in range(N - 1, -1, -1):
                old_dpj = dp[j]

                if s[i] == t[j]:
                    dp[j] += prev

                prev = old_dpj

        return dp[0]

    def numDistinct(self, s: str, t: str) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()
    for data in [("rabbbit", "rabit", 3), ("babgbag", "bag", 5)]:
        s = data[0]
        t = data[1]
        want = data[2]
        got1 = solution.recursion_cache(s, t)
        got2 = solution.iterative_dynamic(s, t)
        got3 = solution.iterative_dynamic_space_efficient(s, t)
        # got1 = solution.numDistinct(s, t)

        assert want == got1 == got2 == got3, (
            f"\ns={s}\nt={t}want={want}\n" f"got1={got1}\ngot2={got2}\n" f"got3={got3}"
        )
