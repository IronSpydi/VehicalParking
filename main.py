from tabulate import tabulate
from mall_architecture import mall_architecture
from bill_formate import Bill
from datetime import datetime
import json
from textwrap import indent


def slot_avail(wheeler_check):
        if wheeler_check == '2':
            total_slot_avail = sum(x.count(0) for x in TW)
            if(total_slot_avail > 0):
                """ message = f"total {total_slot_avail} slots are available for two wheeler"
                print(message) """
                return total_slot_avail
            else:
                return 0
                #print("no slot available")
        elif wheeler_check == '4':
            total_slot_avail = sum(x.count(0) for x in TW)
            if(total_slot_avail > 0):
                """ message = f"total {total_slot_avail} slots are available for four wheeler"
                print(message) """
                return total_slot_avail
            else:
                return 0
                # print("no slot available")    

def slot_provider(Wheel_check):
    if Wheel_check == '2':
        for i in range(mall.two_wheeler):
            for j in range(mall.floor):
                if TW[i][j] == 0:
                    slot_for_TW = [i,j]
                    print(slot_for_TW)
                    return slot_for_TW

    if Wheel_check == '4':
        for i in range(mall.four_wheeler):
            for j in range(mall.floor):
                if FW[i][j] == 0:
                    slot_for_FW = [i,j]  
                    return slot_for_FW



def token_generator(Wheel_check,vehicle_number):
    slot_booked = slot_provider(Wheel_check)
    if Wheel_check == '2':
        TW[slot_booked[0]][slot_booked[1]] = vehicle_number
        print(TW[slot_booked[0]][slot_booked[1]])
        date_time = datetime.now()
        Entry_time = date_time.strftime("%H:%M:%S")
        new_data = {vehicle_number:{'date & time':str(date_time),'vehicle Park time':str(Entry_time),'booked slot':slot_booked,'Wheeler type':Wheel_check}}
        with open('data_stor.json') as f:
            data = json.load(f)
        data.update(new_data)

        with open('data_stor.json','w') as f:
            json.dump(data,f,indent=2)
        """ message = f'this is your token on datetime {date_time} for vehicle type {Wheel_check} wheeler your slot is {slot_booked[0]} floor and {slot_booked[1]} slot'
        print(message) """
        print(data[vehicle_number])
        TW_table = tabulate(TW,headers=['s '+str(x) for x in range(mall.two_wheeler)],tablefmt='orgtbl')
        print(TW_table)

    if Wheel_check == '4':
        FW[slot_booked[0]][slot_booked[1]] = vehicle_number
        print(FW[slot_booked[0]][slot_booked[1]])
        date_time = datetime.now()
        Entry_time = date_time.strftime("%H:%M:%S")
        new_data = {vehicle_number:{'date & time':str(date_time),'vehicle Park time':str(Entry_time),'booked slot':slot_booked,'Wheeler type':Wheel_check}}
        with open('data_stor.json') as f:
            data = json.load(f)
        data.update(new_data)

        with open('data_stor.json','w') as f:
            json.dump(data,f,indent=2)

        print(data[vehicle_number])
        FW_table = tabulate(FW,headers=['s '+str(x) for x in range(mall.four_wheeler)],tablefmt='orgtbl')
        print(FW_table)


def exit_lot(vehicle_number):
    with open('data_stor.json','r') as f:
        data = json.load(f)
        vehicle_type = data[vehicle_number]['Wheeler type']
        print(vehicle_type)
        if vehicle_type == '2':
            date_time = datetime.now()
            exit_time = date_time.strftime("%H:%M:%S")
            entrytime = data[vehicle_number]['vehicle Park time']
            frmt = '%H:%M:%S'
            total_parked_time = datetime.strptime(exit_time,frmt) - datetime.strptime(entrytime,frmt) 
            hr = total_parked_time.seconds/3600
            bill = Bill()
            total_bill = bill.bill_2(hr)
            msg = f'your bill is {total_bill} rupee'
            print(msg)
            data[vehicle_number].update({'exit time':exit_time,'total parked time':str(total_parked_time),'bill':str(total_bill)+' rupee'})
            with open('data_stor.json','w') as f:
                json.dump(data,f,indent=2)
            TW[data[vehicle_number]['booked slot'][0]][data[vehicle_number]['booked slot'][1]] = 0
            TW_table = tabulate(TW,headers=['s '+str(x) for x in range(mall.two_wheeler)],tablefmt='orgtbl')
            print(TW_table)
        
        if vehicle_type == '4':
            date_time = datetime.now()
            exit_time = date_time.strftime("%H:%M:%S")
            entrytime = data[vehicle_number]['vehicle Park time']
            frmt = '%H:%M:%S'
            total_parked_time = datetime.strptime(exit_time,frmt) - datetime.strptime(entrytime,frmt) 
            hr = total_parked_time.seconds/3600
            bill = Bill()
            total_bill = bill.bill_4(hr)
            msg = f'your bill is {total_bill} rupee'
            print(msg)
            data[vehicle_number].update({'exit time':exit_time,'total parked time':str(total_parked_time),'bill':str(total_bill)+' rupee'})
            with open('data_stor.json','w') as f:
                json.dump(data,f,indent=2)

            FW[data[vehicle_number]['booked slot'][0]][data[vehicle_number]['booked slot'][1]] = 0
            FW_table = tabulate(FW,headers=['s '+str(x) for x in range(mall.four_wheeler)],tablefmt='orgtbl')
            print(FW_table)

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
with open('data_stor.json','w') as file:
    file.truncate(0)
    
    file.write('{}')

while True:
    # take input from the user
    choice = input("Enter choice(P/E/DR/Q): ")

    # check if choice is one of the four options
    if choice in ('P', 'E', 'DR', 'Q'):
        if choice == 'P':
            print("vehicle is two wheeler or four")
            Wheel_check = input("Enter 2 for two wheeler and 4 for four wheeler:")
            if slot_avail(Wheel_check)>0:
                park_confirm = input("Do you wanna park your vehicle ?(y/any key to cancle):")
                if park_confirm == 'y':
                    vehicle_number = input("enter your vehicle number : ")
                    token_generator(Wheel_check,vehicle_number)
            else:
                print("no slot available")
            
        elif choice == 'E':
            exit_confirm = input("Do you wanna exit?(y/any key to cancle):")
            if exit_confirm == 'y':
                vehicle_number = input("enter your vehicle number : ")
                with open('data_stor.json','r') as f:
                    data = json.load(f)
                    if vehicle_number in data:
                        exit_lot(vehicle_number)
                        print('done')
                    else:
                        print('please enter right vehicle number')


        elif choice == 'DR':
            bill = Bill()
            bill.display_bill_rates()            

        else:
            if choice=='Q':
                break
    else:
        print("invalid Input")


