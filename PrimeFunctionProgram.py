def prime(n):
	"""
	This function will seek to find out if a list of numbers,
	from 0 to n, has prime numbers.
	"""
    listx = list()
    for num in range(2, n+1):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            listx.append(num)
        else:
        	return 'Not prime'
    return listx


print prime (10)
# Function call.
