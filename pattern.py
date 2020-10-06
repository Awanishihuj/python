'''
write a peogram to take user input in bool and print half primide 
if true then
*
**
***
****
*****
if false then 
*****
****
***
**
*
'''
choice = bool(input('yes for forward pattern\nLeft blank for backward pattern\nEnter your choice: '))
print('-'*50)
n = int(input('Enter the Range for pattern: '))
if choice == True:
    z = 1
    print('-'*50)
    while(z<=n):
        print("*"*z)
        z = z+1
    print('-'*50)
elif choice == False:
    print('-'*50)
    z = n
    while(z > 0):
        print('*'*z)
        z = z-1
    print('-'*50)