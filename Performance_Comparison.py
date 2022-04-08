from  algorithms import backtracking, hillclimbing, genetic_algorithm
import numpy as np
from matplotlib import pyplot as plt

Hill_time= hillclimbing.main()
Genetic_time= hillclimbing.main()
backtracking_time= backtracking.main()

Time_Array=[Hill_time,backtracking_time,Genetic_time]
Algo_Name=["HillClimbing",'Backtracking','Genetic_algorithm']

plt.bar(Algo_Name,Time_Array)
plt.xlabel('Algorithms')
plt.ylabel('Time Taken in millisecond')
#plt.legend(loc='upper right')
plt.title('Algorithm performance')
plt.show()