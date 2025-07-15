<template>
  <!--http://localhost:8080/pages/edit/edit.html-->
  <main>
    <!--标题-->
    <header>
      <div id="topic">标题</div>
    </header>
  </main>
</template>

<script>
import {basic_api} from "@/assets/main.js";

//登录状态验证
basic_api.is_logged();
</script>
