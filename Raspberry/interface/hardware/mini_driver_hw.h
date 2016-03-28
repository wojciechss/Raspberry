#ifndef MINI_DRIVER_HW_H_
#define MINI_DRIVER_HW_H_

#include <iostream>

namespace robot {
namespace hardware {

class mini_driver_hw {

public:
	std::string read_line();
	bool write_data(const std::string& data);

};

} // hardware
} // robot

#endif /* MINI_DRIVER_HW_H_ */
