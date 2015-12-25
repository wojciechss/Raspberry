include_directories(${Raspberry_SOURCE_DIR}/src/startup)

include_directories(${Raspberry_SOURCE_DIR}/interface)
include_directories(${Raspberry_SOURCE_DIR}/interface/sensors)
include_directories(${Raspberry_SOURCE_DIR}/interface/hardware)
include_directories(${Raspberry_SOURCE_DIR}/interface/display)

link_directories(${Raspberry_BINARY_DIR}/src/hardware)
link_directories(${Raspberry_BINARY_DIR}/src/sensors)
link_directories(${Raspberry_BINARY_DIR}/src/startup)
link_directories(${Raspberry_BINARY_DIR}/src/display)

add_executable(Raspberry src/main.cpp)
target_link_libraries(Raspberry hardware)
target_link_libraries(Raspberry sensors)
target_link_libraries(Raspberry display)
