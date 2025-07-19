# 🏘️ Duo小镇

> 一个温暖、轻量、去中心化的中文社交平台 😄

<div style="text-align: center;">
    <img src="https://img.shields.io/badge/python-3.1+-blue.svg" alt="Python">
    <img src="https://img.shields.io/badge/django-5.2+-green.svg" alt="Django">
    <img src="https://img.shields.io/badge/vue-3.x-brightgreen.svg" alt="Vue3">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
</div>

---
## 📌 项目简介

Duo小镇是一个开源的中文社交网站，致力于为用户提供一个
**无广告、无算法操控**
的纯净交流空间。你可以在这里：

- 🏡 创建属于自己的小镇（社区）
- 👋 与邻居（用户）进行兴趣社交
- 📜 发布动态、文章等内容

> **愿景**：让每座Duo小镇成为互联网中的一片“自留地”

---

## 🔧 快速开始

### 环境要求

- Python 3.1+
- Node.js 18+

### 本地启动

```shell
# 克隆项目
git clone https://gitee.com/duo-studio/duo-town.git
cd duo-town

# 后端启动
cd Django
python -m venv venv
souce venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# 前端启动
cd Vue
npm install
npm run dev 
```

访问 http://localhost:8000 即可体验！

---

## 🤝 参与贡献
1. Fork 本仓库 
2. 新建分支：git checkout -b feature
3. 提交代码：git commit -m 'Add AmazingFeature'
4. 发起 __Pull Request__
5. 等待 Review & Merge 🎉

### 🔓 开源许可证
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🛣️ 路线图
- [ ] 网站基础功能
- [ ] 网站部署

---

## ❤️ 鸣谢
首先感谢 __Duo小镇核心团队__

| 角色       | 成员                                                  |
|----------|-----------------------------------------------------|
| 前端       | [@q-year](https://gitee.com/q-year)                 |
| 前端       | [@cheng-jingchun](https://gitee.com/cheng-jingchun) |
| 前端 & 后端  | [@xxg-yyds](https://gitee.com/xxg-yyds)             |
| 前端 & 后端  | [@linsifan123](https://gitee.com/linsifan123)       |

### 🌱 开源伙伴
- [Django](https://www.djangoproject.com/) 社区
- [Vue](https://vuejs.org/) 团队
---

## 📞 联系我们
- 📮 邮件：[3867085448@qq.com]()
- 📰 公众号：duo_town

> 支持我们！ 你的关注是推动Duo小镇前进的动力。