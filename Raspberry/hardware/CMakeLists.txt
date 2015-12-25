include_directories(${Raspberry_SOURCE_DIR}/hardware)

include_directories(${Raspberry_SOURCE_DIR}/interface)
include_directories(${Raspberry_SOURCE_DIR}/interface/hardware)

link_directories(${Raspberry_BINARY_DIR}/hardware)

add_library(hardware hardware_api.cpp)
