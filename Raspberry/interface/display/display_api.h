#ifndef DISPLAY_API_H_
#define DISPLAY_API_H_

namespace robot {
namespace display {

class display_api {

public:
	void turn_led_on();
	void turn_led_off();
	void stop();
};

} // display
} // robot

#endif /* DISPLAY_API_H_ */
