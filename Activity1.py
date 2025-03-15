def swap_three_numbers(a, b, c):
    return b, c, a

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        
        print(f"Before swapping: num1 = {num1}, num2 = {num2}, num3 = {num3}")
        
        num1, num2, num3 = swap_three_numbers(num1, num2, num3)
        
        print(f"After swapping: num1 = {num1}, num2 = {num2}, num3 = {num3}")
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()