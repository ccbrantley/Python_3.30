#population data
def main():
    list_pop = get_list()
    avg_annual_change = avg_change(list_pop)
    min_max(list_pop)
    

def get_list():
    list_pop = []
    file_pop = open('USPopulation.txt', 'r')
    line_pop = file_pop.readline()
    while line_pop != '':
        line_pop = line_pop.rstrip()
        list_pop.append(line_pop)
        line_pop = file_pop.readline()
    return list_pop

def avg_change(list_pop):
    total_change = 0
    len_list = len(list_pop)
    for value in range(len_list - 1):
        total_change += (int(list_pop[value + 1]) - int(list_pop[value]))
    avg_annual_change = total_change / len_list
    print('The total population change was: ', total_change, sep='')
    print('The average annual change in population: ', avg_annual_change, sep='')
    return avg_annual_change

def min_max(list_pop):
    list_change = []
    len_list = len(list_pop)
    for value in range(len_list - 1):
        yearly_change = (int(list_pop[value + 1]) - int(list_pop[value]))
        list_change.append(yearly_change)
    max_value = max(list_change)
    max_index = list_change.index(max_value)
    min_value = min(list_change)
    min_index = list_change.index(min_value)
        
    print('The year with the greatest increase in population is ',max_index + 1950, ' with a population growth of ', max_value, sep='')
    print('The year with the smallest increase in population is ',min_index + 1950, ' with a population growth of ', min_value, sep='')
        
    
main()
