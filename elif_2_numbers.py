def main(a,b):
    if type(a) == str and type(b) ==str:
        if a == b:
            return 1
        elif a != b and len (a) > len (b):
            return 2
        elif a != b and b == 'learn':
            return 3
        else:  
            return 0


if __name__ == "__main__":
    print(main('123','123'))
    print(main('123','abc'))
    print(main('123','12'))
    print(main('123','learn'))