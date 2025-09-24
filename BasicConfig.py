import serial
import time

def configure_device(port, hostname, username, passwrod, domain, baudrate=1600):
    try:
        # Open serial port
        ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # Wait for the connection to establish
        ser.write("Conexión establecida☑️")
        ser.write(f"{port}\r\n".encode())
        ser.write(f"enable\r\n".encode())
        ser.write(f"configure terminal\r\n".encode())
        ser.write(f"hostname {hostname}\r\n".encode())
        ser.write(f"username {username} password {passwrod}\r\n".encode())
        ser.write(f"ip domain-name {domain}\r\n".encode())
        ser.write(f"generate rsa key modulus 1024\r\n".encode())
        ser.write(f"line vty 0 4\r\n".encode())
        ser.write(f"login local\r\n".encode())
        ser.write(f"transport input ssh\r\n".encode())
        ser.write(f"transport output ssh\r\n".encode())
        ser.write(f"exit\r\n".encode())
        ser.write(f"line console 0\r\n".encode())
        ser.write(f"login local\r\n".encode())
        ser.write(f"write memory\r\n".encode())
        ser.write("Conexión cerrada☑️")
        ser.close()
    except serial.SerialException as e:
        print(f"❎Error: {e}")
        
r1 = configure_device("COM3", "R1", "cisco", "cisco", "example.com")