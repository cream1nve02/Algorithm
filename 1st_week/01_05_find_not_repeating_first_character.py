from pickletools import read_stringnl_noescape_pair
from turtledemo.sorting_animate import instructions1

input = "abadabac"

def find_not_repeating_first_character(string):
    # 반복되지 않는 첫번째 알파벳
    # 반복되는지 아닌지를 판단해야 함
    # alphabet_occurence_array
    # string에서 알파벳의 빈도수를 찾는다.
    # 그리고 빈도수가 1인 알파벳들 중에서 string에서 뭐가 먼저 나왔는지를 차장본다,
    occurrence_array =find_alphabet_occurrence_array(string)
    not_repeating_character_array = []
    for index in range(len(occurrence_array)):
        alphabet_occurrence = occurrence_array[index]
        if alphabet_occurrence == 1:

            not_repeating_character_array.append(chr(index+ord("a")))
    for char in string:
        if char in not_repeating_character_array:
            return char
    return "_"

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] +=1

    return alphabet_occurrence_array

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))

