include_directories(${Raspberry_SOURCE_DIR}/interface)
include_directories(${Raspberry_SOURCE_DIR}/interface/sensors)

add_library(sensors src/sensors_api.cpp)
