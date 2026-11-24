"""Tiny demo app: a few arithmetic helpers.

This repo is a test target for Shipmate (Agentware T2).
One function has a real bug on purpose: average([]) crashes.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def average(nums):
    # BUG: empty list raises ZeroDivisionError instead of returning 0.
    return sum(nums) / len(nums)
