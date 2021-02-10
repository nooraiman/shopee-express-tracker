import requests
import os
import tzlocal
from datetime import datetime

# Clear Console On Windows/Linux
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Format SPX Tracking Number To Be Accurate
def formatSPX(tr):
    length = 3
    status = False
    los = []
    for i in range(0, len(tr), length):
        los.append(tr[i:length+i])
    
    if los[0] == 'SPX':
        status = True
    else:
        status = False

    return status

def exit():
    ex = str(input("\nDo You Want To Continue? (Y/N):"))
    ex = ex.upper()

    print("\n")
    if ex == 'Y':
        cls()
        main()
    else:
        return


def main():
    print("##############################")
    print("# ShopeeExpress Tracker v0.1 #")
    print("# Coded By Noor Aiman        #")
    print("##############################\n")

    tr_num = str(input("Tracking Number: "))
    tr_num = tr_num.upper()

    if(formatSPX(tr_num)):
        url = "https://shopeexpress.com.my/api/v2/fleet_order/tracking/search"
        payload = {"sls_tracking_number":tr_num}
        res = requests.get(url,payload)

        res = res.json()

        if res['message'] == 'Success':

            tr_data = res['data']

            for key in tr_data['tracking_list']:
                print("\nStatus: ", key['status'])

                # Get Local Time
                unix_time = key['timestamp']
                local_timezone = tzlocal.get_localzone()
                local_time = datetime.fromtimestamp(unix_time,local_timezone)
                print("Time: ", local_time)

                print("Details: ", key['message'])
        else:
            print("Status: Tracking Not Found!")

    else:
        print("Wrong Format!")

    exit()

main()