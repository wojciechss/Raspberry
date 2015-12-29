#ifndef LED_CONTROLLER_H_
#define LED_CONTROLLER_H_

#include <hardware/gpio.h>
#include <memory>

namespace robot {
namespace display {

class led_controller {

public:
	led_controller();
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
