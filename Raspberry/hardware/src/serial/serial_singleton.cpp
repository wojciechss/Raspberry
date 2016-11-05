#include "serial_singleton.h"
//#include "termios_serial/termios_serial.h"
#include "boost_serial/boost_serial.h"

namespace robot {
namespace hardware {

serial_singleton::serial_singleton()
{
	serial_holder = serial_handle(new boost_serial());
	//serial_holder = serial_handle(new termios_serial());
}

serial_singleton::~serial_singleton()
{
}

std::string serial_singleton::read_line()
{
	return serial_holder->read_line();
}

bool serial_singleton::write_data(const std::string& data)
{
	return serial_holder->write_data(data);
}

} // hardware
} // robot
