#include <iostream>
#include <vector>
#include <map>
#include <cmath>
using namespace std;

vector<int> prime_factors(int number) {
    vector<int> factors;
    for (int i = 2; i * i <= number; ++i) {
        while (number % i == 0) {
            factors.push_back(i);
            number /= i;
        }
    }
    if (number > 1) {
        factors.push_back(number);
    }
    return factors;
}

bool divide_factorial(int n, int m, map<int, map<int, int>>& memo) {
    if ((m == 0) || (m==1)) return true;

    if (memo.find(m) == memo.end()) {
        vector<int> factors = prime_factors(m);
        map<int, int> factor_count;
        for (int factor : factors) {
            factor_count[factor]++;
        }
        memo[m] = factor_count;
    }

    const map<int, int>& factors = memo[m];
    for (const auto& [prime, power] : factors) {
        int count = 0;
        long long p = prime;
        while (p <= n) {
            count += n / p;
            p *= prime;
        }
        if (count < power) {
            return false;
        }
    }
    return true;
}

int main() {
    map<int, map<int, int>> memo;
    int n, m;

    while (cin >> n >> m) {
        if (divide_factorial(n, m, memo)) {
            cout << m << " divides " << n << "!" << endl;
        } else {
            cout << m << " does not divide " << n << "!" << endl;
        }
    }

    return 0;
}
