def main():
    count = 0

    while count < 50:
        amount = 50 -count
        print(f"Amount Due: {amount}")
        coin = int(input("Insert Coin: "))
        if not (coin == 5 or coin == 10 or coin == 25):
            count = count
        else:
            count = count + coin
    if count >= 50:
        print(f"Change Owed: {count - 50}")

main()