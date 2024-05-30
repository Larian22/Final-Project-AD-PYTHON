import random
import time

class Lobster:
    def __init__(self, id, length, value):
        self.id = id
        self.length = length
        self.value = value

def value_per_unit(lobster):
    return lobster.value / lobster.length

def sort_lobsters(lobsters):
    lobsters.sort(key=value_per_unit, reverse=True)

def distribute_lobsters(lobsters, net_capacity):
    current_capacity = net_capacity
    total_value = 0.0
    selected_lobsters = []

    for lobster in lobsters:
        if lobster.length <= current_capacity:
            selected_lobsters.append(lobster)
            total_value += lobster.value
            current_capacity -= lobster.length

    for lobster in selected_lobsters:
        print(f"Lobster ID: {lobster.id}, Value: {lobster.value}, Length: {lobster.length}")
    print(f"Max value obtained: {total_value}")

def generate_lobsters(num_lobsters):
    lobsters = []
    for i in range(num_lobsters):
        length = random.randint(1, 500)
        value = random.randint(1, 500)
        lobsters.append(Lobster(i, length, value))
    return lobsters

def main():
    random.seed(time.time())
    start_time = time.time()

    num_lobsters = 1120
    net_capacity = 11200
    lobsters = generate_lobsters(num_lobsters)

    print(f"Number of lobsters: {num_lobsters}\nNet capacity: {net_capacity}")
    print("==== Lobsters selected ====")
    sort_lobsters(lobsters)
    distribute_lobsters(lobsters, net_capacity)

    elapsed_time = time.time() - start_time
    print(f"\nElapsed: {elapsed_time:.6f} seconds")

if __name__ == "__main__":
    main()
