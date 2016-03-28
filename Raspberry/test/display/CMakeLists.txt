include_directories(${Raspberry_SOURCE_DIR}/interface)

file(GLOB SRCS *.cpp)

add_executable(display_test ${SRCS})

target_link_libraries(display_test
    display
    libgtest
    libgmock
)

add_test(NAME display_test COMMAND display_test)
