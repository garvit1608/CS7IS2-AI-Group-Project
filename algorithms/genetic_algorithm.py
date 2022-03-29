import random
#Based on Darwin's Survival of The Fittest 
#Here Fitness is taken as the Pair of Non Attacking Queens arrangement
def random_space(size): 
    return [ random.randint(1, num_queen) for _ in range(num_queen) ]

def pairOfNonAttackingQueens(arrangement): #Find the fittest arrangement
    horizontal_collisions = sum([arrangement.count(queen)-1 for queen in arrangement])/2
    diagonal_collisions = 0

    n = len(arrangement)
    left_diagonal = [0] * 2*n
    right_diagonal = [0] * 2*n
    i=0
    while i<=n-1:
        left_diagonal[i + arrangement[i] - 1] += 1
        right_diagonal[len(arrangement) - i + arrangement[i] - 2] += 1
        i=i+1

    diagonal_collisions = 0
    i=0
    while i<=((2*n-1) -1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i]-1
        diagonal_collisions += counter / (n-abs(i-n+1))
        i=i+1
    
    return int(maxPairOfNonAttackingQueens - (horizontal_collisions + diagonal_collisions)) #28-(2+3)=23

def probability(arrangement, pairOfNonAttackingQueens):
    return pairOfNonAttackingQueens(arrangement) / maxPairOfNonAttackingQueens

def random_pick(setOfAllSolutions, probabilities):
    populationWithProbabilty = zip(setOfAllSolutions, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(setOfAllSolutions, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"
        
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
    probabilities = [probability(n, pairOfNonAttackingQueens) for n in setOfAllSolutions]
    i=0
    while i<=len(setOfAllSolutions) - 1:
        x = random_pick(setOfAllSolutions, probabilities) 
        y = random_pick(setOfAllSolutions, probabilities) 
        child = reproduce(x, y) 
        if random.random() < alter_probability:
            child = alter(child)
        print_arrangement(child)
        new_SetOfSolutions.append(child)
        if pairOfNonAttackingQueens(child) == maxPairOfNonAttackingQueens: break
        i=i+1
    return new_SetOfSolutions

def print_arrangement(pos): #For every position in each fitness (Pair of non-attacking queens), show
    print("Position = {},  Fitness = {}"
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
    num_queen = int(input("Enter Number of Queens: ")) #say N = 8
    maxPairOfNonAttackingQueens = (num_queen*(num_queen-1))/2  # 8*7/2 = 28
    setOfAllSolutions = [random_space(num_queen) for _ in range(100)]
    
    generation = 1

    while not maxPairOfNonAttackingQueens in [pairOfNonAttackingQueens(pos) for pos in setOfAllSolutions]:

        setOfAllSolutions = generate_solutionSet(setOfAllSolutions, pairOfNonAttackingQueens)

        generation += 1
    position_ = []

    for pos in setOfAllSolutions:
        if pairOfNonAttackingQueens(pos) == maxPairOfNonAttackingQueens:
            print("");
            print("One of the solutions: ")
            position_ = pos
            print_arrangement(pos)
            
    board = []
    
    for x in range(num_queen):
        board.append(["0"] * num_queen)
        
    for i in range(num_queen):
        board[num_queen-position_[i]][i]="1"
            

    def print_board(board): #Show the board
        print("This is board")
        for row in board:
            print (" ".join(row))
            
    print()
    print_board(board)
            