

while True:
    try:
        inp = input('Enter a number less than 200 for fizzbuzz to solve: ')
        inp = int(inp) + 1
        if inp >= 202:
            print('That number is too large')
            continue
        def fizzbuzz_block():
            if n % 15 == 0:
                print('Fizzbuzz')
            elif n % 5 == 0:
                print('Buzz')
            elif n % 3 == 0:
                print ('Fizz')
            else:
                print n
        for n in range(1, inp):
            fizzbuzz_block()
        print ('All done')
        break
    except:
        print('Please enter a numeric value!')
        continue
    
       
        
    
    
        
