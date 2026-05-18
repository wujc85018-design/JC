cmake_minimum_required(VERSION 3.10)
aux_source_directory(./src SRC)
add_library(A2 STATIC ${SRC})
target_include_directories(A2 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

