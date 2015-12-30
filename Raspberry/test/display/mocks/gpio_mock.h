#ifndef GPIO_MOCK_H_
#define GPIO_MOCK_H_

#include "gmock/gmock.h"
#include <hardware/gpio.h>

namespace robot {
namespace hardware {

class gpio_mock : public gpio {
public:
	gpio_mock() : gpio("4") {}
    MOCK_METHOD0(export_gpio, int());
    MOCK_METHOD0(unexport_gpio, int());
    MOCK_METHOD1(setdir_gpio, int(const std::string&));
    MOCK_METHOD1(setval_gpio, int(const std::string&));
    MOCK_METHOD1(getval_gpio, int(std::string&));
    MOCK_METHOD0(get_gpionum, std::string());
};

} // display
} // robot

#endif /* GPIO_MOCK_H_ */
