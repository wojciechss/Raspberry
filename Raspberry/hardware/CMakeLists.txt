include_directories(${Raspberry_SOURCE_DIR}/interface)
include_directories(${Raspberry_SOURCE_DIR}/interface/hardware)

add_library(hardware src/hardware_api.cpp)
