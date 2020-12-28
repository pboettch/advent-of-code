#include <cstdint>
#include <iostream>

uint64_t lines[] =
    {19, 0, 0, 0, 0, 0, 0, 0, 0,
     41, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     521, 0, 0, 0, 0, 0, 0, 0,
     23, 0, 0, 0, 0, 0, 0, 0, 0,
     17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     29, 0,
     523, 0, 0, 0, 0, 0,
     37, 0, 0, 0, 0, 0, 0,
     13};

int main(void)
{
	uint64_t t = 100000000000403;
	uint64_t step = 523;
	uint64_t count = 0;

	while (1) {
		int ok = 0;
		for (uint64_t i = 0; i < sizeof(lines)/sizeof(lines[0]); i++) {
			if (lines[i] == 0)
				continue;

			if ((t + i) % lines[i] == 0)
				ok++;
			else
				break;
		}

		if (ok == 9)
			break;

		t += step;

		count++;
		if ((count % 1000000) == 0)
			std::cout << t << "\n";
	}
	std::cout << "first timestamp " << t << "\n";

	return 0;
}
