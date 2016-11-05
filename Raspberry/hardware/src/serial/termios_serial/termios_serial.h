#ifndef TERMIOS_SERIAL_H_
#define TERMIOS_SERIAL_H_

#include "../serial.h"
#include <iostream>

namespace robot {
namespace hardware {

class termios_serial : public serial {

public:
	termios_serial();
	virtual ~termios_serial();

	virtual std::string read_line();
	virtual int write_data(const std::string& data);

private:
	bool begin_connection();
	void close_connection();
	char read_byte();

private:
	int uart0_filestream = -1;

};

} // hardware
} // robot

#endif /* TERMIOS_SERIAL_H_ */
