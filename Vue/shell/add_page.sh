# 自动化添加组件+页面程序

# 输入添加页面名
read -r -p "请输入要添加的组件名: " name
first_char_uppercase="${name^}"

# 创建Page的子文件夹
cd ../pages/ || exit
mkdir "$name"

# 进入子文件夹
cd "$name" || exit
# 编写HTML文件
cat > "$name.html" << EOF
<!doctype html>
<html lang="zh-Hans">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>demo</title>
</head>
<body>
<div id="app"></div>
<script type="module" src="$name.js"></script>
</body>
</html>
EOF
# 编写连接的JS文件
cat > "$name.js" << EOF
import "../../src/assets/main.css"

import {createApp} from "vue";
import Login from "../../src/views/$first_char_uppercase/$first_char_uppercase.vue"

createApp(Login).mount("#app")
EOF

# 编写vue文件
mkdir "../../src/views/$first_char_uppercase/"
cat > "../../src/views/$first_char_uppercase/$first_char_uppercase.vue" << EOF
<template>
  <main></main>
</template>、

<script>
import {api} from "@/assets/main.js";

//登录状态验证
api.is_logged();
</script>
EOF

echo "已添加($name)组件"