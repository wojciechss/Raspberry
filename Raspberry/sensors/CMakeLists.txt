include_directories(${Raspberry_SOURCE_DIR}/sensors)

include_directories(${Raspberry_SOURCE_DIR}/interface)
include_directories(${Raspberry_SOURCE_DIR}/interface/sensors)

link_directories(${Raspberry_BINARY_DIR}/sensors)

add_library(sensors sensors_api.cpp)
