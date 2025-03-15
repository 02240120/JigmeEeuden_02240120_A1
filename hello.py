def main():
    while True:
        print("\n__menu bar__")
        print('1.unit converter')
        print('2.min_max_finder')
        print('3.palindrome_checker')
        
        choose=input('enter your choice(1-3):')
        if choose=='1':
            unit_converter()
        elif choose=='2':
            ()
        elif choose=='3':
            print('exiting...')
            break
        else:
            print('invalid.please enter 1-3')
if __name__ == "__main__":
    main()
