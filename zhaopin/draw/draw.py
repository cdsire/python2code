# coding:utf-8
import matplotlib
import matplotlib.pyplot as plt # 数据可视化


# 配置字体
matplotlib.rcParams["font.sans-serif"] = ["simhei"]
matplotlib.rcParams["font.family"] = "sans-serif"

plt.bar([1],[123],label=u"广东")
plt.bar([2],[103],label=u"江苏")
plt.bar([3],[93],label=u"山东")
plt.bar([4],[73],label=u"河南")

# matplotlib.use("Agg")
plt.legend()    # 绘制
plt.savefig("1.png")
plt.show()  # 显示