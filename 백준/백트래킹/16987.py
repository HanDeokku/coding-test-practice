n = int(input())

eggs = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def back(depth, egg, cnt):
    global answer
    if depth == n:
        answer = max(answer, cnt)
        return

    if egg[depth][0] <= 0:
        back(depth + 1, egg, cnt)
        return

    broke = False
    for i in range(n):
        if i == depth or egg[i][0] <= 0:
            continue

        p_a, p_b = egg[depth]
        f_a, f_b = egg[i]

        egg[depth][0] -= f_b
        egg[i][0] -= p_b

        broken = 0
        if egg[depth][0] <= 0:
            broken += 1
        if egg[i][0] <= 0:
            broken += 1

        back(depth + 1, egg, cnt + broken)

        egg[depth][0] = p_a
        egg[i][0] = f_a

        broke = True

    if not broke:
        back(depth + 1, egg, cnt)

back(0, eggs, 0)

print(answer)