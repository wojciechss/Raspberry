include_directories(${Raspberry_SOURCE_DIR}/startup)
include_directories(${Raspberry_SOURCE_DIR}/interface)
include_directories(${Raspberry_SOURCE_DIR}/interface/sensors)
include_directories(${Raspberry_SOURCE_DIR}/interface/hardware)

link_directories(${Raspberry_BINARY_DIR}/hardware)
link_directories(${Raspberry_BINARY_DIR}/sensors)
link_directories(${Raspberry_BINARY_DIR}/startup)

add_executable(Raspberry main.cpp)
target_link_libraries(Raspberry hardware)
target_link_libraries(Raspberry sensors)
