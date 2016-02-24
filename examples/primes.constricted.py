PC = {}

def RETR(*k): return PC['.'.join(k)]
def STORE(v, *k): PC['.'.join(k)] = v


def naturals():
    RT = 'naturals'
    STORE(1, RT, 'n')
    while True:
        yield RETR(RT, 'n')
        STORE(RETR(RT, 'n') + 1, RT, 'n')

def primes():
    prev_primes = set()
    n = 2
    while True:
        has_divisors = any(n % prime == 0 for prime in prev_primes)
        if not has_divisors:
            prev_primes.add(n)
            yield n
        n += 1

def grange(g, start, stop, step = 1):
    num_iterations = 0
    for value in g:
        if stop <= value:
            break
        if value < start:
            continue
        if num_iterations % step == 0:
            yield value
        num_iterations += 1

def test():
    assert(list(grange(naturals(), 10, 20, 2)) == list(range(10, 20, 2)))
    assert(list(grange(primes(), 5, 20, 1)) == [5, 7, 11, 13, 17, 19])

if __name__ == "__main__":
    test()
    print(list(grange(primes(), 0, 100)))

