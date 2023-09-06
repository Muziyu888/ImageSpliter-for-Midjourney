# Midjourney批量切图软件✂️
---
## 超快🚀超简单的切图工具,开包即用,乐享切图 🤣 

<div align="center"><img src="https://github.com/Muziyu888/ImageSpliter-for-Midjourney/blob/main/pics/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE(4).jpg?raw=true" alt="Example Image" width="600"></div>

我是一个**纯粹的python小白**,我从未学习过任何编程或者代码之类的
我发现我找不到一个用于**批量切割MIDJOURNEY图片的工具**
于是!! **我打算自己做一个!!**  😤 
于是我成为了**OPENAI**的plus会员(~~我才不是单纯的想尝试chatgpt-4.0和代码解释器~~:)


### 我在制作的过程当中,遇到了非常多的问题,比如:

- **程序界面应该是怎么样子的?**( 😡 这个问题我思考了接近2个小时!!! 🧠 )

- **我的切割的逻辑是怎么样的?**(  👏  多亏了 chatgpt)

- **哦对了,我还需要一个预览图.**( 😚 其实这是给你准备的,因为我会怎么样切割)

- **我需要能够切换预览图**( 💋 好吧,这也是给你准备的)


但是最激动人心的是,**我意识到了一个问题!**
那就是当我切割的**图片数量非常多**的时候,比如200张或者300张图片
那么我的程序就太过缓慢了
于是,我(chatgpt推荐)加入了**多进程处理**的功能, ✊🏼 直接把cpu占用率提升至**100%!!!!**
所以当你使用这个程序仍然觉得切割速度很慢时,~~你要知道,这不是我的问题~~ :)

<div align="center"><img src="https://github.com/Muziyu888/ImageSpliter-for-Midjourney/blob/main/pics/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE(5).jpg?raw=true" alt="Example Image" width="700"></div>

### 而且为了让程序看起来更加像那么回事儿
我还添加了2个**重磅更新!**
~~(为了添加这两个功能我熬夜到凌晨4点!)~~

- **让预览图可以跟随窗口的缩放**( 🧙🏻‍♂️ 啊,对了我还加入了延迟检测, 以确保不会在重复缩放中造成卡顿)
- **让你可以使用拖拽功能选择图片!**( ✋🏻直接将图片们或者文件夹拖入程序界面就OK了,我真是**天才**啊)

~~我敢打赌,这一定是最好用的midjourney图片切割工具,如果你认为不好用的话,请去责怪openai~~
哈利路亚!

---

## 好了,现在开始食用说明:

1. **打开程序** ✌🏼
1. **拖入**你要切割的图片 🎴 (可以是**一张**🎴或者**多张**🎴🎴🎴,如果拖入的是文件夹 📁 ,那么文件夹内**所有图片**都要被切)
1. 如果你不想使用**酷炫的拖拽功能**,那么你也可以使用 **按钮选择**
1. 再选择一个切割完成的图片的 💾 **保存文件夹**(这个**没法使用拖拽,我也不知道为什么.**)
1. 设置 **切割方式** (行和列,如果你不清楚,你可以观看**预览图上的绿线** 🤢 ,这有助于你理解切割方式)
1. 设置你想要的格式(jpg,png,origin,**建议使用JPG,🧠不怕死的使用PNG**)
1. 用 ⬅️ 和 ➡️ 按钮**随便预览**一下,看看有没有出岔子(~~因为既然我做了这个功能,你要是不用我会很难过~~)
1. 点击 **开始切割** 💪 按钮(点击之前,**保存你的PS程序或者VScode代码**,或者别的什么东西)
1. 然后你会陷入一阵 **绝望的卡顿** ☠️ (我建议你此刻什么都不要做,因为你的cpu已经在爆炸的边缘了)\
1. 如果你运气好的话,那么你将👌👌**成功的完成图片切割**


---

以下是我与ChatGPT的问答链接,如果你感兴趣的话,你可以点开看一看,虽然他们只会浪费你几分钟的时间,且你不会得到任何收益.

[第一次聊天:建立基本的代码框架](https://chat.openai.com/share/f65686db-bae7-4b7d-83d4-f870a268463e)
[第二次聊天:修复各种bug](https://chat.openai.com/share/ba836d06-5c96-42d8-85d1-b158e39b21d8)

#### 这是我对chatgpt提出的需求!这可是我思考了2个小时的成果!

```
我希望使用pyside6制作一个用于切割图片的工具,我已经制作好了他的ui界面,我会发送给你,请你逐段阅读这份ui文件,直到你完整的查看了完整的代码,查看完成后,帮助我实现以下的功能:
1,我可以使用pushbutton来选择一个或多个图片文件作为输入文件,并将文件的地址设置到lineedit的地址栏当中,如果选择了多个文件,使用';'将他们的路径分隔开
2,我可以使用pushbutton_2来选一个文件夹,并将文件夹内的所有图片文件作为输入文件,并将文件夹的地址设置到lineedit的地址栏当中.
3,我可以使用pushbutton_3来选择一个文件夹作为输出文件夹, 并将文件夹的地址设置到lineedit_2的地址栏当中,所有被切割完成的图片将保存在这个文件夹当中
4,通过radiobutton,radiobutton_2,radiobutton_3来选择所需要保存的图片的格式,其中radiobutton被选择时已JPG格式保存被分割的图片,radiobutton_2被选择时,以png格式保存被分割的图片,当radiobutton_3被选择时,使用图片的原格式保存被分割的图片
5,当我点击pushbutton_4时,开始进行分割操作,并且分割的操作需要用多进程的方式来进行,调用我的全部CPU核心,以保证分割的速度,切割的方式需要参考spinBox_2和spinBox中的值,其中spinBox_2代表图片将被切成几列,spinBox代表图片将被切成几行,例如spinBox_2 = 2,spinBox = 2,那么图片将被等比切割为4份.
6,当我使用pushbutton或者pushbutton_2完成了选择文件或者文件夹时,在graphicsView窗口会显示图片,图片的尺寸不应该超过graphicsView窗口的大小,并且图片位于graphicsView窗口的中心位置,并会根据spinBox_2和spinBox中的值,用绿色的线条,实时的显示图片即将被切割的方式,当我选择一张或多张图片作为输入时,使用第一张进行显示,当我选择一个文件夹作为输入时,使用文件夹内的第一个图片作为显示.
7,在label_5中会实时的显示我一共选择了多少张图片作为输入,并显示当前预览图片的序列,例如当我选择了5张图片作为输入时,这里应该显示"1 / 5",并且我可以使用pushButton_5选择上一张图片作为预览图和使用pushButton_6选择下一张图片作为预览图,来依次查看预览图,每当我切换预览图时label_5和graphicsView会实时的更新预览图.
8,我可以使用拖拽的方式来完成输入文件或者输入文件夹的选择,并且会正确的更新lineedit的地址信息,和label_5的显示和graphicsview的显示图片.
```