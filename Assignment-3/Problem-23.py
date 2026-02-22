def combinationSum2(candidates, target):
    candidates.sort()
    res = []

    def backtrack(start, path, total):
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return

        prev = -1
        for i in range(start, len(candidates)):
            if candidates[i] == prev:
                continue
            backtrack(i+1, path + [candidates[i]], total + candidates[i])
            prev = candidates[i]

    backtrack(0, [], 0)
    return res