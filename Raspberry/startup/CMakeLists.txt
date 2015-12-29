include_directories(${Raspberry_SOURCE_DIR}/interface)

file(GLOB SOURCES "src/*.cpp")

add_executable(Raspberry ${SOURCES})

target_link_libraries(Raspberry control)
target_link_libraries(Raspberry hardware)
target_link_libraries(Raspberry sensors)
target_link_libraries(Raspberry display)
