i = 1
lst = []
r = int(input("Enter the number of member in list "))

for i in range(r):
	k =int(input("Enter member "))
	i +=1
	lst.append(k)

def Reverse(lst):

	new_list = lst[::-1]
	return new_list


print(Reverse(lst))
