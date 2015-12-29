#include <control/control_api.h>
#include <iostream>
#include "signal_handler.h"

namespace robot {
namespace control {

void control_api::run()
{

	signal_handler sig_handler;
	while (true) {
		int data;
		std::cin >> data;
		std::cout << "Pressed: "<< data << std::endl;

		if (sig_handler.was_ctrl_c_pressed()) {
			std::cout << "Ctrl^C Pressed" << std::endl;
			break;
		}
	}
    std::cout << "Exiting....." << std::endl;
}

} // control
} // robot
