from tabulate import tabulate
class Bill:

    def bill_2(total_parked_time):
        if(total_parked_time>0 and total_parked_time<=1):
            return 0
        elif(total_parked_time>1 and total_parked_time<=3):
            return total_parked_time*15
        elif(total_parked_time>3 and total_parked_time<=10):
            return total_parked_time*20
        else:
            return total_parked_time*30

    def bill_4(total_parked_time):
        if(total_parked_time>0 and total_parked_time<=1):
            return 0
        elif(total_parked_time>1 and total_parked_time<=3):
            return total_parked_time*25
        elif(total_parked_time>3 and total_parked_time<=10):
            return total_parked_time*35
        else:
            return total_parked_time*40
            
    def display_bill_rates(self):
        l = [['upto 1hr','free','free'],['1-3 hrs','Rs.15 Per hr','Rs.25 Per hr'],['3-10 hrs','Rs.20 Per hr','Rs.35 Per hr'],['More than 10 hrs','Rs.35 Per hr','Rs.45 Per hr']]
        table = tabulate(l,headers=['timing','two wheeler','four wheeler'],tablefmt='orgtbl')
        print(table)
