
# Sample1.py
import IfxPy
# import IfxPyDbi as dbapi2
import datetime

#################################################
# We can use this for SPEED TEST between Py and C
# Find the number of prime numbers between X and Y
# The equivalent C function is SpeedTestWithCPrimeCount
def MySpeedTestWithPyPrimeCount(x, y):
    i = 0
    j = 0
    VRange = 0.0
    isPrime = 0
    PrimeCount = 0

    if x < 2:
        x = 2

    y += 1
    i = x
    while ( i < y):
        isPrime = 1
        VRange = i / 2 # This Validation Range is good enough

        j = 2
        VRange += 1
        while ( j < VRange ):
            if ( i%j == 0):
                j += 1
                isPrime = 0
                break
            j += 1

        if (isPrime):
            #print( ' [{:d}] '.format(i))
            PrimeCount += 1

        i += 1

    return PrimeCount



def Main():
    print(' ')
    print('Speed Test: C vs Pure Python code')
    print('Please Wait....')
 
    x = 2
    y = 30000

    print(' ')
    print('C  functin, Calculating Prime numbers bwtween {:d} and {:d}'.format(x, y))
    s = datetime.datetime.now()
    rc3_c = IfxPy.SpeedTestWithCPrimeCount( x, y)
    e = datetime.datetime.now()
    delta_c = e - s
    
    print('# of Primes is {}'.format(rc3_c))


    #print(' ')
    print('Py functin, Calculating Prime numbers bwtween {:d} and {:d}'.format(x, y))
    rc3 = 0
    s = datetime.datetime.now()
    
    # rc3 = dbapi2.SpeedTestWithPyPrimeCount( x, y)
    rc3 = MySpeedTestWithPyPrimeCount( x, y)
    e = datetime.datetime.now()
    delta_py = e - s
    # print('{}'.format(rc3))

    if rc3 == rc3_c:
        # print('    To Count number of primes between {:d} and {:d} = {:d} '.format(x, y, rc3))
        print(' ')
        print('Time taken by :')
        print('C  function = {};'.format(delta_c))
        print('Py function = {};'.format(delta_py))
        print(' ')
        r = delta_py / delta_c
        print( "The C function appeared to be {0:.2f} times faster".format( r ))
    else:
        print( "Error: Prime Count not matching C={} Py={}".format(rc3_c, rc3))

    print(' ')


if __name__ == "__main__":
    Main()



