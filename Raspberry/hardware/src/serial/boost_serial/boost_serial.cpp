#include "boost_serial.h"
#include "blocking_reader.h"

#include <string>
#include <boost/asio/serial_port.hpp>
#include <boost/asio.hpp>

namespace robot {
namespace hardware {

namespace constant {
	const static std::string device_name = "/dev/ttyUSB0";
	const static int baud_rate = 9600;
	const static int timeout_ms = 25000;
}

boost_serial::boost_serial()
{
	begin_connection();
}

boost_serial::~boost_serial() {
	close_connection();
}

bool boost_serial::begin_connection()
{
	boost::system::error_code ec;

	if (serial_port) {
		std::cout << "error : port is already opened..." << std::endl;
		return false;
	}

	serial_port = serial_port_handle(new boost::asio::serial_port(io_service));
	serial_port->open(constant::device_name, ec);

	if (ec) {
		std::cout << "Cannot open port: " <<
				constant::device_name << ", e=" << ec.message().c_str() << std::endl;
		return false;
	}

	set_port_options();
	return true;
}

void boost_serial::close_connection()
{
	if (serial_port) {
		serial_port->cancel();
		serial_port->close();
		serial_port.reset();
	}
	io_service.stop();
	io_service.reset();
}

std::string boost_serial::read_line()
{
	blocking_reader reader(*serial_port, constant::timeout_ms);
	char c;
	std::string rsp;

	// read from the serial port until we get a
	// \n or until a read times-out (500ms)
	while (reader.read_char(c) && c != '\n') {
		rsp += c;
	}

	if (c != '\n') {
		throw std::exception(/*"Read timed out!"*/);
	}

	return rsp;
}

int boost_serial::write_data(const std::string& buf)
{
	return write_some(buf.c_str(), buf.size());
}

int boost_serial::write_some(const char* buf, const int& size)
{
	boost::system::error_code ec;

	if (!serial_port) {
		return -1;
	}

	if (size == 0) {
		return 0;
	}

	return serial_port->write_some(boost::asio::buffer(buf, size), ec);
}

void boost_serial::set_port_options()
{
	serial_port->set_option(
				boost::asio::serial_port_base::baud_rate(constant::baud_rate));
	serial_port->set_option(
				boost::asio::serial_port_base::character_size(8));
	serial_port->set_option(
				boost::asio::serial_port_base::stop_bits(boost::asio::serial_port_base::stop_bits::one));
	serial_port->set_option(
				boost::asio::serial_port_base::parity(boost::asio::serial_port_base::parity::none));
	serial_port->set_option(
				boost::asio::serial_port_base::flow_control(boost::asio::serial_port_base::flow_control::none));
}

} // hardware
} // robot

