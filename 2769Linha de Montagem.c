#include <stdio.h>
#include <stdlib.h>

//função auxiliar para encontrar o valor mínimo entre dois inteiros
int min(int a, int b) {
    return (a < b) ? a : b;
}

int main() {
    int n;

    //enquanto houver entrada para o número de estações (n)
    while (scanf("%d", &n) != EOF) {
        int e1, e2, x1, x2;
        
        //entrada: Custos de entrada e1 e e2
        scanf("%d %d", &e1, &e2);

        //alocação dos arrays baseada no número de estações n
        int a1[n], a2[n];
        int trocaA_B[n - 1], trocaB_A[n - 1];
        int f1[n], f2[n];

        //entrada: Tempos de processamento em cada estação da linha 1
        for (int i = 0; i < n; i++) scanf("%d", &a1[i]);
        //entrada: Tempos de processamento em cada estação da linha 2
        for (int i = 0; i < n; i++) scanf("%d", &a2[i]);

        //entrada: Custos de troca de linha (A para B e B para A)
        for (int i = 0; i < n - 1; i++) scanf("%d", &trocaA_B[i]);
        for (int i = 0; i < n - 1; i++) scanf("%d", &trocaB_A[i]);

        //entrada: Custos de saída x1 e x2
        scanf("%d %d", &x1, &x2);

        //caso base: Tempo gasto para completar a primeira estação
        f1[0] = e1 + a1[0];
        f2[0] = e2 + a2[0];

        //preenchimento das tabelas de DP (Programação Dinâmica)
        for (int i = 1; i < n; i++) {
            // f1[i] = melhor tempo vindo da mesma linha ou trocando da linha 2
            f1[i] = min(f1[i - 1] + a1[i], f2[i - 1] + trocaB_A[i - 1] + a1[i]);

            // f2[i] = melhor tempo vindo da mesma linha ou trocando da linha 1
            f2[i] = min(f2[i - 1] + a2[i], f1[i - 1] + trocaA_B[i - 1] + a2[i]);
        }

        //resultado final somando os custos de saída
        int resultado = min(f1[n - 1] + x1, f2[n - 1] + x2);
        printf("%d\n", resultado);
    }

    return 0;
}