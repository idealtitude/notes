CXX := clang++
CXXFLAGS_DEBUG := -Wall -Wextra -std=c++23 -fPIC -O0 -g
CXXFLAGS_RELEASE := -Wall -Wextra -std=c++23 -fPIC -O2
SHARED_FLAGS := -shared
LDFLAGS := -lreadline -Wl,-rpath=.

SRC_DIR := src
BUILD_DIR := build
SRCS := $(wildcard $(SRC_DIR)/*.cpp)

OBJ_DEBUG := $(patsubst $(SRC_DIR)/%.cpp, $(BUILD_DIR)/%.debug.o, $(SRCS))
OBJ_RELEASE := $(patsubst $(SRC_DIR)/%.cpp, $(BUILD_DIR)/%.release.o, $(SRCS))

CORE_OBJ_DEBUG := $(filter %notes_core.debug.o, $(OBJ_DEBUG))
CFFI_OBJ_DEBUG := $(filter %notes_cffi.debug.o, $(OBJ_DEBUG))
CORE_OBJ_RELEASE := $(filter %notes_core.release.o, $(OBJ_RELEASE))
CFFI_OBJ_RELEASE := $(filter %notes_cffi.release.o, $(OBJ_RELEASE))

CORE_LIB := libnotes_core.so
CFFI_LIB := notes_cffi.so

.PHONY: all debug release run clean cleanall

all: debug

debug: CXXFLAGS := $(CXXFLAGS_DEBUG)
debug: $(BUILD_DIR) debug_core debug_cffi

release: CXXFLAGS := $(CXXFLAGS_RELEASE)
release: $(BUILD_DIR) release_core release_cffi

run: all
	./notes.py

debug_core: $(CORE_OBJ_DEBUG)
	$(CXX) $(SHARED_FLAGS) $(LDFLAGS) -o $(CORE_LIB) $^

debug_cffi: $(CFFI_OBJ_DEBUG) $(CORE_LIB)
	$(CXX) $(SHARED_FLAGS) $(LDFLAGS) -o $(CFFI_LIB) $^

release_core: $(CORE_OBJ_RELEASE)
	$(CXX) $(SHARED_FLAGS) $(LDFLAGS) -o $(CORE_LIB) $^

release_cffi: $(CFFI_OBJ_RELEASE) $(CORE_LIB)
	$(CXX) $(SHARED_FLAGS) $(LDFLAGS) -o $(CFFI_LIB) $^

$(BUILD_DIR)/%.debug.o: $(SRC_DIR)/%.cpp | $(BUILD_DIR)
	$(CXX) $(CXXFLAGS_DEBUG) -c $< -o $@ -I$(SRC_DIR)

$(BUILD_DIR)/%.release.o: $(SRC_DIR)/%.cpp | $(BUILD_DIR)
	$(CXX) $(CXXFLAGS_RELEASE) -c $< -o $@ -I$(SRC_DIR)

$(BUILD_DIR):
	mkdir -p $@

clean:
	rm -rf $(BUILD_DIR)

cleanall: clean
	rm *.so
