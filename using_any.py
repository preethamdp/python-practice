if __name__ == '__main__':
    s = input()
   
    for each in ['.isalnum()','.isalpha()','.isdigit()','.islower()','.isupper()']:
        print(any(eval("c" +each ) for c in s))