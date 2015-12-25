#include <iostream>
#include <memory>
#include <sensors/sensors_api.h>
#include <display/display_api.h>
#include <hardware/hardware_api.h>

using namespace robot;

int main(int argc, char *argv[]) {
   std::shared_ptr<int> sp;
   display::display_api d_api;
   sensors::sensors_api s_api;
   hardware::hardware_api h_api;
   d_api.fun();
   s_api.fun();
   h_api.fun();
   std::cout << "Hello World!" << std::endl;
   return 0;
}
