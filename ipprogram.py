#user input or the main menu
def classfull(input_ip):

    
    #choose the class of those ip
    ip_1st_segment=input_ip[0]
    if (1<=int(ip_1st_segment)<=126):
        
        ip_class="A"
        ip_part=input_ip[0]+'.'
        
    elif (128<=int(ip_1st_segment)<=191):

        ip_class="B"
        ip_part=input_ip[0]+'.'+input_ip[1]+'.'

    elif (192<=int(ip_1st_segment)<=223):
        
        ip_class="C"
        ip_part=input_ip[0]+'.'+input_ip[1]+'.'+input_ip[2]+'.'

    else:
        print('Class D and E addresses cannot be used for subnetting.')
        return


    #user input for the numbers of subnets
    raw_subnet_amount=int(input('Enter required number of subnets:'))
    power=len(bin(raw_subnet_amount-1)[2:])
    subnet_amount=2**power#calculatable amount

    #calculation
    adding_number=(2**24)/subnet_amount

    subnet_ip_net,subnet_ip_bc=[],[]

    for i in range(subnet_amount):
        subnet_ip_net.append(bin(int(adding_number*i))[2:].zfill(24))
        subnet_ip_bc.append(bin(int(adding_number*(i+1)-1))[2:].zfill(24))



    #output
    #table heading raw
    print('')
    print('Subnet'.ljust(8) + 'Network Address'.ljust(17) + 'Broadcast IP'.ljust(20))
    #class c
    if (ip_class=='C'):
        for i in range(subnet_amount):

            print(('['+str(i+1)+']').ljust(8),end='')
            print((ip_part+f'{int(subnet_ip_net[i][:8],2)}').ljust(17),end='')
            print((ip_part+f'{int(subnet_ip_bc[i][:8],2)}').ljust(17))
        #subnetmask
        print('')
        print(f"Subnet Mask : 255.255.255.{int(('1'*power+'0'*(8-power)),2)}")


    #class B
    if (ip_class=='B'):
        for i in range(subnet_amount):

            print(('['+str(i+1)+']').ljust(8),end='')
            print((ip_part+f'{int(subnet_ip_net[i][:8],2)}.'+f'{int(subnet_ip_net[i][8:16],2)}').ljust(17),end='')
            print((ip_part+f'{int(subnet_ip_bc[i][:8],2)}.'+f'{int(subnet_ip_bc[i][8:16],2)}').ljust(17))
        #subnetmask
        print('')
        print(f"Subnet Mask : 255.255.{int(('1'*power+'0'*(16-power))[:8],2)}.{int(('1'*power+'0'*(16-power))[8:],2)}")

    #class A
    if (ip_class=='A'):
        for i in range(subnet_amount):

            print(('['+str(i+1)+']').ljust(8),end='')
            print((ip_part+f'{int(subnet_ip_net[i][:8],2)}.'+f'{int(subnet_ip_net[i][8:16],2)}.'+f'{int(subnet_ip_net[i][16:],2)}').ljust(17),end='')
            print((ip_part+f'{int(subnet_ip_bc[i][:8],2)}.'+f'{int(subnet_ip_bc[i][8:16],2)}.'+f'{int(subnet_ip_bc[i][16:],2)}').ljust(17))
        #subnetmask
        print('')
        print(f"Subnet Mask : 255.{int(('1'*power+'0'*(24-power))[:8],2)}.{int(('1'*power+'0'*(24-power))[8:16],2)}.{int(('1'*power+'0'*(24-power))[16:],2)}")

    
def classless(input_ip,raw_input):
    #convert ip in to binary ex-111000110111011010

    input_ip_str_raw=bin(int(input_ip[0]))[2:].zfill(8)+bin(int(input_ip[1]))[2:].zfill(8)+bin(int(input_ip[2]))[2:].zfill(8)+bin(int(input_ip[3]))[2:].zfill(8)
    #filtering the valid ip and convert it into int 
    real_ip_in_int=int(input_ip_str_raw[:int(raw_input[1])]+'0'*(32-int(raw_input[1])),2)

    #subnet input
    raw_subnet_amount=int(input('Enter required number of subnets:'))
    accual_numbers_of_hosts,power=[],[]

    for i in range(raw_subnet_amount):

        raw_numbers_of_hosts=int(input(f'Number of host IPs required for subnet {i+1}:'))

        power.append(len(bin(raw_numbers_of_hosts-1)[2:]))
         
        calculatable_number=2**len(bin(raw_numbers_of_hosts-1)[2:])

        accual_numbers_of_hosts.append(calculatable_number)

    power.sort()
    power.reverse()
    accual_numbers_of_hosts.sort()
    accual_numbers_of_hosts.reverse()

    #process
    sub_ip_address=[real_ip_in_int,]
    sub_bc_address=[]
    for i in range(raw_subnet_amount):

        sub_ip_address.append(sub_ip_address[i]+accual_numbers_of_hosts[i])
        sub_bc_address.append(sub_ip_address[i]+(accual_numbers_of_hosts[i]-1))

    #output
    print('-' * 75)
    print(f"| {'NOH':<4} | {'Network IP':<20} | {'Broadcast IP':<20} | {'Subnet Mask':<15} |")
    print('-' * 75)
    for i in range(raw_subnet_amount):
        #network IP
        network_ip = f"{int((bin(sub_ip_address[i])[2:].zfill(32))[:8],2)}." \
                     f"{int((bin(sub_ip_address[i])[2:].zfill(32))[8:16],2)}." \
                     f"{int((bin(sub_ip_address[i])[2:].zfill(32))[16:24],2)}." \
                     f"{int((bin(sub_ip_address[i])[2:].zfill(32))[24:],2)}/{32-power[i]}"
    
        #broadcast IP
        broadcast_ip = f"{int((bin(sub_bc_address[i])[2:].zfill(32))[:8],2)}." \
                       f"{int((bin(sub_bc_address[i])[2:].zfill(32))[8:16],2)}." \
                       f"{int((bin(sub_bc_address[i])[2:].zfill(32))[16:24],2)}." \
                       f"{int((bin(sub_bc_address[i])[2:].zfill(32))[24:],2)}/{32-power[i]}"
    
        #subnet mask
        subnet_mask = f"{int(('1'*(32-power[i])+'0'*power[i])[:8],2)}." \
                      f"{int(('1'*(32-power[i])+'0'*power[i])[8:16],2)}." \
                      f"{int(('1'*(32-power[i])+'0'*power[i])[16:24],2)}." \
                      f"{int(('1'*(32-power[i])+'0'*power[i])[24:],2)}"
    
        print(f"| {str(accual_numbers_of_hosts[i]):<4} | {network_ip:<20} | {broadcast_ip:<20} | {subnet_mask:<15} |")
    print('-' * 75)
    
    
    



def menu():
    print('Example inputs: 192.22.33.0/24 or 172.33.22.11')  
    raw_input=input('ip address:').split('/')
    input_ip=raw_input[0].split('.')

    #ip validity checking
    if (len(input_ip)!=4):
        
        print('A valid IPv4 address should contain four numbers, each separated by a dot.')
        return

    else:

        for i in range(4):
            if not(0<=int(input_ip[i])<=255):
                print('Every number in the IP address must be within the range of 0 to 255.')
                return

    #select the iptype and pass to a different module
    if (len(raw_input)==1):
        classfull(input_ip)
        return
    elif (len(raw_input)==2):
        classless(input_ip,raw_input)
        return
    else:
        print('Enter a valid IPv4 address (e.g., 172.33.22.11) or CIDR notation (e.g., 192.22.33.0/24). Each number must be between 0 and 255.')

menu()
