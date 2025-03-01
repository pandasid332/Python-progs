
LINE = 3
COLUMN = 5
ROW = 3

SYNBOLS = {
    1: "🍒",
    2: "🍊",
    3: "🍋",
    4: "🍉",
    5: "🍇"
}

def get_deposite():
    while True:
        try:
            deposite = int(input("Enter your deposite: "))
            if deposite < 0:
                print("Deposite should be positive")
                continue
            return deposite
        except ValueError:
            print("Enter a valid number")
    return deposite
def get_line():
    while True:
        line = input("Enter the number of lines(1 - {}): ".format(LINE))
        if line.isdigit() and 0<int(line)<=LINE:
            break
        print(f"Enter a number between 1 and {LINE}")
    return int(line)

def get_bet(deposite):
    while True:
        bet = input("Enter your bet: ")
        if bet.isdigit() and 0 < int(bet) <= deposite:
            break
        print(f"Enter a number between 1 and {deposite}")
    return int(bet)


def main():
    deposite = get_deposite()
    line = get_line()
    bet=get_bet(deposite)
    total_bet = bet * line
    deposite -= total_bet
    print(f"Your deposite is {deposite}")
    print(f"Your line is {line}")
    print(f"Your bet is {bet}")
    print(f"Your total bet is {total_bet}")
    for symbol in SYNBOLS.values():
        print(symbol)
    
if __name__ == "__main__":
    main()