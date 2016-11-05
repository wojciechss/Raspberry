include_directories(${Raspberry_SOURCE_DIR}/interface)

SET (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -ldl -lpthread")
file(GLOB SOURCES "src/*.cpp" "src/serial/*.cpp" "src/serial/boost_serial/*.cpp")

add_library(hardware ${SOURCES})

#add_definitions(-DBOOST_ALL_NO_LIB)

#set(BOOST_ROOT /home/wojtek/src/Raspberry/Raspberry/3rdparty/lib)
#set(BOOST_INCLUDEDIR /include)
#set(BOOST_LIBRARYDIR /home/wojtek/src/Raspberry/Raspberry/3rdparty/lib/arm-linux-gnueabihf)
set(Boost_LIBRARIES /home/wojtek/src/Raspberry/Raspberry/3rdparty/lib/arm-linux-gnueabihf/libboost_system.so)

#set(Boost_USE_STATIC_LIBS OFF) 
#set(Boost_USE_MULTITHREADED ON)  
#set(Boost_USE_STATIC_RUNTIME OFF) 

#message(status " ** Boost Librrydir: ${BOOST_LIBRARYDIR} **")
message(status " ** Boost Librraries: ${Boost_LIBRARIES} **")

#find_package(Boost 1.54 COMPONENTS filesystem system)

#link_directories(${BOOST_LIBRARYDIR})

target_link_libraries(hardware ${Boost_LIBRARIES})
  
SET (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -ldl -lpthread")

#if(Boost_FOUND)
#  include_directories(${Boost_INCLUDE_DIRS})
#  target_link_libraries(hardware ${Boost_LIBRARIES})
#endif()