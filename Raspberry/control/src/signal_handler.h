#ifndef SIGNAL_HANDLER_H_
#define SIGNAL_HANDLER_H_

namespace robot {
namespace control {

class signal_handler {

public:
	signal_handler();

	bool was_ctrl_c_pressed();
};

} // control
} // robot

#endif /* SIGNAL_HANDLER_H_ */
