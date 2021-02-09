# # def det_smaller_matrix(mat):    
# #     if len(mat) == 3:
# #         count = 0
# #         det_value_sum = 0
# #         for x in range(len(mat)):
# #             mat = func()
# #             mat_length = len(mat)
# #             det = mat[0][x]
# #             for y in range(1,len(mat)):
# #                 del mat[y][x]
# #             del mat[0]            
# #             det_value = det * (mat[0][0] * mat[1][1] - mat[0][1]*mat[1][0])
# #             count += 1
# #             if count % 2 == 0:
# #                 det_value_sum -= det_value
# #             else:
# #                 det_value_sum += det_value
# #             if count == mat_length:
# #                 return det_value_sum
# #     else:        
# #         for x in range(len(mat)):
# #             new_matrix = None
# #             mat = func()
# #             outer_det = mat[0][x]
# #             for y in range(1,len(mat)):
# #                 del mat[y][x]
# #             del mat[0]
# #             new_matrix = mat
# #             matrixes(new_matrix)

# def smaller_matrix(mat):    
#     new_matrix = []  
#     for x in range(len(mat)):
#         outer_det = mat[0][x]
#         for y in range(1,len(mat)):
#             del mat[y][x]   
#         del mat[0]
#         new_matrix.append(mat)
#     return new_matrix
#     # for element in new_matrix:
#     #     print(element)
#     # if len(element) != 3:
#     #     smaller_matrix(element)
#     # else:
#     #     det_smaller_matrix(new_matrix)

# def foo(matrix):
#     smaller_mat = smaller_matrix(matrix)
#     for element in smaller_mat:
#         if element != 3:
#             func(smaller_mat)
#             foo(smaller_mat)
#         # else:

# def func():
#     matrix = [
#     [1,2,3,4,1],
#     [5,6,7,8,1],
#     [9,0,1,2,1],
#     [3,4,5,6,1],
#     [3,4,5,6,1]]
#     return matrix
 
# def main():
#     matrix = func()
#     foo(matrix)

# print(main())

# def matrixes(x=0, accumulated=0):
#     mat = func()
#     count=0
#     if len(mat) == 3:
#         for x in range(len(mat)):
#             mat = func()
#             mat_length = len(mat)
#             det = mat[0][x]
#             for y in range(1,len(mat)):
#                 del mat[y][x]
#             del mat[0]            
#             det_value = det * (mat[0][0] * mat[1][1] - mat[0][1]*mat[1][0])
#             count += 1
#             if count % 2 == 0:
#                 accumulated -= det_value
#             else:
#                 accumulated += det_value
#             if count == mat_length:
#                 return accumulated
# def func():
#     matrix_a = [
#     [5,2,3],
#     [4,-25,6],
#     [7,18,9]]
#     return matrix_a
# print(matrixes())

#     matrix = [
#     [1,2,3,4,1],
#     [5,6,7,8,1],
#     [9,0,1,2,1],
#     [3,4,5,6,1],
#     [3,4,5,6,1]]
#     return matrix
def base_matrix():
    # matrix = [
    # [1,2,3,4,1],
    # [5,6,7,8,1],
    # [9,0,1,2,1],
    # [3,4,5,6,1],
    # [3,4,5,6,1]]
    # return matrix

    matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2],
    [3,4,5,6]]
    return matrix

    # matrix = [
    # [1,7,7],
    # [6,6,4],
    # [4,2,1]]
    # return matrix

def resizing_matrix(matrix):
    accumulate = 0
    i=0
    list_of_matrixes = []
    list_ = [num for num in range(len(matrix))]
    dets = matrix[0]
    for z in range(len(matrix)):
        del list_[z]
        inter_matrix = [[matrix[y][x] for x in list_] for y in range(len(matrix))]
        list_of_matrixes.append(inter_matrix)          
        list_ = [num for num in range(len(matrix))]

    for element in list_of_matrixes:
        del element[0]        
        print(element)        
        if len(element) == 2:
            value_smallest_matrix = dets[i] * (element[0][0] * element[1][1] - element[0][1]*element[1][0])
            print(dets[i])
            i += 1
            accumulate += value_smallest_matrix        
        else:                
            resizing_matrix(element)
        
def main():
    matrix = base_matrix()
    resizing_matrix(matrix)
main()
