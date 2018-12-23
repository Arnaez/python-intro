#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0

epsilon = 0.01
k = 24.0
guess = k/2.0
guesses = 0
while abs(guess*guess - k) >= epsilon:
    guesses += 1
    guess = guess - (((guess**2) - k)/(2*guess))
print('Square root of', k, 'is about', guess)
print('This took', guesses, 'guesses using Newton-Raphson.')

low = min(k, 0)
high = max(1.0, k)
ans = (high + low)/2.0
guesses = 0
while abs(ans**2 - k) >= epsilon:
    guesses += 1
    if ans**2 > k:
        high = ans
    else:
        low = ans
    ans = (high + low)/2.0

print('Square root of', k, 'is about', guess)
print('This took', guesses, 'guesses in a bijection search.')


def findRoot(x, power, epsilon):
    """Assumes x and epislon int or float, power an int,
            epislon > 0 & power >= 1
        Returns float y such that y**power is within epsilon f x.
        If such a float does not exist, it returns None"""