# 几何图形

## 几何图形绘制
```
class OriginShape {
  constructor (ctxTemp = null) {
    this.ctxTemp = ctxTemp
    this.opts = {}
  }

  getCenterPoint () {
    let x = (this.opts.end.x + this.opts.start.x) / 2
    let y = (this.opts.end.y + this.opts.start.y) / 2
    return { x, y }
  }
  // 公共函数，画圆、椭圆、半圆、虚线圆、实线圆
  _circle (center, a, b, semiCircle) {
    this.ctxTemp.beginPath()
    let r = a > b ? a : b
    let ratioX = a / r
    let ratioY = b / r
    this.ctxTemp.save()
    this.ctxTemp.scale(ratioX, ratioY)
    if (semiCircle === 'up') {
      // 上半圆 虚线
      this.ctxTemp.save()
      this.ctxTemp.setLineDash([10, 15])
      this.ctxTemp.arc(
        center.x / ratioX,
        center.y / ratioY,
        r,
        0,
        Math.PI,
        true
      )
      this.ctxTemp.stroke()
      this.ctxTemp.restore()
    } else if (semiCircle === 'down') {
      // 下半圆 实线
      this.ctxTemp.beginPath()
      this.ctxTemp.arc(
        center.x / ratioX,
        center.y / ratioY,
        r,
        0,
        Math.PI,
        false
      )
      this.ctxTemp.stroke()
    } else {
      // 整圆
      this.ctxTemp.beginPath()
      this.ctxTemp.arc(
        center.x / ratioX,
        center.y / ratioY,
        r,
        0,
        2 * Math.PI,
        false
      )
      this.ctxTemp.stroke()
    }
    this.ctxTemp.restore()
    this.ctxTemp.closePath()
  }
  _axis (direction) {
    let lineWidth = this.ctxTemp.lineWidth
    let p1 = {}
    let p2 = {}
    let p3 = {}
    let p4 = {}
    let p5 = {}
    if (direction === 'x') {
      p1 = {
        x: this.opts.start.x,
        y: (this.opts.end.y + this.opts.start.y) / 2
      }
      if (this.opts.end.x < this.opts.start.x) {
        p2 = {
          x: this.opts.end.x + 15,
          y: (this.opts.end.y + this.opts.start.y) / 2
        }
        p5 = {
          x: p2.x - 15,
          y: p2.y
        }
      } else {
        p2 = {
          x: this.opts.end.x - 15,
          y: (this.opts.end.y + this.opts.start.y) / 2
        }
        p5 = {
          x: p2.x + 15,
          y: p2.y
        }
      }
      p3 = {
        x: p2.x,
        y: p2.y - 10 - lineWidth / 2
      }
      p4 = {
        x: p2.x,
        y: p2.y + 10 + lineWidth / 2
      }
    } else if (direction === 'y') {
      if (this.opts.end.y < this.opts.start.y) {
        p1 = {
          x: (this.opts.end.x + this.opts.start.x) / 2,
          y: this.opts.start.y
        }
        p2 = {
          x: (this.opts.end.x + this.opts.start.x) / 2,
          y: this.opts.end.y + 15
        }
      } else {
        p1 = {
          x: (this.opts.end.x + this.opts.start.x) / 2,
          y: this.opts.end.y
        }
        p2 = {
          x: (this.opts.end.x + this.opts.start.x) / 2,
          y: this.opts.start.y + 15
        }
      }
      p3 = {
        x: p2.x - 10 - lineWidth / 2,
        y: p2.y
      }
      p4 = {
        x: p2.x + 10 + lineWidth / 2,
        y: p2.y
      }
      p5 = {
        x: p2.x,
        y: p2.y - 15
      }
    }
    this.ctxTemp.beginPath()
    this.ctxTemp.moveTo(p1.x, p1.y)
    this.ctxTemp.lineTo(p2.x, p2.y)
    this.ctxTemp.stroke()
    this.ctxTemp.beginPath()
    this.ctxTemp.moveTo(p3.x, p3.y)
    this.ctxTemp.lineTo(p4.x, p4.y)
    this.ctxTemp.lineTo(p5.x, p5.y)
    this.ctxTemp.closePath()
    this.ctxTemp.fill()
  }
  // 矩形
  rectangle () {
    this.ctxTemp.rect(
      this.opts.start.x,
      this.opts.start.y,
      this.opts.end.x - this.opts.start.x,
      this.opts.end.y - this.opts.start.y
    )
    this.ctxTemp.stroke()
  }
  // 三角形
  triangle () {
    let p1 = {
      x: (this.opts.end.x + this.opts.start.x) / 2,
      y: this.opts.start.y
    }
    let p2 = {
      x: this.opts.start.x,
      y: this.opts.end.y
    }
    let p3 = this.opts.end
    this.ctxTemp.moveTo(p1.x, p1.y)
    this.ctxTemp.lineTo(p2.x, p2.y)
    this.ctxTemp.lineTo(p3.x, p3.y)
    this.ctxTemp.closePath()
    this.ctxTemp.stroke()
  }
  // 直角三角形
  rightTriangle () {
    let p1 = this.opts.start
    let p2 = {
      x: this.opts.start.x,
      y: this.opts.end.y
    }
    let p3 = this.opts.end
    this.ctxTemp.moveTo(p1.x, p1.y)
    this.ctxTemp.lineTo(p2.x, p2.y)
    this.ctxTemp.lineTo(p3.x, p3.y)
    this.ctxTemp.closePath()
    this.ctxTemp.stroke()
  }
  // 直线
  line () {
    this.ctxTemp.moveTo(this.opts.start.x, this.opts.start.y)
    this.ctxTemp.lineTo(this.opts.end.x, this.opts.end.y)
    this.ctxTemp.stroke()
  }
  // 虚线
  dashed () {
    this.ctxTemp.save()
    this.ctxTemp.setLineDash([10, 15])
    this.ctxTemp.moveTo(this.opts.start.x, this.opts.start.y)
    this.ctxTemp.lineTo(this.opts.end.x, this.opts.end.y)
    this.ctxTemp.stroke()
    this.ctxTemp.restore()
  }
  // 圆
  circle () {
    let center = {
      x: (this.opts.end.x + this.opts.start.x) / 2,
      y: (this.opts.end.y + this.opts.start.y) / 2
    }
    let a = Math.abs((this.opts.end.x - this.opts.start.x) / 2)
    let b = Math.abs((this.opts.end.y - this.opts.start.y) / 2)
    this._circle(center, a, b)
  }
  // 平行四边形
  parallelogram () {
    let w = this.opts.end.x - this.opts.start.x
    let offset = w / 4
    let p1 = {
      x: this.opts.start.x + offset,
      y: this.opts.start.y
    }
    let p2 = {
      x: this.opts.end.x,
      y: this.opts.start.y
    }
    let p3 = {
      x: this.opts.end.x - offset,
      y: this.opts.end.y
    }
    let p4 = {
      x: this.opts.start.x,
      y: this.opts.end.y
    }
    this.ctxTemp.moveTo(p1.x, p1.y)
    this.ctxTemp.lineTo(p2.x, p2.y)
    this.ctxTemp.lineTo(p3.x, p3.y)
    this.ctxTemp.lineTo(p4.x, p4.y)
    this.ctxTemp.closePath()
    this.ctxTemp.stroke()
  }
  // 坐标系
  coordinate () {
    this._axis('x')
    this._axis('y')
  }
  // 数轴
  axis () {
    this._axis('x')
  }
  // 立方体
  cube () {
    let w = this.opts.end.x - this.opts.start.x
    let h = this.opts.end.y - this.opts.start.y
    let offsetX = w / 4
    let offsetY = h / 4

    // 顶部面的4点
    let p1 = {
      x: this.opts.start.x + offsetX,
      y: this.opts.start.y
    }
    let p2 = {
      x: this.opts.end.x,
      y: this.opts.start.y
    }
    let p3 = {
      x: this.opts.end.x - offsetX,
      y: this.opts.start.y + offsetY
    }
    let p4 = {
      x: this.opts.start.x,
      y: this.opts.start.y + offsetY
    }
    // 正面 下面的2点
    let p5 = {
      x: this.opts.start.x,
      y: this.opts.end.y
    }
    let p6 = {
      x: this.opts.end.x - offsetX,
      y: this.opts.end.y
    }
    // 背后的2点
    let p7 = {
      x: this.opts.start.x + offsetX,
      y: this.opts.end.y - offsetY
    }
    let p8 = {
      x: this.opts.end.x,
      y: this.opts.end.y - offsetY
    }
    // 画上面和正面
    this.ctxTemp.moveTo(p4.x, p4.y)
    this.ctxTemp.lineTo(p1.x, p1.y)
    this.ctxTemp.lineTo(p2.x, p2.y)
    this.ctxTemp.lineTo(p3.x, p3.y)
    this.ctxTemp.lineTo(p4.x, p4.y)
    this.ctxTemp.lineTo(p5.x, p5.y)
    this.ctxTemp.lineTo(p6.x, p6.y)
    this.ctxTemp.lineTo(p3.x, p3.y)
    // 画右面
    this.ctxTemp.moveTo(p6.x, p6.y)
    this.ctxTemp.lineTo(p8.x, p8.y)
    this.ctxTemp.lineTo(p2.x, p2.y)
    this.ctxTemp.stroke()
    // 背面的虚线
    this.ctxTemp.save()
    this.ctxTemp.setLineDash([10, 15])
    this.ctxTemp.beginPath()
    this.ctxTemp.moveTo(p1.x, p1.y)
    this.ctxTemp.lineTo(p7.x, p7.y)
    this.ctxTemp.lineTo(p5.x, p5.y)
    this.ctxTemp.moveTo(p7.x, p7.y)
    this.ctxTemp.lineTo(p8.x, p8.y)
    this.ctxTemp.stroke()
    this.ctxTemp.restore()
  }
  // 圆柱体
  cylinder () {
    let h = this.opts.end.y - this.opts.start.y
    let offsetY = h / 8
    let centerA = {
      x: (this.opts.end.x + this.opts.start.x) / 2,
      y: this.opts.start.y + offsetY
    }
    let a = Math.abs((this.opts.end.x - this.opts.start.x) / 2)
    let b = offsetY
    this._circle(centerA, a, b) // 上圆

    let centerB = {
      x: (this.opts.end.x + this.opts.start.x) / 2,
      y: this.opts.end.y - offsetY
    }
    this._circle(centerB, a, b, 'up') // 下虚半圆
    this._circle(centerB, a, b, 'down') // 下半实圆
    let p1 = {
      x: this.opts.start.x,
      y: this.opts.start.y + offsetY
    }
    let p2 = {
      x: this.opts.start.x,
      y: this.opts.end.y - offsetY
    }
    let p3 = {
      x: this.opts.end.x,
      y: this.opts.start.y + offsetY
    }
    let p4 = {
      x: this.opts.end.x,
      y: this.opts.end.y - offsetY
    }
    this.ctxTemp.beginPath()
    this.ctxTemp.moveTo(p1.x, p1.y)
    this.ctxTemp.lineTo(p2.x, p2.y)
    this.ctxTemp.moveTo(p3.x, p3.y)
    this.ctxTemp.lineTo(p4.x, p4.y)
    this.ctxTemp.stroke()
  }
  // 圆锥体
  cone () {
    let h = this.opts.end.y - this.opts.start.y
    let offsetY = h / 8
    let a = Math.abs((this.opts.end.x - this.opts.start.x) / 2)
    let b = offsetY
    let center = {
      x: (this.opts.end.x + this.opts.start.x) / 2,
      y: this.opts.end.y - offsetY
    }
    this._circle(center, a, b, 'up') // 下虚半圆
    this._circle(center, a, b, 'down') // 下半实圆
    let p1 = {
      x: (this.opts.start.x + this.opts.end.x) / 2,
      y: this.opts.start.y
    }
    let p2 = {
      x: this.opts.start.x,
      y: this.opts.end.y - offsetY
    }
    let p3 = {
      x: this.opts.end.x,
      y: this.opts.end.y - offsetY
    }
    this.ctxTemp.beginPath()
    this.ctxTemp.moveTo(p2.x, p2.y)
    this.ctxTemp.lineTo(p1.x, p1.y)
    this.ctxTemp.lineTo(p3.x, p3.y)
    this.ctxTemp.stroke()
  }
  drawShape (opts, ctx) {
    if (opts) {
      this.opts = opts
    }
    if (ctx) {
      this.ctxTemp = ctx
    } else {
      throw new Error('Parameter ctx is empty')
    }
    this.ctxTemp.save()
    this.ctxTemp.lineCap = 'round'
    this.ctxTemp.lineJoin = 'round'
    this.ctxTemp.strokeStyle = opts.color
    this.ctxTemp.fillStyle = opts.color
    this.ctxTemp.lineWidth = opts.width
    if (this.opts.angle) {
      let origin = this.getCenterPoint()
      this.ctxTemp.translate(origin.x, origin.y)
      this.ctxTemp.rotate(this.opts.angle)
      this.ctxTemp.translate(-origin.x, -origin.y)
    }
    this.ctxTemp.beginPath()
    switch (this.opts.type) {
      case 'rectangle': // 矩形
        this.rectangle()
        break
      case 'triangle': // 等腰三角形
        this.triangle()
        break
      case 'rightTriangle': // 直角三角形
        this.rightTriangle()
        break
      case 'line': // 直线
        this.line()
        break
      case 'dashed': // 虚线
        this.dashed()
        break
      case 'circle': // 圆
        this.circle()
        break
      case 'parallelogram': // 平行四边形
        this.parallelogram()
        break
      case 'coordinate': // 坐标系
        this.coordinate()
        break
      case 'axis': // 数轴
        this.axis()
        break
      case 'cube': // 立方体
        this.cube()
        break
      case 'cylinder': // 圆柱体
        this.cylinder()
        break
      case 'cone': // 圆锥体
        this.cone()
        break
    }
    this.ctxTemp.restore()
  }
}
export default OriginShape
```