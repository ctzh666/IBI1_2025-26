import numpy as np
import matplotlib.pyplot as plt

N = 10000
beta = 0.3
gamma = 0.05
V = [i/100.0 for i in range(0, 101, 10)]
time = 1000
plt.figure(figsize=(10, 6), dpi=150)

for idx, va in enumerate(V):
    vaccinated = int(N * va)
    S = max(0, N - vaccinated - 1)
    I = 1
    R = 0
    I_list = [I]
    for t in range(time):
        infection_prob = beta * (I / N)
        if S > 0 and infection_prob > 0:
            I_new = np.random.binomial(S, infection_prob)
        else:
            I_new = 0
        if I > 0:
            R_new = np.random.binomial(I, gamma)
        else:
            R_new = 0
        S -= I_new
        I += I_new - R_new
        R += R_new
        S = max(S, 0)
        I = max(I, 0)
        I_list.append(I)
    plt.plot(range(len(I_list)), I_list, 
             label=f'Vaccinated {int(va*100)}%',
             linewidth=1.5)
plt.xlabel('Time Steps')
plt.ylabel('Number of Infected People')
plt.title('Impact of Vaccination Coverage on Disease Spread\n(Stochastic SIR Model, 10,000 Population)')
plt.legend(title='Vaccination Rate', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("SIR_vaccination_impact.png", dpi=150)
plt.show()


