# Simple Genetic Algorithm
# Author : Teuku Rizky Noviandy
# 2020

import random
import matplotlib.pyplot as plt

data = [10,30,70,90,40,50,20,10,50,90,20,10,30,20]

pop_size = 50

# Generate initial population

initial_population =[[] for _ in range(pop_size)]

best_fitness = []

for n in range(pop_size):
    for n_gen in range(len(data)):
        rand = random.randint(0,1)
        initial_population[n].append(rand)

# Print Output

iteration = 500

x = 0
while x in range(iteration):
    print('=======ITERASI KE {}======='.format(x+1))

    counter = 1
    print("\n-------Initial Population-------\n")
    for item in initial_population:
        print('Kromosom', counter, ':', item)
        counter +=1

    # Calculate fitness for each individual

    fitness_value = [[] for _ in range(pop_size)]
    save_fitness = [[] for _ in range(pop_size)]

    for n_kromosom in range(pop_size):
        for n_gen in range(len(data)):
            if initial_population[n_kromosom][n_gen] == 1:
                calc_fitness = data[n_gen]
                save_fitness[n_kromosom].append(calc_fitness)
            else:
                save_fitness[n_kromosom].append(0)
    z = 0
    for item in save_fitness:
        fit = sum(item)
        fitness_value[z].append(fit)
        z +=1

    counter = 1
    print("\n-------Calculate Fitness-------\n")
    for item in fitness_value:
        print('Fitness Kromosom', counter, ':', item)
        counter += 1

    #Parents selection

    rand_parent1 = random.randint(0, pop_size-1)
    rand_parent2 = random.randint(0, pop_size-1)

    while rand_parent2 == rand_parent1:
        rand_parent2 = random.randint(0, pop_size-1)

    parent_1 = initial_population[rand_parent1]
    parent_2 = initial_population[rand_parent2]

    print("\n-------Selection Result-------\n")
    print('Parent 1 adalah kromosom', rand_parent1+1)
    print('Parent 2 adalah kromosom', rand_parent2+1)

    #Crossover

    gen_size = len(initial_population[0])

    offspring_1 = parent_1[0:7] + parent_2[7:14]
    offspring_2 = parent_1[7:14] + parent_2[0:7]

    save_offspring1 = [] 
    save_offspring2 = [] 

    for n_gen in range(14):
        if offspring_1[n_gen] == 1:
            calc_fitness = data[n_gen]
            save_offspring1.append(calc_fitness)

    for n_gen in range(14):
        if offspring_2[n_gen] == 1:
            calc_fitness = data[n_gen]
            save_offspring2.append(calc_fitness)

    fitness_offspring_1 = [sum(save_offspring1)]
    fitness_offspring_2 = [sum(save_offspring2)]

    print("\n-------Crossover Result-------\n")
    print('Offspring 1 :', offspring_1)
    print('Fitness Offspring 1 :', fitness_offspring_1)
    print('\n')
    print('Offspring 2 :', offspring_2)
    print('Fitness Offspring 1 :', fitness_offspring_2)

    #Mutation

    rand_mutation = random.randint(1, 100)
    if rand_mutation <= 10:
        print('\nTerjadi Mutasi\n')
        pos_mutate = random.randint(0, len(data)-1)
        print('Sebelum : ', offspring_1)
        print('Fitness sebelum :', fitness_offspring_1)
        if offspring_1[pos_mutate] == 1:
            offspring_1[pos_mutate] = 0
        else:
            offspring_1[pos_mutate] = 1
        print('Sesudah :', offspring_1)

        save_offspring1 = [] 

        for n_gen in range(14):
            if offspring_1[n_gen] == 1:
                calc_fitness = data[n_gen]
                save_offspring1.append(calc_fitness)

        fitness_offspring_1 = [sum(save_offspring1)]
        print('Fitness sesudah :', fitness_offspring_1)
    else:
        print('\nTidak Terjadi Mutasi\n')

    
    #Elitism

    print("\n-------Elitism Result-------\n")

    current_lowest = min(fitness_value)
    index = fitness_value.index(min(fitness_value)) + 1

    print("Kromosom Terburuk adalah Kromosom", index, "dengan nilai Fitness", current_lowest)

    if fitness_offspring_1 > current_lowest:
        print("Offspring 1 lebih baik dibandingkan dengan Kromosom", index)
        print("Offspring 1 menggantikan Kromosom", index)
        print("Sebelum : ", initial_population[index-1])
        print("Direplace dengan :", offspring_1)
        initial_population[index-1] = offspring_1
        fitness_value[index-1] = fitness_offspring_1
        print("Sesudah : ", initial_population[index-1])
    else:
        print("Offspring 1 lebih buruk dibandingkan kromosom", index)
        print("Tidak terjadi proses elitism")

    current_lowest = min(fitness_value)
    index = fitness_value.index(min(fitness_value)) + 1

    print("Kromosom Terburuk adalah Kromosom", index, "dengan nilai Fitness", current_lowest)

    if fitness_offspring_2 > current_lowest:
        print("Offspring 2 lebih baik dibandingkan dengan Kromosom", index)
        print("Offspring 2 menggantikan Kromosom", index)
        print("Sebelum : ", initial_population[index-1])
        print("Direplace dengan :", offspring_2)
        initial_population[index-1] = offspring_2
        fitness_value[index-1] = fitness_offspring_2
        print("Sesudah : ", initial_population[index-1])
    else:
        print("Offspring 2 lebih buruk dibandingkan kromosom", index)
        print("Tidak terjadi proses elitism")

    best_individual = max(fitness_value)
    best_fitness.append(best_individual)

    x += 1

print(best_fitness)

plt.title('Best Fitness in Each Generation')
plt.plot(best_fitness)
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.show()