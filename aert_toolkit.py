# AERT - Algorithmic Efficiency & Recursion Toolkit
# Name: Rohit Kushwaha
# Roll No: 2501730440


class StackADT:
    def _init_(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"

    
    if n == 0 or n == 1:
        return 1

    
    return n * factorial(n - 1)


naive_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return n

    return fib_naive(n - 1) + fib_naive(n - 2)


memo_calls = 0

def fib_memo(n, memo=None):
    global memo_calls
    memo_calls += 1

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]

def hanoi(n, source, auxiliary, destination, stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        stack.push(move)
        return

    hanoi(n - 1, source, destination, auxiliary, stack)

    move = f"Move disk {n} from {source} to {destination}"
    stack.push(move)

    hanoi(n - 1, auxiliary, source, destination, stack)

def binary_search(arr, key, low, high):
    # Base case: not found
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)   


def main():
    print("Testing Stack ADT...\n")

    stack = StackADT()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack size:", stack.size())
    print("Top element:", stack.peek())
    print("Popped element:", stack.pop())
    print("Stack size after pop:", stack.size())


    print("\nTesting Factorial...\n")

    test_values = [0, 1, 5, 10]

    for value in test_values:
      print(f"Factorial of {value} =", factorial(value))


    print("\nTesting Fibonacci...\n")

    test_values = [5, 10, 20, 30]

    for value in test_values:
     global naive_calls, memo_calls

     naive_calls = 0
     memo_calls = 0

     naive_result = fib_naive(value)
     memo_result = fib_memo(value)

     print(f"n = {value}")
     print("Naive Fibonacci:", naive_result)
     print("Naive Call Count:", naive_calls)
     print("Memoized Fibonacci:", memo_result)
     print("Memoized Call Count:", memo_calls)


    print("\nTower of Hanoi for n = 3 (Using Stack)\n")

    hanoi_stack = StackADT()
    hanoi(3, 'A', 'B', 'C', hanoi_stack)

    while not hanoi_stack.is_empty():
     print(hanoi_stack.pop())

    print("\nTesting Recursive Binary Search\n")

    arr = [1, 3, 5, 7, 9, 11, 13]

    test_keys = [7, 1, 13, 2]

    for key in test_keys:
     result = binary_search(arr, key, 0, len(arr) - 1)
     print(f"Searching {key}: Index =", result)

    
    empty_arr = []
    print("Searching in empty array:", binary_search(empty_arr, 5, 0, len(empty_arr) - 1))

if __name__ == "_main_":
    main()