def check_duplicate_list_all(l_2d):
    kiemtra = []
    unique_list = [x for x in l_2d if x not in kiemtra and not kiemtra.append(x)]
    if len(l_2d) != len(unique_list):
        return "Tồn tại phần tử trùng lặp trong list"
    else:
        return "Không có phần tử trùng lặp trong list"


l_2d1 = [[0, 0], [0, 1], [1, 1], [1, 0]]
print(check_duplicate_list_all(l_2d1))
#>> Không có phần tử trùng lặp trong list

l_2d2 = [['a', 'b'], ['a', 'b'], [1, 1], [1, 1]]
print(check_duplicate_list_all(l_2d2))
#>> Không có phần tử trùng lặp trong list
