from time import time
from sys import stdout
from simplex_algorithm import simplex

def unbounded_example():
    """
    an example of of the simplex algorithm
    when the basic solution is unbounded

    z =  2x_1 - 3x_2 - 3x_3
        -3x_1 + 2x_2         <= 80
        - x_1 + 1x_2 + 4x_3  <= 20
        -2x_1 - 2x_2 + 5x_3  <= 30
        x_1, x_2, x_3        >=  0
    """

    # Insert an object vector on list form
    object_vector = [-8, 3, 3, -3, 3, -4, 3, 3, -2, 6, 3, -6]

    # Insert the constraints on nested list form
    constraints = [[5, 3, -4, -7, 0, -2, -9, 0, 6, 9, 3, 4], [-6, 1, -1, 6, 4, -7, 5, -9, -6, 3, -8, 9], [-1, 5, 9, -4, 3, -5, -4, 5, -3, -3, -8, -9], [-6, 4, -8, -6, 9, 3, 7, 8, 4, -4, -6, -3], [7, -1, -4, 3, 9, -5, -6, -1, -2, -5, -9, -7], [7, 1, 6, 1, 4, 1, -8, -2, -4, -6, 7, 0], [9, -3, 5, 9, -5, 2, 1, 2, 9, -3, -6, 0], [-2, 2, -8, -3, -9, 9, 1, 8, 9, -4, -3, 7], [8, -4, 0, -8, -7, 0, 6, -2, -4, -3, -6, 6], [-8, -9, 2, 7, 1, -8, -2, 1, 5, 0, 2, -1], [1, 1, -2, 6, -4, 5, 1, 2, 4, -1, 8, -3], [3, 6, -4, -5, -9, 3, 4, 4, -5, 9, -2, 6]]

    # Insert the weight vector on list form
    weight_vector = [3, 2, 7, 8, 9, 2, 6, 9, 8, 5, 3, 7]

    return object_vector, constraints, weight_vector

def random_example(n, width=0):
    from random import randint, choice

    width = randint(-width,width)

    rng = range(n+width)

    c_rng = list(range(19))
    c_rng.remove(9)

    A = [[randint(-9,9) for i in rng] for j in rng]
    B = [randint(1,9) for i in rng]
    C = [choice(c_rng)-9 for i in rng]

    return C,A,B

def average(sum_list):

    return sum(sum_list) / len(sum_list)

def main():
    iterations = 10

    n, width = 25, 3

    start_time = time()
    dt = time() - start_time
    dt_time = dt


    steps = []
    for i in range(iterations):
        C, A, B = random_example(n,width)
        a,b,c, step = simplex(C,A,B, silent = True)
        steps.append(step)
        dt = time() - start_time
        avg_time = dt / (i+1)
        #stdout.write("\rAverage time {:<8.7} with {} iterations".format(avg_time-dt_time, i))

    dt = time() - start_time
    avg_time = dt / iterations

    stdout.write("Average time {:<8.7} with {} iterations\n".format(avg_time-dt_time, iterations))
    print("Average pivots made %s" % average(steps))
    print()



if __name__ == '__main__':
    main()
