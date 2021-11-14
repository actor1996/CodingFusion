//
// Created by 36636 on 2021/11/13.
//
#pragma once

//#ifndef CODING_DATAFRAME_H
//#define CODING_DATAFRAME_H


class FindKthLargest {
public:
    virtual int findKthLargest(std::vector<int> &nums, int k) = 0;

    void test_case1() {
        std::vector<int> nums = {3, 2, 1, 5, 6, 4};
        int k = 2;
        int ans = findKthLargest(nums, k);

        std::cout << "expected: 5 " << "actual: " << ans << std::endl;
    }

    void test_case2() {
        std::vector<int> nums = {3, 2, 3, 1, 2, 4, 5, 5, 6};
        int k = 4;
        int ans = findKthLargest(nums, k);

        std::cout << "expected: 4 " << "actual: " << ans << std::endl;
    }

    void test() {
        test_case1();
        test_case2();
    }
};

//
// Created by 36636 on 2021/11/13.
//

class FindKthLargestFastSorting : public FindKthLargest {
public:
    int quickSelect(std::vector<int> &a, int l, int r, int index);

    int randomPartition(std::vector<int> &a, int l, int r);

    int partition(std::vector<int> &a, int l, int r);

    int findKthLargest(std::vector<int> &nums, int k) override;
};

class FindKthLargestHeapSorting : public FindKthLargest {
public:
    void maxHeapify(std::vector<int> &a, int i, int heapSize);


    void buildMaxHeap(std::vector<int> &a, int heapSize);


    int findKthLargest(std::vector<int> &nums, int k) override;
};



//#endif //CODING_DATAFRAME_H
