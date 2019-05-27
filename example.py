""" docstring for example simplex problem
    has 3 different sample problems

    - working_example
    - unbounded_example
"""

from simplex_algorithm import *

def working_example():
    """
    a working example of the simplex algorithm
    applied in python

    z = 17x_1 + 70x_2 + 13x_3
        2x_1  -  6x_2 -  4x_3   <= -4
        -x_1  -  2x_2 -  3x_3   <= -2
        4x_1  +  2x_2 -  1x_3   <=  3
        3x_1  -  3x_2 +  3x_3   <= -1
        x_1, x_2, x_3         >=  0
    """

    # Insert an object vector on list form
    object_vector = [
    17, 70, 13
    ]

    # Insert the constraints on nested list form
    constraints = [
    [ 2, -6, -4],
    [-1, -2, -3],
    [ 4,  2, -1],
    [ 3, -3,  3]
    ]

    # Insert the weight vector on list form
    weight_vector = [
    -4,
    -2,
    3,
    -1
    ]

    return object_vector, constraints, weight_vector

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
    object_vector = [2, -3, -3]

    # Insert the constraints on nested list form
    constraints = [[-3, 2, 0], [-1, 1, 4], [-2, -2, 5]]

    # Insert the weight vector on list form
    weight_vector = [80, 20, 30]

    return object_vector, constraints, weight_vector

# When file is run, execute the example
def main(problem):
    #print(problem)
    object_vector, constraints, weight_vector = problem()

    value, tableux, statement, pivots = simplex(object_vector, constraints, weight_vector, silent=False, step = True)

    if not statement.startswith('ERR100'):
        print(statement)
        return

    print("\nReturn statement: %s \n" % statement)
    print("Solved tableux for the problem: \n %s \n" % tableux)
    print("Took %s pivots to reach optimal point" % pivots)
    print('The maximum value of the problem: %s \n' % round(value,2))

    # import test
    #
    # latex = test.format_tableux(tableux)
    # latex = latex.replace('-0.0', '0')
    # latex = latex.replace('.0', '')
    #
    # with open("output2.tex", 'w') as f:
    #     f.write(latex)

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        main(locals()[sys.argv[1]])
    else:
        print("""Please specify which example to run;
        - working_example
        - unbounded_example""")
