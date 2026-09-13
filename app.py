def hkd_to_usd(hkd):
    rate = 7.8
    return hkd / rate

def main():
    print("HKD to USD Converter")
    print("--------------------")
    while True:
        user_input = input("Enter amount in HKD (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        try:
            hkd = float(user_input)
            usd = hkd_to_usd(hkd)
            print(f"{hkd} HKD -> {usd:.2f} USD")
        except ValueError:
            print("Error: please enter a number.")

if __name__ == "__main__":
    main()
