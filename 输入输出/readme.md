https://www.nowcoder.com/exam/oj?page=1&tab=%E7%AE%97%E6%B3%95%E7%AC%94%E9%9D%A2%E8%AF%95%E7%AF%87&topicId=372
练习


---

好的，下面是一份**Python笔试/刷题输入读取全模板**，覆盖你能遇到的几乎所有情形。代码都基于 `sys.stdin`，速度快且通用。

---

## 🚀 基础前置（推荐写在最前面）

```python
import sys

# 将标准输入转为迭代器，便于逐行读取
input = sys.stdin.readline
```

> 用 `input()` 代替内置 `input()` 能避免大量输入时的性能瓶颈。

---

## 📋 情形速查表

| 编号 | 情形描述                                 | 关键方法                         |
|------|------------------------------------------|----------------------------------|
| 1    | 单行单个数据                             | `int(input())`                   |
| 2    | 单行多个数据（已知个数）                 | `map(int, input().split())`      |
| 3    | 单行多个数据（未知个数）                 | `list(map(int, input().split()))` |
| 4    | 已知行数 N，每行一个数据                 | 循环 `range(N)`                  |
| 5    | 已知行数 N，每行多个数据                 | 循环 + `split()`                 |
| 6    | 第一行给定 N，接下来 N 行                | 同上                             |
| 7    | 直到 EOF（文件结束）所有行               | `for line in sys.stdin`          |
| 8    | 多组测试数据，由空行分隔                 | `split('\n\n')`                  |
| 9    | 多组测试数据，每组首行给定组内行数       | 循环读取直至 EOF                 |
| 10   | 有标题行（跳过第一行）                   | `next(sys.stdin)`                |
| 11   | 忽略空行和注释行（`#` 开头）             | `if not line.strip() or line.startswith('#'): continue` |
| 12   | 读取整个文件为一个大字符串               | `sys.stdin.read()`               |
| 13   | 读取整个文件为一个二维数组（矩阵）       | 逐行 `split()`                   |
| 14   | 混合类型（字符串 + 数字）                | 部分转 `int/float`               |
| 15   | 需要保留空格/原格式                      | 用 `rstrip('\n')` 而非 `strip()` |

---

## 📖 详细模板与代码

### 1️⃣ 单行单个数据

**输入**：
```
42
```

**代码**：
```python
n = int(input())
s = input().strip()   # 字符串
```

---

### 2️⃣ 单行多个数据（已知个数，如 3 个整数）

**输入**：
```
10 20 30
```

**代码**：
```python
a, b, c = map(int, input().split())
```

---

### 3️⃣ 单行多个数据（未知个数，存入列表）

**输入**：
```
1 2 3 4 5 6 7
```

**代码**：
```python
nums = list(map(int, input().split()))
```

---

### 4️⃣ 已知行数 N，每行一个数据

**输入**：
```
5
apple
banana
cherry
date
elderberry
```

**代码**：
```python
n = int(input())
items = [input().strip() for _ in range(n)]
```

---

### 5️⃣ 已知行数 N，每行多个数据（固定列数）

**输入**：
```
3
1 2
3 4
5 6
```

**代码**：
```python
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
```

---

### 6️⃣ 第一行给定 N，接下来 N 行（同上，最常见）

**输入**：
```
4
Alice 85
Bob 92
Charlie 78
David 88
```

**代码**：
```python
n = int(input())
for _ in range(n):
    name, score = input().split()
    score = int(score)
    # 处理逻辑
```

---

### 7️⃣ 直到 EOF（文件结束）所有行

**适用场景**：没有给出总行数，读至输入流结束（本地运行按 `Ctrl+D` / `Ctrl+Z`）

**输入**：
```
line1
line2
line3
...
```

**代码**：
```python
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue   # 可选择跳过空行
    # 处理 line
```

或一次性读入全部行列表：
```python
lines = [line.strip() for line in sys.stdin if line.strip()]
```

---

### 8️⃣ 多组测试数据，由**空行**分隔

**输入**：
```
1 2 3
4 5 6

7 8 9
10 11 12
```

**代码**（按块处理）：
```python
content = sys.stdin.read().strip()
blocks = content.split('\n\n')   # 空行分隔
for block in blocks:
    lines = block.splitlines()
    # 处理一个 block 的数据
    for line in lines:
        nums = list(map(int, line.split()))
        # ...
```

---

### 9️⃣ 多组测试数据，每组首行给出该组行数（直到 EOF）

**输入**：
```
3
1 2
3 4
5 6
2
7 8
9 10
```

**代码**：
```python
while True:
    line = input()
    if not line:
        break
    n = int(line.strip())
    group = []
    for _ in range(n):
        group.append(list(map(int, input().split())))
    # 处理这一组 group
```

---

### 🔟 有标题行（跳过第一行）

**输入**：
```
Name    Age
Alice   30
Bob     25
```

**代码**：
```python
header = input()          # 读走标题行，不用
# 方法一：继续读剩余行
for line in sys.stdin:
    name, age = line.split()
    age = int(age)
    # ...
# 方法二：全部读入再切片
lines = sys.stdin.readlines()
for line in lines:
    # ...
```

---

### 1️⃣1️⃣ 忽略空行和 `#` 开头的注释行

**输入**：
```
# This is a comment
1 2 3

4 5 6
# Another comment
7 8 9
```

**代码**：
```python
for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    nums = list(map(int, line.split()))
    # ...
```

---

### 1️⃣2️⃣ 读取整个文件为一个大字符串

**输入**（任意格式）：
```
Hello World
This is a test.
```

**代码**：
```python
data = sys.stdin.read()
# data 是一个包含所有内容（含换行符）的字符串
```

---

### 1️⃣3️⃣ 读取整个文件为二维数组（矩阵），行数/列数未知

**输入**：
```
1 2 3
4 5 6
7 8 9
```

**代码**：
```python
matrix = [list(map(int, line.split())) for line in sys.stdin if line.strip()]
```

---

### 1️⃣4️⃣ 混合类型（例如第一行整数 N，第二行字符串 S，第三行浮点数）

**输入**：
```
5
hello world
3.14
```

**代码**：
```python
n = int(input())
s = input().strip()
f = float(input())
```

---

### 1️⃣5️⃣ 需要保留行内空格（如字符串可能包含空格）

**输入**：
```
John Doe
Jane   Smith   # 中间有多个空格
```

**代码**（用 `rstrip('\n')` 仅去掉换行，保留空格）：
```python
for line in sys.stdin:
    line = line.rstrip('\n')   # 不去掉行首尾空格
    # 处理 line
```

---

## 🧰 常用小技巧

| 需求                               | 代码                                                                 |
|------------------------------------|----------------------------------------------------------------------|
| 一行中取前两个数，忽略后面多余部分 | `a, b, *_ = map(int, input().split())`                               |
| 读取后立即判断是否输入结束         | `if not line: break`（配合 `input = sys.stdin.readline`）            |
| 一次性读入所有数字（忽略空格换行） | `nums = list(map(int, sys.stdin.read().split()))`                    |
| 快速读取大文件（不逐行处理）       | `data = sys.stdin.buffer.read()` 获取 bytes，自行解码                |

---

## ✅ 标准程序框架（竞赛用）

```python
import sys

def solve():
    input = sys.stdin.readline
    # 你的代码从这里开始
    pass

if __name__ == "__main__":
    solve()
```

---

如果还有特殊的输入格式（比如二进制数据、带引号的 CSV、嵌套结构等），告诉我具体样例，我可以再补充对应的模板。