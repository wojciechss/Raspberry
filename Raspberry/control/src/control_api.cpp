#include <control/control_api.h>
#include <display/led_controller.h>
#include <iostream>
#include "signal_handler.h"

namespace robot {
namespace control {

void control_api::run()
{
	signal_handler sig_handler;
	display::led_controller led_ctrl;

	while (true) {
		led_ctrl.blink();
		if (sig_handler.was_ctrl_c_pressed()) {
			std::cout << "Ctrl^C Pressed" << std::endl;
			break;
		}
	}
    std::cout << "Exiting....." << std::endl;
}

} // control
} // robot
