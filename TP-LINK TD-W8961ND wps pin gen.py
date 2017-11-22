#Converting the last 6 characters of the MAC address to dec and calculating the checksum
#WORKS ONLY FOR TD-8961ND // may work for ZTE ZXHNH108L -- not tested

import sys

def main():
    while True:
        try:
            mac = raw_input("Please enter the MAC address of the router (or the last 6 symbols): ")
            mac = mac.replace(':', '').replace('-', '') #replace full MAC
            if len(mac) == 6 or len(mac) == 12:         #check if mac is valid
                if len(mac) == 12:
                    mac = mac[-6:]
            else:
                raise WPSException("Invalid MAC address: [%s]" % mac)
            pin = int(mac, 16)                          #hex->dec
            pin = int(str(pin)[-7:])                    #we don't need the first char -> so pin is 7 digits right now
            print str(pin) + str(checksum(pin))         #calculate checksum (last digit) and print the full pin
        except WPSException as e:
            print (str(e))
            sys.exit(1)
        except:
            print "Error!
            sys.exit(1)

def checksum(pin):
    accum = 0
    while pin:
        accum += (3 * (pin % 10))
        pin = int(pin / 10)
        accum += (pin % 10)
        pin = int(pin / 10)
    return ((10 - accum % 10) % 10)


if __name__=="__main__":
    main()
