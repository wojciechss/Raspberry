#ifndef SERIAL_SINGLETON_H_
#define SERIAL_SINGLETON_H_

#include "serial.h"
#include <memory>

namespace robot {
namespace hardware {

typedef std::shared_ptr<serial> serial_handle;

class serial_singleton {
private:
	serial_singleton();
	serial_singleton(const serial_singleton &);
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
	serial_handle serial_holder;
};

} // hardware
} // robot

#endif /* SERIAL_SINGLETON_H_ */
