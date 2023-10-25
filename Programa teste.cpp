#include <iostream>
#include <algorithm>
#include <chrono>
#include <vector>
#include <random>

// Função para gerar um vetor aleatório de tamanho 'size'
std::vector<int> generateRandomVector(int size) {
    std::vector<int> vec(size);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dist(1, 100000);

    for (int i = 0; i < size; i++) {
        vec[i] = dist(gen);
    }

    return vec;
}

// Função para medir o tempo de execução de um algoritmo de ordenação
template <typename SortFunction>
std::chrono::milliseconds measureSortTime(SortFunction sortFunc, std::vector<int>& vec) {
    auto start = std::chrono::high_resolution_clock::now();
    sortFunc(vec.begin(), vec.end());
    auto end = std::chrono::high_resolution_clock::now();
    return std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
}

int main() {
    const int numTests = 5; // Número de testes para cada tamanho
    const std::vector<int> inputSizes = {1000, 5000, 10000, 50000, 100000}; // Tamanhos de entrada

    for (int size : inputSizes) {
        long long totalTime = 0;

        for (int test = 0; test < numTests; test++) {
            std::vector<int> input = generateRandomVector(size);
            std::vector<int> copy = input;

            // Medir o tempo de execução do algoritmo de ordenação aqui
            auto sortTime = measureSortTime(std::sort, input); // Usando std::sort como exemplo

            totalTime += sortTime.count();
        }

        double averageTime = static_cast<double>(totalTime) / numTests;
        std::cout << "Tamanho do vetor: " << size << ", Tempo Médio (ms): " << averageTime << std::endl;
    }

    return 0;
}
