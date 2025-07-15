<template>
  <header>
    <img src="../../../assets/svg/me/侧边栏.svg" alt="侧边栏" @click="toggleEdit">
    <AnimatePresence>
      <motion.div
          id="edit"
          v-if="is_show"
          :initial="{transform: 'translateX(250px)',opacity: 0}"
          :animate="{transform: 'translateX(0px)', opacity: 1}"
          :exit="{transform: 'translateX(250px)', opacity: 0}"
      >
        <span>🪪 个人资料</span>
        <span>⚙️ 通用</span>
        <span>🤣 我的好友</span>
        <span>📖 我的帖子</span>
        <span>🤙 联系官方</span>
        <span>❤️ 给我们赞助一杯可乐</span>
      </motion.div>
    </AnimatePresence>
  </header>
</template>

<style scoped>
header{
  display: flex;
  justify-content: end;
  padding-right: 36px;
  margin-top: 35px;
}

img[alt="侧边栏"]{
  width: 36px;
  height: 36px;
}

#edit{
  width: 250px;
  height: auto;
  position: absolute;
  right: 0;
  top: 90px;
  border-radius: 20px 0 0 20px;
  background-color: #ededed;
  font-size: 18px;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 0 5px #b2b2b2;
}

#edit span{
  width: 100%;
  margin-left: 20px;
  height: 50px;
  line-height: 50px;
}
</style>

<script setup>
import {AnimatePresence, motion} from "motion-v";
import {ref} from "vue";

//侧边栏默认状态
let is_show = ref(false);
//http://127.0.0.1:8000 可以打开吗？OK

//控制is_show的值
const toggleEdit = () => {
  is_show.value = !is_show.value;
};

</script>