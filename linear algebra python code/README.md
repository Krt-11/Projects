FOR USERS: {

    HOW TO USE IT:
        When the program is run:
        1. enter the size of the matrix
        2. enter elements of each row individually by pressing ENTER/RETURN between EACH element
        3. it will print out the input matrix + RREF of the matrix

    FUNCTION:
        This code take an input matrix from the user and prints out the reduced row echelon form of the matrix input along with its pivot columns

        pivot columns - columns that have a non-zero entry
        EX. the pivot columns for
        [ [1,0,0,0]
        [0,1,0,0]
        [0,0,0,1] ]
        would be 1,2,4 because they have a non zero entry.
        These columns can be used to find inverse, coefficient matrix, etc for the original matrix.

}

MORE INFORMATION: {

    HOW IT WORKS:
        The program uses sympy library which has a built in RREF calculator and can create matrix objects to use this function on.

        Sympy also has many more functions such as matrix airthmetic, inverse calculator, etc. for higher functionality. Here is a link for more information: https://www.sympy.org/en/features.html


    TIME COMPLEXITY:
    O(n^2) : O(rows * columns)

}
