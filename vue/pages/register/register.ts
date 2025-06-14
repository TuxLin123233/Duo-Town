import '../../src/assets/main.css'      //导入公共css

import { createApp } from 'vue'
import Register from '../../src/views/Register/Register.vue'    //导入vue文件

createApp(Register).mount('#app')   //绑定vue文件到html的ID:app中
