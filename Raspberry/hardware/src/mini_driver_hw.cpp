#include <hardware/mini_driver_hw.h>
#include "serial/serial_singleton.h"

namespace robot {
namespace hardware {

std::string mini_driver_hw::read_line()
{
	return serial_singleton::instance().read_line();
}

bool mini_driver_hw::write_data(const std::string& data)
{
	return serial_singleton::instance().write_data(data);
}

} // hardware
} // robot
