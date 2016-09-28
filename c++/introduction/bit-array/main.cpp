#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */   
	int  n, s, p, q;
	int  a[2];

	map<int, int> m;

	cin >> n >> s >> p >> q;

	a[0] = ( s & 0x7fffffff );
	int cnt = 1;

	a[1] = (a[0] * p + q) & 0x7fffffff;
	a[0] = a[1];
	int bb = a[0];
	

	for(int i = 1; i <= (n-1); i++) {
		a[1] = ( (a[0]*p + q) );
		a[1] &= 0x7fffffff;

//		cout << a[1] << endl;
		cnt++;
		if (a[0] == a[1]) break;
		a[0] = a[1];
	}

	cout << cnt << endl;

	return 0;
}

