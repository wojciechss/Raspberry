#ifndef GPIO_H
#define GPIO_H

#include <string>

/* GPIO Class
 * Purpose: Each object instantiated from this class will control a GPIO pin
 * The GPIO pin number must be passed to the overloaded class constructor
 */
class gpio {
public:
    gpio(const std::string& x); // create a GPIO object that controls GPIOx, where x is passed to this constructor
    int export_gpio(); // exports GPIO
    int unexport_gpio(); // unexport GPIO
    int setdir_gpio(const std::string& dir); // Set GPIO Direction
    int setval_gpio(const std::string& val); // Set GPIO Value (putput pins)
    int getval_gpio(std::string& val); // Get GPIO Value (input/ output pins)
    std::string get_gpionum(); // return the GPIO number associated with the instance of an object
private:
    std::string gpionum; // GPIO number associated with the instance of an object
};

#endif // GPIO_H
