```vue
<template>
  <div>

<!-- 반응형 네브바 --> 
<nav class="total-nav navbar navbar-expand-md navbar-light">
  <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    
    <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
        <!-- logo 자리 --> 
        <div style="width: 20%;margin-right:50px">
          <div class="logo">
            <RouterLink :to="{ name: 'main' }">
                <img src="@/assets/logo.png" width="170" class="pt-1">
            </RouterLink>
          </div>
        </div>

      <!-- 로고 제외 네브바 --> 
      <div style="width: 80%; display: contents">
      <RouterLink class="routerLink" :to="{ name: 'serviceIntro' }">
            <p class="nav-text">About</p>
          </RouterLink>
          <RouterLink class="routerLink" :to="{ name: 'infoDetail' }">
            <p class="nav-text">infoDetail</p>
          </RouterLink>
          <RouterLink class="routerLink" :to="{ name: 'welcome' }">
            <p class="nav-text">welcome</p>
          </RouterLink>
          <RouterLink class="routerLink" :to="{ name: 'esgRank' }">
            <p class="nav-text">Rank</p>
          </RouterLink>
          <RouterLink class="routerLink" :to="{ name: 'newsList' }">
            <p class="nav-text">News</p>
        </RouterLink>

      <!-- sub nav --> 
      <div class="nav sub-nav" v-if="isLogin">
          <RouterLink class="routerLink" :to="{ name: 'myPage' }">
            <p class="nav-text2">{{nickname}}</p>
          </RouterLink>

          <RouterLink @click.native="logout" to="#" class="routerLink">
            <p class="nav-text2">로그아웃</p>
          </RouterLink>
        </div>

        <div class="nav sub-nav" v-else>

          <p id="show-modal" @click="showModal = true" class="nav-text2">Log in</p>
          <modal v-if="showModal" @close="showModal = false">
            <h3 slot="header" style="color:#FABD02">Login </h3>
          </modal> 

          <p id="show-modal2" @click="showModal2 = true" class="nav-text2">Sign up</p>
          <modal2 v-if="showModal2" @close="showModal2 = false">
            <h3 slot="header" style="color:#FABD02">Sign Up </h3>
          </modal2> 
        </div>


      </div>

    </div>
  </div>
</nav>

  </div>
</template>

<script>
import Modal from "./login.vue"

import Modal2 from "./signup.vue"
export default {
  components:{
    Modal,
    Modal2
  },
  data:function(){
    return{
      isLogin: false,
      nickname: null,
      doItem:"",
      showModal:false,
      showModal2:false,
    };
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      localStorage.removeItem('nickname')
      console.log('logout 성공')

      this.$router.push({ name: 'welcome' })
    },
  },
  async mounted() {
    try {
      const token = localStorage.getItem('jwt')
      if (token) {
        this.isLogin = true
        this.nickname = localStorage.getItem('nickname')
      }
    }
    catch (err) {
      console.log(err)
    }
  }
};
</script>

<style>
.routerLink {
  text-decoration: none;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

.main-nav {
  color:#FABD02;
  width: 40%;
  justify-content: space-around;
  align-content: center;
}

.sub-nav {
  color:#FABD02;
  width: 20%;
  margin-left: 90px;
  align-content: center;
  justify-content: space-around;
}

.nav-text {
  font-size: 1.5rem;
  align-content: center;
  margin-bottom: 0px;
  padding: 5px;
}

.nav-text2 {
  font-size: 1.1rem;
  margin-bottom: 0px;
  align-content: center;
  padding: 5px;
}
.nav-content{
  display: contents;
}
.total-nav {
  background-color:black;
  display: contents;
  color: #FABD02;
}
p {  
  color:#FABD02;
  }
</style>

```







들어오자마자 welcome 페이지 보임(얜 다신 안보임) -> 

회원가입 -> 로그인   메인화면(로고)-> 

서비스소개(about)-> Rank 전체 차트(Rank) -> 

한 기업 선택 시 기업 상세 페이지로 이동(infoDetail)

-> 마이페이지