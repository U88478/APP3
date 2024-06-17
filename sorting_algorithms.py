# sorting_algorithms.py
import time

import matplotlib.pyplot as plt
from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def fetch_user_scores():
    users = session.query(User).all()
    return [user.stats.average_score for user in users if user.stats]


def select_sizes(total_users):
    sizes = []
    step = max(1, total_users // 10)
    for i in range(1, 11):
        sizes.append(min(i * step, total_users))
    return sizes


def compare_sorting_algorithms():
    user_scores = fetch_user_scores()
    total_users = len(user_scores)
    sizes = select_sizes(total_users)

    bubble_times = []
    insertion_times = []
    merge_times = []

    for size in sizes:
        arr = user_scores[:size]

        # Bubble Sort
        arr_copy = arr.copy()
        start_time = time.time()
        bubble_sort(arr_copy)
        bubble_times.append(time.time() - start_time)

        # Insertion Sort
        arr_copy = arr.copy()
        start_time = time.time()
        insertion_sort(arr_copy)
        insertion_times.append(time.time() - start_time)

        # Merge Sort
        arr_copy = arr.copy()
        start_time = time.time()
        merge_sort(arr_copy)
        merge_times.append(time.time() - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bubble_times, label='Bubble Sort', marker='o')
    plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
    plt.plot(sizes, merge_times, label='Merge Sort', marker='o')

    plt.text(sizes[-1], bubble_times[-1], f'{bubble_times[-1]:.4f}s', fontsize=9, verticalalignment='bottom')
    plt.text(sizes[-1], insertion_times[-1], f'{insertion_times[-1]:.4f}s', fontsize=9, verticalalignment='bottom')
    plt.text(sizes[-1], merge_times[-1], f'{merge_times[-1]:.4f}s', fontsize=9, verticalalignment='bottom')

    plt.xlabel('Number of Users')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()
