find_package(OpenCV REQUIRED COMPONENTS core)
aux_source_directory(src m2)
add_library(M2 STATIC ${m2})
target_include_directories(M2 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include ${CMAKE_CURRENT_SOURCE_DIR}/../../common/kalman/include ${OpenCV_INCLUDE_DIRS}
)
target_link_libraries(M2 PUBLIC A1 A2)
