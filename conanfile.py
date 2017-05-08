from conans import ConanFile, tools

class LinmathConan(ConanFile):
    name = "linmath"
    version = "latest"
    license = "WTFPL"
    url = "https://github.com/thoughton/conan-linmath"
    #build_policy = "always"
    description = "a lean linear math library, aimed at graphics programming. Supports vec3, vec4, mat4x4 and quaternions"

    # No settings/options are necessary, this is header only

    def source(self):
        tools.download("https://github.com/datenwolf/linmath.h/raw/master/linmath.h", "linmath.h")

    def package(self):
        self.copy("*.h", "include")

    def package_info(self):
        self.cpp_info.libdirs = []
        #self.cpp_info.bindirs = [] # To avoid binary directories being added to some generators like visual_studio

