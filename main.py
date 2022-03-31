from  algorithms import backtracking, hillclimbing, genetic_algorithm

if __name__ == '__main__':
    print(
        '''
        1. Backtracking
        2. Hill Climbing
        3. Genetic Algorithm
        '''
    )
    choice = int(input("Which algorithm you want to run? \t"))

    if choice == 1:
        backtracking.main()
    elif choice == 2:
        hillclimbing.main()
    elif choice == 3:
        genetic_algorithm.main()
    else:
        print("Wrong input")

