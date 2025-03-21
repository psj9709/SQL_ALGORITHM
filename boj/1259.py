num = ''

while num != '0':
    num = input()
    if num == '0':
        break
    reverse_num = num[::-1]

    if num == reverse_num:
        print('yes')
    else:
        print('no')

