m = 0
v = 0
ke = 1/2*m*v**2
print('This program calculates kinetic energy')
def main():
    m = int(input('Please enter in the mass of object (kg) : '))
    v = int(input('Please enter in the velocity of object (meter per second)'))
    print('The kinetic energy is ', format(kinetic_energy(m, v), ',.2f'), 'joules')

def kinetic_energy(m, v):
    return 1/2*m*v**2

main()
