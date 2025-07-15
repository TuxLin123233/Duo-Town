<template>
  <!--用户信息-->
  <div id="user-info">
    <img src="@/assets/img/头像测试.jpg" alt="头像">
    <span id="username">---</span>

    <!-- 标签 -->
    <div id="tags">
      <img src="@/assets/svg/me/男.svg" alt="男性">
      <span id="age">---</span>
    </div>
  </div>
</template>

<style scoped>
#user-info{
  margin-top: 44px;
  padding-left: 36px;
}

img[alt='头像']{
  width: 112px;
  height: 112px;
  border-radius: 50%;

}

#tags{
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100px;
  line-height: 32px;
}


#username{
  display: block;
  position: relative;
  margin-top: 21px;
  font-size: 26px;
  color: rgba(255, 255, 255, 1);
  margin-bottom: 26px;
  font-weight: bold;
}

img[alt='男性']{
  width: 30px;
  height: 26px;
  border-radius: 10px;
}

#age{
  width: 41px;
  height: 26px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 12px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  padding-left: 5px;
  padding-right: 5px;
}
</style>