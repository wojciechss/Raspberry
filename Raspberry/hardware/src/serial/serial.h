#ifndef SERIAL_H_
#define SERIAL_H_

#include <iostream>

namespace robot {
namespace hardware {

class serial {

public:
	virtual ~serial() {};

	virtual std::string read_line() = 0;
	virtual int write_data(const std::string& data) = 0;

};

} // hardware
} // robot

#endif /* SERIAL_H_ */
