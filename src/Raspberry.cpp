//============================================================================
// Name        : Raspberry.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "gpio_class.h"

using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!

	GPIOClass* gpio4 = new GPIOClass("4"); //create new GPIO object to be attached to  GPIO4

	gpio4->export_gpio(); //export GPIO4

	cout << " GPIO pins exported" << endl;

	gpio4->setdir_gpio("out"); // GPIO17 set to input

	cout << " Set GPIO pin directions" << endl;

	gpio4->setval_gpio("1"); // turn LED ON
	return 0;
}
