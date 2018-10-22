
# Py_C_SpeedTest.py
import IfxPy
import IfxPyDbi as dbapi2
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


###############################
def Main( x, y ):
    print(' ')
    print("Speed Test: \'Pure Python\' vs \'Native Code\'. ")
    print('Calculating Prime Numbers Between {:d} and {:d}'.format(x, y))

    print(' ')
    print('Executing C  function, please wait....' )
    s = datetime.datetime.now()
    rc3_c = IfxPy.SpeedTestWithCPrimeCount( x, y)
    e = datetime.datetime.now()
    delta_c = e - s

    print('Number of Primes count is {}'.format(rc3_c))

    print('Executing Py function, please wait....' )
    rc3 = 0
    s = datetime.datetime.now()

    rc3 = dbapi2.SpeedTestWithPyPrimeCount( x, y)

    # Try enhancing Python function to improve the result,
    # then you may use 'MySpeedTestWithPyPrimeCount()'
    # rc3 = MySpeedTestWithPyPrimeCount( x, y)

    e = datetime.datetime.now()
    delta_py = e - s

    if rc3 == rc3_c:
        print(' ')
        print('Time taken by :')
        print('     Native function = {};'.format(delta_c))
        print('     Python function = {};'.format(delta_py))
        print(' ')
        r = delta_py / delta_c
        print( "The Native C function appeared to be {0:.2f} times faster".format( r ))
    else:
        print( "Error: Prime Count not matching C={} Py={}".format(rc3_c, rc3))

    print(' ')


#########################################
if __name__ == "__main__":
    #Find the number of prime numbers between X and Y
    Main( 2, 50000 )



