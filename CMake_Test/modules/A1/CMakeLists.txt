cmake_minimum_required(VERSION 3.10)
aux_source_directory(./src SRC)
add_library(A1 STATIC ${SRC})
target_include_directories(A1 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
