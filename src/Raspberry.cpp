//============================================================================
// Name        : Raspberry.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include "gpio_class.h"
#include <unistd.h>
#include <time.h>

using namespace std;
int main() {
	cout << "!!!Hello World2!!!" << endl; // prints !!!Hello World!!!

	string inputstate;
	GPIOClass* gpio4 = new GPIOClass("4"); //create new GPIO object to be attached to  GPIO4
	GPIOClass* gpio17 = new GPIOClass("17"); //create new GPIO object to be attached to  GPIO17

	gpio4->export_gpio(); //export GPIO4
	gpio17->export_gpio(); //export GPIO17

	cout << " GPIO pins exported" << endl;

	gpio17->setdir_gpio("in"); //GPIO4 set to output
	gpio4->setdir_gpio("out"); // GPIO17 set to input

	cout << " Set GPIO pin directions" << endl;

	while(1)
	{
		timespec t;
		t.tv_nsec = 0;
		t.tv_sec = 1;
		nanosleep(&t, &t);  // wait for 0.5 seconds
		gpio17->getval_gpio(inputstate); //read state of GPIO17 input pin
		cout << "Current input pin state is " << inputstate  <<endl;
		if(inputstate == "0") // if input pin is at state "0" i.e. button pressed
		{
			cout << "input pin state is \"Pressed \".n Will check input pin state again in 20ms "<< endl;
			timespec t2;
			t2.tv_nsec = 20000000;
			t2.tv_sec = 0;
			nanosleep(&t2, &t2);
					cout << "Checking again ....." << endl;
					gpio17->getval_gpio(inputstate); // checking again to ensure that state "0" is due to button press and not noise
			if(inputstate == "0")
			{
				cout << "input pin state is definitely \"Pressed\". Turning LED ON" << endl;
				gpio4->setval_gpio("1"); // turn LED ON

				cout << " Waiting until pin is unpressed....." << endl;
				while (inputstate == "0"){
				gpio17->getval_gpio(inputstate);
				};
				cout << "pin is unpressed" << endl;

			}
			else
				cout << "input pin state is definitely \"UnPressed\". That was just noise." <<endl;

		}
		gpio4->setval_gpio("0");

	}
	cout << "Exiting....." << endl;

	return 0;
}
