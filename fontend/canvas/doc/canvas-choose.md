# 笔记点选和圈选
***

## 笔记的数据化和笔记选择含义

> 对于每一条笔记，在数据层面，只要储存笔记的点的数组（点是有序的）且知道每个点的连接方式（直线，贝赛尔曲线连接等）就可以还原出该条笔记。

所以，对于笔记的选择，只要判断所选区域里是否含有点数组中的某一点，即可判定在所选区域内。

## 笔记圈选

#### 所选区域

笔记圈选的所选区域其实是该条曲线绘制后，首尾点连接后canvas判定的区域。

#### 笔记圈选区域的简单判断

我们知道，每一条笔记里储存的点的量都是很大的，有些甚至能到上万点，而我们需要对每一条笔记都进行判断，所以，非常耗性能，那我们是否能进行一些简单的预判断，来处理一些笔记容易判断的情况呢？

我们知道，每一天笔记都可以用一个矩形包围起来，矩形的可以通过遍历这些点获取，矩形的左上点为((left)min, (top)min)即所有点的left，top值最小值时的点，矩形的右下角点为((right)max, bottom(max))

所以，假设两个笔记的外矩形不想交，则证明两条笔记肯定不相交。

#### 使用ctx.isPointInPath(x, y)来判断

在 canvas 中，我们可以使用ctx.isPointInPath(x, y)来判断点是否在当前ctx围成的区域中。

<font color=#D4B51B>注意：ctx.isPointInPath(x, y)判断的区域指的是当前最后一条路径（即最后一次beginPath()）的最后一次子路径（即最后一次moveTo()）围城的区域,同时ctx.scale不能设置成倍数，否则得进行其他处理</font>

```
// 框选处理
handleChoosePen () {
  // this.eles 储存当前笔记的数组，每一个元素就是一条笔记（一条笔记是一个对象）
  if (this.eles.length < 1) return
  // 获取框选的笔记,
  let chooseZone = this.eles.pop()
  // this.historyIndex记录当前显示笔记的index
  this.historyIndex = this.eles.length - 1
  if (chooseZone.drawPoints.length < 1) return
  let choosedEleIdxArr = [] // 被选中的笔记index
  let choosedEleZoomOpt = null // 被选中的区域框
  // 点选，点选的话就是将当前点为中心的一个正方形区域
  if (chooseZone.drawPoints.length <= 10) {
    this.clear(this.ctxTemp, this.canvTemp)
    let clickPoint = chooseZone.drawPoints[0]
    let baseRect = 20
    this.ctxTemp.beginPath()
    this.ctxTemp.moveTo(clickPoint.x - baseRect / 2, clickPoint.y - baseRect / 2)
    this.ctxTemp.lineTo(clickPoint.x - baseRect / 2, clickPoint.y + baseRect / 2)
    this.ctxTemp.lineTo(clickPoint.x + baseRect / 2, clickPoint.y + baseRect / 2)
    this.ctxTemp.lineTo(clickPoint.x + baseRect / 2, clickPoint.y - baseRect / 2)
    this.ctxTemp.fill()
    let arr = [
      {
        x: clickPoint.x - baseRect / 2,
        y: clickPoint.y - baseRect / 2
      },
      {
        x: clickPoint.x - baseRect / 2,
        y: clickPoint.y + baseRect / 2
      },
      {
        x: clickPoint.x + baseRect / 2,
        y: clickPoint.y + baseRect / 2
      },
      {
        x: clickPoint.x + baseRect / 2,
        y: clickPoint.y - baseRect / 2
      }
    ]
    chooseZone.drawPoints = arr
  }
  // 圈选
  let chooseZoneInfo = this.getPenOuterZone(chooseZone.drawPoints)
  let shapePoint = new ShapePoint()
  for (let i = 0; i < this.eles.length; i++) {
    let tmpEle = this.eles[i]
    // 检测当前笔记是几何图形
    if (tmpEle.type === 'shape') {
      // 获取几何图形的点，通过线获取点
      let shapeArr = shapePoint._getShapePoints(tmpEle.config.type, tmpEle.config.start, tmpEle.config.end)
      tmpEle.drawPoints = shapeArr
    }
    if (tmpEle.type === 'pen' || tmpEle.type === 'shape') {
      // 获取每一个笔记的外框
      const info = this.getPenOuterZone(tmpEle.drawPoints)
      // 判断选中区域的外框与笔记外框是否相交
      if (this.isRectOverlap(chooseZoneInfo, info)) {
        // 对每一个点进行检测
        for (let j = 0; j < tmpEle.drawPoints.length; j++) {
          let point = tmpEle.drawPoints[j]
          // 判断点是否在选中区域的外框，如果在外框中则使用isPointInPath判断
          if (this.isPointInRect(point, chooseZoneInfo) && this.ctxTemp.isPointInPath(point.x, point.y)) {
            console.warn(`第${i + 1}笔被选中`)
            choosedEleIdxArr.push(i)
            break
          }
        }
      }
    }
  }
  this.clear(this.ctxTemp, this.canvTemp)
}

// 获取笔记的外方框
getPenOuterZone (pointList = []) {
  if (pointList.length < 1) return null
  let left = pointList[0].x
  let right = pointList[0].x
  let top = pointList[0].y
  let bottom = pointList[0].y
  for (let i = 1; i < pointList.length; i++) {
    if (pointList[i].x < left) {
      left = pointList[i].x
    }
    if (pointList[i].x > right) {
      right = pointList[i].x
    }
    if (pointList[i].y < top) {
      top = pointList[i].y
    }
    if (pointList[i].y > bottom) {
      bottom = pointList[i].y
    }
  }
  // if (top <= bottom || left <= right) {
  //   return null
  // }
  return {
    left: left,
    right: right,
    top: top,
    bottom: bottom
  }
}

// 判断两个方框是否相交
isRectOverlap (r1, r2) {
  return !(((r1.right < r2.left) || (r1.bottom < r2.top)) || ((r2.right < r1.left) || (r2.bottom < r1.top)))
}

// 判断点是否在方框里
isPointInRect (point, r) {
  return ((point.x >= r.left) && (point.x <= r.right) && (point.y >= r.top) && (point.y <= r.bottom))
}
```

