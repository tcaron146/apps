def addition(num1, num2):
    total = num1+num2
    return total;

def ageToDays(age):
    days = age * 365
    return days

def lastitem(list):
    return list[-1]

def main():
    list = [1,2,3]
    print(addition(3,2))
    print(ageToDays(65))
    print(lastitem(list))
    
    #Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
    track = []
    for i in range(1500, 2701):
        mult = i%5;
        div = i%7;
        if div==0 and mult==0:
            track.append(str(i))
    print(','.join(track))

main()