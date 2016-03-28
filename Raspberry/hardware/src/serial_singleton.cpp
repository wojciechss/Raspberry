#include "serial_singleton.h"

namespace robot {
namespace hardware {

serial_singleton::serial_singleton()
{
	serial_holder.begin_connection();
}

serial_singleton::~serial_singleton()
{
	serial_holder.close_connection();
}

std::string serial_singleton::read_line()
{
	return serial_holder.read_line();
}

bool serial_singleton::write_data(const std::string& data)
{
	return serial_holder.write_data(data);
}

} // hardware
} // robot
