# Question 1
#-----------------------------------------------------------------
def double_precision(binary:str):
    length = len(binary)

    # print(length)
    s = float(binary[0])
    exponent = 10
    c = 0
    for i in range (1,12):
        c = c + float(binary[i]) * pow(2, exponent)
        exponent = exponent-1
    #---------------------------------

    mantissa = 1
    bit = 12
    f = 0
    for i in range (bit, 24):

        f = f + float(binary[i]) * pow(0.5, mantissa)
        mantissa = mantissa + 1
    # ------------------------------------
    x = c - 1023
    result = pow(-1, s) * pow(2, x) * (1 + f)
    print(result)

    # -------------------------------------

    # Question 2
    # convert result to the normalized form then chopp kth digit
    normalized = result * pow(10, -3)
    k = 3
    chopped = int(result * pow(10,k) / pow(10,k))
    print(chopped*1.0)

    # --------------------------------------
    #  Question 3
    rounded = result /1000
    rounded = int(rounded* pow(10, k) + 0.5)/pow(10,k)
    rounded = rounded * 1000
    print(rounded)

    #------------------------------
    # Question 4 absolute error

    print(absolute_error(result, rounded))

    # relative error
    print(relative_error(result, rounded))

# -------------------------------------------------------

# Question 4 helper function

def absolute_error(precise:float, approximate: float):

    sub_operation = precise - approximate

    return abs(sub_operation)

def relative_error(precise:float, approximate: float):

    sub_operation = absolute_error(precise, approximate)
    div_operation = sub_operation / precise

    return div_operation

#---------------------------------------------------------------
# Question 5
def check_for_alternating(function_we_got: str):
    term_check = check_for_negative_1_exponent_term(function_we_got)

    return term_check

def check_for_decreasing(function_we_got: str, x: int):
    decreasing_check = True
    k = 1
    starting_val = abs(eval(function_we_got))
    for k in range(2, x):
        result = abs(eval(function_we_got))

        print(result)
        if starting_val <= result:
            decreasing_check = False

    return decreasing_check


def check_for_negative_1_exponent_term(function: str) -> bool:
    if "-1**k" in function:
        return True

    return False

#----------------------------------------------
def use_minimum_term_function():
    k = 0
    error = 1
    while error >= pow(10, -4):
        k = k + 1
        result = pow(-1, k)/ pow(k,3)
        error = abs(result)

    print(k)

#-----------------------------------------------------------------
# Question 6
def bisection_method(left: float, right: float, given_function: str):
    x = left
    intial_left = eval(given_function)
    x = right
    intial_right = eval(given_function)
    if intial_left * intial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return

    tolerance: float = .0001
    diff: float = right - left
    max_iterations = 20
    iteration_counter = 0

    while (diff >= tolerance and iteration_counter <= 20):
        iteration_counter += 1
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)

        if evaluated_midpoint == 0.0:
            break
        x = left
        evaluated_left_point = eval(given_function)

        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0

        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point

        diff = abs(right - left)

    print(iteration_counter)

# --------------------------------------------
def custom_derivative(value):
    return (3 * value* value) - (2 * value)
# --------------------------------------------
def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):

    iteration_counter = 0
    x = initial_approximation
    f = eval(sequence)

    f_prime = custom_derivative(initial_approximation)

    approximation: float = f / f_prime
    while(abs(approximation) >= tolerance):

        x = initial_approximation
        f = eval(sequence)

        f_prime = custom_derivative(initial_approximation)

        approximation = f / f_prime

        initial_approximation -= approximation
        iteration_counter += 1
    print(iteration_counter)

#-----------------------------------------------

if __name__ == "__main__":

    # Question 1[Double Percision]

    str = "010000000111111010111001"

    double_precision(str)

    # -------------------------------------------
    # Question 5

    function_a: str = "(-1**k) * (x**k) / (k**3)"
    x: int = 1
    check1: bool = check_for_alternating(function_a)
    check2: bool = check_for_decreasing(function_a, x)



    if check1 and check2:
        use_minimum_term_function()
    # ------------------------------------------------------
    # Question 6
    #  a
    left = -4
    right = 7
    function_string = "x**3 - (4*(x**2)) - 10"
    bisection_method(left, right, function_string)
    # b
    # newton_raphson method
    initial_approximation: float = -4
    tolerance: float = .0001
    sequence: str = "(x**3) - (x**2) + 2"

    newton_raphson(initial_approximation, tolerance, sequence)
