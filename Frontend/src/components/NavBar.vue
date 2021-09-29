<template>
<div>
  <div class="navbar nav">
    
    <!-- logo image --> 
    <div class="logo ms-5">
      <RouterLink :to="{ name: 'main' }">
          <img src="@/assets/logo.png" width="170" class="pt-2">
      </RouterLink>
    </div>

    <!-- 글씨만 있는 네브 --> 
    <div class="letter-nav">

      <nav class="nav main-nav">
        <RouterLink class="routerLink" :to="{ name: 'serviceIntro' }">
          <p class="nav-text">About</p>
        </RouterLink>
        <!-- <RouterLink class="routerLink" :to="{ name: 'infoDetail' }">
          <p class="nav-text">infoDetail</p>
        </RouterLink> -->
        <!-- <RouterLink class="routerLink" :to="{ name: 'welcome' }">
          <p class="nav-text">welcome</p>
        </RouterLink> -->
        <RouterLink class="routerLink" :to="{ name: 'esgRank' }">
          <p class="nav-text">Rank</p>
        </RouterLink>
        <RouterLink class="routerLink" :to="{ name: 'newsList' }">
          <p class="nav-text">News</p>
        </RouterLink>
      </nav>
    

      <nav class="nav sub-nav" v-if="isLogin">
        <RouterLink class="routerLink" :to="{ name: 'myPage' }">
          <p class="nav-text2">{{nickname}}</p>
        </RouterLink>

        <RouterLink @click.native="logout" class="routerLink">
          <p class="nav-text2">로그아웃</p>
        </RouterLink>
      </nav>

      <nav class="nav sub-nav" v-else>
        <p id="show-modal" @click="showModal = true" class="nav-text2">Log in</p>
        <modal v-if="showModal" @close="showModal = false">
          <h3 slot="header">Login </h3>
        </modal> 
        <p id="show-modal2" @click="showModal2 = true" class="nav-text2">Sign up</p>
        <modal2 v-if="showModal2" @close="showModal2 = false">
          <h3 slot="header">Sign Up </h3>
        </modal2> 
      </nav>
  </div>

  <!-- 전체 네브바 닫기--> 
  </div>
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
p {
  color:#FABD02;
}
.logo {
  width: 20%;
  min-width: 15%
}
.nav {
  width: 95%;
  display: contents;
  margin-left: 10px;
}
.letter-nav {
  margin: auto;
  display:contents;
}

.main-nav {
  width: 40%;
  min-width: 200px;
  justify-content: space-around;
}

.sub-nav {
  width: 15%;
  align-content: center;
  text-align: end;
  justify-content: space-around;
  min-width: 80px;
}

.nav-text {
  font-size: 1.5rem;
  margin-bottom: 0px;
  padding: 5px;
}

.nav-text2 {
  font-size: 1.2rem;
  margin-bottom: 0px;
  padding: 5px;
}

</style>