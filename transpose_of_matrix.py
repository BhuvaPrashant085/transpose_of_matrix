"""
Transpose of a square matrix

"""

def get_matrix(n):
    """Input from the user"""
    matrix = []
    for i in range(n):
        row = []
        print(f"For Row {i+1}:")
        for j in range(n):
            while True:
                try:
                    val = int(input(f"{j+1}st element - "))
                    break
                except ValueError:
                    print("not valid.... enter again")
            row.append(val)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    """print the matrix"""
    for row in matrix:
        for val in row:
            print(val, end="  ")
        print()

def main():
    print("Transpose Of Matrix")
    print("Transpose - valid for square matrix only")

    # Input from the user 
    while True:
        try:
            n = int(input("\n\nEnter dimensions N \ncondition :- (positive integer): "))
            if n <= 0:
                print("Please enter a positive integer greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print(f"\nFor matrix of {n}x{n}\n")

    a = get_matrix(n)
    print("\nGiven Matrix is:")
    print_matrix(a)

    # main logic of Transpose matrix  
    for i in range(n):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]  # swap of elements

    print("\nTranspose of this matrix is:")
    print_matrix(a)

if __name__ == "__main__":
    main()
