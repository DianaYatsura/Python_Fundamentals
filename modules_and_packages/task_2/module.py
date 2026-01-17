"""Write python module. All your code will be writed in file module.py. If we run pyhon module.py it must print
'Hello world!' in terminal. But if we import this file we must be able to call function say_greeting,
which obtain one argument name and print in terminal 'Hello {name}'."""

def say_greeting(name):
    print (f'Hello {name}')

if __name__ == '__main__':
    print ("Hello world!")

    