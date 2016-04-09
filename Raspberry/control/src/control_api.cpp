#include <control/control_api.h>
#include <iostream>
#include <chrono>
#include <thread>

#include "signal_handler.h"

namespace robot {
namespace control {

void control_api::run()
{
	signal_handler sig_handler;

	while (true) {
		std::this_thread::sleep_for(std::chrono::milliseconds(2));
		handle_mini_board();

		if (sig_handler.was_ctrl_c_pressed()) {
			std::cout << "Ctrl^C Pressed" << std::endl;
			disp.stop();
			break;
		}
	}
    std::cout << "Exiting....." << std::endl;
}

void control_api::handle_mini_board()
{
	double value = sensor.read_ultrasonic();
	if (value == 0) {
		return;
	}
	if (value > 0 && value < 20) {
		disp.turn_led_on();
	} else {
		disp.turn_led_off();
	}
}

} // control
} // robot
