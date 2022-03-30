import random
from itertools import permutations
#Based on Darwin's Survival of The Fittest 
#Here Fitness is taken as the Pair of Non Attacking Queens arrangement
def random_space(num_queen):
    new_list = []
    for i in range(num_queen):
        new_list.append(random.randint(1, num_queen))
    return new_list

def pairOfNonAttackingQueens(arrangement): #Find the fittest arrangement
    row_attacks = 0
    for position in arrangement:
        row_attacks += arrangement.count(position)-1
    row_attacks /= 2    
    arrangement_len = len(arrangement)
    left_diagonal = [0] * 2 * arrangement_len
    right_diagonal = [0] * 2 * arrangement_len
    i=0
    while i<=arrangement_len-1:
        left_diagonal[i + arrangement[i] - 1] += 1
        right_diagonal[len(arrangement) - i + arrangement[i] - 2] += 1
        i=i+1

    diagonal_attacks = 0
    i=0
    while i<=((2*arrangement_len-1) -1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i]-1
        diagonal_attacks += counter / (arrangement_len-abs(i-arrangement_len+1))
        i=i+1
    
    nonAttackingPositions = int(maxPairOfNonAttackingQueens - (row_attacks + diagonal_attacks))
    return  nonAttackingPositions



def random_solution(setOfAllSolutions, probabilities):
    total_prob = 0
    for solution, probability in zip(setOfAllSolutions, probabilities):
        total_prob += probability
    r = random.uniform(0, total_prob)
    end = 0
    for solution, probability in zip(setOfAllSolutions, probabilities):
        if end + probability >= r:
            return solution
        end += probability
        
def reproduce(x, y): #Re-arrange the position in the matrix
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]

def alter(x):  
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x

def generate_solutionSet(setOfAllSolutions, pairOfNonAttackingQueens): #Populate or generate the list of solutions
    alter_probability= 0.03
    new_SetOfSolutions = []
    probabilities = []
    for n in setOfAllSolutions:
        probabilities.append(pairOfNonAttackingQueens(n) / maxPairOfNonAttackingQueens)
    
    i=0
    while i<=len(setOfAllSolutions) - 1:
        x = random_solution(setOfAllSolutions, probabilities) 
        y = random_solution(setOfAllSolutions, probabilities) 
        child = reproduce(x, y) 
        if random.random() < alter_probability:
            child = alter(child)
        print_arrangement(child)
        new_SetOfSolutions.append(child)
        if pairOfNonAttackingQueens(child) == maxPairOfNonAttackingQueens: break
        i=i+1
    return new_SetOfSolutions

def print_arrangement(pos): #For every position in each fitness (Pair of non-attacking queens), show
    print("Position = {},  Fitness Score = {}"
        .format(str(pos), pairOfNonAttackingQueens(pos)))
    matrix = [] 
    for i in range(len(pos)):          # A for loop for row entries 
        a =[] 
        for j in range(len(pos)):      # A for loop for column entries 
            if j+1 == pos[i]:
                entry=1
                a.append(entry)
            else:
                entry=0
                a.append(entry)
        matrix.append(a) 
    print(matrix)
    for element in matrix:
        print(''.join(str(element)))
    #print_board(matrix)

if __name__ == "__main__":
    num_queen = int(input("Enter the Number of Queens to be placed on the board: ")) 
    maxPairOfNonAttackingQueens = (num_queen*(num_queen-1))/2  
    setOfAllSolutions = []
    for i in range(100):
        setOfAllSolutions.append(random_space(num_queen))
         
    while [pairOfNonAttackingQueens(pos) for pos in setOfAllSolutions].count(maxPairOfNonAttackingQueens) <1:
        setOfAllSolutions = generate_solutionSet(setOfAllSolutions, pairOfNonAttackingQueens)
        

    final_position = []

    for pos in setOfAllSolutions:
        if pairOfNonAttackingQueens(pos) == maxPairOfNonAttackingQueens:
            print("")
            new_list =[list(p) for p in permutations(pos)]
            for item in new_list:
                if pairOfNonAttackingQueens(item) == maxPairOfNonAttackingQueens:
                    print("One solution is: ")
                    final_position = item
                    print_arrangement(item)
            
    board = []
    
    for x in range(num_queen):
        board.append(["0"] * num_queen)
        
    for i in range(num_queen):
        board[num_queen-final_position[i]][i]="1"
            

    def print_board(board): #Show the board
        print("This is board")
        for row in board:
            print (" ".join(row))
            
    print_board(board)
            