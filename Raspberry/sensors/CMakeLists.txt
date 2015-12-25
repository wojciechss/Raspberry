include_directories(${Raspberry_SOURCE_DIR}/src/sensors)

include_directories(${Raspberry_SOURCE_DIR}/interface)
include_directories(${Raspberry_SOURCE_DIR}/interface/sensors)

link_directories(${Raspberry_BINARY_DIR}/src/sensors)

add_library(sensors src/sensors_api.cpp)
