include_directories(${Raspberry_SOURCE_DIR}/interface)
include_directories(${Raspberry_SOURCE_DIR}/interface/hardware)

file(GLOB SOURCES "src/*.cpp")

#add_library(hardware SHARED ${SOURCES})
add_library(hardware SHARED ${SOURCES})
