#ifndef LED_CONTROLLER_H_
#define LED_CONTROLLER_H_

#include <memory>
#include <hardware/gpio.h>

namespace robot {

namespace hardware {
	class gpio;
}

namespace display {

class led_controller {

public:
	led_controller(std::shared_ptr<robot::hardware::gpio> gpio =
			std::make_shared<robot::hardware::gpio>("4"));
	~led_controller();
	void blink();
	void turn_led_on();
	void turn_led_off();

private:
	std::shared_ptr<robot::hardware::gpio> gpio_handler;
};

} // display
} // robot

#endif /* LED_CONTROLLER_H_ */
