include_directories(${Raspberry_SOURCE_DIR}/interface)
include_directories(${Raspberry_SOURCE_DIR}/interface/control)

add_library(control src/control_api.cpp)
