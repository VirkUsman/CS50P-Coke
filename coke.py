                                                        # total_amount = 50
                                                        # print(f"amount due: {total_amount}")

amount_balance = 50

while amount_balance > 0:
    print("Amount Due:", amount_balance)

    coin = int(input("Insert Coin:"))

                                                        # if coin == 5 and coin == 10 and coin == 25:
                                                            # amount_balance = amount_balance - coin


    if coin == 5 or coin == 10 or coin == 25:
        amount_balance = amount_balance - coin
                                                        # amount_balance = abs(amount_balance - coin)
                                                        # print("Change Owned : ", amount_balance)

change_owned = abs(amount_balance)
print("Change Owed:",change_owned)