my_hobby=['coding','reading','travelling','eating','watching']
print "my first hobby is {1} and the second are {0} and {ketiga}".format(my_hobby[2],"stalking",ketiga=my_hobby[3])

#jumlah
len(my_hobby)
print "i have {} hobbies".format(len(my_hobby))

#for
for hobby in my_hobby:
	print hobby

#append
my_hobby.append('sleeping')
print my_hobby

#input to append
hobby=raw_input("input a hobby:")
my_hobby.append(hobby)
print my_hobby

#ganti hobby
my_hobby.insert(0,'listening')
print my_hobby

print my_hobby.index('reading')

my_hobby.remove('coding')
print my_hobby

#hapus list dengan indeks
print my_hobby.pop(4)
print my_hobby

#urutkan
my_hobby.sort()
print my_hobby

#balik arah
my_hobby.reverse()
print my_hobby
