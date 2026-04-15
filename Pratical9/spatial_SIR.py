import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100, 100))
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.show()

beta = 0.3
gamma = 0.05
time = 100

for t in range(time):
    infected_indices = np.argwhere(population == 1)#try to find where the infextions are
    for infected in infected_indices:
        i, j = infected[0], infected[1]
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):#find the neighbers
                if x == i and y == j:
                    continue#not himself
                if 0 <= x < 100 and 0 <= y < 100:#make sure in the figur
                    if population[x, y] == 0:
                        if np.random.random() < beta:
                            population[x, y] = 1
    for infected in infected_indices:
        i, j = infected[0], infected[1]
        if np.random.random() < gamma:
            population[i, j] = 2
    if t % 10 == 0:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time step {t}')
        plt.show()