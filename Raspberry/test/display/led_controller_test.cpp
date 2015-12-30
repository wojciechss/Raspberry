#include "gtest/gtest.h"
#include <display/led_controller.h>
#include "mocks/gpio_mock.h"
#include <memory>

using namespace robot;
using namespace display;

using ::testing::Return;
using ::testing::_;

class led_controller_test : public ::testing::Test {
public:
	led_controller_test()
	{
		gpio = std::make_shared<robot::hardware::gpio_mock>();

		EXPECT_CALL(*gpio, export_gpio()).WillOnce(Return(0));
		EXPECT_CALL(*gpio, setdir_gpio(_)).WillOnce(Return(0));
		EXPECT_CALL(*gpio, unexport_gpio()).WillOnce(Return(0));
		uut = std::make_shared<led_controller>(gpio);
	}

	virtual ~led_controller_test() {}

	std::shared_ptr<robot::hardware::gpio_mock> gpio;

	std::shared_ptr<led_controller> uut;
};

TEST_F(led_controller_test, should_turn_led_on)
{
	EXPECT_CALL(*gpio, setval_gpio(_)).WillOnce(Return(0));
	uut->turn_led_on();
}
