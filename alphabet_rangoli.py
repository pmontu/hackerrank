"""
a

1/a
0 dots a

--b--
b-a-b
--b--

2/b
0 dots b to a back to b with single hiphen
2 dots b 2 dots again

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

3/c
0 dots c to C-3+0=a and back to c with single hipen followed by 0*2 dots
1*2 dots c to c-3+1=b and back to c with single hipen followed by 1*2 dots
"""

def get_sequence(from_ord, to_ord):
	res = []
	for o in range(from_ord, to_ord-1, -1):
		res.append(chr(o))
	for o in range(to_ord+1, from_ord+1):
		res.append(chr(o))
	return "-".join(res)

i=26

main_ch_ord = ord("a")+(i-1)
def execute(j):
	two_hipen_count = (j)*2
	to_alfabet_ord = main_ch_ord-i+j
	print(two_hipen_count*"-"+get_sequence(main_ch_ord, to_alfabet_ord+1)+two_hipen_count*"-")
for j in range(i-1,0,-1):
	execute(j)
for j in range(i):
	two_hipen_count = (j)*2
	execute(j)