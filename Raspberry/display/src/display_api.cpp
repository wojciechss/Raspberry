#include <display/display_api.h>
#include <hardware/mini_driver_hw.h>
#include <iostream>
#include <hardware/gpio.h>

namespace robot {
namespace display {

void display_api::turn_led_on()
{
	hardware::mini_driver_hw mini_driver_holder;
	std::string to_send = "on;";
	mini_driver_holder.write_data(to_send);
}

void display_api::turn_led_off()
{
	hardware::mini_driver_hw mini_driver_holder;
	std::string to_send = "off;";
	mini_driver_holder.write_data(to_send);
}

void display_api::stop()
{
	hardware::mini_driver_hw mini_driver_holder;
	std::string to_send = "stop;";
	mini_driver_holder.write_data(to_send);
}

} // display
} // robot
