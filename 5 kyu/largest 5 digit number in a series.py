def solution(digits):
    length = min(len(digits), 5)
    max_digit = 9
    while digits.find(str(max_digit), 0, len(digits) + 1 - length) == -1:
        max_digit -= 1
        if max_digit < 1:
            return 0

    start = 0
    max_number = 0
    while(True):
        current = digits.find(str(max_digit), start, len(digits) + 1 - length)
        if current == -1:
            break
        if max_number < int(digits[current: current + 5]):
            max_number = int(digits[current: current + 5])
        start = current + 1

    return max_number;


number = "7316717653133062491922511967442657474235534919493496983520368542506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753123457977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257540920752963450"
number2 = '62273790'
number3 = '0'
number4 = ''
number5 = '488648690000'
number6 = '48864869000'
number7 = '8236'
# print 'number 1', solution(number)
# print '\nnumber 2', solution(number2)
# print '\nnumber 3', solution(number3)
# print '\nnumber 4', solution(number4)
# print '\nnumber 5', solution(number5)
# print '\nnumber 6', solution(number6)
# print '\nnumber 7', solution(number7)


# other solutions
def solution2(dd):
    return max(int(dd[i:i+5]) for i in range(len(dd) - 4))


# measuring time
import time
import random

random.seed(123)

start = time.time()
n = ''
for i in range(10000000):
    n += str(random.randint(1, 9))

end = time.time()
print 'preparing:', (end - start)


start = time.time()
solution(n)
end = time.time()
print 'first:', (end - start)

start = time.time()
solution2(n)
end = time.time()
print 'second:', (end - start)