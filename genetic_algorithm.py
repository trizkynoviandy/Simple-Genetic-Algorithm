import random
import matplotlib.pyplot as plt
from progress.bar import Bar

SEED = 1234
random.seed(SEED)

data = [10,30,70,90,40,50,20,10,50,90,20,10,30,20]

pop_size = 50
iteration = 50

bar = Bar('GA is running', max=iteration)

# Generate initial population
initial_population =[[] for _ in range(pop_size)]
best_fitness = []
average_fitness = []

for n in range(pop_size):
    for n_gen in range(len(data)):
        rand = random.randint(0,1)
        initial_population[n].append(rand)

current_iteration = 0
while current_iteration in range(iteration):

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
    counter = 0
    for item in save_fitness:
        fit = sum(item)
        fitness_value[counter].append(fit)
        counter +=1

    #Parents selection
    rand_parent1 = random.randint(0, pop_size-1)
    rand_parent2 = random.randint(0, pop_size-1)

    while rand_parent2 == rand_parent1:
        rand_parent2 = random.randint(0, pop_size-1)

    parent_1 = initial_population[rand_parent1]
    parent_2 = initial_population[rand_parent2]

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

    #Mutation
    rand_mutation = random.randint(1, 100)
    if rand_mutation <= 10:
        pos_mutate = random.randint(0, len(data)-1)
        if offspring_1[pos_mutate] == 1:
            offspring_1[pos_mutate] = 0
        else:
            offspring_1[pos_mutate] = 1

        save_offspring1 = [] 

        for n_gen in range(14):
            if offspring_1[n_gen] == 1:
                calc_fitness = data[n_gen]
                save_offspring1.append(calc_fitness)

        fitness_offspring_1 = [sum(save_offspring1)]

    #Elitism
    current_lowest = min(fitness_value)
    index = fitness_value.index(min(fitness_value)) + 1

    if fitness_offspring_1 > current_lowest:
        initial_population[index-1] = offspring_1
        fitness_value[index-1] = fitness_offspring_1

    current_lowest = min(fitness_value)
    index = fitness_value.index(min(fitness_value)) + 1

    if fitness_offspring_2 > current_lowest:
        initial_population[index-1] = offspring_2
        fitness_value[index-1] = fitness_offspring_2

    best_individual = max(fitness_value)
    best_fitness.append(best_individual)

    current_iteration += 1
    bar.next()

bar.finish()

plt.title('Best Fitness in Each Generation')
plt.plot(best_fitness)
plt.xlabel('Generation')
plt.ylabel('Fitness Value')
plt.show()