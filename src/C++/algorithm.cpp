#include "dataframe.h"

int FindKthLargestFastSorting::quickSelect(std::vector<int> &a, int l, int r, int index) {
    int q = randomPartition(a, l, r);
    if (q == index) {
        return a[q];
    } else {
        return q < index ? quickSelect(a, q + 1, r, index) : quickSelect(a, l, q - 1, index);
    }
}

int FindKthLargestFastSorting::randomPartition(std::vector<int> &a, int l, int r) {
    int i = rand() % (r - l + 1) + l;
    std::swap(a[i], a[r]);
    return partition(a, l, r);
}

int FindKthLargestFastSorting::partition(std::vector<int> &a, int l, int r) {
    int x = a[r], i = l - 1;
    for (int j = l; j < r; ++j) {
        if (a[j] <= x) {
            std::swap(a[++i], a[j]);
        }
    }
    std::swap(a[i + 1], a[r]);
    return i + 1;
}

int FindKthLargestFastSorting::findKthLargest(std::vector<int> &nums, int k) {
    srand(time(0));
    return quickSelect(nums, 0, nums.size() - 1, nums.size() - k);
}

void FindKthLargestHeapSorting::maxHeapify(std::vector<int> &a, int i, int heapSize) {
    int l = i * 2 + 1, r = i * 2 + 2, largest = i;
    if (l < heapSize && a[l] > a[largest]) {
        largest = l;
    }
    if (r < heapSize && a[r] > a[largest]) {
        largest = r;
    }
    if (largest != i) {
        std::swap(a[i], a[largest]);
        maxHeapify(a, largest, heapSize);
    }
}


void FindKthLargestHeapSorting::buildMaxHeap(std::vector<int> &a, int heapSize) {
    for (int i = heapSize / 2; i >= 0; --i) {
        maxHeapify(a, i, heapSize);
    }
}


int FindKthLargestHeapSorting::findKthLargest(std::vector<int> &nums, int k) {
    int heapSize = nums.size();
    buildMaxHeap(nums, heapSize);
    for (int i = nums.size() - 1; i >= nums.size() - k + 1; --i) {
        std::swap(nums[0], nums[i]);
        --heapSize;
        maxHeapify(nums, 0, heapSize);
    }
    return nums[0];
}

int main() {
    FindKthLargest *fast_sorting = new FindKthLargestFastSorting();
    fast_sorting->test();

    FindKthLargest *heap_sorting = new FindKthLargestHeapSorting();
    heap_sorting->test();

    std::cout << "test end" << std::endl;
    return 0;
}