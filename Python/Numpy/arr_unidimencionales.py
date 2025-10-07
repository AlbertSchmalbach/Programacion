import numpy as np

values = np.array(range(10, 16))
print(values)

# Acceso
print(values[3])

# modificacion
values[0] = values[1] + values[4]
print(values)

# borrado
np.delete(values, 2)
print(values)

# Insercion
np.append(values, 16)
print(values)