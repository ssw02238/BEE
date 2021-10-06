<template>
<div>
  <div class="navbar nav">
    
    <!-- logo image --> 
    <div class="logo ms-5">
      <RouterLink :to="{ name: 'main' }">
          <img src="@/assets/logo.png" width="170">
      </RouterLink>
    </div>

    <!-- 글씨만 있는 네브 --> 
    <div class="letter-nav mt-4 d-flex justify-content-around">

      <nav class="nav main-nav">
        <RouterLink class="routerLink" :to="{ name: 'serviceIntro' }">
          <p class="nav-text">About</p>
        </RouterLink>
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

      <RouterLink @click.native="logout" to="#" class="routerLink">
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
      localStorage.removeItem('email')
      localStorage.removeItem('mbti')
      localStorage.removeItem('uid')
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

<style scoped>
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

/*00. 글씨 네브바  */
.letter-nav {
  width: 70%;
  /* margin-top: 12px */
}

/* 01. 로고 */
.logo {
  width: 15%;
  min-width:100px;
}

/* 02. 3개 메뉴 */
.main-nav {
  width: 40%;
  min-width: 250px;
  justify-content: space-between;
}

/* 03. 로그인 회원가입 */
.sub-nav {
  width: 20%;
  min-width: 100px; 
  align-content: center;
  text-align: end;
  justify-content: space-around;
}

.nav-text {
  font-size: 1.5rem;
  padding: 5px;
}

.nav-text2 {
  font-size: 1.2rem;
  padding: 5px;
}

</style>