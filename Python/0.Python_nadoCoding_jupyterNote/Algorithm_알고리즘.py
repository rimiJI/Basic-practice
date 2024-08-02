# 버블 정렬 (Bubble Sort) 코드
def bubble_sort(arr):
    n = len(arr)  # 배열의 길이를 변수 n에 저장합니다.
    
    for i in range(n):  # 배열을 순회하기 위한 외부 루프입니다.
        # 외부 루프: 첫 번째 요소부터 마지막 요소까지 차례로 순회합니다.
        for j in range(0, n - i - 1):  # 내부 루프는 배열의 마지막에서 이미 정렬된 부분을 제외하고 순회합니다.
            # 내부 루프: 현재 요소와 다음 요소를 비교합니다.
            if arr[j] > arr[j + 1]:  # 현재 요소가 다음 요소보다 크다면,
                # 교환이 필요한 경우, 두 요소의 위치를 바꿉니다.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 두 요소의 위치를 바꿉니다.
    return arr  # 정렬된 배열을 반환합니다.

# 예시
numbers = [5, 2, 9, 1]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)  # 출력: [1, 2, 5, 9]




#선형 탐색 (Linear Search) 코드
def linear_search(arr, target):
    for i in range(len(arr)):  # 배열의 각 요소를 순회합니다.
        # 순회: 배열의 처음부터 끝까지 차례로 탐색합니다.
        if arr[i] == target:  # 현재 요소가 찾고자 하는 값과 일치하는지 확인합니다.
            # 일치 확인: 요소가 찾고자 하는 값인지 확인합니다.
            return i  # 일치하면 현재 인덱스를 반환합니다.
    return -1  # 배열을 다 순회해도 찾지 못하면 -1을 반환합니다.

# 예시
numbers = [3, 8, 2, 7, 5]
index = linear_search(numbers, 7)
print(index)  # 출력: 3 (7이 위치한 인덱스)




#이진 탐색 (Binary Search) 코드
def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # 배열의 양 끝을 가리키는 두 변수를 초기화합니다.
    # 초기화: 탐색 범위를 설정합니다.
    
    while left <= right:  # 왼쪽 포인터가 오른쪽 포인터보다 작거나 같은 동안 반복합니다.
        # 반복: 탐색 범위가 유효한 동안 반복합니다.
        mid = (left + right) // 2  # 중간 인덱스를 계산합니다.
        # 중간값 계산: 현재 탐색 범위의 중간 인덱스를 찾습니다.
        
        if arr[mid] == target:  # 중간 요소가 찾고자 하는 값과 같다면,
            # 일치 확인: 중간 요소가 찾는 값인지 확인합니다.
            return mid  # 중간 인덱스를 반환합니다.
        elif arr[mid] < target:  # 중간 요소가 찾고자 하는 값보다 작다면,
            # 비교: 중간 요소가 작으면 탐색 범위를 오른쪽으로 좁힙니다.
            left = mid + 1  # 왼쪽 포인터를 중간 인덱스의 오른쪽으로 이동합니다.
        else:  # 중간 요소가 찾고자 하는 값보다 크다면,
            # 비교: 중간 요소가 크면 탐색 범위를 왼쪽으로 좁힙니다.
            right = mid - 1  # 오른쪽 포인터를 중간 인덱스의 왼쪽으로 이동합니다.
    return -1  # 값을 찾지 못하면 -1을 반환합니다.

# 예시
numbers = [1, 3, 5, 7, 9]
index = binary_search(numbers, 7)
print(index)  # 출력: 3 (7이 위치한 인덱스)


################################################################







