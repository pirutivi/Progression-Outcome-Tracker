# Writing to a text file
with open('credit.txt', 'w') as file:
    file.write("Progress-120,0,0\n")
    file.write("Progress(module trailer)-100,0,20\n")
    file.write("Module retriever-80,20,20\n")
    file.write("Module retriever-60,0,60\n")
    file.write("Exclude-40,0,80\n")

# Reading from a text file
with open('credit.txt', 'r') as file:
    for line in file:
        print(line.strip())
