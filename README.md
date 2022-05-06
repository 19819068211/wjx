"# wjx" 

这是一个针对问卷星考试已知答案为了解放双手自动点击快速提交而仿写的程序

之前使用python+selenium，但会触发各种各样的智能验证，比较麻烦且耽误时间，从搜索引擎得知使用pyppeteer可以有效避免此问题，故仿造了此程序

早先，在github中没有找到pyppeteer实现的例子，就当抛砖引玉了

此程序根据网络资源改写，可以实现问卷星自动点击答题提交，仅供学习使用

举一反三，可以用于很多网站类答题

这是我自用的一个程序，可能与大家的不太适配，我们的问卷停止收集了，不再贴出了，相应部分在程序中有所标注，大家可以根据自己的问卷进行修改

调出F12开发人员工具，既可以找到元素位置，右键复制xpath或selector，对程序进行修改即可

比较常用的chromium淘宝源：https://registry.npmmirror.com/binary.html?path=chromium-browser-snapshots/

chromium根据自己需要选择

这是一个仅供学习娱乐的玩具程序，我本身不是计算机专业，对python也不太熟悉，拙劣之处还请pull requests或issue，谢谢

感谢网络开源大神保姆式的教程

使用最笨的方法，各位大神如果有更好更快的实现办法，欢迎提交issue或pr

如果报错no module named "xxx"，那就pip install "xxx"

首先，按win+r，打开运行，输入cmd，回车，进入命令行

git clone https://github.com/19819068211/wjx.git

cd wjx

python wjx.py

修改程序方法不再赘述了

才疏学浅，班门弄斧，献丑了

谢谢大家！
