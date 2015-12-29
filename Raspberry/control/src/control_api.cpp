#include <iostream>
#include <control/control_api.h>

namespace robot {
namespace control {

void control_api::run()
{
	while (true) {
		//std::string data;
		int data;
		//data = getchar();
		std::cin >> data;
		std::cout << "Pressed: "<< data << std::endl;
	}
    std::cout << "hello control" << std::endl;
}

} // control
} // robot
