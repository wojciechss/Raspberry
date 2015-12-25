cmake_minimum_required(VERSION 2.8.9)
add_definitions(-std=c++11)

# Target operating system name.
#set(CMAKE_SYSTEM_NAME Linux)

#set(CROSS_PATH /home/wojtek/rpi/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian/)
#set(CMAKE_CXX_COMPILER "${CROSS_PATH}/bin/arm-linux-gnueabihf-g++")

project (Raspberry)

add_subdirectory(startup)
add_subdirectory(sensors)
add_subdirectory(hardware)
