#ifndef BLOCKING_READER_H_
#define BLOCKING_READER_H_

#include <boost/asio.hpp>
#include <boost/asio/serial_port.hpp>
#include <boost/bind.hpp>

namespace robot {
namespace hardware {

class blocking_reader {
public:

	blocking_reader(boost::asio::serial_port& port, size_t timeout);

	bool read_char(char& val);
private:
	void read_complete(const boost::system::error_code& error,
							size_t bytes_transferred);

	void time_out(const boost::system::error_code& error);

private:
	boost::asio::serial_port& port;

	size_t timeout;
	char c;
	boost::asio::deadline_timer timer;
	bool read_error;
};

} // hardware
} // robot

#endif /* BLOCKING_READER_H_ */
