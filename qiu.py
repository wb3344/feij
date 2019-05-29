# 先构造一个类，类包含我们分析中提到的所需的三个信息
class ball:
    def __init__(self, name, ori, posi):
        self.name = name
        self.ori = ori
        self.posi = posi


# 存储小球信息的0位置不用，从1开始
ball_info = [0]
n, l, t = input().split()
n, l, t = int(n), int(l), int(t)
# 输入小球位置信息
posi_info = input().split()
# 将小球信息初始化后添加到ball_info数组中
for i in range(1, n + 1):
    ball_info += [ball(i, 1, int(posi_info[i - 1]))]
# 时间一秒一秒增加t次
for i in range(t):
    for info in range(1, n + 1):
        # 小球到达边界时，方向变为相反方向
        if (ball_info[info].posi == l and ball_info[info].ori == 1) or (
                ball_info[info].posi == 0 and ball_info[info].ori == -1):
            ball_info[info].ori *= -1
        # 小球位置改变，在对应方向上加一
        ball_info[info].posi += ball_info[info].ori
    ##
    for info in range(1, n):
        # 如果存在两个小球位置相同，即他们两个相撞。则各自方向改变
        for oinfo in range(info + 1, n + 1):
            if ball_info[info].posi == ball_info[oinfo].posi:
                ball_info[info].ori *= -1
                ball_info[oinfo].ori *= -1
                break
print(ball_info[1].posi, end='')
for i in range(2, n + 1):
    print("", ball_info[i].posi, end='')
