def to_string(li): #리스트를 문자열로 변환(글자 사이 공백 추가)
    answer = ''
    for i in li:
        answer = answer + str(i) + ' '
    return answer.rstrip()

def quicksort(li):
    if len(li) <= 1:
        return li

    left = []
    right = []
    pivot = li[-1]
    for element in li[:-1]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)
    
    strleft = to_string(left)
    strright = to_string(right)
    print('\033[93m' + strleft, '\033[96m' + "/" + str(pivot) + "/" , '\033[91m' + strright)
    result = quicksort(left) + [pivot] + quicksort(right)
    return result
    
Input = [3, 8, 5, 6, 9, 1 ,4, 2, 7]
Output = quicksort(Input)
stringOutput = to_string(Output)
print('\033[37m' + stringOutput)