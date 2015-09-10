count_of_three =  (1, 2, 5)
try:
	count_of_three[2] = "three"
except TypeError as ex:
	msg = ex.args[0]
print(msg)
