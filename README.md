# !!!建议看PDF或者跳转语雀：[《Meta仿真 Habitat-Sim使用文档》](https://www.yuque.com/u1647260/ggkiip/kx3bxbsgs2dbitz1?singleDoc#)，这里排版不好

> Github：[https://github.com/facebookresearch/habitat-sim](https://github.com/facebookresearch/habitat-sim)
> 官网：[https://aihabitat.org/](https://aihabitat.org/)


<a name="pPE93"></a>
# 动机
由于配置环境、掌握新软件老是一个麻烦的事情，我通常会先看一下各位前辈的卓越奉献，非常感谢。<br />现在为了能够帮助大家快速熟悉Facebook（或Meta，总感觉Facebook更有感觉）的Habitat仿真器，同时避免踩坑。
<a name="kNf6p"></a>
# 
<a name="DxmS0"></a>
# Habitat简介
在安装之前首先介绍一下Habitat是干嘛的吧，Habitat是Facebook做的一个环境仿真器，对于研究机器人等需要交互的技术是一个比较好的选择，并且也兼容比较多数据集和场景。环境相对逼真，并且还能够和环境中的3D物体进行接触。目前应该主要用于研究Embodied AI。不过之前还有看到和ROS一起使用来运行CMU开发TARE等一系列环境探索算法，这个我也作为一个坑，之后填。现在先看一下它的环境效果吧：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2028181/1670918592426-75119455-1a9e-4433-a0db-458f0a822605.png#averageHue=%23827164&clientId=uc5e27f0b-33ca-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=370&id=u8e1388a7&margin=%5Bobject%20Object%5D&name=image.png&originHeight=668&originWidth=950&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1203343&status=done&style=none&taskId=u657ff2c9-43d8-40b1-b5a8-61431913696&title=&width=526.62109375)<br />支持的一些环境和模型：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2028181/1670918546039-57747018-0809-45e4-9964-8855f7aa5af6.png#averageHue=%23fcfaf8&clientId=uc5e27f0b-33ca-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=251&id=u02e76cbb&margin=%5Bobject%20Object%5D&name=image.png&originHeight=201&originWidth=757&originalType=binary&ratio=1&rotation=0&showTitle=false&size=53735&status=done&style=none&taskId=ub0f8176b-1af9-412b-b7ba-4e643fa5ce9&title=&width=946.2499858997764)


<a name="RWwYe"></a>
# 安装
<a name="CY0iJ"></a>
## 1. 环境准备：
<a name="U8m1z"></a>
### 1.1 系统版本
> 在`windows`下面是搜索不到库的：，这里可以看到

目前Habitat只支持两个版本：`MacOS`和`Linux`<br />我的环境：`Ubuntu18.04`
<a name="fgV1s"></a>
### 1.2 Conda环境配置：
> python版本可以用`3.7`或者`3.8`，`3.9`是不支持的

<a name="bzvEy"></a>
#### 官方环境配置：
```
# We require python>=3.7 and cmake>=3.10
conda create -n habitat python=3.7 cmake=3.14.0
conda activate habitat
```
<a name="VESpK"></a>
#### 我的环境配置：
```
conda create -n habitat python=3.8 cmake
conda activate habitat
```

<a name="nM6PZ"></a>
### 1.3 Habitat安装：
我的安装命令【最常用】：`conda install habitat-sim withbullet -c conda-forge -c aihabitat`
<a name="sSgVY"></a>
#### 详细介绍
Habitat安装分别支持以下参数：

   - 有显示器版本和无显示器版本：`headless`
   - 是否安装`bullet`物理引擎：`withbullet`
   - 最新版本`nightly`（仅当您需要最新版本中尚未提供的特定功能时才应使用此功能）：将`-c aihabitat` 换成`-c aihabitat-nightly`
> 以上参数可以自由组合，通常都是安装最常用版本

- 【最常用版本】有显示器、有`bullet`物理引擎：
```
conda install habitat-sim withbullet -c conda-forge -c aihabitat
```

- 有显示器版本：
```
conda install habitat-sim -c conda-forge -c aihabitat
```

- 无显示器版本（即没有附加显示器，例如在集群中）和具有多个 GPU 的机器上安装（此参数依赖于 EGL，因此不适用于` MacOS`）：
```
conda install habitat-sim headless -c conda-forge -c aihabitat
```

- 无显示器、有`bullet`物理引擎
```
conda install habitat-sim withbullet headless -c conda-forge -c aihabitat
```
> 对于指定版本只需要用`=`指定就行：
> 如安装0.1.6版本：`conda install habitat-sim=0.1.6 -c conda-forge -c aihabitat`


<a name="mjHXy"></a>
# 测试使用
<a name="xAl9b"></a>
## 没有物理交互的版本：

1. 下载3D场景：
```
python -m habitat_sim.utils.datasets_download --uids habitat_test_scenes --data-path /path/to/data/
```
> /path/to/data/ 是你想将数据放在的文件夹
> 这个下载的场景并不提供予以标签，如果想要测试`example.py`程序的语义功能，需要下载[Matterport3D](https://github.com/facebookresearch/habitat-sim/blob/main/DATASETS.md)

2. 下载3D物体：
```
python -m habitat_sim.utils.datasets_download --uids habitat_example_objects --data-path /path/to/data/
```

3. 测试运行：
> 如果是直接conda安装的使用C++版本的命令就好
> 注意：源码安装应该要调整路径，小白慎用

C++：
```
#C++
# ./build/viewer if compiling locally
habitat-viewer /path/to/data/scene_datasets/habitat-test-scenes/skokloster-castle.glb
```
Python：用conda安装好像是没法用的
```
#Python
#NOTE: depending on your choice of installation, you may need to add '/path/to/habitat-sim' to your PYTHONPATH.
#e.g. from 'habitat-sim/' directory run 'export PYTHONPATH=$(pwd)'
python examples/viewer.py --scene /path/to/data/scene_datasets/habitat-test-scenes/skokloster-castle.glb
```

4. 按键使用（详细见[Habitat C++查看器](#rTuen)）

W、S、A、D就是前后左右，Z是飞升，X是下地，鼠标左键是调整视角。
> 后面对于有接触部分详细介绍各种按键操作



<a name="VA7FE"></a>
## 有物理交互的版本：能够抓取3D物体，Habitat的物理基于`Bullet`物理引擎

1. 首先需要下载ReplicaCAD apartment 数据集（140MB）：下不下来找我

默认数据会下载到`habitat-sim/data/`路径下，可以通过添加`--data-path /path/to/data/`来修改
```
python -m habitat_sim.utils.datasets_download --uids replica_cad_dataset
```
源码安装的可以运行以下命令：
```
# with source (from inside habitat_sim/)
python src_python/habitat_sim/utils/datasets_download.py --uids replica_cad_dataset
```
> 比较完整有光照的数据，将`replica_cad_dataset`换成`replica_cad_baked_lighting`（480MB）

2. 测试使用

C++：
```
habitat-viewer --enable-physics --dataset data/replica_cad/replicaCAD.scene_dataset_config.json -- apt_1
```
Python：
```
python examples/viewer.py --dataset data/replica_cad/replicaCAD.scene_dataset_config.json --scene apt_1
```
> 运行有光照的数据：
> `--dataset data/replica_cad_baked_lighting/replicaCAD_baked.scene_dataset_config.json --scene Baked_sc1_staging_00`

3. 场景功能指令（详细见[Habitat C++查看器](#rTuen)）：

对着场景窗口点击H能够在命令行看到控制指令的详情，这里提供中文翻译版本

<a name="KELjt"></a>
## example.py脚本功能使用
conda安装的没有example.py，但是可以直接下载github的examples文件夹就行，在chrome浏览器有个插件`GitZip for github`，能够只下载单个文件，不需要进行git clone了，方便conda安装的伙伴使用。<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2028181/1670923020988-d91a5149-5dc1-4799-8931-aae1e53819cf.png#averageHue=%23fcfcfc&clientId=u9e3cc53d-9887-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=40&id=bskQ7&margin=%5Bobject%20Object%5D&name=image.png&originHeight=32&originWidth=185&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2698&status=done&style=none&taskId=uea232584-1802-435b-ad65-2684fc6d202&title=&width=231.24999655410653)<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2028181/1670923147163-2d411e4c-8c37-4308-adcb-405e45dfc280.png#averageHue=%2396989c&clientId=u9e3cc53d-9887-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=305&id=eKfYC&margin=%5Bobject%20Object%5D&name=image.png&originHeight=244&originWidth=376&originalType=binary&ratio=1&rotation=0&showTitle=false&size=34920&status=done&style=none&taskId=u1c5df0d2-1519-47b4-8c7f-3d1aa319d0d&title=&width=469.99999299645435)

<a name="S6S0O"></a>
### 没有显示画面的测试：
这个例子是agent（机器人）按照规定路径走动，最终能够看到统计信息，类似：<br />`640 x 480, total time: 3.208 sec. FPS: 311.7`
```
python /path/to/habitat-sim/examples/example.py --scene /path/to/data/scene_datasets/habitat-test-scenes/skokloster-castle.glb
```

<a name="gkcNd"></a>
### 运行example.py的一个交互的小例子
```
python examples/example.py --scene /path/to/data/scene_datasets/habitat-test-scenes/skokloster-castle.glb --enable_physics
```
> 其实没什么卵用，就是一个固定视角下，看到几个物体能够掉落在桌子上，以体现物理交互特性。


加上`--save_png`能够生成每一个时刻的第一视角图像，注意会在当前的文件夹底下生成。<br />我为此写了一个脚本，能够将生成的图像放到一个`demo`文件夹，并且输出视频`demo.mp4`，运行如下：
> Github：[https://github.com/GuoPingPan/Habitat-Sim-Usage-Chinese](https://github.com/GuoPingPan/Habitat-Sim-Usage-Chinese)

```
 #其他参数见脚本
python img_2_video..py ./
```
<a name="rpW50"></a>
#### 
<a name="IKguU"></a>
### 复现[Habitat ICCV'19](https://arxiv.org/abs/1904.01201)的榜单
> 注意：这里应该需要先下载MP3D数据集

```
examples/benchmark.py --scene /path/to/mp3d_example/17DRP5sb8fy/17DRP5sb8fy.glb
```
<a name="Yaq0e"></a>
### 
<a name="kI3IH"></a>
### 加载MP3D或者是Gibson house
```
examples/example.py --scene path/to/mp3d/house_id.glb
```
<a name="TW0PW"></a>
### 
<a name="z1hEN"></a>
### 官方提供的`pointnav_mp3d`的一个例子
[https://aihabitat.org/docs/habitat-lab/habitat-lab-demo.html](https://aihabitat.org/docs/habitat-lab/habitat-lab-demo.html)

<a name="rTuen"></a>
# Habitat-sim C++ 查看器
欢迎使用 Habitat-sim C++ 查看器应用程序！鼠标功能<br />在 LOOK 模式下（默认）：<br />   左键：单击并拖动以旋转代理并向上/向下查看。<br />   右键：（物理）随机产生一个物体。<br />   shift + left：取被点击物体的语义ID和标签（目前只支持HM3D）；<br />   shift + right：显示物体的表明网格。<br />   ctrl + right：（物理）单击一个对象以对其进行体素化并显示体素化。<br />   滚轮：视野放大和缩小（+shift 用于细粒度控制）

在 GRAB 模式下（需要在命令行加上使用“--enable-physics”）：<br />左键：并拖动以拾取和移动具有点对点约束的对象（例如球形接头）。<br />右键：拖动物体不受重力影响。<br />右键拖动物体不放开 + 滚轮：<br />     + alt：拖住的物体进行yaw轴旋转<br />     + ctrl：拖住的物体进行pitch轴旋转<br />     + alt+ctrl：拖住的物体进行roll轴旋转

关键命令：<br />   esc：退出应用程序。<br />   'H'：显示此帮助信息。<br />   'm': 切换鼠标模式 (LOOK | GRAB)。<br />   TAB/Shift-TAB ：循环到场景数据集中的下一个/上一个场景。<br />   ALT+TAB：重新加载当前场景。<br />代理控制：<br />   'wasd'：向前/向后、向左/向右移动代理的身体。<br />   'zx'：向上/向下移动代理的身体。<br />   箭头键：向左/向右转动特工的身体，让相机向上/向下看。<br />   '9'：将代理随机放置在 NavMesh 上（如果已加载）。<br />   'q'：查询代理的状态并打印到终端。<br />   '['：将代理位置/方向保存到“./saved_transformations/camera.year_month_day_hour-minute-second.txt”。<br />   ']'：从文件系统加载代理位置/方向，或者从当前实例中的上次保存加载代理位置/方向。

相机设置<br />   '4'：循环切换相机模式（相机、鱼眼、等距柱状）<br />   '5'：切换正射/透视相机。<br />   '6'：重置正射相机缩放/透视相机 FOV。<br />   '7'：循环渲染模式（RGB、深度、语义）

可视化实用程序：<br />   'l'：使用“default_light_override.lighting_config.json”中配置的设置覆盖默认照明设置。<br />   'e'：启用/禁用视锥体剔除。<br />   'c'：显示/隐藏 UI 覆盖。<br />   'n'：显示/隐藏 NavMesh 线框。<br />   'i'：将屏幕截图保存到“./screenshots/year_month_day_hour-minute-second/#.png”。<br />   ','： 渲染子弹碰撞形状调试线框覆盖（白色=活动，绿色=睡觉，蓝色=想睡觉，红色=不能睡觉）

对象交互：<br />   SPACE：打开/关闭物理模拟<br />   '.'：如果不是连续模拟，则进行单个模拟步骤。<br />   '8'：在代理前面实例化一个随机原始对象。<br />   'o'：在代理前面实例化一个随机的基于文件的对象。<br />   'u'：删除最近实例化的刚体对象。<br />   't'：通过在出现提示时输入文件路径，从 URDF 文件实例化相机前面的铰接对象。<br />     +ALT：导入带有固定基础的对象。<br />     +SHIFT 快速重新加载先前指定的 URDF。<br />   'b'：切换对象边界框的显示。<br />   'p'：将当前模拟状态保存到 SceneInstanceAttributes JSON 文件（具有非冲突文件名）。<br />   'v'：（物理学）反转重力。<br />   'g'：（物理）显示阶段的有符号距离梯度矢量场。<br />   'k'：（物理）迭代舞台体素化符号距离场的不同范围。

附加实用功能：<br />   'r'：将最近模拟帧的重播写入 --gfx-replay-record-filepath 指定的文件。<br />   '/'：将当前场景的元数据信息写入控制台。

导航轨迹可视化：<br />   '1'：切换轨迹可视化的记录位置。<br />   '2'：构建并显示轨迹可视化。<br />   '3'：切换单色/多色轨迹。<br />   '+'：增加弹道直径。<br />   '-'：减小轨迹直径。

   'F'：（音频）在代理前面添加音频源<br />   '0'：（音频）运行音频模拟


<a name="Kn6HO"></a>
# Reference

---

**其他问题还是看官网叭：**[**https://github.com/facebookresearch/habitat-sim**](https://github.com/facebookresearch/habitat-sim)<br />**还可以在这留言，我尽力解答！**
