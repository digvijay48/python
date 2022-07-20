try:
    list=[8,9,6,7,45,90]
    print(list.index(90))
    print(max(list))
    print(sum(list))
    print("Sorted",sorted(list))
    print("Sorted List",list)
except ValueError as e:
    print("Value error happened",e)