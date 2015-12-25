include_directories(${Raspberry_SOURCE_DIR}/src/display)

include_directories(${Raspberry_SOURCE_DIR}/interface)
include_directories(${Raspberry_SOURCE_DIR}/interface/display)

link_directories(${Raspberry_BINARY_DIR}/src/display)

add_library(display src/display_api.cpp)
