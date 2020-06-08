import random


N=1000


n_list = []
for i in range (N):
    get_random = random.randint((-N)*10,N*10)
    n_list.append(get_random)

print(n_list)
for j in range(N):
    for i in range(j,0,-1):
        if n_list[i-1] > n_list[i]:
            n_list[i],n_list[i-1]=n_list[i-1],n_list[i]
        else:
            break

print(n_list)