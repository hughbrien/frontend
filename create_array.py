def eat_memory():  # liveness
    big_array = [999999.999999999] * 1000
    print(big_array)
    element_value = big_array[0]
    print(element_value)

if __name__ == '__main__':
    eat_memory()