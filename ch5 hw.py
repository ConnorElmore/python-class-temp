def main():
    hour = 23
    minute = 59
    print("enter hours first and then minutes")
    hours = read(0,hour)
    minutes = read(0,minute)
    print(f'you entered {hours} hours and {minutes} minutes')



    

def read(low, high):
    
    value= int(input(f'enter a value between {low} and {high} '))
    while value < low or value > high:
        print("error - enter a correct value")
        value = int(input("enter a value"))
    return value
        
main()
