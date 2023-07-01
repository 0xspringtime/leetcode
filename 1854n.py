def maximumPopulation(logs):
    # Initialize a population array for years 1950 to 2050
    population = [0]*101
    
    # For each log, increment the population for all years from birth to death
    for birth, death in logs:
        for i in range(birth - 1950, death - 1950):
            population[i] += 1
            
    # Find the year with the maximum population
    max_population = max(population)
    for i in range(101):
        if population[i] == max_population:
            return i + 1950  # return the earliest year with maximum population
#time O(n*k)
#space O(1)
