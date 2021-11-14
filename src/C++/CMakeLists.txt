cmake_minimum_required(VERSION 3.0)
project(algorithm_src)

set(CMAKE_CXX_STANDARD 20)


add_executable(algorithm algorithm.cpp)
target_include_directories(algorithm PRIVATE algorithm.h)
