listy=[4,3,2,1,0]
empty=[]
tup=("Let","it","be")
song=""
for nums in listy:
	empty.append(nums*4)
for words in tup:
	song+=words
print(empty)
print(song)