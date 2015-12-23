#include <iostream>
#include <memory>
#include <sensors/sensors_api.h>
 
int main(int argc, char *argv[]) {
   std::shared_ptr<int> sp;
   sensors_api api;
   api.fun(); 
   std::cout << "Hello World!" << std::endl;
   return 0;
}
