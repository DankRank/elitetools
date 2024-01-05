#include <stdio.h>
#include <vector>

int main()
{
	const char shipname[256] = "";
	std::vector<int> vs, es, fs;
	auto saveship = [&]() {
		printf("('%s',\n", shipname);
		std::vector<int> *as[3] = {&vs, &es, &fs};
		int ns[3] = {8, 5, 4};
		for (int i = 0; i < 3; i++) {
			printf("(");
			for (int j = 0; j < as[i]->size(); j++) {
				printf("%d,", (*as[i])[j]);
			}
			printf("),\n");
		}

		printf("),\n");
	};
	printf("(\n");
	int c = 0;
	int t[8];
	while (scanf(" %c", &c) == 1) {
		switch (c) {
		case '.':
			if (shipname[0])
				saveship();
			scanf("SHIP_%s", shipname);
			vs.clear();
			es.clear();
			fs.clear();
			break;
		case 'V':
			scanf("ERTEX%d,%d,%d,%d,%d,%d,%d,%d",&t[0],&t[1],&t[2],&t[3],&t[4],&t[5],&t[6],&t[7]);
			vs.insert(vs.end(), &t[0], &t[8]);
			break;
		case 'E':
			scanf("DGE%d,%d,%d,%d,%d",&t[0],&t[1],&t[2],&t[3],&t[4]);
			es.insert(es.end(), &t[0], &t[5]);
			break;
		case 'F':
			scanf("ACE%d,%d,%d,%d",&t[0],&t[1],&t[2],&t[3]);
			fs.insert(fs.end(), &t[0], &t[4]);
			break;
		default:
			fprintf(stderr, "??? %c %s\n", c, shipname);
			return 1;
			break;
		}
	}
	saveship();
	printf(")\n");
}
