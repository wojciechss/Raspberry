#ifndef SERIAL_H_
#define SERIAL_H_

#include <iostream>

namespace robot {
namespace hardware {

class serial {

public:
	serial();
	~serial();

	bool begin_connection();
	void close_connection();

	std::string read_line();
	bool write_data(const std::string& data);

private:
	char read_byte();

private:
	int uart0_filestream = -1;

};

} // hardware
} // robot

#endif /* SERIAL_H_ */
