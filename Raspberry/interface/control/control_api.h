#ifndef CONTROL_API_H_
#define CONTROL_API_H_

#include <display/display_api.h>
#include <sensors/sensors_api.h>

namespace robot {
namespace control {

class control_api {

public:
	void run();

private:
	void handle_mini_board();

private:
	sensors::sensors_api sensor;
	display::display_api disp;
};

} // control
} // robot

#endif /* CONTROL_API_H_ */
