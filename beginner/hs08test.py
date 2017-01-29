withdraw, account = [float(v) for v in input().split()]
# process the withdraw only if it's a multiple of 5
if withdraw % 5 == 0 and withdraw + 0.5 < account:
    account = account - withdraw - 0.5
print("%.2f" % account)