import itertools

m = int(input('Enter the base for modular arithematic: '))
print('Enter the numbers of the set (Space seperated, MAX 8): ')
ls = sorted(list(map(int, input().split())))

# creating all the possible permutations of the elements of the given set for ease of use
# permutations with 2 elements each
xy = itertools.permutations(ls,2)
# permutations with 3 elements each
xyz = itertools.permutations(ls,3)

# Common functions used for both Addition and Multiplication
def identity(a,b,operator):
	if operator == 'add':
		if (a+b)%m == a:
			return True
	else:
		if (a*b)%m == a:
			return True
	return False

def inverse(a,b,operator):
	if operator == 'add':
		if (a+b)%m == 0:
			return True
	else:
		if (a*b)%m == 1:
			return True
	return False

def closure(a,b,operator):
	if operator == 'add':
		if (a+b)%m in ls:
			return True
	else:
		if (a*b)%m in ls:
			return True
	return False

def associative(x,y,z,operator):
	if operator == 'add':
		if ((x+y)+z)%m == (x+(y+z))%m:
			return True
		else:
			return False
	else:
		if ((x*y)*z)%m == (x*(y*z))%m:
			return True
		else:
			return False

def commutative(a,b,operator):
	if operator == 'add':
		if (a+b)%m == (b+a)%m:
			return True
	else:
		if (a*b)%m == (b*a)%m:
			return True
	return False

# Addition specific functions
def a1():
	for two in xy:
		a = two[0]
		b = two[1]
		if not closure(a,b,'add'):
			return False
	return True

def a2():
	for three in xyz:
		a = three[0]
		b = three[1]
		c = three[2]
		if not associative(a,b,c,'add'):
			return False
	return True

def a3():
	flag = [0 for i in range(len(ls))]
	for i in range(len(ls)):
		a = ls[i]
		for j in range(len(ls)):
			b = ls[j]
			if (a+b)%m == a:
				flag[i] = 1
	if sum(flag) == len(ls):
		return True
	else:
		return False

def a4():
	flag = [0 for i in range(len(ls))]
	for i in range(len(ls)):
		a = ls[i]
		for j in range(len(ls)):
			b = ls[j]
			if (a+b)%m == 0:
				flag[i] = 1
	if sum(flag) == len(ls):
		return True
	else:
		return False

def a5():
	for two in xy:
		a = two[0]
		b = two[1]
		if not commutative(a,b,'add'):
			return False
	return True

# Multiplication specific functions
def m1():
	for two in xy:
		a = two[0]
		b = two[1]
		if not closure(a,b,'mul'):
			return False
	return True

def m2():
	for three in xyz:
		a = three[0]
		b = three[1]
		c = three[2]
		if not associative(a,b,c,'mul'):
			return False
	return True

def m3():
	for three in xyz:
		a = three[0]
		b = three[1]
		c = three[2]
		if not ((a*(b+c))%m == a*b + a*c) and (((a+b)*c)%m == a*c + b*c):
			return False
	return True

def m4():
	for two in xy:
		a = two[0]
		b = two[1]
		if not commutative(a,b,'mul'):
			return False
	return True

def m5():
	flag = [0 for i in range(len(ls))]
	for i in range(len(ls)):
		a = ls[i]
		for j in range(len(ls)):
			b = ls[j]
			if (a*b)%m == a:
				flag[i] = 1
	if sum(flag) == len(ls):
		return True
	else:
		return False

def m6():
	for two in xy:
		a = two[0]
		b = two[1]
		if a != 0 and b != 0 and (a*b)%m == 0:
			return False
	return True

def m7():
	flag = [0 for i in range(len(ls))]
	for i in range(len(ls)):
		a = ls[i]
		for j in range(len(ls)):
			b = ls[j]
			if (a*b)%m == 1:
				flag[i] = 1
	if sum(flag) == len(ls):
		return True
	else:
		return False


# check list
print('\n**************************\n')
if a1() and a2() and a3() and a4():
	print('Normal Group\t->\tTrue')
	if not a5():
		print('Abelian Group\t\t->\tFalse')
	else:
		print('Abelian Group\t->\tTrue')
		if m1() and m2() and m3():
			print('Normal Ring\t\t->\tTrue')
			if not m4():
				print('Commutative Ring->\tFalse')
			else:
				print('Commutative Ring->\tTrue')
				if m5() and m6():
					print('Integral Domain\t->\tTrue')
					if not m7():
						print('Field\t\t\t->\tFalse')
					else:
						print('Field\t\t\t->\tTrue')
				else:
					print('Integral Domain\t->\tFalse')
		else:
			print('Normal Ring\t\t->\tFalse')
else:
	print('Not a Group')
print('\n**************************\n')