try:
	fo = open("t2t.txt", "r")
	fo.close()
except:
	fo = open("t2t.txt", "w")
	fo.write("0")
	fo.close()

s = fo.read()
print(s)