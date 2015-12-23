include_directories(${Raspberry_SOURCE_DIR}/startup)
include_directories(${Raspberry_SOURCE_DIR}/interface)
include_directories(${Raspberry_SOURCE_DIR}/interface/sensors)

link_directories(${Raspberry_BINARY_DIR}/sensors)
link_directories(${Raspberry_BINARY_DIR}/startup)

add_executable(Raspberry main.cpp)
target_link_libraries(Raspberry sensors)
