#!/usr/bin/python3
"""Game Module"""


def sieve(n):
    """
    Sieve of Eratosthenes to generate a list of primes up to n.
    Args: n: integer
    Returns: list of booleans indicating if index is prime
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False
    return is_prime


def isWinner(x, nums):
    """
    Prime Game
    Args: x: number of rounds, nums: list of integers
    Returns: name of the player that won the most rounds
    """
    if not nums or x < 1:
        return None
    max_num = max(nums)
    is_prime = sieve(max_num)
    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        n = nums[i]

        if n == 1:
            ben_wins += 1
            continue

        play_numbers = list(range(1, n + 1))
        maria_turn = True

        while play_numbers:
            prime_number = None
            for num in play_numbers:
                if is_prime[num]:
                    prime_number = num
                    break
            if prime_number is None:
                break

            play_numbers = [num for num in
                            play_numbers if num % prime_number != 0]
            # toggling to switch players
            maria_turn = not maria_turn

        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
