from main import TW
from main import FW
class slot:
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
