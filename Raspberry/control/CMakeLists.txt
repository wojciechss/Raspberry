include_directories(${Raspberry_SOURCE_DIR}/interface)

file(GLOB SOURCES "src/*.cpp")

#add_library(control SHARED ${SOURCES})
add_library(control ${SOURCES})
