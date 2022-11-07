t = input()
st = []
while(t!="="):
	if( t in "0123456789" or (len(t)>1)):
		st+=[int(t)]

	elif(t=="+"):
		b = st[-1]+st[-2]
		st.pop(-1)
		st.pop(-1)
		st+=[b]
	elif(t=="*"):
		b = st[-1]*st[-2]
		st.pop(-1)
		st.pop(-1)
		st+=[b]
	elif(t=="-"):
		b = st[-2]-st[-1]
		st.pop(-1)
		st.pop(-1)
		st+=[b]
	#print("***********", len(st))
	t = input()
print(st[0])

