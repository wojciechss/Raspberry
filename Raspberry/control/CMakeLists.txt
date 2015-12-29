include_directories(${Raspberry_SOURCE_DIR}/control/src)

include_directories(${Raspberry_SOURCE_DIR}/interface)
include_directories(${Raspberry_SOURCE_DIR}/interface/control)

file(GLOB SOURCES "src/*.cpp")

#add_library(control SHARED ${SOURCES})
add_library(control ${SOURCES})
