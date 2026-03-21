def getDigit(n:int):
    if not n :
        return [0]
    return [int(d) for d in str(n)]
    
'''
在 Python 中，拆分数位最快的方式通常是 字符串转换 + 列表推导，
而不是手动循环取余。
这是因为 Python 的整数除法和取余操作虽然底层是 C 实现的，
但 while 循环本身在 Python 解释器中运行，有较大的开销；
而 str(n) 和字符串迭代完全在 C 层面执行，速度更快。

'''
def isHappy(n: int) -> bool:
    if n==1 :
        return True
    '''
    
    '''
    result=set()
    curnumber = n
    while curnumber not in  result:
        result.add(curnumber)
        digit=getDigit(curnumber)
        curnumber = sum(key * key for key in digit) #重点 
        if curnumber == 1:
            return True    
    return False



if __name__ == "__main__":
    print(isHappy(19))
    print(isHappy(2))
    print(isHappy(10))

