#include "serial.h"

#include <stdio.h>
#include <cstring>
#include <unistd.h>			//Used for UART
#include <fcntl.h>			//Used for UART
#include <termios.h>		//Used for UART

namespace robot {
namespace hardware {

namespace constant {
	const static std::string device_name = "/dev/ttyUSB0";
}

serial::serial()
{
}

serial::~serial()
{
}

bool serial::begin_connection()
{
	//OPEN THE UART
	//The flags (defined in fcntl.h):
	//	Access modes (use 1 of these):
	//		O_RDONLY - Open for reading only.
	//		O_RDWR - Open for reading and writing.
	//		O_WRONLY - Open for writing only.
	//
	//	O_NDELAY / O_NONBLOCK (same function) - Enables nonblocking mode. When set read requests on the file can return immediately with a failure status
	//											if there is no input immediately available (instead of blocking). Likewise, write requests can also return
	//											immediately with a failure status if the output can't be written immediately.
	//
	//	O_NOCTTY - When set and path identifies a terminal device, open() shall not cause the terminal device to become the controlling terminal for the process.
	uart0_filestream = open(constant::device_name.c_str(), O_RDWR | O_NOCTTY | O_NDELAY);		//Open in non blocking read/write mode
	if (uart0_filestream == -1) {
		std::cout << "Error - Unable to open UART.  Ensure it is not in use by another application" << std::endl;
		return false;
	}

	//CONFIGURE THE UART
	//The flags (defined in /usr/include/termios.h - see http://pubs.opengroup.org/onlinepubs/007908799/xsh/termios.h.html):
	//	Baud rate:- B1200, B2400, B4800, B9600, B19200, B38400, B57600, B115200, B230400, B460800, B500000, B576000, B921600, B1000000, B1152000, B1500000, B2000000, B2500000, B3000000, B3500000, B4000000
	//	CSIZE:- CS5, CS6, CS7, CS8
	//	CLOCAL - Ignore modem status lines
	//	CREAD - Enable receiver
	//	IGNPAR = Ignore characters with parity errors
	//	ICRNL - Map CR to NL on input (Use for ASCII comms where you want to auto correct end of line characters - don't use for bianry comms!)
	//	PARENB - Parity enable
	//	PARODD - Odd parity (else even)
	struct termios options;
	tcgetattr(uart0_filestream, &options);
	options.c_cflag = B9600 | CS8 | CLOCAL | CREAD;		//<Set baud rate
	options.c_iflag = IGNPAR | ICRNL;
	options.c_oflag = 0;
	options.c_lflag = 0;
	tcflush(uart0_filestream, TCIFLUSH);
	tcsetattr(uart0_filestream, TCSANOW, &options);

	std::cout << "UART connection established" << std::endl;
	return true;
}

void serial::close_connection()
{
	std::cout << "UART connection closed" << std::endl;
	//----- CLOSE THE UART -----
	close(uart0_filestream);
}

bool serial::write_data(const std::string& data)
{
	int bytes_sent = write(uart0_filestream, data.c_str(), std::strlen(data.c_str()));
	if (bytes_sent < 0) {
		std::cout << "Error [serial_communcation]: write" << std::endl;;
		return false;
	}
	return true;
}

std::string serial::read_line()
{
	char rx_buffer[255];
	int pos = 0;
	char c;
	do {
		c = read_byte();
		if (c && c == '\n') {
			rx_buffer[pos++] = '\0';
		} else if (c) {
			rx_buffer[pos++] = c;
		}
	} while (c != '\n');

	return std::string(rx_buffer);
}

char serial::read_byte()
{
	char result = 0;
	if (uart0_filestream != -1) {
		char rx_buffer[1];
		int rx_length = read(uart0_filestream, rx_buffer, 1);
		if (rx_length < 0) {
			//An error occured (will occur if there are no bytes)
		} else if (rx_length == 0) {
			//No data waiting
		} else if (rx_length == 1) {
			//Byte received
			result = rx_buffer[0];
		}
	}
	return result;
}

} // hardware
} // robot
