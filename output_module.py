def print_results(sum_result, difference, product, quotient):
    print(f"The sum of the numbers is: {sum_result}")
    print(f"The difference between the numbers is: {difference}")
    print(f"The product of the numbers is: {product}")
    print(f"The quotient of the numbers is: {quotient}")

def append_to_file(sum_result, difference, product, quotient):
    with open("calculations.txt", "a") as file:
        file.write(f"The sum of the numbers is: {sum_result}\n")
        file.write(f"The difference between the numbers is: {difference}\n")
        file.write(f"The product of the numbers is: {product}\n")
        file.write(f"The quotient of the numbers is: {quotient}\n")
