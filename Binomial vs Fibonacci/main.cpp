#include <iostream>
#include <chrono>
#include <vector>
#include <unordered_map>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <utility>
#include <boost/heap/fibonacci_heap.hpp>
#include <boost/heap/binomial_heap.hpp>

using namespace std::chrono;
using namespace boost::heap;

using uint_pair = std::pair<unsigned int, unsigned int>;

template <class Heap>
uint_pair test_with_elements(int n) {
	Heap heap;
	
	auto start = high_resolution_clock::now();

	for (int i = 0; i < n; i++) {
		heap.push(std::rand());
	}

	auto end = high_resolution_clock::now();

	unsigned int full = duration_cast<nanoseconds>(end - start).count();


	start = high_resolution_clock::now();
	heap.push(std::rand());
	end = high_resolution_clock::now();

	unsigned int last = duration_cast<nanoseconds>(end - start).count();

	return {full, last};
}

template <class Heap>
void run_experiment(std::ostream& output, const std::string& heap_name) {
	for (int i = 0; i < 20; i++) {
		int n = std::pow(2, i);
		
		for (int j = 0; j < 30; j++) {
			uint_pair result = test_with_elements<Heap>(n);

			output << heap_name << "," << n << "," << result.first << "," << result.second << "\n";
		}
	}
}

int main(int argc, char** argv) {
	std::srand(std::time(nullptr));
	std::ofstream output("experiments.csv");

	output << "heap,n,full,last\n";

	run_experiment<binomial_heap<int>>(output, "binomial");
	run_experiment<fibonacci_heap<int>>(output, "fibonacci");
}
