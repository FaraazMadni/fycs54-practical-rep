file1=open("myfile.txt","w")

file1.write("Hello World\n")
file1.writelines("This Is FYCS \n I am in Batch2 \n My Roll NO Is 54 \n Hi \n I m amazing \n This is line 6 \n line 7 \n test \n abc \n")
file1.close()

file1=open("myfile.txt","r+")

print("Output of read function is")
print(file1.read())


file1.seek(0)

print("Output of Readline function is")
print(file1.readline())

print("Output of Read(9) function is")
print(file1.read(9))

file1.seek(0)

print("Output of Readline(9) function is")
print(file1.readline(9))

file1.seek(0)
print("Output of Readlines function is")
print(file1.readlines())
file1.close()
