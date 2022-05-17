from tabulate import tabulate
from mall_architecture import mall_architecture
from bill_formate import Bill
bill = Bill()
def slot_avail(wheeler_check):
        if wheeler_check == '2':
            total_slot_vail = sum(x.count(0) for x in TW)
            if(total_slot_vail > 0):
                message = f"total {total_slot_vail} slots are available for two wheeler"
                print(message)
            else:
                print("no slot available")
        elif wheeler_check == '4':
            total_slot_vail = sum(x.count(0) for x in TW)
            if(total_slot_vail > 0):
                message = f"total {total_slot_vail} slots are available for four wheeler"
                print(message)
            else:
                print("no slot available")    


mall = mall_architecture()

TW = [[0 for i in range(mall.two_wheeler)] for j in range(mall.floor)]
FW = [[0 for i in range(mall.four_wheeler)] for j in range(mall.floor)]
TW_table = tabulate(TW,headers=['s '+str(x) for x in range(mall.two_wheeler)],tablefmt='orgtbl')
FW_table = tabulate(FW,headers=['s '+str(x) for x in range(mall.four_wheeler)],tablefmt='orgtbl')
print("parking display for two wheelers\n")
print(TW_table)
print("\nparking display for four wheelers\n")
print(FW_table)

print("\nSelect operation.")
print("P  : Park a Vehicle")
print("E  : Exit a lot")
print("DR : Display vehicle parking rates")
print("Q  : Quit an application")

while True:
    # take input from the user
    choice = input("Enter choice(P/E/DR/Q): ")

    # check if choice is one of the four options
    if choice in ('P', 'E', 'DR', 'Q'):
        if choice == 'P':
            print("vehicle is two wheeler or four")
            Wheel_check = input("Enter 2 for two wheeler and 4 for four wheeler:")
            slot_avail(Wheel_check)

        elif choice == 'E':
            pass


        elif choice == 'DR':
            bill.display_bill_rates()            

        else:
            if choice=='Q':
                break
    else:
        print("invalid Input")


