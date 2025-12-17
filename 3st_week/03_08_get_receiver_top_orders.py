top_heights = [6, 9, 5, 7, 4]

#인덱스
#0 1 2 3 4

# for i in range(4, 0, -1):
#     for j in range(i - 1, -1, -1):
#         print(j)


def get_receiver_top_orders(heights):
    answer = [0] * len(heights) # 아무 것도 못 받으면 0으로 반환!
    for i in range(len(heights) - 1, 0, -1):  # O(N)
        for j in range(i - 1, -1, -1): # O(N)
            if heights[i] <= heights[j]:
               answer[i] = j + 1
               break
            print(i,j)
    return answer

print(get_receiver_top_orders(top_heights))

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ", get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 6] / 현재 풀이 값 = ", get_receiver_top_orders([3,9,9,3,5,7,2]))