#rainfall statistics
def main():
    months = get_input()
    avg_rain(months)
    min_max(months)
    
def get_input():
    months = []
    for index in range(12):
        user_input = float(input('Enter the amount of rainfall for month {}:'.format(index + 1)))
        months.append(user_input)
    return months
def avg_rain(months):
    total_rain = 0
    average = 0
    for value in range(12):
        total_rain += months[value]
        average = total_rain / len(months)
    print('Total Yearly Rainfall: ', total_rain, sep='')
    print('Avereage Monthly Rainfall: ', average, sep='')
    

def min_max(months):
    print('Minimum Rainfall: ', min(months), sep='')
    print('Maximum Rainfall: ', max(months), sep='')
            
    
    

main()
    
    
