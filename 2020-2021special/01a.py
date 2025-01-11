

try:
    filename = input('Enter the file name: ')
    with open(filename, 'r') as file:
          myfile= file.read()
          print(myfile)

          wrd = myfile.split()
          print(wrd)


          words = {}
          
          for word in wrd:
                if word in words:
                      words[word] += 1
                else:
                      words[word] = 1
          for i, j in words.items():
                print(i, ": ", j)

                

except FileNotFoundError:
        print('File not found')
