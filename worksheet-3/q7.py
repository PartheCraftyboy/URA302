def outer_function(x):
    def inner_function(y):
        return y * y
    
    result = inner_function(x)  # Call the inner function
    return result

# Example usage
value = 5
output = outer_function(value)
print(f"The square of {value} is {output}")