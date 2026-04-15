import numpy as np
import matplotlib.pyplot as plt
N = 10000
beta = 0.3
gamma = 0.05
I = 1
S = N-I
R = 0
time = 1000
I_list=[I]
S_list=[S]
R_list=[R]
for t in range(time):
    infection = beta*(I/N)
    I_new = np.random.binomial(S,infection)
    R_new = np.random.binomial(I,gamma)
    S -= I_new
    I +=I_new - R_new
    R += R_new
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)
plt . figure ( figsize =(6,4),dpi=150)
time = list(range(time + 1))
plt.plot(time, S_list,label='Susceptible (S)', color='blue')
plt.plot(time, I_list,label='Infected (I)', color='red')
plt.plot(time, R_list,label='Recovered (R)', color='green')
plt.xlabel('Time Steps')
plt.ylabel('Number of People')
plt.title('Stochastic SIR Model Simulation (Basic)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("infection.png")#I try to use the code in guidence, but it can't work.So I change it.
plt.show()
