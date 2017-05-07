#include <iostream>

#include "linmath.h"

int main()
{
	const vec2 v = {1.f, 0.f};

	const float f = vec2_len(v);

	std::cout << "Length of vector {" << v[0] << ", " << v[1] << "} is " << f << std::endl;
}

