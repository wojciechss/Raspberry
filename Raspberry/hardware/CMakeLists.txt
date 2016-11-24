include_directories(${Raspberry_SOURCE_DIR}/interface)

file(GLOB SOURCES "src/*.cpp" "src/serial/*.cpp" "src/serial/boost_serial/*.cpp")

add_library(hardware ${SOURCES})

#add_definitions(-DBOOST_ALL_NO_LIB)

#set(BOOST_ROOT /home/wojtek/src/Raspberry/Raspberry/3rdparty/lib)
#set(BOOST_INCLUDEDIR /include)
#set(BOOST_LIBRARYDIR /home/wojtek/src/Raspberry/Raspberry/3rdparty/lib/arm-linux-gnueabihf)
set(Boost_LIBRARIES ${Raspberry_SOURCE_DIR}/3rdparty/lib/arm-linux-gnueabihf/libboost_system.so)


#message(status " ** Boost Librrydir: ${BOOST_LIBRARYDIR} **")
message(status " ** Boost Librraries: ${Boost_LIBRARIES} **")

#find_package(Boost 1.54 COMPONENTS filesystem system)

#link_directories(${BOOST_LIBRARYDIR})

target_link_libraries(hardware ${Boost_LIBRARIES} pthread)
  
#SET (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -LX11 -Lpthread")

#if(Boost_FOUND)
#  include_directories(${Boost_INCLUDE_DIRS})
#  target_link_libraries(hardware ${Boost_LIBRARIES})
#endif()