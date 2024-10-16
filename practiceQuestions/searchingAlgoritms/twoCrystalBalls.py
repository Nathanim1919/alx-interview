import math

def twoCrystalBalls(n) -> int:
    jumb = int(math.sqrt(len(n)))
    initialValue = 0
    
    while initialValue < len(n):
        if n[initialValue]:
            break
        initialValue += jumb
        
    for i in range(initialValue - jumb, len(n)):
        if n[i]:
            return i
        
    return -1

# Example usage:
# Let's assume we have a building with 100 floors, and the ball breaks from the 70th floor onwards.
floors = [False] * 69 + [True] * 31

# Find the floor where the ball breaks
break_floor = twoCrystalBalls(floors)
print(f"The ball breaks at floor: {break_floor}")