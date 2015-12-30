#ifndef GPIO_H_
#define GPIO_H_

#include <string>

namespace robot {
namespace hardware {

/* GPIO Class
 * Purpose: Each object instantiated from this class will control a GPIO pin
 * The GPIO pin number must be passed to the overloaded class constructor
 */
class gpio {
public:
    gpio(const std::string& x); // create a GPIO object that controls GPIOx, where x is passed to this constructor
    virtual ~gpio() {}
    virtual int export_gpio(); // exports GPIO
    virtual int unexport_gpio(); // unexport GPIO
    virtual int setdir_gpio(const std::string& dir); // Set GPIO Direction
    virtual int setval_gpio(const std::string& val); // Set GPIO Value (putput pins)
    virtual int getval_gpio(std::string& val); // Get GPIO Value (input/ output pins)
    virtual std::string get_gpionum(); // return the GPIO number associated with the instance of an object

private:
    std::string gpionum; // GPIO number associated with the instance of an object
};

} // hardware
} // robot

#endif /* GPIO_H_ */
