from collections import deque

cola = deque([1, 2, 3, 4, 5])

cola.append(6)
cola.append(7)

cola.popleft() # Elimina el primero
cola.pop() # Elimina el ultimo

print(cola)