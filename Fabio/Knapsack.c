#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool canPartition(int* nums, int numsSize) {
    int total = 0;
    for (int i = 0; i < numsSize; i++) {
        total += nums[i];
    }

    if (total % 2 != 0) return false;

    int target = total / 2;
    bool dp[target + 1];
    memset(dp, false, sizeof(dp));
    dp[0] = true;

    for (int i = 0; i < numsSize; i++) {
        int num = nums[i];
        for (int j = target; j >= num; j--) {
            dp[j] = dp[j] || dp[j - num];
        }
    }

    return dp[target];
}

int main() {
    int nums[1000];  // limite máximo arbitrário
    int n;

    printf("Digite a quantidade de números: ");
    scanf("%d", &n);

    if (n <= 0 || n > 1000) {
        printf("Tamanho inválido.\n");
        return 1;
    }

    printf("Digite os %d números:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }

    if (canPartition(nums, n)) {
        printf("true\n");
    } else {
        printf("false\n");
    }

    return 0;
}
