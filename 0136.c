#include <stdio.h>
#include <time.h>
#include <assert.h>

int singleNumber(int* nums, int numsSize){
    int res = 0;
    for (int i = 0; i < numsSize; i++) {
        res = nums[i] ^ res;
    }
    return res;
}

void test() {
    struct test_case {
        char* name;
        int* input;
        int size;
        int expected;
    };
    struct test_case test_cases[] = {
        {"Example 1", (int[]){2, 2, 1}, 3, 1},
        {"Example 2", (int[]){4, 1, 2, 1, 2}, 5, 4},
        {"Example 3", (int[]){1}, 1, 1}
    };

    int num_tests = sizeof(test_cases)/sizeof(test_cases[0]);

    for (int i = 0; i < num_tests; i++) {
        struct test_case tc = test_cases[i];
        int result = singleNumber(tc.input, tc.size);
        assert(result == tc.expected);
        printf("%s passed\n", tc.name);
    }
}

int main() {
    clock_t start_time = clock();
    test();
    clock_t end_time = clock();
    printf("Everything passed\n");
    printf("Duration: %f seconds\n", (double)(end_time - start_time) / CLOCKS_PER_SEC);
    return 0;
}

