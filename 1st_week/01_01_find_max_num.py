def find_max_num_ex1(array):
    for number in array:
        is_max_num = True
        for compare_number in array:
            if number < compare_number:
                is_max_num = False
        if is_max_num:
            return number

def find_max_num_ex2(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num

def find_max_num_ex3(array):
    temp_max = 0
    for i in range(len(array)):
        if array[i] > temp_max:
            temp_max = array[i]
    return temp_max



print("정답 = 6 / 현재 풀이 값 = ", find_max_num_ex1([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num_ex2([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num_ex3([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num_ex1([6, 6, 6]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num_ex2([6, 6, 6]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num_ex3([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num_ex1([6, 9, 2, 7, 1888]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num_ex2([6, 9, 2, 7, 1888]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num_ex3([6, 9, 2, 7, 1888]))
