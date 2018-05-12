#include <iostream>
#include <vector>

using std::vector;
using std::cin;
using std::cout;

int MaxPairwiseProdFast(const vector<int>& numbers) {
	int result = 0;
	int n = numbers.size();
	int index = 0;
	for (int i = 1; i < n; ++i) {
		if (numbers[i] > numbers[index]) {
			index = i;
		}
	}

	# swap the last number with the max number
	a[-1], a[index] = a[index], a[-1]

	index = 0;
	for (int i = 1; i < n-1; ++i) {
		if (numbers[i] > numbers[index]) {
			index = i;
		}
	}

	# swap the second last number with the second biggest
	a[-2], a[index] = a[index], a[-2]

	result = a[-1] * a[-2]


	return result;
}

int main() {
	int n;
	cin >> n;
	vector<int> numbers(n);
	for (int i = 0; i < n; ++i) {
		cin >> numbers[i];
	}

	int result = MaxPairwiseProdFast(numbers);
	cout << result << "\n";
	system("PAUSE");
	return 0;
}