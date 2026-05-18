cmake_minimum_required(VERSION 3.10)
find_package(OpenCV REQUIRED COMPONENTS core)
aux_source_directory(./src SRC)
add_library(Math STATIC ${SRC})
target_include_directories(Math PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include ${OpenCV_INCLUDE_DIRS})
target_link_libraries(Math PUBLIC ${OpenCV_LIBS})



