#ifndef BOOST_SERIAL_H_
#define BOOST_SERIAL_H_

#include "../serial.h"
#include <boost/asio/serial_port.hpp>
#include <boost/asio.hpp>
#include <memory>

namespace robot {
namespace hardware {

typedef std::shared_ptr<boost::asio::serial_port> serial_port_handle;

class boost_serial : public serial {

public:
	boost_serial();
	virtual ~boost_serial();

	virtual std::string read_line();
	virtual int write_data(const std::string& buf);

private:
	bool begin_connection();
	void close_connection();
	void set_port_options();
	int write_some(const char* buf, const int& size);

private:
	serial_port_handle serial_port;
	boost::asio::io_service io_service;
};

} // hardware
} // robot

#endif /* BOOST_SERIAL_H_ */
