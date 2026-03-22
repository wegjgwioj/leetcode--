# 无重叠区间
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda p: p[0])  # [1,2][1,3][2,3][3,4]
        end = intervals[0][1]
        ans = 0

        for start, current_end in intervals[1:]:
            if start < end:
                ans += 1
                end = min(end, current_end)
            else:
                end = current_end

        return ans


if __name__ == "__main__":
    
    s1=Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
    s2=Solution().eraseOverlapIntervals([[1,2], [1,2], [1,2] ])
    s3=Solution().eraseOverlapIntervals([ [1,2], [2,3] ])
    print( "\n",s1,s2,s3)


'''
最像 `435. 无重叠区间` 的，是这一组“区间 + 贪心”题：

1. `452. 用最少数量的箭引爆气球`
相似度最高。也是区间题，也常用“按右端点排序”做贪心。

2. `646. 最长数对链`
本质和 `435` 很接近，可以看成“最多选多少个不重叠区间”。

3. `252. 会议室`
更简单，判断区间是否冲突。

4. `253. 会议室 II`
同样是区间冲突，但要算最少需要几个会议室，常用堆。

5. `56. 合并区间`
经典区间题，先排序再扫一遍。

6. `57. 插入区间`
是在 `56` 的基础上多一步插入处理。

7. `1288. 删除被覆盖区间`
也是排序后处理区间包含关系。

8. `986. 区间列表的交集`
双指针处理两个区间数组，区间题里很常见。

如果你想按“和 435 的思路接近程度”刷，我建议顺序是：

`56 -> 57 -> 1288 -> 435 -> 452 -> 646 -> 252 -> 253 -> 986`

其中最值得一起记模板的是：

- `435`：最少删除多少个区间
- `452`：最少用多少支箭
- `646`：最多能选多少个链

这三题都和“尽量保留右端点更小的区间”关系很深。

如果你愿意，我可以直接帮你整理一份“区间题刷题清单”，按模板分类成：
- 排序合并类
- 贪心选择类
- 堆处理冲突类
- 双指针交集类

'''