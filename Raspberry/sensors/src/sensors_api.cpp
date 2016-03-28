#include <sensors/sensors_api.h>
#include <hardware/mini_driver_hw.h>
#include <stdlib.h>

#include <iostream>

namespace robot {
namespace sensors {

double sensors_api::read_ultrasonic()
{
	hardware::mini_driver_hw mini_driver_holder;
	std::string value = mini_driver_holder.read_line();
	return atof(value.c_str());
}

} // sensors
} // robot
