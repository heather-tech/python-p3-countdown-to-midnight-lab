# your code goes here!


def countdown(x):
    while x:
        print(f'{x} SECOND(S)!')
        x -= 1

    print("HAPPY NEW YEAR!")

def countdown_with_sleep(x):
    import time
    time.sleep(1)
    while x:
        print(f'{x} SECOND(S)!')
        x -= 1

    print("HAPPY NEW YEAR!")

