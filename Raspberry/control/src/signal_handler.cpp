#include "signal_handler.h"

#include <iostream>
#include <signal.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

namespace robot {
namespace control {

void sig_handler(int sig);

bool ctrl_c_pressed = false;

signal_handler::signal_handler()
{
	struct sigaction sig_struct;
	sig_struct.sa_handler = sig_handler;
	sig_struct.sa_flags = 0;
	sigemptyset(&sig_struct.sa_mask);

	if (sigaction(SIGINT, &sig_struct, NULL) == -1) {
		std::cout << "Problem with sigaction" << std::endl;
		return;
	}
}

bool signal_handler::was_ctrl_c_pressed()
{
	return ctrl_c_pressed;
}

void sig_handler(int sig)
{
    write(0, "\nCtrl^C pressed in sig handler\n", 32);
    ctrl_c_pressed = true;
}

} // control
} // robot
