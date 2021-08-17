#program to find all the words from above string where first letter of word is 'c' and last letter is 'r'

string1 = """A computer is a machine that can be programmed to carry out sequences of
arithmetic or logical operations automatically. Modern computers can perform
generic sets of operations known as programs. These programs enable computers
to perform a wide range of tasks. A computer system is a complete computer
that includes the hardware operating system main software  and peripheral
equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""

lst = string1.split(" ")
lst_fil = list(filter(lambda x : x != "" and x[0] == "c" and x[-1] == "r" , lst))
print(lst_fil)
