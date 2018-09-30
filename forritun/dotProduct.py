def input_vector(size):
    vector = list()
    for i in range(1, size + 1):
        element = float(input("Element no " + str(i) + ": "))
        vector.append(element)
    return vector

def dot_product(vector_a, vector_b):
    dot = 0
    for i in range(len(vector1)):
        dot += vector_a[i] * vector_b[i]
    return dot


# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))