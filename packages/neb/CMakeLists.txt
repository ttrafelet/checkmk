cmake_minimum_required(VERSION 3.24)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMK_VERSION 2.3.0)
set(PLANTUTML_VERSION 1.2022.13)
set(CMAKE_CXX_COMPILER g++-13) # TODO: replace with more intelligent approach
set(root_repo_dir ${CMAKE_CURRENT_SOURCE_DIR}/../..)
add_compile_options(
  -Wall
  -Wextra
  -Werror
  -DHAVE_RE2
  -DASIO_DISABLE_CONCEPTS
  -DASIO_NO_DEPRECATED
  -fPIC
  -gdwarf-4
  -std=c++17
  -O3)

string(REGEX REPLACE "([0-9]+)\.([0-9]+)\.([0-9]+).*" "\\1.\\2.\\3"
                     MANGLED_VERSION ${CMK_VERSION})
project(
  neb
  VERSION ${MANGLED_VERSION}
  DESCRIPTION "Livestatus NEB"
  LANGUAGES CXX)

# SUB-DIRS:
add_subdirectory(src)
add_subdirectory(test)
