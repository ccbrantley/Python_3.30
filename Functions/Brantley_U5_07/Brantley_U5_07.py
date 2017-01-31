def main():
    a = int(input('Tickets sold for class A: '))
    b = int(input('Tickets sold for class B: '))
    c = int(input('Tickets sold for class C: '))
    print('Income generated: $', total(a,b,c), sep='')
    
def total(a,b,c):
    aInc = a * 20
    bInc = b * 15
    cInc = c * 10
    return aInc + bInc + cInc

main()
    
    
