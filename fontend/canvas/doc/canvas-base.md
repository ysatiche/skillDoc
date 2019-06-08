# canvas基础

***

## 初始化画布

在html中声明画布，本例中画布的长为 1366px 宽为 768px (可根据需求自定义)
```
<canvas id="canvas" style="width: 1366px; height: 768px;"></canvas>
```

在 js 中初始化画布
```
let canv = document.getElementById('canvas') // 获取canvas dom对象
let ctx = canv.getContext('2d') // 得到 canvas CanvasRenderingContext2D对象，对画布的操作基本都是基于ctx来的
```

## 绘制路径

> 图形的基本元素是路径，路径是通过不同颜色和宽度的线段或曲线相连形成的不同形状的点的集合。

<font color=#D4B51B>路径的绘制步骤？</font><br>
1. 首先，你需要创建路径起始点(beginPath(), moveTo())
2. 然后你使用画图命令去画出路径(lineTo(), arcTo()等)
3. 把路径封闭(不是必须的)(closePath())
4. 一旦路径生成，你就能通过描边或填充路径区域来渲染图形(fill, stroke)

我们来一一说下这几个绘图常用的api

`beginPath()` 新建一条路径

`moveTo(x, y)` 在当前路径下新建一条子路径，并将笔触移动到指定的坐标x以及y上

`lineTo(x, y)` 绘制一条从当前位置到指定x以及y位置的直线

`arc(x, y, radius, startAngle, endAngle, anticlockwise)` 画一个以（x,y）为圆心的以radius为半径的圆弧（圆），从startAngle开始到endAngle结束，按照anticlockwise给定的方向（默认为顺时针）来生成

`quadraticCurveTo(cp1x, cp1y, x, y)` 绘制二次贝塞尔曲线，cp1x,cp1y为一个控制点，x,y为结束点

`bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y)` 绘制三次贝塞尔曲线，cp1x,cp1y为控制点一，cp2x,cp2y为控制点二，x,y为结束点

`stroke()` 通过线条来绘制图形轮廓

`fill()` 通过填充路径的内容区域生成实心的图形

比如我们要绘制一个实心三角形，如下：
```
function draw() {
  var canvas = document.getElementById('canvas');
  if (canvas.getContext) {
    var ctx = canvas.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(75, 50);
    ctx.lineTo(100, 75);
    ctx.lineTo(100, 25);
    ctx.fill(); // 填充图形区域
  }
}
```

> Path2D 对象 -- Path2D()会返回一个新初始化的Path2D对象（可能将某一个路径作为变量——创建一个它的副本，或者将一个包含SVG path数据的字符串作为变量）


## 样式设置

> 色彩 如果我们想要给图形上色，有两个重要的属性可以做到：fillStyle 和 strokeStyle

```
ctx.fillStyle = "rgb(255,165,0)"; // 填充颜色值
ctx.strokeStyle = "rgba(255,165,0,1)"; // 边框颜色值
```

我们用下面的方法新建一个 canvasGradient 对象，并且赋给图形的 fillStyle 或 strokeStyle 属性，实现线性或者径向的渐变
```
var lingrad2 = ctx.createLinearGradient(0,50,0,95);
lingrad2.addColorStop(0.5, '#000');
lingrad2.addColorStop(1, 'rgba(0,0,0,0)');
ctx.strokeStyle = lingrad2;
```

也可以使用图案的应用跟渐变很类似的，创建出一个 pattern 之后，赋给 fillStyle 或 strokeStyle 属性即可
```
var img = new Image();
img.src = 'someimage.png';
var ptrn = ctx.createPattern(img,'repeat');
ctx.fillStyle = ptrn;
```

> 线条样式 通过lineTo() arc()等绘制路径的api所绘制的线条都受它的影响

`lineWidth = value`  线条的宽度

`lineCap = type type=[butt, round, square]` 线条尾端的样式

`lineJoin = type type=[round, bevel, miter]` 设定线条与线条间接合处的样式

`setLineDash(segments)` 设置当前虚线样式

## save() 与 restore()

## 两层画布