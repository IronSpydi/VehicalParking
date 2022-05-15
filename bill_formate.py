class TwoWheelerBill:
    def bill_2(total_parked_time):
        if(total_parked_time>0 and total_parked_time<=1):
            return 0
        elif(total_parked_time>1 and total_parked_time<=3):
            return total_parked_time*15
        elif(total_parked_time>3 and total_parked_time<=10):
            return total_parked_time*20
        else:
            return total_parked_time*30

class FourWheelerBill:
    def bill_4(total_parked_time):
        if(total_parked_time>0 and total_parked_time<=1):
            return 0
        elif(total_parked_time>1 and total_parked_time<=3):
            return total_parked_time*25
        elif(total_parked_time>3 and total_parked_time<=10):
            return total_parked_time*35
        else:
            return total_parked_time*40