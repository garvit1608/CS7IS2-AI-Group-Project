from  algorithms import backtracking, hillclimbing, genetic_algorithm,baseline
import numpy as np
from matplotlib import pyplot as plt

N_queen=[]
Hill_time=[]
Genetic_time=[]
backtracking_time=[]
baseline_time=[]

for i in range(4,6):
    N_queen=np.append(N_queen,i)
    Hill_time= np.append(Hill_time,hillclimbing.main(i))
    Genetic_time= np.append(Genetic_time,genetic_algorithm.main(i))
    backtracking_time= np.append(backtracking_time,backtracking.main(i))
    baseline_time = np.append(baseline_time,baseline.main(i))


plt.plot(N_queen,Hill_time,label="Hill Climbing")
plt.plot(N_queen,Genetic_time,label="Genetic algorithm")
plt.plot(N_queen,backtracking_time,label="Back tracking")
plt.plot(N_queen,baseline_time,label="Baseline algorithm")
plt.xlabel('Number of Queens')
plt.ylabel('Time taken in milliseconds')
plt.legend(loc='upper right')
plt.title('Algorithm performance')
plt.show()