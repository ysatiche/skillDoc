# 笔记撤销恢复

## 数据结构

```
this.eles = [] // 当前页画布元素集合
this.historyDatas = {} // 整个课件数据存储 this.historyDatas[this.pageId] = this.eles
this.historyIndex = -1 // 当前页撤销回退坐标
```

## 画布的渲染

```
renderByData () {
  this.clear()
  if (this.historyIndex >= 0) {
    for (let i = 0; i < this.historyIndex + 1; i++) {
      let ele = this.eles[i]
      if (!ele || !ele.isFinish()) continue
      if (ele.type === 'clearCanvas') {
        let config = ele.getConfig()
        config.width = this.canv.width / this.scale
        config.height = this.canv.height / this.scale
        ele.setConfig(config)
      }
      // 渲染每一笔画笔
      ele.render(this.ctx)
    }
  }
}
```