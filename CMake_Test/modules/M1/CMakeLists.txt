aux_source_directory(src m1)

add_library(M1 STATIC ${m1})

target_include_directories(M1 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
target_link_libraries(M1 PUBLIC A1)
