def goemt_progres(b_first, q, n_user):
    b_prev = b_first
    n = 1
    for i in range(n,n_user):
        b_cur = b_prev * q
        b_prev = b_cur
        n += 1
        yield b_cur


test_1 = goemt_progres(1,7,5)
print(next(test_1))
print(next(test_1))
print(next(test_1))
print(next(test_1))

