# 用于Edge浏览器的PDF文档补丁

Language: [English](README.md)

---

解决打开在Edge中打开PDF时无法跳转至上次阅读位置的问题。

## 概述

根据[Pick up where you left off on Microsoft Edge PDF Reader][pick-up-where-you-left-off]一文，从Edge 95版本发布时起，Edge就新增了一个功能，能够让你再次打开PDF文档时自动跳转到上次浏览位置。当你在Edge中重新打开PDF文档时，浏览器会恢复为你上次阅读PDF时的页面位置、缩放比例和滚动位置。

但是，此功能对有部分PDF文档却无效。本项目将告诉你原因及解决方法。

## 原理

在Edge浏览器启用了PDF视图设置的情况下，Edge浏览器会在本地保存用户阅读PDF时的状态信息，包括页面位置、缩放比例和滚动位置，每次阅读PDF时，浏览器会记录当前状态并存储在本地，重新打开时读取这些信息并恢复。

而那些无法恢复上次浏览状态的PDF中往往都定义了一个OpenAction属性，这个属性用于定义PDF文档打开时的默认行为，如跳转到特定页面或执行JavaScript脚本。

如果PDF文档定义了OpenAction属性，该属性就会覆盖Edge浏览器默认的阅读状态恢复功能，比如OpenAction定义为跳转到第一页，那么用户每次用Edge打开PDF时就会跳转到第一页，而不是上次阅读的位置。

所以，只需要修改一下PDF文档，将无法自动跳转的PDF文档中的OpenAction属性删除，这个问题就能迎刃而解。

## 使用方法

本项目提供了Python和JavaScript两种实现：

Python实现需要在本地搭建Python环境运行，适合批量处理PDF的场景，详见python目录下的[README][python-readme-zh]文档。

JavaScript实现是一个单独的HTML文件，用浏览器打开就能直接使用，只需将javascript目录下的HTML文件托管到服务器上即可部署。

JavaScript实现的一个在线示例：[https://patchpdf.netlify.app][javascript-online-demo]

[pick-up-where-you-left-off]: https://techcommunity.microsoft.com/discussions/edgeinsiderannouncements/pick-up-where-you-left-off-on-microsoft-edge-pdf-reader/2771351

[python-readme-zh]: python/README.zh_CN.md

[javascript-online-demo]: https://patchpdf.netlify.app