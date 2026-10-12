from LinkedListSet import LinkedListSet

def set_checker(filename):
    set_A = LinkedListSet()  # words length ≤ 5
    set_B = LinkedListSet()  # words length ≥ 5
    set_C = LinkedListSet()  # words length == 5

    with open(filename, 'r') as file:
        for line in file:
            for word in line.strip().split():
                if len(word) <= 5:
                    set_A.add(word)
                if len(word) >= 5:
                    set_B.add(word)
                if len(word) == 5:
                    set_C.add(word)
    return set_A, set_B, set_C

def set_stats(set_A, set_B, set_C):
    # Set Sizes
    print(f"Set A size (≤5): {set_A.size()}")
    print(f"Set B size (≥5): {set_B.size()}")
    print(f"Set C size (=5): {set_C.size()}")
    print()

    # Unions
    print(f"A u B size: {LinkedListSet.Union(set_A, set_B).size()}")
    print(f"A u C size: {LinkedListSet.Union(set_A, set_C).size()}")
    print(f"B u C size: {LinkedListSet.Union(set_B, set_C).size()}")

    # Intersections
    print(f"A n B size: {LinkedListSet.Intersection(set_A, set_B).size()}")
    print(f"A n C size: {LinkedListSet.Intersection(set_A, set_C).size()}")
    print(f"B n C size: {LinkedListSet.Intersection(set_B, set_C).size()}")

    # Differences
    print(f"A - B size: {LinkedListSet.Difference(set_A, set_B).size()}")
    print(f"A - C size: {LinkedListSet.Difference(set_A, set_C).size()}")
    print(f"B - A size: {LinkedListSet.Difference(set_B, set_A).size()}")
    print(f"B - C size: {LinkedListSet.Difference(set_B, set_C).size()}")
    print(f"C - A size: {LinkedListSet.Difference(set_C, set_A).size()}")
    print(f"C - B size: {LinkedListSet.Difference(set_C, set_B).size()}")

if __name__ == "__main__":
    set_A, set_B, set_C = set_checker("CS 2420/final/Partial_Book.txt")
    set_stats(set_A, set_B, set_C)