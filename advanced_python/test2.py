#pycentral script to test the python code
from netmiko import ConnectHandler

# Define the connection parameters
aruba_controller = {
    'device_type': 'aruba_os',
    'host': 'your_aruba_controller_ip',
    'username': 'your_username',
    'password': 'your_password',
    'port': 22,  # optional, default is 22
    'secret': 'your_enable_password',  # optional, if you need to enter enable mode
}

# Establish SSH connection
connection = ConnectHandler(**aruba_controller)

# Execute a command
output = connection.send_command('show version')

# Print the output
print(output)

# Close the connection
connection.disconnect()