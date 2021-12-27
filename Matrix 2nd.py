
print("\n\nProgram Written & Performed by SAI&D75 Vivek Harwani\n")

mat1 = [[15, 21, 31],
        [21, 28, 11],
        [35, 33, 18]]

mat2 = [[41, 52, 61],
        [53, 59, 53],
        [49, 55, 44]]

mat3 = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

print("\nMatrix 1 is: ")
for i in mat1:
    print("           ", i)
    
print("\nMatrix 2 is: ")
for i in mat2:
    print("           ", i)

print("\n\n")



##############################################################
def mat_addititon(mat1, mat2, mat3):

    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat3[i][j] = mat1[i][j] + mat2[i][j]

    print("\nAddition of Matrix 1 and Matrix 2 is: ")
    for i in mat3:
        print("           ", i)



###############################################################
def mat_substraction(mat1, mat2, mat3):

    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat3[i][j] = mat2[i][j] - mat1[i][j]

    print("\nSubstraction of Matrix 1 and Matrix 2 is: ")
    for i in mat3:
        print("           ", i)



###############################################################
def mat_multiplication(mat1, mat2, mat3):

    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat3[i][j] = mat2[i][j] * mat1[i][j]

    print("\nMultiplication of Matrix 1 and Matrix 2 is: ")
    for i in mat3:
        print("           ", i)



#################################################################
def mat_transpose(mat1, mat2):

    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat2[i][j] = mat1[j][i]

    print("\nTranspose of Matrix 1 is: ")
    for i in mat2:
        print("           ", i)


check = 1

while check == 1:
    print("1:Addition of Matrices")
    print("2:Substraction of Matrices")
    print("3:Multiplication of Matrices")
    print("4:Transpose of Matrix")
    print("5: Exit")
    choice = int(input("Enter your Choice: "))

    if choice == 1:
        mat_addititon(mat1, mat2, mat3)
        cont = input("Do You want to continue...? y/n: ")
        if cont == 'y' or cont =='Y':
            check = 1
        else:
            check = 0
    elif choice == 2:
        mat_substraction(mat1, mat2, mat3)
        cont = input("Do You want to continue...? y/n: ")
        if cont == 'y' or cont =='Y':
            check = 1
        else:
            check = 0
    elif choice == 3:
        mat_multiplication(mat1, mat2, mat3)
        cont = input("Do You want to continue...? y/n: ")
        if cont == 'y' or cont =='Y':
            check = 1
        else:
            check = 0
    elif choice == 4:
        mat_transpose(mat1, mat3)
        cont = input("Do You want to continue...? y/n: ")
        if cont == 'y' or cont =='Y':
            check = 1
        else:
            check = 0
    elif choice == 5:
        check = 0
    







