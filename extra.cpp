#include <chrono>
#include <iostream>
#include <iomanip>
#define USUARIOS 100

using namespace std;

void algoritmo1() {
    int usuarios[USUARIOS];

}

void algoritmo2() {
    
    
}


int main(int argc, char const *argv[])
{
    auto comeco = chrono::steady_clock::now();
    algoritmo1();
    auto fim = chrono::steady_clock::now();

    double duracao = chrono::duration_cast<chrono::milliseconds>(fim - comeco).count() / 1000.0;   

    cout << fixed << setprecision(4) << duracao << endl;

    return 0;
}
