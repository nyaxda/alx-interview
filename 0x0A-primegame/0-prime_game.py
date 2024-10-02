#!/usr/bin/python3
"""Game Module"""


def prime_helper(number):
    """
    Helper function to determine if a number is prime
    Args: number: integer
    Returns: True if number is prime, False otherwise
    """
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Prime Game
    Args: x: number of rounds, nums: list of integers
    Returns: name of the player that won the most rounds
    """
    if not nums or len(nums) == 0 or x < 1:
        return None
    maria_wins = 0
    ben_wins = 0

    # False Means it is Maria's Turn, True means it is Ben's Turn
    flag = False
    for i in range(x):
        n = nums[i]
        play_numbers = list(range(1, n + 1))
        while play_numbers:
            prime_number = None
            for num in play_numbers:
                if prime_helper(num):
                    prime_number = num
                    break
            if prime_number is None:
                break

            play_numbers = [num for num in
                            play_numbers if num % prime_number != 0]
            # toggling to switch players
            flag = not flag
        if not flag:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
