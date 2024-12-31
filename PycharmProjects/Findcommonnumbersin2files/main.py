# import pandas
#
# data1 = pandas.read_csv('file1.txt', delimiter='\t')
# data2 = pandas.read_csv('file2.txt', delimiter='\t')
# num_list1 = data1.num1.to_list()
# num_list2 = data2.num2.to_list()
#
# result = [num for num in num_list1 if num in num_list2]
#
# print(result)

with open("file1.txt") as file1:
    num_list1 = file1.readlines()


with open("file2.txt") as file2:
    num_list2 = file2.readlines()

result = [int(num) for num in num_list1 if num in num_list2]
print(num_list1)
print(result)