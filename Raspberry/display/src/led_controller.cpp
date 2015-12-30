#include <display/led_controller.h>
#include <hardware/gpio.h>
#include <iostream>
#include <thread>

namespace robot {
namespace display {

namespace constant {
	const int blink_time_ms = 4000;
}

led_controller::led_controller(std::shared_ptr<robot::hardware::gpio> gpio)
{
	gpio_handler = gpio;
	gpio_handler->export_gpio();
	std::cout << "GPIO pins exported" << std::endl;
	gpio_handler->setdir_gpio("out");
	std::cout << "Set GPIO pin directions" << std::endl;
}

led_controller::~led_controller()
{
	std::cout << "unexporting pins" << std::endl;
	gpio_handler->unexport_gpio();
}

void led_controller::blink()
{
	turn_led_off();
	std::this_thread::sleep_for(std::chrono::milliseconds(constant::blink_time_ms));
	turn_led_off();
	std::this_thread::sleep_for(std::chrono::milliseconds(constant::blink_time_ms));
}

void led_controller::turn_led_on()
{
	std::cout << "Turn led on" << std::endl;
	gpio_handler->setval_gpio("1");
}

void led_controller::turn_led_off()
{
	std::cout << "Turn led off" << std::endl;
	gpio_handler->setval_gpio("0");
}

} // display
} // robot
