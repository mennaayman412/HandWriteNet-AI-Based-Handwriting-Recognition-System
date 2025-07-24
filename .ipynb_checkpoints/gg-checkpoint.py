list1 = [3, 1, 4,4,4,5]
list2 = [2, 5, 0,5,5]
double=[]
for i in list1 :
    if i in list2:
        if i in double:
            continue
        else:
            double.append(i)
            continue
    else:
        list2.append(i)

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

print(set(bubble_sort(list2)))
print(double)
