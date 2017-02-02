g = 9.8
t = 0
d = 1/2*g*t**2

def main():
    print('Time\tDistance\n----\t--------\nSeconds\t Meters')
    for t in range(1,11,1):
        print(t, '\t', format(falling_distance(t), ',.2f'), sep='')

def falling_distance(t):
        return 1/2*g*t**2



main()
    
    
