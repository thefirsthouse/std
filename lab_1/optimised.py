def find_best_partition(N):
    best_d = 1
    for d in range(2, int(N**0.5) + 1):  # проверяем делители до корня
        if N % d == 0:
            best_d = max(best_d, d, N // d)  # берем максимальный возможный делитель
    
    A = best_d
    B = N - best_d
    print(A, B, "Аненко Василий Сергеевич, 020303-АИСа-о24")

N = int(input())
find_best_partition(N)
