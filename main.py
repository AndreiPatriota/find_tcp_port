import socket

def search_port_in_host(in_port_number: int, in_host_name: str):
    
    # Create a socket object and set the timeout
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        # Attempt to connect to the port
        result_cod = sock.connect_ex((in_host_name, in_port_number))
        if result_cod == 0:
            print(f"Port {in_port_number} is open on host {in_host_name}")
        else:
            print(f"Port {in_port_number} is closed on host {in_host_name}")
    except:
        print(f"Error scanning port {in_port_number}")

    sock.close()



host_names = [f'10.234.192.{val}' for val in range(101,240)]
port2test = int(input('Provide the TCP port number you wanna teste: '))

for host_name in host_names:
    search_port_in_host(port2test, host_name)

end_ofline = input('Type anything to quite: ')