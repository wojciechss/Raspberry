include_directories(${Raspberry_SOURCE_DIR}/interface)
include_directories(${Raspberry_SOURCE_DIR}/interface/display)

file(GLOB SOURCES "src/*.cpp")

#add_library(display SHARED ${SOURCES})
add_library(display ${SOURCES})
