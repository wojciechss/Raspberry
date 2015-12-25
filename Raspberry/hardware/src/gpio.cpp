#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
#include "gpio.h"

gpio::gpio(const std::string& gnum)
{
    gpionum = gnum;  //Instatiate gpio object for GPIO pin number "gnum"
}

int gpio::export_gpio()
{
    std::string export_str = "/sys/class/gpio/export";
    std::ofstream exportgpio(export_str.c_str()); // Open "export" file. Convert C++ std::string to C std::string. Required for all Linux pathnames
    if (exportgpio < 0) {
        std::cout << " OPERATION FAILED: Unable to export GPIO"<< gpionum <<" ."<< std::endl;
        return -1;
    }

    exportgpio << gpionum ; //write GPIO number to export
    exportgpio.close(); //close export file
    return 0;
}

int gpio::unexport_gpio()
{
    std::string unexport_str = "/sys/class/gpio/unexport";
    std::ofstream unexportgpio(unexport_str.c_str()); //Open unexport file
    if (unexportgpio < 0) {
        std::cout << " OPERATION FAILED: Unable to unexport GPIO"<< gpionum <<" ."<< std::endl;
        return -1;
    }

    unexportgpio << gpionum ; //write GPIO number to unexport
    unexportgpio.close(); //close unexport file
    return 0;
}

int gpio::setdir_gpio(const std::string& dir)
{
    std::string setdir_str ="/sys/class/gpio/gpio" + gpionum + "/direction";
    std::ofstream setdirgpio(setdir_str.c_str()); // open direction file for gpio
	if (setdirgpio < 0){
		std::cout << " OPERATION FAILED: Unable to set direction of GPIO"<< gpionum <<" ."<< std::endl;
		return -1;
	}

	setdirgpio << dir; //write direction to direction file
	setdirgpio.close(); // close direction filegpionum
	return 0;
}

int gpio::setval_gpio(const std::string& val)
{
    std::string setval_str = "/sys/class/gpio/gpio" + gpionum + "/value";
    std::ofstream setvalgpio(setval_str.c_str()); // open value file for gpio
	if (setvalgpio < 0) {
		std::cout << " OPERATION FAILED: Unable to set the value of GPIO"<< gpionum <<" ."<< std::endl;
		return -1;
	}

	setvalgpio << val ;//write value to value file
	setvalgpio.close();// close value file
	return 0;
}

int gpio::getval_gpio(std::string& val){

    std::string getval_str = "/sys/class/gpio/gpio" + gpionum + "/value";
    std::ifstream getvalgpio(getval_str.c_str());// open value file for gpio
    if (getvalgpio < 0) {
        std::cout << " OPERATION FAILED: Unable to get value of GPIO"<< gpionum <<" ."<< std::endl;
        return -1;
    }

    getvalgpio >> val ;  //read gpio value

    if (val != "0") {
        val = "1";
    } else {
        val = "0";
    }

    getvalgpio.close(); //close the value file
    return 0;
}

std::string gpio::get_gpionum()
{
	return gpionum;
}
