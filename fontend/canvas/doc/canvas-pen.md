# 画笔 

***

## 添加事件监听
实现画笔功能，最基础就是得到鼠标（或者触摸）的点，所以，我们得先添加事件监听来获取点的数组。

对于鼠标来说，我们常常使用mouse相关事件，对于可触摸屏来说，我们常常使用touch事件，其实，可以使用point事件它对于鼠标和触摸屏都可以兼容。

```
this.canv.addEventListener('pointerdown', this.drawBegin.bind(this))
this.canv.addEventListener('pointermove', this.drawing.bind(this), { passive: true })
this.canv.addEventListener('pointerup', this.drawEnd.bind(this))
```

## 绘制简单路径

#### 获取点和过滤点
对于点的处理，我们单独对点封装成一个类
```
export default class Point {
  constructor (x, y) {
    this.x = x // x坐标
    this.y = y // y坐标
  }
}
```
#### 直线绘制和曲线绘制
有了封装的点的类，接下来，我们来对画笔的基础处理进行一个封装。
```
class ElementBase {
  constructor () {
    this.pointList = [] // 绘制的点的数组
  }
}
```
首先，我们来封装一个获取点的方法
```
_getPoint (event) {
  return new Point(event.layerX, event.layerY)
}

/**
  * 添加过滤之后的采样点
  * @param {Point} point 点
  * @returns {number} 如果成功添加采样点，返回过滤后采样点数组长度，否则返回-1
  */
_addPoint (point) {
  if (this._pointFilter(point)) {
    this.pointList.push(point)
    return this.pointList.length
  } else {
    return -1
  }
}
```
我们应该还需要一个点过滤器，防止画笔不动时，同样的点不断被添加到该数组
```
/**
  * 点过滤器
  * @param {Point} point 点
  * @returns {Boolean} 返回是否被过滤，true表示不过滤，false表示被过滤
  */
_pointFilter (point) {
  if (this.pointList.length === 0) return true
  const lastPoint = this.pointList[this.pointList.length - 1]
  if (point.x === lastPoint.x && point.y === lastPoint.y) {
    return false
  } else {
    return true
  }
}
```

有了这些点，我们封装一些常见的绘制方法
```
/**
  * 绘制一个点
  * @param {Point} point 点
  */
_renderPoint (ctx, { color, width }) {
  ctx.fillStyle = color
  ctx.beginPath()
  ctx.arc(this.pointList[0].x, this.pointList[0].y, width / 2, 0, 2 * Math.PI, true)
  ctx.fill()
}

/**
  * 绘制一个路径
  * @param pointList 点的集合
  */
_renderPath (ctx, { color, width }) {
  ctx.strokeStyle = color
  ctx.lineWidth = width
  ctx.lineCap = 'round'
  ctx.lineJoin = 'round'
  let endIndex = this.pointList.length - 1
  for (let i = this.from; i < endIndex; i++) {
    if (i === 0) {
      const middlePoint = this._getMiddlePoint(this.pointList[i], this.pointList[i + 1])
      this._renderLineTo(ctx, this.pointList[i], middlePoint)
    } else if (i === endIndex) {
      if (this.finish) {
        const middlePoint = this._getMiddlePoint(
          this.pointList[i - 1],
          this.pointList[i]
        )
        this._renderLineTo(ctx, this.pointList[i], middlePoint)
      }
    } else {
      this._renderQuadraticCurve(
        ctx,
        this.pointList[i - 1],
        this.pointList[i],
        this.pointList[i + 1]
      )
    }
  }
}
/**
  * 绘制一条直线
  * @param {Point} p1 点
  * @param {Point} p2 点
  */
_renderLineTo (ctx, p1, p2) {
  ctx.beginPath()
  ctx.moveTo(p1.x, p1.y)
  ctx.lineTo(p2.x, p2.y)
  ctx.stroke()
}
/**
  * 获取中点
  * @param {Point} p1 点
  * @param {Point} p2 点
  */
_getMiddlePoint (p1, p2) {
  return {
    x: Math.floor((p1.x + p2.x) / 2),
    y: Math.floor((p1.y + p2.y) / 2)
  }
}
/**
  * 绘制一条二次贝塞尔曲线，根据连续三个点，绘制中间的贝塞尔曲线
  * @param {Point} p1 点
  * @param {Point} p2 点
  * @param {Point} p3 点
  */
_renderQuadraticCurve (ctx, p1, p2, p3) {
  let preMiddelPoint = this._getMiddlePoint(p1, p2)

  let lastMiddelPoint = this._getMiddlePoint(p2, p3)

  let controlPoint = p2
  ctx.beginPath()
  ctx.moveTo(preMiddelPoint.x, preMiddelPoint.y)
  ctx.quadraticCurveTo(
    controlPoint.x,
    controlPoint.y,
    lastMiddelPoint.x,
    lastMiddelPoint.y
  )
  ctx.stroke()
}
```
#### 笔记优化
