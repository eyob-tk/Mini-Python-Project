#1. This is the answer for the first project:
while True:
    try:
       import requests
       url = "https://api.exchangerate-api.com/v4/latest/USD"
       response = requests.get(url)
       data = response.json()
       exchange_rate = data["rates"]["ETB"]
       usd = float(input("Enter amount in USD: "))
       etb = usd * exchange_rate
       print(f"Current USD to ETB rate: {exchange_rate}")
       print(f"Equivalent ETB: {etb}")
       break
    except ValueError:
        print("Your input is not a number!")


#2. This is answer for the second project:
while True:
    try: 
        num = list(map(int,input("Enter the numbers separated by space: ").split()))
        print("max = ", max(num))
        print("min = ", min(num))

        even_count = sum(1 for n in num if n % 2 == 0)
        odd_count = len(num) - even_count
        print(f"the number of even numbers from the given data is {even_count}")
        print(f"the number of odd numbers from the given data is {odd_count}")

        avg = sum(num)/len(num)
        print(f"the average of the numbers given is {avg}")

    except ValueError:
        print("Your input is not a number!")
    else:
        break