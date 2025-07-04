<template>
  <main>
    <p>HelloWorld</p>
  </main>
</template>、

<script>
import {api} from "@/assets/main.js";
window.location.href = "http://localhost:8080/pages/game_2048/game_2048.html";
//登录状态验证
api.is_logged();
</script>