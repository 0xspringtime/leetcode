#include <stdio.h>
#include <time.h>
#include <assert.h>

double average(int *arr, int size) {
    // implementation of average function
}

void test() {
    struct test_case {
        char* name;
        int* input;
        int size;
        double expected;
    };
    struct test_case test_cases[] = {
        {"simple case 1", (int[]){1, 2, 3}, 3, 2.0},
        {"simple case 2", (int[]){1, 2, 3, 4}, 4, 2.5},
        {"list with one item", (int[]){100}, 1, 100.0},
        {"empty list", NULL, 0, 0.0}
    };

    int num_tests = sizeof(test_cases)/sizeof(test_cases[0]);

    for (int i = 0; i < num_tests; i++) {
        struct test_case tc = test_cases[i];
        int result = average(tc.input, tc.size);
        assert(result == tc.expected);
        printf("%s passed\n", tc.name);
    }
}

int main() {
    clock_t start_time = clock();
    test();
    printf("Everything passed\n");
    clock_t end_time = clock();
    printf("Duration: %f seconds\n", (double)(end_time - start_time) / CLOCKS_PER_SEC);
    return 0;
}

