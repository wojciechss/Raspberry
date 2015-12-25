include_directories(${Raspberry_SOURCE_DIR}/src/hardware)

include_directories(${Raspberry_SOURCE_DIR}/interface)
include_directories(${Raspberry_SOURCE_DIR}/interface/hardware)

link_directories(${Raspberry_BINARY_DIR}/src/hardware)

add_library(hardware src/hardware_api.cpp)
