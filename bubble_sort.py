import random


N=1000
n_list = []


for i in range (N):
    get_random = random.randint((-N)*10,N*10)
    n_list.append(get_random)

for  j in range(N-1):
    for i in range(N-1-j):
        sorted_number = n_list[i]
        compared_number = n_list[i+1]
        if sorted_number >= compared_number:
            n_list[i],n_list[i+1] = n_list[i+1],n_list[i]




print(n_list)



