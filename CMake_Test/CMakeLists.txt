cmake_minimum_required(VERSION 3.10)
project(Test)
add_subdirectory(common)
add_subdirectory(modules)

add_executable(test main.cpp)

target_link_libraries(test PUBLIC Math A1 A2 M1 M2)

