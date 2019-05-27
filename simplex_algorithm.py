""" import - notation and classes from matrix.py """
from matrix import *
""" import - example project from example.py"""
import example


def identity_matrix(n):
    """function to make an n-degree identity mat-
    rix, and return the matrix object """

    mat = [[1 if j == i else 0 for j in range(n)] for i in range(n)]

    return Matrix(mat)



# Returns tuple of
#               [0]: boolean for succes
#               [1]: error message
def curate(object_vector, constraints, weight_vector):
    """takes the input given to the simplex and
    curates it, raises appropriate errors
    """

    # Test if all input types are lists
    types = [True if type(obj) == list else False for obj in [object_vector, constraints, constraints[0], weight_vector]]
    if not all(types):
        raise TypeError("All input types must be lists, and constraints must be a nested list.")


    constraints_n = len(constraints[0])

    # Tests if the dimensions are
    if len(object_vector) != constraints_n:
        raise ValueError("Object vector must have same amount of variables as constraints. If a variable doesn't exist in a constraint, add a 0.")

    if len(constraints) != len(weight_vector):
        raise ValueError("Each constraint must have a weight.")

    return True


def simplex(object_vector, constraints, weight_vector, silent=False, step = False):
    """
    input
    object_vector is an list of coefficients
    constraints is a list of list of coefficients
    weight_vector is a list of coefficients
    silent, if it should print out what it does

    takes a maximization problem on tableux form
    and uses the simplex method, combined with b
    lands pivot rule, to optimize the set of li-
    near equations.

    returns
    optimal value: int
    tableux matrix: matrix; matrix object of final tableux
    statement: str; ERR100 if succes, ERR200 if unbound
    pivot_amount: int; amount of pivots required
    """


    # Clean the input
    curate(object_vector, constraints, weight_vector)

    if not silent:
        print(
        """Starting simplex on
    Object vector: {}
    Constraints: {}
    Weight vector: {}
        """.format( object_vector, constraints, weight_vector ))

    object_vector = Vector(object_vector)
    constraints = Matrix(constraints)
    weight_vector = Vector(weight_vector)

    # Make sure the amount of constraints == amount of weights
    if len(constraints) != len(weight_vector):
        raise 'amount of restraints does not match amount of contraints'

    # Make an identity matrix, one slackvariable per constraint
    slack_variables = identity_matrix(len(constraints))

    if not silent:
        print("Setting up tableux...\n")
    # Set up tableux
    tableux = constraints.smr(slack_variables)
    tableux = tableux.svr(weight_vector)
    tableux = tableux.add_row(-1*object_vector)

    # Count how many pivots have been executed
    pivot_amount = 0

    while True:
        # Rule 1: If all values in the object vector is positive, the solution is found.
        positive_object = [v >= -eps for v in tableux[-1]] # epsilon instead of 0 because rounding error

        if all(positive_object):
            return (tableux[-1][-1], tableux, "ERR100: Problem is optimal", pivot_amount)

        # Find lowest coefficient in object vector
        relevant_column = argmin(tableux[-1][:-1])

        # Compute ratios between contraints in relevant_column and weights
        ratios = []
        for row in tableux[:-1]:
            if row[relevant_column] != 0:
                ratios.append(row[-1] / row[relevant_column])
            else:
                ratios.append(9999999)
        #ratios = [99999999999 if row[relevant_column] == 0 else row[-1] / row[relevant_column] for row in tableux[:-1]]

        # Rule 2: If all ratios are negative, problem is unbounded
        positive_ratios = [False if v < 0 else True for v in ratios]
        if not any(positive_ratios):
            return (False, None,"ERR200: Problem is unbounded", pivot_amount)

        # Rule 3: Pivot in the relevant cell
        # Find the lowest ratio greater than 0

        relevant_row = argmin( ratios, 0)
        print(ratios, relevant_row)
        # Pivot in this variable
        if not silent:
            print("Objective value is {obj:7}. Pivoting in ({m}, {n})...".format(m=relevant_row+1,n=relevant_column+1, obj=round(tableux[-1][-1],4)))
        pivot_amount += 1
        tableux = tableux.column_pivot(relevant_row, relevant_column)
        if step:
            input()


def main():
    pass

if __name__ == '__main__':
    main()
