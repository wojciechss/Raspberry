#ifndef SERIAL_SINGLETON_H_
#define SERIAL_SINGLETON_H_

#include "serial.h"

namespace robot {
namespace hardware {

class serial_singleton {
private:
	serial_singleton();
	serial_singleton( const serial_singleton & );
	~serial_singleton();

public:
    static serial_singleton& instance()
    {
        static serial_singleton singleton;
        return singleton;
    }

	std::string read_line();
	bool write_data(const std::string& data);

private:
    serial serial_holder;
};

} // hardware
} // robot

#endif /* SERIAL_SINGLETON_H_ */
