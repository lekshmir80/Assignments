#program to convert each alternate index word to upper case in above string. 
string1 = """A computer is a machine that can be programmed to carry out sequences of
arithmetic or logical operations automatically. Modern computers can perform
generic sets of operations known as programs. These programs enable computers
to perform a wide range of tasks. A computer system is a complete computer
that includes the hardware operating system main software  and peripheral
equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""

lst = string1.split(" ")

x = list(filter(lambda x: lst.index(x)%2 == 0,lst))
upper =  list(map(lambda a: a.upper(),x))
print(upper)
