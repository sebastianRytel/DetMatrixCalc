# def base_matrix():
    # matrix = [
    # [1,2,3,4,1],
    # [5,6,7,8,1],
    # [9,0,1,2,1],
    # [3,4,5,6,1],
    # [3,4,5,6,1]]
    # return matrix

    # matrix = [
    # [1,2,3,4],
    # [5,6,7,8],
    # [9,0,1,2],
    # [3,4,5,6]]
    # return matrix

    # matrix = [
    # [1,7,7],
    # [6,6,4],
    # [4,2,1]]
    # return matrix

# def resizing_matrix(matrix):
#     accumulate = 0
#     i=0
#     list_of_matrixes = []
#     list_ = [num for num in range(len(matrix))]
#     dets = matrix[0]
#     for z in range(len(matrix)):
#         del list_[z]
#         inter_matrix = [[matrix[y][x] for x in list_] for y in range(len(matrix))]
#         list_of_matrixes.append(inter_matrix)          
#         list_ = [num for num in range(len(matrix))]

#     for element in list_of_matrixes:
#         del element[0]        
#         print(element)        
#         if len(element) == 2:
#             value_smallest_matrix = dets[i] * (element[0][0] * element[1][1] - element[0][1]*element[1][0])
#             print(dets[i])
#             i += 1
#             accumulate += value_smallest_matrix        
#         else:                
#             resizing_matrix(element)
        
# def main():
#     matrix = base_matrix()
#     resizing_matrix(matrix)
# main()


def resizing_matrix(element):
    
    i=0
    list_of_matrixes = []
    # list_ = [num for num in range(len(element))]
    
    dets = element[0]
    for z in range(len(element)):
        list_ = [num for num in range(len(element))]
        del list_[z]
        inter_matrix = [[element[y][x] for x in list_] for y in range(len(element))]
        list_of_matrixes.append(inter_matrix)          
        # list_ = [num for num in range(len(element))]
    # print(list_of_matrixes)
    for element in list_of_matrixes:
        accumulate = 0
        del element[0]        
        print('element->',element)
        if len(element) == 2:
            value_smallest_matrix = dets[i] * (element[0][0] * element[1][1] - element[0][1]*element[1][0])
            print('dets->',dets[i])
            i += 1
            if i % 2 == 0:
                accumulate -= value_smallest_matrix
            else:
                accumulate += value_smallest_matrix
            print('accu->',accumulate)
        else:
            resizing_matrix(element)
    
def bigger_matrix():
    matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2],
    [3,4,5,6]]
    # matrix = [
    # [1,2,3,4,1],
    # [5,6,7,8,1],
    # [9,0,1,2,1],
    # [3,4,5,6,1],
    # [3,4,5,6,1]]
    print(resizing_matrix(matrix))

# def small_matrix():

#     matrix = [
#     [1,7,7],
#     [6,6,4],
#     [4,2,1]]
#     return matrix

# def main():
#     print(bigger_matrix())
#     print(resizing_matrix(matrix))
# main()

bigger_matrix()
