Leetcode Scratching Recorder
===
Author: Zhong-Liang Xiang
Start from: August 7th, 2017

## 1. Two Sum
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```
人家媳妇：
time $O(n)$, space $O(n)$
方法中巧妙使用map，一次遍历完成任务．
遍历数组时，若未在map中找到想要的元素，则把数组中当前元素投入map．(注key=数组元素值，val=该元素indx)

```c++
vector<int> twoSum(vector<int> &numbers, int target) {
	//Key is the number and value is its index in the vector.
	map<int, int> hash; //原来人家用的是unordered_map
	vector<int> result;
	for (int unsigned i = 0; i < numbers.size(); i++) {
		int numberToFind = target - numbers[i];

		//if numberToFind is found in map, return them
		if (hash.find(numberToFind) != hash.end()) {
      //map 中若找到
			//+1 because indices are NOT zero based
			result.push_back(hash[numberToFind] + 1);
			result.push_back(i + 1);
			return result;
		}

		//number was not found. Put it in the map.
		hash[numbers[i]] = i;
	}
	return result;
}
```

自家媳妇 :)
time $O(n^2)$, space $O(1)$
Brute Force

```c++
class Solution {
public:
    vector<int> twoSum(vector<int> nums, int target) {
        vector<int> result;
        for (int i = 0; i < nums.size(); i++)
            for (int j = i + 1; j < nums.size(); j++)
                if (nums[j] == target - nums[i]) {
                    result.push_back(i);
                    result.push_back(j);
                }
        return result;
    }
};
```
## 27. Remove Element
Given input array ```nums = [3,2,2,3]```, ```val = 3```

Your function should return length = 2, with the first two elements of nums being 2.
就是把不是3的元素往前移动至队首，再返回不是３的元素个数．
$O(n)$ time, $O(0)$ space.
```c++
int removeElement(vector<int> nums, int val){
	int i = 0, k = 0;
	while(i < nums.size()){
		if(nums[i] != val)
			nums[k++] = nums[i];
		i++;
	}
	return k;
}
```
## 26. Remove Duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array ```nums = [1,1,2]```, 变成```[1,2]```

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

自家：
$O(n)$ time, $O(1)$ space.
```c++
int removeDuplicates(vector<int> &nums) {
    if (nums.size() == 1) return 1;
    if (nums.size() == 0) return 0;
    int i = 1, k = 1;
    while (i < nums.size()) {
        if (nums[i] != nums[i - 1])
            nums[k++] = nums[i];
        i++;
    }
    return k;
}
```

人家:
$O(n)$ time, $O(1)$ space.
```c++
int removeDuplicates(vector<int> &A) {
    int count = 0;
    int n = A.size();
    for (int i = 1; i < n; i++) {
        if (A[i] == A[i - 1]) count++;
        else A[i - count] = A[i];
    }
    return n - count;
}
```

## 35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
```
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
```
自家媳妇：
$O(n)$ time, $O(1)$ space. 忘记使用 $Binary Search$ 了．
请记住一件事，<font color = "red">有序数组操作，必用$Binary Search$</font>.

```c++
int searchInsert(vector<int>& A, int target) {
    if (A.size() == 0) return 0;
    if (A[A.size() - 1] < target) return A.size();
    if (A[0] >= target) return 0;
    int i = 1;
    while (i < A.size()) {
        if (A[i] == target) return i;
        if (A[i - 1] < target && A[i] > target) return i;
        i++;
    }
```
自己的二分查找.
$O(logn)$ time, $O(1)$ space.
经验：
* 1. 设定条件 ```while(lo < hi)```
* 2. 退出 ```while``` 后，```lo``` 一定等于 ```hi```.
* 3. 在循环外，应再次判断```A[lo]```所指向的值，　因为这个值前面没读取过．
```c++
int searchInsert(vector<int>& A, int target) {
    int n = A.size();
    if (n == 0) return 0;
    if (A[n - 1] < target) return n;
    if (A[0] >= target) return 0;
    int lo = 0, hi = n - 1, mid;

    while (lo < hi) {
        mid = (lo + hi) / 2;
        if (A[mid] == target) return mid;
        if (A[mid] < target)
            lo = mid + 1;
        if (A[mid] > target)
            hi = mid - 1;
    }
    // lo == hi
    if (A[lo] < target) return lo + 1;
    else return lo;
}
```

人家媳妇：
$O(logn)$ time, $O(1)$ space. 用了二分查找．
```c++
//TODO
int searchInsert(vector<int>& nums, int target) {
    int n = nums.size();
    if (n == 0) return 0;
    int i = 0, j = n - 1;
    while (i < j - 1) {
        int mid = i + (j - i) / 2;
        if (nums[mid] == target) return mid;
        if (nums[mid] > target) j = mid;
        else i = mid;
    }
    if (target <= nums[i]) return i;
    if (target <= nums[j]) return j;
    return j + 1;
}
```
## 53. Maximum Subarray
同121题.
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array ```[-2,1,-3,4,-1,2,1,-5,4]```,
the contiguous subarray ```[4,-1,2,1]``` has the largest sum = ```6```.

人家媳妇：
$O(n)$ time, $O(1)$ space.
想法：子序列若小于０，还不如重新设定子序列，既，通过 <font color = "red"> ```max(f+A[i],A[i])``` </font>  就可以搞定.
```c++
int maxSubArray(vector<int>& A) {
    int n = A.size();
    if (n == 0) return 0;

    int re = A[0], sum = 0, i;
    for (i = 0; i < n; i++) {
        sum += A[i];
        re = sum > re ? sum : re; //re 始终存着最大子序列的和
        sum = sum > 0 ? sum : 0; //重新设定子序列
    }
    return re;
}
```
这帮变态还应用了动态规划方法($DP\ approach$).

## 66. Plus One
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

该题目要求：将一整数按位存储在vector中，对其实现+1操作，返回结果.
对存储序列vector中元素，倒序遍历，末位+1，若<10可直接返回，否则，保存进位加之到下一位，循环至最高位.
若此时，进位依然为1，则新建长度增一的vector首位为1，其余为0，返回即可.

$O(n)$ time, $O(1)$ space.
他人思路, 自己的代码:
```c++
vector<int> plusOne(vector<int>& A) {
    int n = A.size();
    if (A[n - 1] + 1 < 10) {
        A[n - 1] += 1;
        return A;
    } else A[n - 1] = 0;

    //最后一位有为10
    int i;
    for (i = n - 2; i >= 0; i--) {
        A[i] += 1; //倒数第二位+1
        if (A[i] == 10) A[i] = 0;
        else return A;
    }

    // 若循环执行完，仍没return，
    // 则另建一个vector，长度为n+1，首位为１，其余n为为０，并返回
    vector<int> B;
    B.push_back(1);
    for (i = 0; i < n; i++)
        B.push_back(0);
    return B;
}
```

人家更牛逼的代码:
```c++
vector<int> plusOne(vector<int> &digits) {
    int n = digits.size();
    for (int i = n - 1; i >= 0; --i) {
        if (digits[i] == 9) digits[i] = 0;
        else {
            digits[i]++;
            return digits;
        }
    }

    // 很牛逼的样子
    digits[0] = 1;
    digits.push_back(0);
    return digits;
}
```
## 88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

默认了升序.
重点是在数组尾部插入元素:```int i = m - 1, j = n - 1, k = m + n - 1;```
还有就是A中元素若比B多,就不管了,A中元素们都在正确位置,但若B元素多需赋值到A中, 这点处理需注意.

$O(n)$ time, $O(1)$ space.
照葫芦画瓢代码:
```c++
void merge(vector<int>& A, int m, vector<int>& B, int n) {
    int i = m - 1, j = n - 1, k = m + n - 1;
    while (i >= 0 & j >= 0)
        A[k--] = A[i] > B[j] ? A[i--] : B[j--];

    while (j >= 0) //A多不管,元素在正确位置,B多得管
        A[k--] = B[j--];
}
```

## 118. Pascal's Triangle
Given numRows, generate the first numRows of Pascal's triangle.

For example, given ```numRows = 5```,
Return
```
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```
在每一行后面+1, 再更新该行.
另外学会向```vector```容器中放```vector```元素.
人家代码,自己理解:

```c++
vector<vector<int>> generate(int numRows) {
    vector<vector<int>> result;
    vector<int> row;

    // i = 0, 该行有1元素, j = -1, 但合并条件是j > 0
    // i = 1, 该行有2元素, j = 0, 但合并条件是j > 0
    // i = 2, 该行有3元素, j 指向倒数第二个元素
    // i = 3, 该行有4元素, j 指向倒数第二个元素
    for (int i = 0; i < numRows; i++) {
        row.push_back(1); // 在尾部先+1

        for (int j = i - 1; j > 0; j--)
            //和j的前一个元素合并至j位置
            row[j] = row[j - 1] + row[j];
        result.push_back(row);
    }
    return result;
}
```

自己代码：
```c++
#include<iostream>
#include<vector>
using namespace std;

vector<vector<int> > generate(int num);
int main()
{
    vector<vector<int> > res = generate(40);
    for (int i = 0; i < res.size(); ++i)
    {
        cout<<"[";
       for (int j = 0; j < res[i].size(); ++j)
       {
            if(j < res[i].size()-1)
                cout << res[i][j] << ", ";
            else cout << res[i][j];
       }
       cout << "]" << endl;
    }
    return 0;
}

vector<vector<int> > generate(int num){
    vector<vector<int> > res;
    vector<int> row;
    for(int i = 1; i <= num; i++){
        row.push_back(1);
        int len = row.size();
        for(int j = 0; j < len; j++){
            int temp1, temp2;
            if(j == 1){
                temp1 = row[1];
                if(len > 2)
                    row[j] = row[j - 1] + row[j];
            }
            else if(j > 0 && j < len - 1){
                temp2 = row[j];
                row[j] = temp1 + row[j];
                temp1 = temp2;
            }
        }
        res.push_back(row);
    }
    return res;
}

```

## 119. Pascal's Triangle II
Given an index $k$, return the $k^{th}$ row of the Pascal's triangle.

For example, given $k = 3$,
Return ```[1,3,3,1]```.

直接生成由0组成的数组,设定```a[0] = 1```,迭代生成最后结果.
纯人家代码,不易理解:
```c++
vector<int> getRow(int rowIndex) {
    vector<int> A(rowIndex + 1, 0);
    A[0] = 1;
    for (int i = 1; i < rowIndex + 1; i++)
        for (int j = i; j >= 1; j--)
            A[j] += A[j - 1];
    return A;
}
```
## 121. Best Time to Buy and Sell Stock

**Example 1:**
```
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
```

**Example 2:**
```
Input: [7, 6, 4, 3, 1]
Output: 0
```
同53题.
The maximum (minimum) subarray problem. 用到$DP$.
**这题是重点**:
**就是序列从A[0]开始计算, 不符合条件就清0, 从断处继续计算. 好处是 $O(n)$ time 就可以处理**, **牛逼的不行不行的**.
$O(n)$ time, $O(1)$ space.

照葫芦画瓢代码:

```c++
//是个 最大子序列问题 相对应的 有最小子序列问题
//Kadane’s algorithm uses the dynamic programming approach
//to find the maximum (minimum) subarray
int maxProfit(vector<int>& A) {
    int i = 1, profit = 0, temp = 0, p = 0;
    while (i < A.size()) {
        temp = A[i] - A[i - 1];
        p = max(0, p += temp); //难点在这,p要和temp累积,小于0则清0
        profit = max(p, profit); //profit记录累积过程中的最大收益值
        i++;
    }
    return profit;
}

int max(int a, int b) {
    return a > b ? a : b;
}
```
执行过程中, temp, p 和 profit 中值的变化:

```
temp  -6 4 -2 3 -2
p      0 4  2 5  3
profit 0 4  4 5  5
```

更牛逼的代码:
//TODO 还没看呢
```c++
int maxProfit(vector<int>& prices) {
    int mini = INT_MAX;
    int pro = 0;

    for (int i = 0; i < prices.size(); i++) {
        mini = min(prices[i], mini);
        pro = max(pro, prices[i] - mini);
    }
    return pro;
}
```
## 122. Best Time to Buy and Sell Stock II
为获得最高收益而多次买卖,但只能像这样买卖: ```针对 [7, 1, 5, 3, 6, 4], 我们 buy 1, sell 5; buy 3, sell 6.```

$O(n)$ time, $O(1)$ space.

自家代码:
```c++
//这代码就简单了
//  7   1   5   3   6   4
//      B   S   B   S
int maxProfit(vector<int>& A) {
    int i, temp, p = 0, profit = 0;
    for (i = 1; i < A.size(); i++) {
        temp = A[i] - A[i - 1];
        p = 0 > temp ? 0 : temp;
        profit += p;
    }
    return profit;
}
```

## 167. Two Sum II - Input array is sorted
Given an array of integers that is already ***sorted in ascending order***, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have *exactly* one solution and you may not use the *same* element twice.
```
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
```
相当于第1题又重做了一遍.注意```map<int, int> hash;```定义方式.
$O(n)$ time, $O(1)$ space.
自己代码:
```c++
vector<int> twoSum(vector<int>& A, int ta) {
    vector<int> result;
    map<int, int> hash;
    int i, temp, max, min;

    for (i = 0; i < A.size(); i++) {
        temp = ta - A[i];
        if (hash.find(temp) != hash.end()) { //找到了
            max = hash[temp] > i ? hash[temp] : i;
            min = hash[temp] > i ? i : hash[temp];
            result.push_back(min + 1); // bcz base = 1
            result.push_back(max + 1);
            return result;
            //下面代码,就是没找到的话,将对应<k, v>存入hash
        }
        hash[A[i]] = i;
    }
    return result;
}
```

## 169. Majority Element
Given an array of size $n$, find the majority element. The majority element is the element that appears **more than** ```⌊ n/2 ⌋``` times.

You may assume that the array is non-empty and the majority element always exist in the array.

常规办法: 使用 ```map<int, int> hash;``` 然后顺序扫描并投票. 这办法 robust, but $O(n)$ time, $O(n/2)$ space, bcz hash.

这题前提很重要,就是 **the majority element always exist**. 否则下解出错,如 ```3 3 5 6 7```, 会 ```return 7```.

重点是下面精巧的逻辑:
```
初始值 major = A[0], count = 1;
从i = 1开始扫数组:
若count==0, count++; major = A[i];
否则若有相等的, count++;
否则(就是不等,且count未归0,那就count-1) count--;
```
$O(n)$ time, $O(1)$ extra space
人家牛逼代码 without hash:
```c++
int majorityElement(vector<int>& A) {
    int major = A[0], count = 1;
    // 只判断一半是不行的,如 1 2 2 || 3 3 3
    for (int i = 1; i < A.size(); i++) {
        if (count == 0) {
            count++;
            major = A[i];
        } else if (major == A[i]) count++;
        else count--;
    }
    return major;
}
```

## 189. Rotate Array
Rotate an array of $n$ elements to the right by $k$ steps.

For example, with $n = 7$ and $k = 3$, the array ```[1,2,3,4,5,6,7]``` is rotated to ```[5,6,7,1,2,3,4]```.

Related problem: Reverse Words in a String II

限制为 $O(1)$ extra space 的话, 相对有难度.
人家很帅屁的方法:
```[1,2,3,4,5,6,7]``` Original
```[7,6,5,4,3,2,1]``` A[0..n-1] reverse
```[5,6,7,4,3,2,1]``` A[0..k-1] reverse
```[5,6,7,1,2,3,4]``` A[k..n-1] reverse

按人家思路,自己写的代码:
```c++
void rotate(vector<int>& A, int k) {
    int n = A.size();
    k %= n;
    if (n == 0 || n == 1 || k >= n) return;
    reverse(A, 0, n - 1);
    reverse(A, 0, k - 1);
    reverse(A, k, n - 1);
}

void reverse(vector<int>& A, int start, int end) {
    int temp;
    //代码简洁明了
    while (start < end) { //注意条件
        temp = A[start];
        A[start] = A[end];
        A[end] = temp;
        start++;
        end--;
    }
    // start and end are the index based on 0
    // 自己写的这个有些复杂并且还错了!!!
    // int temp, n = end - start + 1;
    // for (int i = start; i <= (n-1)/2; i++){
    //     temp = A[i];
    //     A[i] = A[n - (i + 1)];
    //     A[n - (i + 1)] = temp;
    // }
}
```

## 217. Contains Duplicate
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

本题虽然简单, 看下老外的总结: This problem is trivial but **quite nice example of space-time tradeoff**.

直接想到的是用```set<int> set```:
扫数组, 问是否在set中找到,若有, 则返回 ```false```;
若未找到, 将该元素入set;
若顺利扫完数组, 返回 ```true```;

学习set声明和简单用法:
```
set<int> set;
set.insert(A[i]);

//表找到元素, set.end()表最后一个元素后面的位置
//find()若找到, 返索引, 否则返回最后一个元素后面的位置
set.find(A[i]) != set.end() //表找到
```
方法1: 简单的双重循环, $O(n^2)$ time, $O(1)$ extra space.
方法2: 先排序,再线性查找, $O(nlogn)$ time, $O(1)$ extra space.

```c++
bool containsDuplicate(vector<int>& A) {
    int n = A.size();
    if (n == 0 || n == 1) return false;

    sort(A.begin(), A.end()); // 注意: vector中sort的应用
    for (int i = 1; i < n; i++) {
        if (A[i] == A[i - 1]) return true;
    }
    return false;
}
```
方法3: 用set, 想用hash_set,可能更快. $O(n)$ time, $O(n)$ extra space.
```c++
//用set
bool containsDuplicate(vector<int>& A) {
    int n = A.size();
    set<int> set;
    for (int i = 0; i < n; i++) {//注意下面如何表示找到
        if (set.find(A[i]) != set.end()) return true;
        set.insert(A[i]);
    }
    return false;
}
```

## 219. Contains Duplicate II
Given an array of integers and an integer $k$, find out whether there are two distinct indices $i$ and $j$ in the array such that **nums[i] = nums[j]** and the **absolute** difference between $i$ and $j$ is at most $k$.

首先想到,用```map<int, int>, 其中key = A[i], value = i;```
还想到, 同一个key可以挂多个value. 所以就有了下面的代码.
自己代码:
```c++
bool containsNearbyDuplicate(vector<int>& A, int k) {
    map<int, int> map;
    for (int i = 0; i < A.size(); i++) {
        if (map.find(A[i]) != map.end() && (i - map[A[i]]) <= k)
            return true;
        map[A[i]] = i;
    }
    return false;
}
```
人家代码:
```
人家代码, 用set
核心是: 维护一个set,其中只包含i之前的k个元素,有重复的也会被set干掉.
如k=3, 当前i=4, 下面indx=0的元素应从set中删除!
0       1 2 3      4
```

```c++
bool containsNearbyDuplicate(vector<int>& A, int k) {
    unordered_set<int> set; //基于hash实现,比set查询速度快
    if (k < 0) return false;
    for (int i = 0; i < A.size(); i++) {
        if (i > k) set.erase(A[i - k - 1]);
        if (set.find(A[i]) != set.end()) return true;
        set.insert(A[i]);
    }
    return false;
}
```

## 268. Missing Number
Given an array containing $n$ distinct numbers taken from ```0, 1, 2, ..., n```, find the one that is missing from the array.

For example,
Given ```nums = [0, 1, 3]``` return ```2```.

**Note**:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

题意: 从0..n中随机选n个不同的数入数组, 注意:数组乱序. 找出缺失的那个数.
三种方法, XOR, sum, 二分查找(要求数组sorted).

人家牛逼想法:XOR
XOR 相同为0不同为1. `0 ^ 1 ^ 2 ^ 3 ^ 2 ^ 1 ^ 0 = 3`

$O(n)$ time, $O(1)$ extra space. 比下面sum方法快(bit运算).
```cpp
// xor 位运算
int missingNumber(vector<int>& A) {
    int re = 0;
    for (int i = 1; i <= A.size(); i++)
        re = re ^ i ^ A[i - 1];
    return re;
}
```

SUM方法:
$O(n)$ time, $O(1)$ extra space.

```cpp
// 0..size()和 - 数组和
int missingNumber(vector<int>& A) {
    int sum = 0, n = A.size();
    for (int i = 0; i < n; i++)
        sum += A[i];
    int re = (n * (n + 1)) / 2 - sum;
    return re;
}
```

## 283. Move Zeroes
Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

For example, given `nums = [0, 1, 0, 3, 12]`, after calling your function, `nums` should be `[1, 3, 12, 0, 0]`.

Note:

1. You must do this in-place without making a copy of the array;
2. Minimize the total number of operations.

人家方法:
扫描数组, 遇非0元素, 送入position的位置. 最后,依据position修改数组末端元素们为0.
$O(n)$ time, $O(1)$ extra space.

```cpp
void moveZeroes(vector<int>& A) {
    int posi = 0, n = A.size();
    for (int i = 0; i < n; i++)
        if (A[i] != 0) A[posi++] = A[i];

    while (posi < n)
        A[posi++] = 0;
}
```

## 414. Third Maximum Number
Given a **non-empty** array of integers, return the **third** maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in $O(n)$.

**Example 1**:

```
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
```

**Example 2**:

```
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
```

**Example 3**:

```
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
```

自己的笨方法, 粗暴, 易理解, 且符合题目要求:

```
使用了set.

扫描三遍数组:
第一遍: 找出max, 并依次把每个元素送入set, 若 set.size() < 3, 返回max;
第二遍找出sec, 第三遍找出third;
返回 third.
```
$O(n)$ time, $O(n)$ extra space.

```cpp
int thirdMax(vector<int>& A) {
    int i, n = A.size();
    int max = INT_MIN, sec = INT_MIN, third = INT_MIN;
    set<int> set;

    for (i = 0; i < n; i++) {
        set.insert(A[i]);
        max = max > A[i] ? max : A[i];
    }

    if (set.size() < 3) return max;

    for (i = 0; i < n; i++)
        if (A[i] != max)
            sec = sec > A[i] ? sec : A[i];

    for (i = 0; i < n; i++)
        if (A[i] != max && A[i] != sec)
            third = third > A[i] ? third : A[i];

    return third;
}
```

人家的精巧方法:
用到`set, set.erase(), set.begin(), set.rbegin()`
set 默认升序. `set.rbegin()`表示最后一个元素的迭代器(指针).
$O(n)$ time, $O(n)$ extra space.

```cpp
int thirdMax(vector<int>& A) {
    set<int> top3;
    for (int i = 0; i < A.size(); i++) {
        top3.insert(A[i]);
        // set 默认按 key 升序排序
        if (top3.size() > 3) top3.erase(top3.begin());
    }
    return top3.size() == 3 ? *top3.begin() : *top3.rbegin();
}
```

## 448. Find All Numbers Disappeared in an Array
Given an array of integers where `1 ≤ a[i] ≤ n` ($n =$ size of array), some elements appear twice and others appear once.

Find all the elements of `[1, n]` inclusive that do not appear in this array.

Could you do it without extra space and in $O(n)$ runtime? You may assume the returned list does not count as extra space.

**Example**:

```
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
```
别人的妙想,实在佩服:
$O(n)$ time, $O(1)$ extra space.
重点: 扫数组,做下面的动作
`nums[nums[i] -1] = -nums[nums[i]-1]`
e.g.

```
 4		 3		 2		 7		8		2		 3		 1
-4		-3		-2		-7		8		2		-3		-1
```

```cpp
vector<int> findDisappearedNumbers(vector<int>& A) {
    vector<int> re;
    int p, i;
    for (i = 0; i < A.size(); i++) {
        p = abs(A[i]) - 1;
        if (A[p] > 0) A[p] = -A[p];
    }
    for (i = 0; i < A.size(); i++)
        if (A[i] > 0) re.push_back(i + 1);
    return re;
}
```

## 485. Max Consecutive Ones
Given a binary array, find the maximum number of consecutive 1s in this array.

**Example 1**:
```
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.
```

**Note**:

* The input array will only contain `0` and `1`.
* The length of input array is a positive integer and will not exceed 10,000

咱家代码:
`count`计数,遇到1则+1并有条件的更新到`max`中(`max = max > co ? max : co;`), 遇到0则`count`清0;
$O(n)$ time, $O(1)$ extra space.


```cpp
int findMaxConsecutiveOnes(vector<int>& A) {
    int co = 0, max = 0, i;
    for (i = 0; i < A.size(); i++) {
        if (A[i] == 1) {
            co++;
            max = max > co ? max : co;
        }
        else co = 0;
    }
    return max;
}
```

## 532. K-diff Pairs in an Array
Given an array of integers and an integer **k**, you need to find the number of **unique** k-diff pairs in the array. Here a **k-diff** pair is defined as an integer pair $(i, j)$, where **i** and **j** are both numbers in the array and their absolute difference($|i - j|$) is **k**.

**Example 1**:

```
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
```

**Example 2**:

```
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
```

**Example 3**:

```
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
```

**Note**:

1. The pairs $(i, j)$ and $(j, i)$ count as the same pair.
2. The length of the array won't exceed 10,000.
3. All the integers in the given input belong to the range: `[-1e7, 1e7]`.

自己代码不对.
```cpp
//TODO 结果不对,需修改
int findPairs(vector<int>& A, int k) {
    if (k < 0 || A.size() == 0) return 0;
    map<int, int> big;
    map<int, int> small;
    int key1, key2, count = 0;
    for (int i = 0; i < A.size(); i++) {

        key1 = A[i] + k;
        key2 = A[i] - k;

        if (big.find(A[i]) == big.end()) big[A[i]] = A[i] + (k + 1);
        if (small.find(A[i]) == small.end()) small[A[i]] = A[i] - (k + 1);

        if (big.find(key1) != big.end()) { //big 和 samll 都找到了 key 1
            if (A[i] >= key1 && big[key1] == key1 + (k + 1)) {
                big[key1] == A[i];
                count++;
            }
            if (A[i] < key1 && small[key1] == key1 - (k + 1)) {
                small[key1] == A[i];
                count++;
            }
        }

        if (big.find(key2) != big.end()) { //big 和 samll 都找到了 key 2
            if (A[i] >= key2 && big[key2] == key2 + (k + 1)) {
                big[key2] == A[i];
                count++;
            }
            if (A[i] < key2 && small[key2] == key2 - (k + 1)) {
                small[key2] == A[i];
                count++;
            }
        }
    }
    return count;
}
```

## 561. Array Partition I
Given an array of **2n** integers, your task is to group these integers into **n** pairs of integer, say $(a_1, b_1), (a_2, b_2), ..., (a_n, b_n)$ which makes sum of $min(a_i, b_i)$ for all $i$ from $1$ to $n$ as large as possible.

**Example 1:**

```
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
```

**Note**:

1. **n** is a positive integer, which is in the range of `[1, 10000]`.
2. All the integers in the array will be in the range of `[-10000, 10000]`.

自家代码:
先排序, 索引为偶数元素求和.
副产品为: vector的排序方式 `sort(A.begin(), A.end())`.
$O(nlogn)$ time, $O(1)$ extra space.

```cpp
int arrayPairSum(vector<int>& A) {
    sort(A.begin(), A.end());
    int sum = 0;
    for (int i = 0; i < A.size(); i += 2) {
        sum += A[i];
    }
    return sum;
}
```

## 566. Reshape the Matrix
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.
**Example 1:**

```
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
```

**Example 2:**

```
Input:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
Output:
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
```

**Note:**

1. The height and width of the given matrix is in range ``[1, 100]``.
2. The given r and c are all **positive**.

我的照葫芦画瓢代码:
精巧想法是: `res[i / c][i % c] = A[i / cc][i % cc];` 老服气了!
副产品: `vector<vector<int>>vec(m,vector<int>(n,0));`
m*n的二维vector，所有元素为0

```cpp
vector<vector<int>> matrixReshape(vector<vector<int>>& A, int r, int c) {
    int rr = A.size(), cc = A[0].size();
    if (rr * cc != r * c) return A;

    vector<vector<int>> res(r, vector<int>(c, 0));
    for (int i = 0; i < r * c; i++)
        res[i / c][i % c] = A[i / cc][i % cc];
    return res;
}
```

## 581. Shortest Unsorted Continuous Subarray (TODO)

Given an integer array, you need to find one **continuous subarray** that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the **shortest** such subarray and output its length.

**Example 1:**

```
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
```

**Note:**

1. Then length of the input array is in range `[1, 10,000]`.
2. The input array may contain duplicates, so ascending order here means `<=`.

## 643. Maximum Average Subarray
Given an array consisting of $n$ integers, find the contiguous subarray of given length $k$ that has the maximum average value. And you need to output the maximum average value.

**Example 1:**

```
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
```

**Note:**

1. `1 <= k <= n <= 30,000`.
2. Elements of the given array will be in the range `[-10,000, 10,000]`.

自己方法1 Brute Force:
窗口`k = 4`, 从数组左到右滑动, 代码省略.
$O(n*k)$ time, $O(1)$ extra space.

自个方法2 改进版的 Brute Force:
想法如下:
```
k = 4 的情形

1	12	-5	-6	50	3
^			 ^

1	12	-5	-6	50	3
	^			 ^
明显的, 第一行的 sum  + 50  -  1 就是第二行的 sum
					A[i]   A[i-k]
```

$O(n)$ time, $O(1)$ extra space.

```cpp
double findMaxAverage(vector<int>& A, int k) {
    int i, sum = 0, max = INT_MIN;
    for (i = 0; i < k; i++) sum += A[i];
    max = max > sum ? max : sum;
    for (i = k; i < A.size(); i++) {
        sum = sum + A[i] - A[i - k];
        max = max > sum ? max : sum;
    }
    return 1.0 * max / k;
}
```

## 628. Maximum Product of Three Numbers
Given an integer array, find three numbers whose product is maximum and output the maximum product.

**Example 1:**

```
Input: [1,2,3]
Output: 6
```

**Example 2:**

```
Input: [1,2,3,4]
Output: 24
```

**Note:**

1. The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
2. Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

理很明白, 逻辑没弄清.
想法是:找出 top3 最大, top2 最小, 一趟找出, 关键是逻辑.
形象一些讲就是: **孩子们长身体,老大穿不了的衣服传给老二,老二穿不了的传给老三,老三找到合适衣服直接穿上**.

人家逻辑:
$O(n)$ time, $O(1)$ extra space.


```cpp
int maximumProduct(vector<int>& A) {
    int m1 = INT_MIN, m2 = INT_MIN;
    int m3 = INT_MIN, s1 = INT_MAX, s2 = INT_MAX, res, i, v;

    //孩子们长身体,老大穿不了的衣服传给老二,老二穿不了的传给老三.
    for (i = 0; i < A.size(); i++) {
        v = A[i];
        if (v > m1) {m3 = m2; m2 = m1; m1 = v;}
        else if (v > m2) {m3 = m2; m2 = v;}
        else if (v > m3) {m3 = v;}

        if (v < s1) {s2 = s1; s1 = v;}
        else if (v < s2) {s2 = v;}
    }
    res = m1 * m2 * m3 > m1 * s1 * s2 ? m1 * m2 * m3 : m1 * s1 * s2;
    return res;
}
```

## 605. Can Place Flowers
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number $n$, return if $n$ new flowers can be planted in it without violating the no-adjacent-flowers rule.

**Example 1:**

```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
```

**Example 2:**

```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
```

**Note:**

1. The input array won't violate no-adjacent-flowers rule.
2. The input array size is in the range of [1, 20000].
3. $n$ is a non-negative integer which won't exceed the input array size.

自己代码:
$n\leq3$ 时, 情况都列出来;
$n>3$ 时, 那点若为首点 `i == 0 && A[i] == 0 && A[1] == 0`,则count+1,且将A[0]=1, 否则那点若为尾点`i == (n - 1) && A[i] == 0 && A[i - 1] == 0`,则count+1,且将A[n-1]=1,否则的话,这个点既不是首也不是尾巴,就可以放心的看这个点和前一个点以及后一个点是否全为0,`A[i] == 0 && A[i - 1] == 0 && A[i + 1] == 0`,若是则count+1,且A[i]=1.
我这个逻辑稍显复杂,较难控制.
编写这个用了多久怎么能和你说呢!
我用了足足1分钟! ^^
$O(n)$ time, $O(1)$ extra space.

```cpp
bool canPlaceFlowers(vector<int>& A, int k) {
    int i, count = 0, n = A.size();
    if (n <= 3) {
        if (n == 1 && A[0] == 0) count = 1;
        if (n == 1 && A[0] == 1) count = 0;

        if (n == 2 && A[0] == 0 && A[1] == 0) count = 1;
        if ((n == 2 && A[0] == 1 && A[1] == 0) || (n == 2 && A[0] == 0 && A[1] == 1)) count = 0;

        if (n == 3 && A[0] == 0 && A[1] == 0 && A[2] == 0) count = 2;
        if (n == 3 && A[0] == 0 && A[1] == 0 && A[2] == 1) count = 1;
        if (n == 3 && A[0] == 1 && A[1] == 0 && A[2] == 0) count = 1;

        return k <= count ? true : false;
    }
    else {
        for (i = 0; i < n; i++) {
            if (i == 0 && A[i] == 0 && A[1] == 0) {A[i] = 1; count++;}
            else if (i == (n - 1) && A[i] == 0 && A[i - 1] == 0) {A[i] = 1; count++;}
            else if (A[i] == 0 && A[i - 1] == 0 && A[i + 1] == 0) {A[i] = 1; count++;}
        }
        return k <= count ? true : false;
    }
}
```

再看看人家的,妈的过分吧,是人脑袋吗,还有点正常人的思维吗,想杀人!
$O(n)$ time, $O(1)$ extra space.

```cpp
bool canPlaceFlowers(vector<int>& A, int n) {
    A.insert(A.begin(), 0);
    A.push_back(0);
    for (int i = 1; i < A.size() - 1; ++i){
        if (A[i - 1] + A[i] + A[i + 1] == 0){
            --n;
            ++i;
        }
    }
    return n <= 0;
}
```

## 153. Find Minimum in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`).

Find the minimum element.

You may assume no duplicate exists in the array.


代码如下:
二分查找变形.
>重要思考: `5 6 7 0 1 2 3`, 为什么当 A[mid] <= A[hi] 时, 是 hi = mid,而不是 hi = mid - 1 ?
1 < 3, 1有可能是要找的值, 故而 hi = mid
7 > 3, 7必然不是要找的, 而mid +1 处才有可能是要找的,故而 lo = mid + 1

$O(logn)$ time, $O(1)$ extra space.

```cpp
// Binary search
int findMin(vector<int>& A) {
    int n = A.size(), lo = 0, hi = n - 1, mid;

    while (lo < hi) {
        if (A[0] < A[n - 1]) return A[0];

        mid = (lo + hi) / 2;
        if (A[mid] > A[hi]) lo = mid + 1;
        else hi = mid;
        // 重要思考
    }
    return A[lo];
}
```

## 154. Find Minimum in Rotated Sorted Array II
>Follow up for "153. Find Minimum in Rotated Sorted Array":
What if **duplicates** are allowed?
Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

**Example 1:**

`0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`.

**Example 2:**

`1 3 3 3` might become `3 3 1 3`.

Find the minimum element.

解题重点:
仍然考虑 `5 6 7 0 1 2 3`, 再结合`3 3 1 3` 或 `3 1 3 3`来思考.
>重要思考: `5 6 7 0 1 2 3`, 为什么当 A[mid] <= A[hi] 时, 是 hi = mid,而不是 hi = mid - 1 ?
>1 < 3, 1有可能是要找的值, 故而 hi = mid
7 > 3, 7必然不是要找的, 而mid +1 处才有可能是要找的,故而 lo = mid + 1
本题再结合`3 3 1 3` 或 `3 1 3 3`来思考.
当 A[mid] == A[hi] 时候, hi 所指的 3 就没用了, 往前挪挪, hi--

与 153题想比, 当A[mid] == A[hi] 时候, hi--就行了.
$O(logn)$ time, $O(1)$ extra space.

```cpp
//思考时最好仍基于 5 6 7 0 1 2 3
int findMin(vector<int>& A) {
    int lo = 0, hi = A.size() - 1, mid;
    while (lo < hi) {
        mid = (lo + hi) / 2;
        if (A[mid] > A[hi]) lo = mid + 1;
        else if (A[mid] < A[hi]) hi = mid;
        else hi--; // 此时 A[mid] == A[hi]
    }
    return A[lo]; //此时 lo == hi
}
```

## 4. Median of Two Sorted Arrays(不会,ＴＯＤＯ)
There are two sorted arrays **nums1** and **nums2** of size $m$ and $n$ respectively.

Find the median of the two sorted arrays. The overall run time complexity should be $O(log (m+n))$.

**Example 1:**

```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

**Example 2:**

```
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

## 11. Container With Most Water
给一个非负数组A,元素们是A[i], i=0,...,n-1. 索引i代表x坐标,值A[i]表示高度.索引i与A[i],既(i, A[i])表示了垂直于x轴的线段. 请找出两条线段,与x轴组成的桶最多能装多少水?
人家想法:
先从底最宽搜起．两个边找最矮的移动，计算容积，保留最大值，循环条件 left < right.
自己代码:
$O(n)$ time, $O(1)$ space.

```cpp
int maxArea(vector<int>& A) {
	int l = 0, r = A.size() - 1, water = 0, h;
	while (l < r) {
		h = min(A[l], A[r]);
		water = max(water, h * (r - l));
		while (A[l] <= h && l < r) //注意不能A[l]==h
			l++;
		while (A[r] <= h && l < r)
			r--;
	}
	return water;
}
```

## 15. 3Sum(中等)
Given an array `S` of `n` integers, are there elements `a, b, c` in `S` such that `a + b + c = 0`? Find all unique triplets in the array which gives the sum of zero.

**Note:** The solution set must not contain duplicate triplets.

```
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

人家想法：
0. **先排序**，再次注意C++排序的使用：`sort(A.begin(), A.end());`
1. 固定１个值（用i指向），另两个值依据 `sum=0 - A[i]` 的情况，通过两个指针`lo, hi` 往中间扫；
具体的：
2. `A[lo] + A[hi] == sum`时，lo++, hi--；
3. `A[lo] + A[hi] < sum`时，说明和太小，那就向右移动 lo 指针；
4. `A[lo] + A[hi] > sum`时，说明和太大，那就向左移动 hi 指针；
5. **消除`i, lo, hi`指针处的重复值** 是另一个难点，注意观察下面程序咋做的．

自个代码及注释：
$O(n^2)$ time, $O(1)$ space.

```cpp
vector<vector<int>> threeSum(vector<int>& A) {
	int n = A.size();
	sort(A.begin(), A.end());
	vector<vector<int>> res;
	for (int i = 0; i < n - 2; i++) {
		if (A[i] > 0) break;
		// 消除i处重复值
		if (i == 0 || (i > 0 && A[i] != A[i - 1])) {
			int lo = i + 1, hi = n - 1, sum = 0 - A[i];
			while (lo < hi) {
				if (A[lo] + A[hi] == sum) {
					// 精华之处
					// 若相等，则移动lo, hi,不可只移动lo或hi,因为这是增序
					vector<int> triplet(3, 0);
					triplet[0] = A[i];
					triplet[1] = A[lo];
					triplet[2] = A[hi];
					res.push_back(triplet);

					//消除lo,hi处重复值
					while (lo < hi && (A[lo] == A[lo + 1])) lo++;
					while (lo < hi && (A[hi] == A[hi - 1])) hi--;
					lo++; hi--;
				}
				//此处无需消除重复值，大不了lo,hi之和仍小于sum,继续移动就是了
				else if (A[lo] + A[hi] < sum) lo++;
				else hi--;
			}
		}
	}
	return res;
}
```

## 73. Set Matrix Zeroes(中等)
Given a `m x n` matrix, if an element is `0`, set its entire row and column to `0`. Do it in place.
重点是空间复杂度限制为常数．

人家想法：
用 matrix 的第０行和第０列的元素分别记录所对应的行和列是否有０．
`A[0][0]`比较特殊，我们只让它记录第０行的情况，声明另一变量`col0`记录第0列的情况．
我的实现代码较长，但思路表达的相当清楚．人家也有贼短的代码，人家很牛逼．

算法分两大阶段(细分为 ８ steps, 在程序注释中所示)
1. 设置第０行，第０列以及col0，让它们正确表达所对应行、列的状态；
2. 依据上述状态将对应行、列置０．

第一第二阶段均需注意顺序，如程序中注释所示．
第二阶段清０时，如下图：

```
^ 表示第０行或第０列的元素;
* 表示非０行，非０列元素
依据状态置0时，先清非第0行和第0列的元素，那就是 * 表示的那帮货！
再清第0行，最后依据col0清第0列．

^ ^ ^
^ * *
^ * *
```

有意思的是：**`col0`展示了她的重要地位，她已跳出三界外，不在五行中．整个程序从她而起，最后又由她而终！**

自己代码和注释:
$O(n^2)$ time, $O(1)$ space.

```cpp
void setZeroes(vector<vector<int>>& A) {
	// 程序分为8个step, 各step顺序不能颠倒
	// 终极目的是避免记录状态的第0行和第0列被误写
	int m = A.size(), n = A[0].size(), col0 = 1;

	// step1. 若第0列有0, col0 = 0
	for (int i = 0; i < m; i++)
		if (A[i][0] == 0) {
			col0 = 0;
			break;
		}

	// step2. 若第0行有0, row0 = 0
	for (int j = 0; j < n; j++)
		if (A[0][j] == 0) {
			A[0][0] = 0;
			break;
		}

	// step3. 依次检查除第0列以外的其他列j,若那列有0,则A[0][j]=0
	for (int j = 1; j < n; j++)
		for (int i = 0; i < m; i++)
			if (A[i][j] == 0) {
				A[0][j] = 0;
				break;
			}

	// step4. 依次检查除第0行以外的其他行i,若那行有0,则A[i][0]=0
	for (int i = 1; i < m; i++)
		for (int j = 0; j < n; j++)
			if (A[i][j] == 0) {
				A[i][0] = 0;
				break;
			}

	// 阶段性胜利：到此为止，我们把第0行与第0列，以及col0的 state 设置完成了
	// 接下来，我们要根据上述状态，将对应元素设置为0

	// step5. 依据第0列，修改第1~(m-1)行元素为0(注意：不改第0行，因为那里存着state)
	for (int i = 1; i < m; i++)
		if (A[i][0] == 0)
			for (int j = 1; j < n; j++)
				A[i][j] = 0;

	// step6. 依据第0行，修改第1~(n-1)列元素为0(注意：不改第0列，因为那里存着state)
	for (int j = 1; j < n; j++)
		if (A[0][j] == 0)
			for (int i = 1; i < m; i++)
				A[i][j] = 0;

	// step7. 按照A[0][0], 修改第0行元素为0
	if (A[0][0] == 0)
		for (int j = 1; j < n; j++)
			A[0][j] = 0;

	// step8. 按照col0, 修改第0列元素为0, 再次强调, 以上次序不能调换
	if (col0 == 0)
		for (int i = 0; i < m; i++) //此时需将A[0][0]元素包含在内
			A[i][0] = 0;
}
```

## 74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

* Integers in each row are sorted from left to right.
* The first integer of each row is greater than the last integer of the previous row.

For example,

Consider the following matrix:

```
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
```

Given target = 3, return true.

自己代码，自己想法，查看了别人的，被一顿教育，请看：
**关于二分法的写法，被网上各帖子一顿教育，教育的 contents 在下面代码的注释中．**

另一方面要注意的是：
* 用1次 BinarySearch，treat matrix as a Array
* `a[x] => matrix[x / 列][x % 列]`


```cpp
bool searchMatrix(vector<vector<int>>& A, int ta) {
	// 用1次 BinarySearch，treat matrix as a Array
	// n * m matrix convert to an array => matrix[x][y] => a[x * m + y]
	// an array convert to n * m matrix => a[x] =>matrix[x / m][x % m];

	if (A.empty() || A[0].empty())
		return false;

	int m = A.size(), n = A[0].size();
	int lo = 0, hi = m * n - 1, mid, ro, co;

	while (lo <= hi) { // 是<=
		mid = lo + (hi - lo) / 2; //据说防溢出
		ro = mid / n;
		co = mid % n;
		if (A[ro][co] == ta) return true; //紧凑的判断
		else if (A[ro][co] > ta) hi = mid - 1;
		else lo = mid + 1;
	}
	return false; // 退出循环就说明没找到！
}
```


最初自己想法，自己代码，超时，未通过（不仅是２次二分，更糟糕的是，我头脑中一直认为并使用的二分法写法，是错的，太可怕了）！
用两次二分．
$O(logn)$ time, $O(1)$ space.

```cpp
bool searchMatrix(vector<vector<int>>& A, int ta) {
	// 注意：我的这个代码是错的：二分写错，两次二分也不妥，但不错．

	// 用两次 BinarySearch
	// 第 1 次，应用于第 0 列，目的是找出元素在哪行，假如在 i 行
	// 第 2 次，应用于第 i 行，目的是找出该行是否存在要找的元素 ta

	int m = A.size(), n = A[0].size();
	int lo = 0, hi = m - 1, loo = 0, hii = n - 1, mid;

	// step1. 应用于第 0 列，目的是找出元素在哪行
	while (lo < hi) {
		mid = (lo + hi) / 2;
		if (A[mid][0] < ta)
			lo = mid + 1;
		if (A[mid][0] > ta)
			hi = mid - 1;
	} // 若退出循环，lo==hi，认为元素在第 lo 行

	if (A[lo][0] == ta)
		return true;

	// step2. 针对第 lo 行，用二分法，找出是否存在要找的元素 ta
	while (loo < hii) {
		mid = (loo + hii) / 2;
		if (A[lo][mid] < ta)
			loo = mid + 1;
		if (A[lo][mid] > ta)
			hii = mid - 1;
	} // 若退出循环，loo==hii，查看 A[lo][loo] 是否为 target

	if (A[lo][loo] == ta)
		return true;
	else
		return false;
}
```

## 33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`).

You are given a target value to search. If found in the array return its index, otherwise return `-1`.

You may assume no duplicate exists in the array.

受教于 **StefanPochmann** 的帖子：
https://discuss.leetcode.com/topic/34491/clever-idea-making-it-simple，文中有特别nice的解释，如下：

**Explanation(下面自己附加了一点中文解释)**

Let's say nums looks like this: `[12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`

Because it's not fully sorted, we can't do normal binary search. But here comes the trick:

* If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
`[12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]`

* If target is let's say 7, then we adjust nums to this:
`[-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`

And then we can simply do ordinary binary search.

Of course we don't actually adjust the whole array but instead adjust only on the fly only the elements we look at. And the adjustment is done by comparing both the target and the actual element against `nums[0]`.

**核心思想强调 mid 若和 target 在同一侧，num = A[mid]，否则,若 target 在左侧，mid 一定就在右侧，num 将被赋值为 inf, 否则自然被赋值为 inf.　经过 inf, -inf 的这种设计后，binary search与传统教科书上的一模一样．**

感动到流泪额，真心佩服这些超级聪明并懂得分享的人．

依据人家思想，自己的 implementation:
$O(logn)$ time, $O(1)$ extra space.

```cpp
int search(vector<int>& A, int ta) {
	int lo = 0, hi = A.size() - 1;

	while (lo <= hi) {
		int mid = lo + ((hi - lo) >> 1);
		// mid 若和 target 在同一侧，num = A[mid]
		// 否则,若 target 在左侧，mid 一定就在右侧，num 将被赋值为 inf
		// 否则自然被赋值为 inf.
		double num = (A[mid] < A[0]) == (ta < A[0]) ? A[mid] :
						ta < A[0] ? -INFINITY : INFINITY;

		if (num > ta)
			hi = mid - 1;
		else if (num < ta)
			lo = mid + 1;
		else
			return mid;
	}
	return -1;
}
```

## 442. Find All Duplicates in an Array
Given an array of integers, `1 ≤ a[i] ≤ n` (n = size of array), some elements appear **twice** and others appear **once**.

Find all the elements that appear **twice** in this array.

Could you do it without extra space and in $O(n)$ runtime?

**Example:**

```
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
```
题意为在一个整形数组且元素值在 [1 .. n] 范围内，要求找出数组中重复２次的元素.

思路为：针对元素值 a 来说，a - 1作为索引对应了另一个元素，若为正数，表明 a 第一次出现,**此时在 A[a-1] 处做个标记，改成负数，表示元素 a 已经到此一游过**，若 A[a-1] 为负数，表明a第二次出现，应该输出到结果集合中．

例子: 顺序扫描数组，假设扫描到第一个2, 我们查看 indx = 2 - 1 ＝ 1的元素是否为 -3, 若为-3，表面 2 是重复元素，　否则将 A[indx = 1]设置为-3.

人家思路，自己代码：
$O(n)$ time, $O(1)$ extra space.

```cpp
vector<int> findDuplicates(vector<int>& A) {
	const int n = A.size();
	vector<int> res;

	for (int i = 0; i < n; i++) {
		int indx = abs(A[i]) - 1;
		if (A[indx] < 0) res.push_back(abs(A[i]));
		else A[indx] = 0 - A[indx];
	}

	return res;
}
```

## 41. First Missing Positive(困难, 用到 counting sort 方法)
Given an unsorted integer array, find the first missing positive integer.

**For example**,

```
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.
```

Your algorithm should run in $O(n)$ time and uses constant space.

**若数组为`[10,20,30]`, 则返回`0+1 = 1`, 因为 `A[0]!=( 0 + 1 )`**.详细情况看下面．

人家解释：
http://www.cnblogs.com/ccsccs/articles/4216113.html
跟Counting sort一样，利用数组的index来作为数字本身的索引，把正数按照递增顺序依次放到数组中。即让A[0]=1, A[1]=2, A[2]=3, ... , 这样一来，最后如果哪个数组元素违反了A[i]=i+1即说明i+1就是我们要求的第一个缺失的正数。

$O(n)$ time, $O(1)$ extra space.
代码：

```cpp
int firstMissingPositive(vector<int>& A) {
	const int n = A.size();
	// 难度是维护一个 A[i] = i + 1 的数组
	// 我们只把小于等于数组长度的并且大于０的并且A[i] != i + 1的元素做调整
	for (int i = 0; i < n; i++) {
		if (A[i] <= n && A[i] > 0 && A[A[i] - 1] != A[i]) {
			int temp = A[A[i] - 1];
			A[A[i] - 1] = A[i];
			A[i] = temp;
			i--; // hard
		}
	}

	// 二次扫描，找出A[i] != i + 1的元素
	for (int i = 0; i < n; i++) {
		if (A[i] != i + 1)
			return i + 1;
	}
	return n + 1;
}
```


## 16. 3Sum Closest(中等)
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

```
For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```
如上例， -1 + 1 = 0 不也接近 1 吗？不行，因为人家要求３数之和．
思路同15题 3Sum. 既固定`i`, 让 `lo = i + 1; hi = len - 1;`
关键是对`sum == ta, sum > ta, sum < ta`的处理，以及退出`while(lo < hi)`之后的处理．

人家想法，咱代码：
$O(n^2)$ time, $O(1)$ extra space.

```cpp
int threeSumClosest(vector<int>& A, int ta) {
	const int n = A.size();
	int min = INT_MAX; // 存放最接近ta的三个数和
	sort(A.begin(), A.end());

	for (int i = 0; i < n - 2; i++) {
		// 剔除连续值
		if (i > 0 && A[i] == A[i - 1]) continue;
		int lo = i + 1, hi = n - 1;

		// lo==hi 不可以，sum = A[i] + A[lo] + A[hi]会出问题
		while (lo < hi) {
			int sum = A[i] + A[lo] + A[hi];

			// 保存最接近ta的３数之和
			min = abs(sum - ta) < abs(min) ? (sum - ta) : min;

			if (sum == ta) return ta;
			else if (sum > ta) hi--;
			else lo++;
		}
	}
	return min + ta; // min = sum - ta, we ask sum now!
}
```

## 18. 4Sum(中等)
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

```
For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```
题目和15题的要求几乎一样，只不过是4Sum.
思路和15题一模一样，但仍要注意去重．

自己思路：
> 有了3sum的经验这个就好做了,思想和3sum没有区别
先排序;
固定i, 固定j, move lo and hi;
We'll come across 3 cases(sum == ta, sum > ta, sum < ta) and deal with them.

自己代码：
$O(n^3)$ time, $O(1)$ extra space.

```cpp
vector<vector<int>> fourSum(vector<int>& A, int ta) {
	const int n = A.size();
	vector<vector<int>> res;
	sort(A.begin(), A.end());

	// 有了3sum的经验这个就好做了,思想和3sum没有区别
	// 固定i, 固定j, move lo and hi
	// we'll come across 3 cases(sum==ta, sum>ta, sum<ta) and deal with them
	for (int i = 0; i < n - 3; i++) {
		if (i > 0 && A[i] == A[i - 1]) continue; //去重
		for (int j = i + 1; j < n - 2; j++) {
			if ((j > i + 1) && (A[j] == A[j - 1])) continue; //去重
			int lo = j + 1, hi = n - 1;

			while (lo < hi) {// lo <= hi 不可以
				int sum = A[i] + A[j] + A[lo] + A[hi];
				if (sum == ta) {
					// vector<int> temp;
					// temp.push_back(A[i]);
					// temp.push_back(A[j]);
					// temp.push_back(A[lo]);
					// temp.push_back(A[hi]);
					// res.push_back(temp);

					res.push_back({A[i], A[j], A[lo], A[hi]});

					while (lo < hi && A[hi] == A[hi - 1]) hi--; //去重
					while (lo < hi && A[lo] == A[lo + 1]) lo++; //去重
					lo++; // 只有lo++或　只有hi--也可　他俩都没有就无限循环了
					hi--;

				} else if (sum > ta) {
					while (lo < hi && A[hi] == A[hi - 1])　hi--; //去重
					hi--;
				} else { // sum < ta
					while (lo < hi && A[lo] == A[lo + 1]) lo++; //去重
					lo++;
				}
			}
		}
	}
	return res;
}
```

## 34. Search for a Range
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of $O(log n)$.

If the target is not found in the array, return `[-1, -1]`.

For example,
```
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
```
题意就是找 target = 8 的索引开始和结束的地方，如上列，就是[3, 4], 找不到 target 的话 return [-1, 1].
网上大神用各种二分做实现，什么两次二分，往左侧二分，右侧二分的．本人智商不够，实在无法理解．
下面的想法也用二分，运行时间不比那些难懂的实现差，且非常易理解，比较亲民, 就像星爷在电影"功夫"里的台词：＂终于有个长的像人的！＂．

拿上列来说，想法超级简单，就是**用二分找到８(既 A[mid] == target 的情况)，我们不管哪个8(可能有多个8), 找到就好．然后向左，右，分别利用循环判断边界**，就这么简单，这才像人思考的样子额^^．

人家想法，咱家代码：
$O(logn)$ time, $O(1)$ extra space.

```cpp
vector<int> searchRange(vector<int>& A, int ta) {
	const int n = A.size();
	vector<int> res(2, -1);
	int lo = 0, hi = n - 1;

	while (lo <= hi) {
		int mid = lo + ((hi - lo) >> 1);

		if (A[mid] > ta) hi = mid - 1;
		else if (A[mid] < ta) lo = mid + 1;
		else { //A[mid] == ta，　然后往分别向左右扫，找边界
			res[0] = res[1] = mid;
			int j = mid - 1;

			while (j >= 0 && A[j] == ta) { // left scan
				res[0] = j;
				j--;
			}

			j = mid + 1;
			while (j < n && A[j] == ta) { // right scan
				res[1] = j;
				j++;
			}
			return res; // 这不加 return, 则超时
		}
	}
	return res;
}
```

## 48. Rotate Image
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

方阵顺时针旋转90度，方法：
1. 按行reverse
2. 交换元素 A[i, j] = A[j, i]

逆时针90度方法：
1. <font color = red>按列reverse</font>

```
for (auto vi : matrix) reverse(vi.begin(), vi.end());
```

2. 交换元素 A[i, j] = A[j, i]

代码们：

```cpp
// clockwise rotate
// 1. 按行reverse  2. 交换元素 A[i, j] = A[j, i]
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
void rotate(vector<vector<int>>& A) {
	const int n = A.size();
	reverse(A.begin(), A.end());

	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			swap(A[i][j], A[j][i]);
		}
	}
}
```

```cpp
/*
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
*/
void anti_rotate(vector<vector<int>>& A) {
	const int n = A.size();
	for(atuo vi : A) reverse(vi.begin(), vi.end());

	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			swap(A[i][j], A[j][i]);
		}
	}
}
```

## 54. Spiral Matrix(中等)
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

```
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
```

You should return `[1,2,3,6,9,8,7,4,5]`.

下面的代码是这样办的： `1 2 3`, `6 9`, `8 7`, `4`, `5`.

题意为旋转输出矩阵元素．
人家想法： travel路线: right -> down -> left -> up 循环直到违反循环条件(`rb <= re && cb <= ce`)为止．
重点是控制 row_begin, row_end, col_begin and col_end. 注意循环条件，以及 left 和 up 时的条件判断．
下面代码展现的思想特清楚．

人个想法，自个代码:
$O(n^2)$ time, $O(1)$ extra space.

```cpp
vector<int> spiralOrder(vector<vector<int>>& A) {
	vector<int> res;
	if (A.size() == 0) return res;

	const int m = A.size(), n = A[0].size();
	int rb = 0, re = m - 1, cb = 0, ce = n - 1;

	while (rb <= re && cb <= ce) {
		// right travel
		for (int j = cb; j <= ce; j++)
			res.push_back(A[rb][j]);
		rb++;

		// down travel
		for (int j = rb; j <= re; j++)
			res.push_back(A[j][ce]);
		ce--;

		// left travel
		if (rb <= re) {
			for (int j = ce; j >= cb; j--)
				res.push_back(A[re][j]);
		}
		re--;

		// up travel
		if (cb <= ce) {
			for (int j = re; j >= rb; j--)
				res.push_back(A[j][cb]);
		}
		cb++;
	}
	return res;
}
```

## 55. Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:

```
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
```

这不是我们小时候玩的跳棋，所以我理解错了题意．所谓正确题意是，如第一个例子：
`A[0] = 2`, 代表 `index = 1, 2` 的元素我们**都可以跳到**(我原来以为得必须跳到 index = 2 的位置呢). 我们把能达到的最远索引保存在变量`reach`中. `A[1] = 3, A[2] = 1`, 那么选最大的, 则 `reach = i + A[i] = 1 + 3`.

说是贪心法.
精简的意思就是:
<font color = red>reach 是前沿阵地位置, i 是后方补给当前所在位置, 补给只在 reach 所定的安全区域逐步前行, i 能否到达数组最后一个元素, 完全取决于 reach 所能到达的位置. 但 i 在前行的过程中, 符合条件的话可以更新 reach. 有时候，虽然 i 还没到达数组最后元素, 但当前的`reach >= n - 1`了, i 就不需要向前走了(循环被 break), 因为reach已经表明共产主义肯定能实现, i 显然就没有向下走的必要了.</font>

人家想法，自己代码：
牛就牛在这想法是$O(n)$的，而笨想法是$O(n^2)$的．
$O(n)$ time, $O(1)$ extra space.

```cpp
bool canJump(vector<int>& A) {
	const int n = A.size();

	int i = 0;
	// 扫描reach范围内, i + A[i] 所能到达的最远位置.
	// 若能超过当前reach,则更新reach.
	for (int reach = 0; i < n && i <= reach; i++) {
		reach = max(i + A[i], reach);
		if (reach >= n - 1)
			return true;
	}
	// 2个事能导致退出循环, 既上面的循环条件
	// 不等于n, 只能因为 reach < i, reach 鞭长莫及了
	return i == n;
}
```

## 59. Spiral Matrix II
Given an integer $n$, generate a square matrix filled with elements from 1 to $n^2$ in spiral order.

For example,
Given n = 3,
You should return the following matrix:

```
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```

思路完全同 54. Spiral Matrix(中等).
自个代码：

```cpp
vector<vector<int>> generateMatrix(int n) {
	vector<vector<int>> A(n, vector<int>(n)); //n行n列,动态的

	// Normal Case
	int rowStart = 0;
	int rowEnd = n - 1;
	int colStart = 0;
	int colEnd = n - 1;
	int num = 1; //change

	while (rowStart <= rowEnd && colStart <= colEnd) {
		for (int i = colStart; i <= colEnd; i++) {
			A[rowStart][i] = num++; //change
		}
		rowStart++;

		for (int i = rowStart; i <= rowEnd; i++) {
			A[i][colEnd] = num++; //change
		}
		colEnd--;

		for (int i = colEnd; i >= colStart; i--) {
			if (rowStart <= rowEnd)
				A[rowEnd][i] = num++; //change
		}
		rowEnd--;

		for (int i = rowEnd; i >= rowStart; i--) {
			if (colStart <= colEnd)
				A[i][colStart] = num++; //change
		}
		colStart++;
	}
	return A;
}
```

## 81. Search in Rotated Sorted Array II（中等）
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`).

Write a function to determine if a given target is in the array.

The array may contain duplicates.

这种题自我感觉比较难．仍遵循二分查找的整体框架:

```
以 [4 5 6 7 0 1 2] 为例

while(lo < hi){
	case1: A[mid] > A[hi] 这时，看看 ta 在 4...mid 之间吗？
	case2: A[mid] < A[hi]　这时，看看 ta 在 mid...2 之间吗？
	case3: A[mid] == A[hi] 这时, hi--;
}
```

人家思想，自个代码:
$O(logn)$ time, $O(1)$ extra space.

```cpp
bool search(vector<int>& A, int ta) {
	const int n = A.size();
	if (n == 0) return false; // special case
	int lo = 0, hi = n - 1;

	while (lo < hi) {
		int mid = lo + ((hi - lo) >> 1);
		if (A[mid] == ta) return true;
		if (A[mid] > A[hi]) {
			if (ta < A[mid] && ta >= A[lo]) hi = mid;
			else lo = mid + 1;
		} else if (A[mid] < A[hi]) {
			if (ta > A[mid] && ta <= A[hi]) lo = mid + 1;
			else hi = mid;
		} else hi--;
	}
	return ta == A[lo] ? true : false;
}
```

## 80. Remove Duplicates from Sorted Array II
有一个升序排序的数组．

For example,
Given sorted array `nums = [1,1,1,2,2,3]`,

Your function should return length = `5`, with the first five elements of nums being `1, 1, 2, 2 and 3`. It doesn't matter what you leave beyond the new length.

元素可重复２次的数组．后面给出了可重复１次的代码，自然的，就有可重复n次的代码．
一开始，**我错误理解了本题，以为给出数组长度就行了．本题不仅要给出数组长度，还得把原数组 nums 整理成元素可重复 2 次的数组，虽然不要求返回该数组．**

人家想法和代码：
$O(n)$ time, $O(1)$ extra space.
可重复2次的代码.

```cpp
int removeDuplicates(vector<int>& A) {
	// 边扫描，边修改数组
	int i = 0;
	for (int n : A) {
		if (i < 2 || n > A[i - 2])
			A[i++] = n;
	}
	return i;
}
```

可重复1次的代码：

```cpp
int removeDuplicates(vector<int>& A) {
	// 边扫描，边修改数组
	int i = 0;
	for (int n : A) {
		if (i < 1 || n > A[i - 1])
			A[i++] = n;
	}
	return i;
}
```

自己一开始错误理解题意，写的代码：

```cpp
// 下面是我的不符合题意的代码
// 针对[1,1,1,2,2,3], 可以返回整数5
// 但本题不仅要求返回长度, 还得修改数组.
// 若[1,1,1,1,2,2,3], 则代码就不对了．
int removeDuplicates(vector<int>& A) {
	const int n = A.size();
	if (n < 3) return n;

	int num_item = 2;

	for (int i = 2; i < n; i++) {
		if (A[i] != A[i - 2])
			num_item++;
	}
	return num_item;
}
```

## 128. Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given `[100, 4, 200, 1, 3, 2]`,
The longest consecutive elements sequence is `[1, 2, 3, 4]`. Return its length: 4.

Your algorithm should run in `O(n)` complexity.

空间换时间，用了 map.
map 咋声明？判断 key = n 是否在该 map 中咋弄？

```cpp
map<int, int> map;
if(map.find(n) == map.end()){} //若 key = n 不在map中
```

本题关键点(思路很清晰)：
<font color = red>主要分 2 steps:</font>
```
扫描数组, n 表示当前扫到的元素．

step1:
	若 key = n 不在 map 中, 就找n的左(n-1)、右(n+1)邻居, 然后sum = left + right + 1,
	再把 map[n] = sum;

step2:
	接着更新　这个连续序列的 边界(boundarys, boundarys, 重要的话说３遍！) 为 sum 值，　如：
	e.g [1,2,3,4,5], A[1] = A[5] = 5, except A[2,..,4]!
	若无　左　或　右　边界，则不受影响 respectively, 如下核心代码：
	map[n - left] = sum;
	map[n + right] = sum;

key = n 在 map 中的话，跳过本次循环，因为重复了，不必理会了．
```

人家想法，咱家代码：
$O(n)$ time, $O(n)$ extra space.

```cpp
int longestConsecutive(vector<int>& A) {
	int res = 0;
	map<int, int> map;

	for (int n : A) {
		// 若 key = n 不在map中
		if (map.find(n) == map.end()) {
			// step 1: left, right issues
			int left = (map.find(n - 1) != map.end()) ? map[n - 1] : 0;
			int right = (map.find(n + 1) != map.end()) ? map[n + 1] : 0;
			int sum = left + right + 1;
			map[n] = sum;

			res = max(res, sum);

			// step 2: boundary(s) issues

			// update the length of
			// this consecutive sequence boundary(s)
			// e.g [1,2,3,4,5], A[1] = A[5] = 5, except A[2,..,4]!
			// 若无　左　或　右　边界，则不受影响 respectively.
			map[n - left] = sum;
			map[n + right] = sum;
		} else {
			// duplicates
			continue;
		}
	}
	return res;
}
```

还有牛人的超短的代码：
https://leetcode.com/problems/longest-consecutive-sequence/discuss/

# 120. Triangle(中等)
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

The minimum path sum from top to bottom is 11 (i.e., `2 + 3 + 5 + 1 = 11`).

**Note:**
Bonus point if you are able to do this using only $O(n)$ extra space, where n is the total number of rows in the triangle.

<font color = red>先说一个坑：本题绝不是找每行最小元素，然后把它们加起来那么简单．原因是这些元素是有路径的！看下例：</font>

```
[
     [-1],
    [2, 3],
   [1,-1,-3],
]
```
<font color = red>结果应为 `-1 + 2 + -1 = 0`, 而不是 `-1 + 2 + -3 = -2`.</font>

idea来自　http://www.cnblogs.com/liujinhong/p/5551932.html　中的图片，感谢这位同学．
本 code 属于	**方法一:	自上而下，破坏原数组A.** $O(n^2)$ time, $O(1)$ space
另一种方法		**方法二:	自下而上，不破坏数组A.** 维护一个长度为 n 的 1-dim 数组. $O(n^2)$ time, $O(n)$ space.

方法一的解题思路(请务必参照上面网址中的图片)：

```
从上至下，将值按照＂路径＂加到下一层
除了A[0][0]这种情况外，还会遇到下列三种(注意判断条件)情况，共 4 cases:
	case 1: left, right 上邻居都存在
	case 2: left上不存在, right上存在
	case 3: left上存在, right上不存在
	case 4: A[0][0](它没left上 和 right上邻居), 我们 do nothing, 保留A[0][0]数值不变.
```

<font color = red>下面的图可以让我们看清上面 4 cases 的判断条件:</font>

```
下面是元素索引:

	[
	     	  [0,0],
	       [1,0],[1,1] ,          [row-1,col-1],[row-1,col],
	    [2,0],[2,1],[2,2],                [row, col]
	 [3,0],[3,1],[3,2],[3,3]
	]

```

人家想法，自个代码(方法一，破坏原数组)：
$O(n^2)$ time, $O(1)$ space

```cpp
// idea来自　http://www.cnblogs.com/liujinhong/p/5551932.html
// 本 code 属于方法一:自上而下，破坏原数组A. $O(n^2)$ time, $O(1)$ space
// 另一种方法方法二:自下而上，不破坏数组A. 维护一个长度为 n 的 1-dim 数组．
//               $O(n^2)$ time, $O(n)$ space.
int minimumTotal(vector<vector<int>>& A) {
	const int n = A.size();
	if (n == 0) return 0;

	// 从上至下，将值按照＂路径＂加到下一层
	// 除了A[0][0]这种情况外，还会遇到下列三种情况，共 4 cases.
	for (int row = 0; row < n; row++) {
		for (int col = 0; col <= row; col++) {
			if ((row - 1 >= 0) && (col - 1 >= 0) && (col <= row - 1)) {
				// case 1: left, right 上邻居都存在
				int mi = min(A[row - 1][col - 1], A[row - 1][col]);
				A[row][col] += mi;
			} else if ((row - 1 >= 0) && (col - 1 < 0) && (col <= row - 1)) {
				// case 2: left上不存在, right上存在
				A[row][col] += A[row - 1][col];
			} else if ((row - 1 >= 0) && (col - 1 >= 0) && (col > row - 1)) {
				// case 3: left上存在, right上不存在
				A[row][col] += A[row - 1][col - 1];
			}
			// case 4: A[0][0](它没left上 和 right上邻居)
			// do nothing, 保留A[0][0]数值不变.
		}
	}

	// 返回A中最下面的一行(A[n-1])最小元素
	int res = INT_MAX;
	for (int i = 0; i < A[n - 1].size(); i++) {
		res = min(res, A[n - 1][i]);
	}
	return res;
}
```

方法二:
自下而上，不破坏数组A．
关键是找本层和上一层元素的关系，那就是 `temp[j] = A[i,j] + min(temp[j], temp[j+1])`.
$O(n^2)$ time, $O(n)$ space.

```cpp
// 方法二：
// 自下而上，不破坏数组A. 维护一个长度为 n 的 1-dim 数组．
// $O(n^2)$ time, $O(n)$ space.
int minimumTotal(vector<vector<int>>& A) {
	const int n = A.size();
	if (n == 0)
		return 0;
	if (n == 1)
		return A[0][0];
	vector<int> temp;
	// A 最后一行存入temp
	for (int j = 0; j < n; j++)
		temp.push_back(A[n - 1][j]);

	// 从倒数第二行到上按路径元素取min的，相加
	// 对应关系:
	//     A[2, 1]
	// temp[1]  temp[1+1]

	for (int i = n - 2; i >= 0; i--) {
		for (int j = 0; j <= i; j++) {
			int smal = min(temp[j], temp[j + 1]);
			// 若当前使用temp[0], temp[1]
			// temp[0] 被改, 但不影响下次使用temp[1], temp[2]
			temp[j] = A[i][j] + smal;
		}
	}
	return temp[0];
}
```

## 62. Unique Paths(中等，我自己解出的第一道DP题^^)
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
有个图来着，Markdown贴起来很麻烦．不贴了．
Above is a 3 x 7 grid. How many possible unique paths are there?

**Note**: $m$ and $n$ will be at most 100.

解题思路，没啥可说， 用 dynamic programming.
步骤：
step 1: 看 https://mp.weixin.qq.com/s/0AgJmQNYAKzVOyigXiKQhA, 动态规划入门最好材料，没有之一！　10分钟看完，然后第二步．
step 2: 画图自己做这个题．^^

主要是先建模型，既，分析出：
1. <font color = red>状态转移公式</font>，本题有３个状态转移公式，分别对应这i,j条件．具体参考最下方的代码（**简单递归，当然无法执行，因为时间复杂度为 $O(2^n)$, 但能很好的展示了转移公式**）;
2. <font color = red>最优子结构</font>(分别对应各自的状态转移公式)；
3. <font color = red>边界</font>，既`F[0,0] = 1`.

自己想法，自个代码^^:
$O(m*n)$ time, $O(n)$ extra space.

```cpp
class Solution {
public:
    // 真正的DP求解
    // $O(m*n)$ time, $O(n)$ extra space.
    // 时间复杂度无法再小了，但空间复杂度还可以再小．
    // space complexity 最低可为 min(m, n);
    // 听说有 $O(1)$ 的空间复杂度？
    // 如果不用 DP, 可用 math 的方法，如下：
    // https://leetcode.com/problems/unique-paths/discuss/

    int uniquePaths(int m, int n) {
        if(m == 1 || n == 1) return 1;
        if(m < n) return uniquePaths(n, m);

        vector<int> temp(n - 1, 0);
        for(int i = 1; i < m; i++){
            for(int j = 1; j < n; j++){
                if(i == 1 && j == 1) temp[0] = 2;
                else if(i == 1 && j > 1) temp[j - 1] = 1 + temp[j - 2];
                else if(i > 1 && j == 1) temp[0] = temp[0] + 1;
                else if(i > 1 && j > 1) temp[j - 1] = temp[j - 1] + temp[j - 2];
            }
        }
        return temp[n - 2];
    }
};
```

下面是简单递归，但 time complexity $O(2^n)$, 太高了.
下面代码可清晰地展示出DP的三要素：
状态转移公式、最优子结构和边界．

```cpp
class Solution {
public:
    // 方法一: 简单递归，但 time complexity $O(2^n)$, 太高了.
    int uniquePaths(int m, int n) {
        int i = m - 1, j = n - 1;
        if(i == 0 && j == 0) return 1;
        else if(i == 0 && j != 0) return uniquePaths(i, j - 1);
        else if(j == 0 && i != 0) return uniquePaths(i - 1, j);
        else if(j > 0 && i > 0) return uniquePaths(i, j - 1) + uniquePaths(i - 1, j);
    }
};
```

## 63. Unique Paths II(中等, 能独立做出来的DP类第二个题^^)
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,

There is one obstacle in the middle of a 3x3 grid as illustrated below.

```
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
```

The total number of unique paths is 2.

**Note:** m and n will be at most 100.

这是自己能独立做出来的DP类第二个题^^.
这题和上一题状体转移公式几乎一样．区别就是在 obstacles 的处理上．下面是方法：
核心思路：
1. 先搞定第 0 行和第 0 列;
2. **第 0 行和第 0 列若有障碍, 则该处及后面的都 = 0;**
3. **非０行、列，则按公式填写 bp matrix, 从 row=1, col=1开始. 若遇 obstacle, 该处设置为0.**

注意处理 **special case**：`if(A[0][0] = 1) return 0;`
为了搞起来方便，申请了一个 m*n 的二维数组．但似乎只申请 n 维的一维数组就足够了．先不管啦．

自己思路，自个媳妇:
$O(m*n)$ time, $O(m*n)$ extra space.

```cpp
// 思路：
// 1. 先搞定第 0 行和第 0 列;
// 2. 第 0 行和第 0 列若有障碍, 则该处及后面的都 = 0;
// 3. 非０行、列，则按公式填写 bp matrix, 从 row=1, col=1开始.
//    若遇 obstacle, 该处设置为0.
int uniquePathsWithObstacles(vector<vector<int>>& A) {
	const int m = A.size(), n = A[0].size();
	// special case
	if (m == 0 || A[0][0] == 1)
		return 0;

	vector<vector<int>> dp(m);

	// dp[m*n] initializaion
	for (int i = 0; i < m; i++)
		dp[i].resize(n);

	// 初始化bp的行
	for (int j = 0; j < n; j++) {
		if (A[0][j] == 0)
			dp[0][j] = 1;
		else { // point A[0,j] is an obstacle
			dp[0][j] = 0;
			break; // 第0行若有障碍,则该处及后面的都 = 0
		}
	}

	// 初始化bp的列
	for (int i = 1; i < m; i++) {
		if (A[i][0] == 0)
			dp[i][0] = 1;
		else { // point A[i,0] is an obstacle
			dp[i][0] = 0;
			break; // 第0列若有障碍,则该处及后面的都 = 0
		}
	}

	// 按公式填写bp matrix, 从 row=1, col=1开始
	for (int i = 1; i < m; i++) {
		for (int j = 1; j < n; j++) {
			if (A[i][j] == 1)
				dp[i][j] == 0; //障碍处设置为0
			// dp的状态转移公式
			else if (A[i][j] == 0)
				dp[i][j] = dp[i][j - 1] + dp[i - 1][j];
		}
	}
	return dp[m - 1][n - 1];
}
```

## 70. Climbing Stairs(easy, 号称 Dynamic Programming 天下第一题)
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Note:** Given n will be a positive integer.

<font color = red>https://mp.weixin.qq.com/s/0AgJmQNYAKzVOyigXiKQhA, 动态规划入门最好材料，也是该题个人认为最完美的解释，没有之一！ 非常感谢该文章的作者和发给我文章的张春玲老师！</font>

自个代码:
$O(n)$ time, $O(1)$ extra space.

```cpp
// A textbook style question for Dynamic Programming.
// I like it!
int climbStairs(int n) {
	// boundarys
	if (n == 1)	return 1;
	if (n == 2)	return 2;

	// state transfer formula
	int a = 1, b = 2, temp;
	for (int i = 3; i <= n; i++) {
		temp = a + b;
		a = b;
		b = temp;
	}
	return temp;
}
```

## 64. Minimum Path Sum(中等, 又做出一个DP题, 你们非问我开不开心，当然开心喽！)
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

动态规划问题．
1. 状态转移公式: `F[i,j] = min(F[i,j-1], F[i-1,j]) + A[i,j]`
2. 最优子结构: `F[i,j-1], F[i-1,j] 和　A[i,j]`
3. 边界: `F[0,0] = A[0,0]`;

参照例子：

```
1 2 3 4
4 3 2 1
2 1 2 3
```

实现中有三种选择：
1. 最优的: $O(m*n)$ time, $O(min(m, n))$ extra space;(maintain an array)
2. 次优的: $O(m*n)$ time, $O(m)+O(n)$ extra space;(维护俩数组，长度分别m, n)
3. 最差的: $O(m*n)$ time, $O(m*n)$ extra space.(maintain a matrix, m*n)

自个想法，自个最优空间复杂度代码：
$O(m*n)$ time, $O(min(m, n))$ extra space;

```cpp
// method 2
// DP
// F[i,j] = min(F[i,j-1], F[i-1,j] + A[i,j])
// O(m*n) time, O(min(m,n)) extra space
int minPathSum(vector<vector<int>>& A) {
	const int m = A.size(), n = A[0].size();
	if (m == 0) return 0;
	if (m == 1 && n == 1) return A[0][0];

	vector<int> dp(n);

	// load the 0st row of A into dp  
	dp[0] = A[0][0];
	for (int j = 1; j < n; j++)
		dp[j] = A[0][j] + dp[j - 1];

	// fill none first row and col in dp by state transfer equation
	for (int i = 1; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (j == 0) dp[j] = dp[j] + A[i][0];
			else dp[j] = min(dp[j - 1], dp[j]) + A[i][j];
		}
	}
	return dp[n - 1];
}
```

自个想法，自个差空间复杂度代码：
$O(m*n)$ time, $O(m*n)$ extra space;

```cpp
// method 1
// DP
// F[i,j] = min(F[i,j-1], F[i-1,j]) + A[i,j]
// O(m*n) time, O(m*n) extra space
// not good
int minPathSum(vector<vector<int>>& A) {
	const int m = A.size(), n = A[0].size();
	if (m == 0) return 0;
	if (m == 1 && n == 1) return A[0][0];

	// initialize dp(m*n) matrix
	vector < vector<int> > dp(m);
	for (int i = 0; i < m; i++)
		dp[i].resize(n);

	// fill first row in dp
	dp[0][0] = A[0][0];
	for (int j = 1; j < n; j++)
		dp[0][j] = A[0][j] + dp[0][j - 1];

	// fill first col in dp
	for (int i = 1; i < m; i++)
		dp[i][0] = A[i][0] + dp[i - 1][0];

	// fill none first row and col in dp by state transfer equation
	for (int i = 1; i < m; i++) {
		for (int j = 1; j < n; j++) {
			dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + A[i][j];
		}
	}
	return dp[m - 1][n - 1];
}
```

## 72. Edit Distance(困难，确实挺难的)

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as **1 step**.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

听人家说，这是 **双序列DP问题**. 确实，对我来说，这个题的解法好难理解，即使之前做出了几个dp问题．我怎么可能说自己笨呢!
四个优秀的解释：
http://www.stanford.edu/class/cs124/lec/med.pdf
http://www.cnblogs.com/pandora/archive/2009/12/20/levenshtein_distance.html
http://www.jianshu.com/p/39115986db5a
http://www.dreamxu.com/books/dsa/dp/edit-distance.html

一个分治、dp、贪心的优秀小 book：
http://www.dreamxu.com/books/dsa/dc/subset.html

看了人家很多解释，还是自己想出个例子，自己再顺一遍才能较好的理解．Come on!

假设有 3 种操作：
插入，删除 和 修改．假设它们的 cost 均为 1;
注意有的题目可能它们的 cost 不相同, 比如:
* The costs of both insertion(插入) and deletion(删除) are same value, that is 1;
* The cost of substitution(替换) is 2．

咱自己的例子：

说例子前需说明什么是 dp[i, j].
dp[i, j] 称为 s1[0..i] 串到 s2[0..j] 的最小距离． 表示 字符串 s1[0..i] 转变成 s2[0..j] 的最小代价．在我们的题中，也可理解为最小步骤(因为无论啥操作，cost都是１).
这句话当初对我来说并不好理解．为了更容易的让大家理解，举个例子：

本解释将跟随题目要求，cost 均为１.
符号 ＂＊＂ 代表空字符串．

```
s1 = "a"
s2 = "b"
```

现在要把 s1 变成 s2，问：最少的步骤是多少？　显然，这种情况下，凭直觉，肯定是1步，既， 1步　substitution.
此时：

```
这是要对 s1 做 substitution 操作, 将 a 替换成 b:
dp[i, j] = dp[i-1, j-1] + 1 = dp[0, 0] + 1 =  0 + 1 = 1;
若 s1 的第一个字符 a 和 s2 的第一个字符一样的话： dp[1, 1] = dp[0, 0] = 0, 就不需要替换操作了．

* 	a
	^
	i=1

* 	b
	^
	j=1
```
dp[i = 1, j = 1] 可以写成 dp[i = 0, j = 0] + 1．　就是 s1[0..1] 的串变成 s2[0..1] 的串可表示成 **s1的空串变成s2的空串所需次数 + 1.**
空串变空串？那还用变？精神病的做法是 `＊ -> a －＞＊`,这个cost = 2, 而dp里存的是最小次数或叫做最下距离，那么显然 `dp[i = 0, j = 0] = 0` (空串变空串？两个空串有什么好变化的，对吧)

但真的只有这一种办法吗？不是的．看下面：

```
这是 s1由空变为b 步骤数已知的情况下, 再删除a:
dp[i, j] = dp[i-1][j] + 1 = 1 + 1 = 2

* 	a
^
i-1=0

* 	b
	^
	j=1
```

还有一个情况：

```
这是 s1="a" ,删除a变成空的步骤数已知的情况下，再在最后面插入一个b:
dp[i, j] = dp[i][j-1] + 1 = dp[1][0] + 1 = 1 + 1 = 2

* 	a
	^
	i=１

* 	b
^
j-1=0
```

<font color = red>dp[i, j]只与其左上，左，上，有关．分别为 `dp[i-1,j-1], dp[i,j-1] and dp[i-1,j]`.</font>

总结起来步骤是这样的：

0. m = s1　的长度，　n = s2　的长度;
1. 初始化边界：`dp[0][j] = j, dp[i][0] = i`，其中`i = [0,..,m], j = [0,..,n]`. 就是空串变某个串, 或某个串变空串的步骤数，肯定是那个串的长度了;
2. 若 `s1[i - 1] = s2[j - 1]`, 则`dp[i][j] = min(dp[i - 1][j - 1],	min(dp[i - 1][j] + 1, dp[i][j - 1] + 1));` 这表示若`dp[i - 1][j - 1], dp[i - 1][j]+1, dp[i][j - 1]+1` 已知, 则由这３种 case所表达的状态 到 `dp[i][i]`的状态．我们取上述三种状态的最小值赋值给`dp[i][j]`. 其中`dp[i - 1][j - 1]`不用加１是因为s1和s2最后一个字符是一样的，当然不用再加１，否则＋１(就是修改s1最后字符为s2最后字符，其实说最后字符是不妥当的，我们直接认为当前正在处理s1,s2最后面的那个字符，这么想能使问题简单一些.)
3. 若`s1[i - 1] != s2[j - 1]`, 则`dp[i][j] = min(dp[i - 1][j - 1] + 1, min(dp[i - 1][j] + 1, dp[i][j - 1] + 1));` 注意，除了`dp[i - 1][j - 1] + 1`有变化外，其他没变．
4. 空间复杂度问题：我们可以维护一个(m+1) * (n+1) 的 dp 矩阵，另一种更好的办法是只维护一个 m 或 n 大小的数组.

人家想法，咱的代码:
方法一:
$O(m*n)$ time, $O(m*n)$ extra space.

```cpp
int minDistance(string word1, string word2) {
	int m = word1.length(), n = word2.length();

	// dp: a (m+1) * (n+1) matrix
	vector < vector<int> > dp(m + 1, vector<int>(n + 1, 0));

	// fill values in boundary
	for (int i = 0; i <= m; i++)
		dp[i][0] = i;
	for (int j = 0; j <= n; j++)
		dp[0][j] = j;

	// dp state transfer formula
	for (int i = 1; i <= m; i++)
		for (int j = 1; j <= n; j++)
			if (word1[i - 1] == word2[j - 1])
				dp[i][j] = min(dp[i - 1][j - 1],
						min(dp[i - 1][j] + 1, dp[i][j - 1] + 1));
			else
				dp[i][j] = min(dp[i - 1][j - 1] + 1,
						min(dp[i - 1][j] + 1, dp[i][j - 1] + 1));

	return dp[m][n];
}
```

方法二:
$O(m*n)$ time, $O(m)$ extra space.
墨迹了挺长时间，没写出来．
看人家的吧．https://leetcode.com/problems/edit-distance/discuss/

写本文的时候发现，文字描述起来好费劲，啰里啰嗦，自己写作水平根本不行啊．

## 78. Subsets(中等，集合的子集，经典问题)
Given a set of **distinct** integers, nums, return all possible subsets.

**Note:** The solution set must not contain duplicate subsets.

For example,
If `nums = [1,2,3]`, a solution is:

```
[
 [3],
 [1],
 [2],
 [1,2,3],
 [1,3],
 [2,3],
 [1,2],
 []
]
```

就是求指定集合的所有子集．
三种解法：
* Recursive (Backtracking) 道理能理解，代码不容易写；
* Iterative　本文用的解法，好直接，**易理解和实现**；
* Bit Manipulation　还没学，再补充．

方法1, Recursive (Backtracking)
代码中的注释是我的理解．

```cpp
// Recursive (Backtracking)
vector<vector<int>> subsets(vector<int>& A) {
	sort(A.begin(), A.end()); // sort
	vector < vector<int> > res;
	vector<int> sub;

	// 四个参数
	// A, 二维res, 临时sub, 待处理数组A元素索引号indx
	genSubset(A, res, sub, 0);
	return res;
}

// DFS:
// box 套 box, 好奇的小儿一直往里面开 box
void genSubset(vector<int>& A, vector<vector<int> >& res, vector<int> sub,
		int start) {
	res.push_back(sub);
	for (int i = start; i < A.size(); i++) {
		// 假设 sub = [1]
		// sub里压入一个2, sub = [1, 2]
		sub.push_back(A[i]);

		// 看看压入2后, 还有谁？！！
		genSubset(A, res, sub, i + 1);

		// 还有谁的事,由genSubset探查完后,
		// 把2弹出去, sub = [1], 然后下轮循环, 看看谁还能和 1 搭个伴,
		// 假设A中还有3, 那么下次循环 sub = [1, 3]
		// 直到 1 和所有A中剩余元素都结合过
		sub.pop_back();
	}
}
```

方法2, Iterative
想法：
就是编程实现下面的东西：

```
[[]]
[[], []] --> [[], [1]]
[[],[1]] -复制-> [[],[1],[],[1]] -添值-> [[],[1],[2],[1, 2]]
[[],[1],[2],[1, 2]] -复制-> [[],[1],[2],[1, 2],[],[1],[2],[1, 2]] -添值-> [[],[1],[2],[1, 2],[3],[1,3],[2,3],[1, 2, 3]]
```

<font color = red>上面的例子不太准确（细节写准确太长了，下面针对一个小东西仔细描述过程），但思路是对的．
下面才是程序真正的执行结果：</font>

```
应该是这样的，我们拿出一小段做解释^^
[[],[1]] -复制-> [[],[1],[]] -添值-> [[],[1],[2]] -复制-> [[],[1],[2],[1]] -添值-> [[],[1],[2],[1,2]]
```

人家想法，自己代码：
$O(n^2)$ time, $O(1)$ extra space.

```cpp
vector<vector<int>> subsets(vector<int>& A) {
	sort(A.begin(), A.end()); // sort
	vector < vector<int> > res(1, vector<int>()); // declare res = [[],];
	const int n = A.size();

	for (int i = 0; i < n; i++) {
		const int m = res.size();
		for (int j = 0; j < m; j++) {
			// 有坑, 注意, 不可妄图写成下面这样:
			// res.push_back(res[j].push_back(A[i]));
			res.push_back(res[j]); // [[], []]
			res.back().push_back(A[i]); // [[], [1]]
		}
	}
	return res;
}
```

顺便上面代码展示了一些关于c++写代码的副产品，如下：
1. 声明一个 `[[],]` 的二维数组： `vector < vector<int> > res(1, vector<int>());`
2. 这么写结果不对：　`for(auto it : res) res.push_back(it.push_back(A[i]));`　我晕！
3. 不能妄图写成这样：　`res.push_back(res[j].push_back(A[i]));` 有点边迭代，边修改数组的意思．
4. push_back() 和 back() 的区别：
	* coll.push_back()是把一个元素，放入这个容器的末尾，相当于末尾添加一个元素;
	* coll.back()是获取最后一个元素的迭代器，你可以理解为最后一个元素的指针.

接下来是第３种方法，Bit Manipulation　但还没学，再补充．
TODO Bit Manipulation

## 90. Subsets II
Given a collection of integers that might contain duplicates, ***nums***, return all possible subsets.

**Note:** The solution set must not contain duplicate subsets.

For example,
If `nums = [1,2,2]`, a solution is:

```
[
 [2],
 [1],
 [1,2,2],
 [2,2],
 [1,2],
 []
]
```
有重复值的序列的所有子集．
核心想法是：
把 [2,2] 看成1个特殊的元素，它不想其他元素只有两种状态(存在，不存在)．
<font color = red>This element([2, 2]) has more than two choices: you can either NOT put it into the subset, or put ONE 2 into the subset, or put TWO 2s into the subset.</font>
上面是老外的解释，很精彩且到位．

这题，对我来说，即使知道想法，编这个东西难度也挺大．
仔细考察人家的代码后，发现下面的事实：

```
下面程序生成序列的顺序如下：

[[]]->[[],[1]]->[[],[1],[2],[2,2],[1,2],[1,2,2]]
                         |<- []->| |<-  [1]  ->|

|<- []->| 这个地方代表 [2],[2,2] 是由 [] 生成的;
|<-[1]->| 这个地方代表 [1,2],[1,2,2] 是由 [1] 生成的.
```

了解了上述生成顺序，下面的代码就好理解了．

人家想法，复写人家代码(那想法好难实现)．
有三个亮点：
1. `i += count; // smart~!`
2. 以 i 为 base,对 count 计数: `while (count + i < A.size() && A[count + i] == A[i]) count++;`
3. preN 保存了 res 未改变前的长度;
4. 用一个 vector 保存 res[k]: `vector<int> inst = res[k]; // []`. <font color = red>这个太重要了，因为可以实现 [1] -> [1,2](store this in res) -> [1,2,2](store this value in res again base on [1, 2])</font>

$O(n^2)$ time, $O(1)$ extra space.

```cpp
// sample: A = [1, 2, 2]
// 即使知道想法，编这个东西难度也挺大
// 把 2,2 看成一个特殊的元素.
// 可以出现1个2, 也可以出现两个2
// 下面程序生成序列的顺序如下：
// [[]]->[[],[1]]->[[],[1],[2],[2,2],[1,2],[1,2,2]]
//                         |<- []->| |<-  [1]  ->|
vector<vector<int>> subsetsWithDup(vector<int>& A) {
	sort(A.begin(), A.end());
	vector<vector<int> > res = { {}}; //[[],]

	for (int i = 0; i < A.size();) {

		// 以 indx = i 为base
		// 在A中向后查和A[i]相同的元素个数 -> count
		int count = 0;
		while (count + i < A.size() && A[count + i] == A[i]) count++;

		// res 未改之前的长度 -- 初始时，这个熊样--> res = [[]]
		int preN = res.size();
		for (int k = 0; k < preN; k++) {
			vector<int> inst = res[k]; // []

			for (int j = 0; j < count; j++) {
				// e.g. 若 inst = []
				// when j = 0, inst = [2]
				//      j = 1, inst = [2, 2]
				// inst 所代表的 array 都将送入 res
				inst.push_back(A[i]);
				res.push_back(inst);
			}
		}
		i += count; // smart~!
	}
	return res;
}
```

## 75. Sort Colors
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

**Note:**
You are not suppose to use the library's sort function for this problem.

这题就是想把乱序的`[2 2 1 0 1 1 0 2]`排列成有序的`[0 0 1 1 1 2 2 2]`.

方法一：两趟循环，第一趟数0,1,2的个数，第二趟修改数组A, 思想简单且无编程难度．
$O(2n)$ time, $O(1)$ extra space.

```cpp
// two-pass algorithm
// [ 2 2 1 0 1 1 0 2]
void sortColors(vector<int>& A) {
	int c_0 = 0, c_1 = 0;

	for (int i = 0; i < A.size(); i++)
		if (A[i] == 0) c_0++;
		else if (A[i] == 1) c_1++;

	for (int i = 0; i < A.size(); i++)
		if (i < c_0) A[i] = 0;
		else if (i >= c_0 && i < (c_1 + c_0)) A[i] = 1;
		else A[i] = 2;
}
```

方法二，人家的想法了，就是扫描数组，发现２就送入队尾方向，发现０就送队首方向，最后１自然就在中间，就排好了．这方法编程不容易．

```
设定 zero = 0, sec = A.size()-1 两个指针.
若　A[i] = 2, swap(A[i], A(sec--));
若　A[i] = 0, swap(A[i], A(zero++));
```

```cpp
// one-pass algorithm
// [ 2 2 1 0 1 1 0 2]
void sortColors(vector<int>& A) {
	int zero = 0, sec = A.size() - 1;
	for (int i = 0; i <= sec; i++) {
		while (A[i] == 2 && i < sec) swap(A[i], A[sec--]);
		while (A[i] == 0 && i > zero) swap(A[i], A[zero++]);
	}
}
```

## 89. Gray Code(中等，了解啥是 gray code)

知道啥是 gray code 就是收获了．
下面介绍了 gray code 发明的 motivation, 了解动机后就知道啥是 gray code 了．
https://zh.wikipedia.org/wiki/格雷码

```cpp
// 这题让我知道了啥是 gray code
// gray code (https://zh.wikipedia.org/wiki/格雷码)
// 編碼的方式定義為每個鄰近數字都只相差一個位元，因此也稱為最小差異碼.
// 可以使裝置做數字步進時只更動最少的位元數以提高穩定性
// The idea is simple. G(i) = i^ (i/2).
vector<int> grayCode(int n) {
	vector<int> res;
	for (int i = 0; i < 1 << n; i++)
		res.push_back(i ^ i >> 1);
	return res;
}
```

## 58. Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters `' '`, return the length of last word in the string.

If the last word does not exist, return 0.

**Note:** A word is defined as a character sequence consists of non-space characters only.

For example,
Given `s = "Hello World"`,
return `5`.

我的方法是：
1. **先消除字符串首、尾的空格;**
2. 再从字符串尾向首查找，直到找到空格或者指针到队首都没找到空格为止，返回最后一个 word 的长度.

我方法，我代码：
$O(n)$ time, $O(1)$ extra space.


```cpp
// 解题关键：消除 s 的首尾空格
int lengthOfLastWord(string s) {
	const int n = s.size() - 1;
	if (s.size() == 0) return 0;

	int begin = 0, end = n;

	//消除字符串首尾空格
	if (s[0] == ' ') {
		for (int i = 0; i < s.size(); i++) {
			if (s[i] != ' ') {
				begin = i;
				break;
			}
		}
	}

	if (s[n] == ' ') {
		for (int i = n; i >= 0; i--) {
			if (s[i] != ' ') {
				end = i;
				break;
			}
		}
	}

	// 从尾部开始查找
	for (int i = end; i >= begin; i--) {
		if (s[i] == ' ') return end - i;
		else if (i == begin) return end - begin + 1;
	}
}
```

## 31. Next Permutation(中等，搞清楚啥是 next permutation)
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

```
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
```

这题我看了半天都没搞懂啥是"下一个排列(next permutation)".找了些资料(http://www.geeksforgeeks.org/find-next-greater-number-set-digits/),才了解啥叫 next permutation.
这么弄：
<font color = green>假设 `A = [2 1 8 7 6 5]`, 它的 next permutation 咋求？　这样求：
1. 从右往左，5 6 7 8 都是增序，突然 1 降下来了， 那就所定 1;
2. 1 右边有 8 7 6 5, 找比1大的但却是这四个数中较小的那个数, 就是 5 喽;
3. 交换 1 和 5, 结果是 `A = [2 5 8 7 6 1]`;
4. 然后 对 `[8 7 6 1]` 增序排序. 最后返回 `A = [2 5 1 6 7 8]`.</font>

打完，收功！
这么做就能得到某序列的所谓的 next permutation 了？
是的！
为啥？
没为啥，边个程序实现它就完事了！

题目要求中有个特殊情况，就是当 `A = [4 3 2 1]` 时，返回 `A = [1 2 3 4]`. 这就是本题的全部解释了.
更加详细的考虑及设置，在我的代码注释中写的很清楚.

人家想法，自个代码:
有个 cpp 副产品: `reverse(A.begin() + start, A.end());`
这个 start 是 `A = [2 1 8 7 6 5]` 中元素 8 的 index, start = 2.
$O(n)$ time, $O(1)$ extra space. 严格来说，里面用到了排序，就不是`O(n)` time 了．

```cpp
// e.g.
// A = [2 1 8 7 6 5]
// step 1: from right to left, seek element '1';
// step 2: from right to left, seek '5' and swap(A[1], A[5])
//  --- After step 2, A = [2 1 8 7 6 5] --> A = [2 5 8 7 6 1]
// step 3: reverse(A.begin() + 2, A.end())
//  --- return A = [2 5 1 6 7 8]

// special case: A = [4 3 2 1] --> will return A = [1 2 3 4]

void nextPermutation(vector<int>& A) {
	const int n = A.size();
	if (n == 0 || n == 1)
		return; //special case

	int start;

	// 4 3 2 1, can not found A[i]<A[i+1]
	bool found = false;

	// step 1
	for (int i = n - 2; i >= 0; i--) {
		if (A[i] < A[i + 1]) {
			start = i + 1;
			found = true; // found the case A[i]<A[i+1]
			break;
		}
	}

	// special case
	// 4 3 2 1 --> return 1 2 3 4 directly
	if (found == false) {
		reverse(A.begin(), A.end());
		return;
	}

	// step 2
	for (int j = n - 1; j >= start; j--) {
		if (A[j] > A[start - 1]) {
			swap(A[j], A[start - 1]);
			break;
		}
	}

	// step 3
	reverse(A.begin() + start, A.end());

	return;
}
```

## 39. Combination Sum(medium, backtrack 的经典应用, 重要)
Given a set of candidate numbers (C) (**without duplicates**) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

* All numbers (including target) will be positive integers.
* The solution set must not contain duplicate combinations.

For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:

```
[
 [7],
 [2, 2, 3]
]
```

本题是 backtrack(回溯法) 的经典应用.通过本题，仔细观察 backtrack 基本框架，并感受其应用.
另外, subset 的题目也用 backtrack 方法.

人家想法，自个代码:
* cpp 副产品： `v.pop_back();` 弹出队尾元素.
* 要注意的是: **下面代码中 backtrack 方法中的 res, temp, A, 尤其是 temp, 他们都分别指向对应的一个对象，无论 backtrack 方法被嵌套地调用多少次！**

```cpp
// backtrace method
vector<vector<int>> combinationSum(vector<int>& A, int ta) {
	sort(A.begin(), A.end());
	vector < vector<int> > res;
	vector<int> temp;
	backtrack(res, temp, A, ta, 0);
	return res;
}

void backtrack(vector<vector<int> >& res, vector<int>& temp, vector<int>& A,
		int remain, int start) {
	if (remain < 0)
		return;
	else if (remain == 0) {
		res.push_back(temp);
		return;
	} else {
		for (int i = start; i < A.size(); i++) {
			temp.push_back(A[i]);

			// not i + 1, because A[i] might be reused.
			backtrack(res, temp, A, remain - A[i], i);

			temp.pop_back();
		}
		return;
	}
}
```


## 40. Combination Sum II
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

**Note:**

* All numbers (including target) will be positive integers.
* The solution set must not contain duplicate combinations.

For example, given candidate set `[10, 1, 2, 7, 6, 1, 5]` and target 8,
A solution set is:

```
[
 [1, 7],
 [1, 2, 5],
 [2, 6],
 [1, 1, 6]
]
```

这题用到 backtrack 方法, 需去重.
e.g.
`A = [1 1 2 5 6 7 10], target = 8`
正确输出应该是：
`[[1,1,6],[1,2,5],[1,7],[2,6]]`

<font color = red>
难点在去重条件：
* 我写的，错误：　`if(i >= 1 && A[i] == A[i - 1]) continue;`
	- 错误输出: `[[1,2,5],[1,7],[2,6]]`
* 人家写的，正确: `if ((i >= 1) && (A[i] == A[i - 1]) && (i > start)) continue;`

差别就是 i > start 条件，挺不容易的想出来的．
</font>

自己想法，自个代码(被人家修正^^):

```cpp
// backtrack
// A = [1 1 2 5 6 7 10]
vector<vector<int>> combinationSum2(vector<int>& A, int ta) {
	sort(A.begin(), A.end());
	vector < vector<int> > res;
	vector<int> temp;
	backtrack(A, res, temp, ta, 0);
	return res;
}

void backtrack(vector<int>& A, vector<vector<int> >& res, vector<int> temp,
		int remain, int start) {
	if (remain < 0)
		return;
	else if (remain == 0)
		res.push_back(temp);
	else {
		for (int i = start; i < A.size(); i++) {

			// not correct: if(A[i] == A[i - 1] && i >= 1) continue;
			// (i > start) is hard think, but important.

			if ((i >= 1) && (A[i] == A[i - 1]) && (i > start))
				continue; // check duplicate combination

			temp.push_back(A[i]);
			backtrack(A, res, temp, remain - A[i], i + 1); // i + 1, next element
			temp.pop_back();
		}
	}
}
```

## 46. Permutations(medium, backtrack, 重要)
Given a collection of **distinct** numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

```
[
 [1,2,3],
 [1,3,2],
 [2,1,3],
 [2,3,1],
 [3,1,2],
 [3,2,1]
]
```

做了几个 backtrack 类的题目了, 对这个题还是没思路.
<font color = red>
我目前的经验, backtrack 题目，要确定下面三个重要部件:
1. 把 temp 压入 res 的条件！
	- 通常这个样 `if (condition) {res.push_back(temp);}`
2. 怎样生成符合题意的 temp!
	- 通常这个样 `else{for(int i=var; i<A.size(); i++){temp.push_back(A[i]); backtrack(params); temp.pop_back();}}`
3. backtrack 函数参数列表.
</font>

上面三点考虑时似乎没个先后顺序，好难哦．

人家想法，自个代码(被教育后的结果):

```cpp
vector<vector<int>> permute(vector<int>& A) {
	vector < vector<int> > res;
	vector<int> temp;
	backtrack(A, res, temp);
	return res;
}

void backtrack(vector<int>& A, vector<vector<int> >& res, vector<int> temp) {
	// 重要部件
	if (temp.size() == A.size()) {
		res.push_back(temp); // 1. 啥时候 把 temp 压入 res, 很重要！！
		return;
	} else {
		// 2. 如何生成 temp 很重要！！
		for (int i = 0; i < A.size(); i++) {
			// contain A[i] is true
			if (find(temp.begin(), temp.end(), A[i]) != temp.end())
				continue;

			temp.push_back(A[i]);
			backtrack(A, res, temp);
			temp.pop_back();
		}
		return;
	}
}
```


## 47. Permutations II(medium, backtrack, 重要, 条件较难思考)
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
`[1,1,2]` have the following unique permutations:

```
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

本题有重复元素，条件较难思考，做这个题费了小劲．
总体框架是应用 backtrack 解决．

样例：`[1 1 2] -> [1 2 1] -> [2 1 1]`
设定一个 `vector<bool> used(A.size(), false);` 表示哪些元素用过, 用过的用`true`表示.

`[1 1 2] -> [1 2 1]` dfs到这种状态后, `i` 将要为 `1`, 就是下面的样子.

```
[1 1 2] 此时所有的 used[0 - 2] 都为 false.
   i
```

`if (i > 0 && A[i - 1] == A[i] && !used[i - 1]) continue; // <--这句话，想不出来啊`

**若无上面那个判断条件(有这个标志的那行 '<--'),将会再次产生下面的序列:
[1 1 2], 这里的第一个1是上面i=1所指的元素，第二个1是i=0的元素.**

**为防止这种事的发生，就应该跳过i=1的那个元素,　仔细观察, 发现：**
<font color = green>
1. `i > 0;`
2. `A[i] = A[i-1];`
3. `A[i-1] = false;`
</font>

**满足上述3条的元素， 就应跳过！**

<font color = red>
经验:
想写清楚条件，必须把简单例子用笔纸走一遍;
找出自己跑的结果与正确结果不同之处;
针对错误点， 设置if()语句,避免之!
</font>

自己代码:

```cpp
// e.g.
// [1 1 2] -> [1 2 1] -> [2 1 1]
vector<vector<int>> permuteUnique(vector<int>& A) {
	sort(A.begin(), A.end());
	vector < vector<int> > res;
	vector<int> temp;

	// 用 used[0-2], true 表用过
	vector<bool> used(A.size(), false);
	backtrack(res, temp, A, used);
	return res;
}

void backtrack(vector<vector<int> >& res, vector<int>& temp, vector<int>& A,
		vector<bool> used) {
	if (temp.size() == A.size())
		res.push_back(temp);
	else {
		for (int i = 0; i < A.size(); i++) {
			if (used[i] == true) {
				continue;
			}
			if (i > 0 && A[i - 1] == A[i] && !used[i - 1])
				continue; // <--这句话，想不出来啊
			// [1 1 2] -> [1 2 1]  dfs到这种状态后, i 将要为 1, 就是下面的样子.

			// [1 1 2]    此时所有的 used[0 - 2] 都为 false.
			//    i
			// 若无上面那个判断条件(有这个标志的那行 '<--'),将会再次产生下面的序列:
			// [1 1 2], 这里的第一个1是上面i=1所指的元素，第二个1是i=0的元素
			// 为防止这种事的发生，就应该跳过i=1的那个元素,　仔细观察, 发现：
			// 1. i > 0;
			// 2. A[i] = A[i-1];
			// 3. A[i-1] = false;
			// 满足上述3条的元素，就应跳过！
			//
			// 经验:
			// 想写清楚条件，必须把简单例子用笔纸走一遍;
			// 找出自己跑的结果与正确结果不同之处;
			// 针对错误点，设置if()语句,避免之!

			temp.push_back(A[i]);
			used[i] = true;
			backtrack(res, temp, A, used);
			used[i] = false;
			temp.pop_back();
		}
	}
}
```

## 77. Combinations(medium, backtrack, 重要, 弄了１小时)
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

```
[
 [2,4],
 [3,4],
 [2,3],
 [1,2],
 [1,3],
 [1,4],
]
```

做了好几个这种题了，就是 backtrack problem, １小时做出，但不容易，各种小毛病.
我的程序蠢蠢的建立了一个 `vector<int> A;`. 其实，只玩弄变量n就行了．

**我犯的错误，如下：**
`start + 1, start++ 和 ++start`

```
自己第一次写的代码是
for (int i = start; i < A.size(); i++) {
	temp.push_back(A[i]);

	// 应把 start+1 改为 ++start, start 应该随 i 变化而变化
	backtrack(res, temp, A, len, start + 1);
	temp.pop_back();
}

e.g.
n = 4, k = 2
[1 2 3 4]
结果应为:        [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
我错误结果为:    [[1,2],[1,3],[1,4],[2,2],[2,3],[2,4],[3,2],[3,3],[3,4],[4,2],[4,3],[4,4]]
```

自个想法，自个代码：

```cpp
vector<vector<int>> combine(int n, int k) {
	vector < vector<int> > res;
	vector<int> temp;
	vector<int> A;
	for (int i = 1; i <= n; i++)
		A.push_back(i);

	backtrack(res, temp, A, k, 0);
	return res;
}

void backtrack(vector<vector<int> >& res, vector<int>& temp, vector<int>& A,
		const int len, int start) {
	if (temp.size() == len) {
		res.push_back(temp);
		return;
	}

	for (int i = start; i < A.size(); i++) {
		temp.push_back(A[i]);
		// start++;
		// 下面血淋淋地体现了
		// start + 1, start++ 和 ++start 的巨大不同了
		backtrack(res, temp, A, len, ++start);
		temp.pop_back();
	}
}
```

## 216. Combination Sum III(medium, backtrack, 本类问题做的最快的一次)
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Example 1:

Input: k = 3, n = 7

Output:

`[[1,2,4]]`


Example 2:

Input: k = 3, n = 9

Output:

`[[1,2,6], [1,3,5], [2,3,4]]`

关于 backtrack problem 做的最快的一次.
定义了２个东西:
* start
* remain

自己想法，自己代码:

```cpp
vector<vector<int>> combinationSum3(int k, int n) {
	vector<int> A = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	vector<vector<int> > res;
	vector<int> temp;
	backtrack(res, temp, A, k, 0, n);
	return res;
}

void backtrack(vector<vector<int> >& res, vector<int>& temp, vector<int>& A,
		int k, int start, int remain) {
	if (temp.size() == k && remain == 0) {
		res.push_back(temp);
		return;
	}
	for (int i = start; i < A.size(); i++) {
		temp.push_back(A[i]);
		backtrack(res, temp, A, k, ++start, remain - A[i]);
		temp.pop_back();
	}
}
```

## 152. Maximum Product Subarray(中等, 神奇的 swap)
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array `[2,3,-2,4]`,
the contiguous subarray `[2,3]` has the largest product = `6`.

Idea:
https://leetcode.com/problems/maximum-product-subarray/discuss/
**keep max(min) value in imax(imin) varable when pointer = i.**

<font color = "blue">
swap起到重要作用.
虽然求子数组最大乘积，但最小乘积也需维护，因为：
A Truth is:
big -> small when (A[i] < 0)
small -> big when (A[i] < 0)
whatever imax, imin is stored negt or posi in.
</font>

人家想法，自个代码：
$O(n)$ time, $O(1)$ extra space.

```cpp
// https://leetcode.com/problems/maximum-product-subarray/discuss/
// A = [2,3,-2,4]   return [2,3] = 6
int maxProduct(vector<int>& A) {
	int r = A[0], imax = r, imin = r;
	for (int i = 1; i < A.size(); i++) {
		// A Truth is:
		// big -> small when (A[i] < 0)
		// small -> big when (A[i] < 0)
		// whatever imax, imin is stored negt or posi in.
		if (A[i] < 0)
			swap(imax, imin);

		// keep max(min) value in imax(imin) when pointer = i
		imax = max(A[i], imax * A[i]);

		// 之所以记录 imin,
		// 是因为 if(A[i] < 0) swap(imax, imin);
		// 用到 imin
		imin = min(A[i], imin * A[i]);
		r = max(r, imax);
	}
	return r;
}
```
