<template>
  <div class="container">
    <div >
      <Profile />
    </div>
    <RouterLink class="routerLink text-decoration-none" :to="{ name: 'test' }">
      <div class="d-flex justify-content-center mb-5" >
        <button class="btn btn-lg" 
        style="width:20%; background-color:#FABD01;">
          ESG mbti TEST
        </button>
      </div>
    </RouterLink>
    
    <div class="mypage d-flex justify-content-center mb-5">
      <scrapList
      :corporates="corporates"
      />
      <recommendList
      :corporates="recommend"
      />
  </div>
  </div>
</template>

<script>
import Profile from '../../components/Profile.vue';
import scrapList from '../../components/scrap_list.vue';
import recommendList from '../../components/recommend_list.vue';

import axios from 'axios';

export default {
  name: 'mypage',
  components: {
    Profile, scrapList, recommendList,
  },
  data: function () {
    return {
      corporates: [],
      recommend: [],
      mbti: [],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getScrap: function () {
      axios.get('accounts/profile/', {headers:this.setToken()})
      .then(res => {
        this.corporates = res.data.corporates
        console.log(this.corporates)
        if (this.corporates.length > 4) {
          this.corporates.slice(this.corporates.length-5 , this.corporates.length-1)
        }
      })
      .catch(err => {
        console.log(err)
      })
    },
    getRecommend: function () {
      axios.get('accounts/profile_esg/', {headers:this.setToken()})
      .then(res => {
        this.recommend = res.data.recommend
        console.log(this.recommend)
        console.log(res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
  },
  created: function () {
    this.getScrap()
    this.getRecommend()
  }
}
</script>

<style scoped>
th,td{
    text-align: center;
}
.mypage {
  display:flex;
  justify-content: space-around;
}
.table {
  color:white;
  background-color:black;
}
</style>