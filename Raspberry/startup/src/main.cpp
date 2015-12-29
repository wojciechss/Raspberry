#include <control/control_api.h>

using namespace robot;

int main(int argc, char *argv[]) {
   control::control_api c_api;
   c_api.run();
   return 0;
}
