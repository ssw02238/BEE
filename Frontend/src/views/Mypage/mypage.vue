<template>
  <div class="container">
    <div class="mb-5">
      <Profile />
    </div>
    <div class="mypage row">
      <scrapList
      :corporates="corporates"
      />
      <recommendList
      :corporates="recommend"
      />
        <!-- ESG Chart 시작 -->
          <!-- <div class="card" style="width: 30%;margin: auto" > -->
            <!-- <div class="card-body"> -->
              <div style="display:flex;width:33%;">
              <!-- <h5 class="card-title"> ESG 성향 </h5> -->

                  <Graph
                  :e_score="e_score"
                  :s_score="s_score"
                  :g_score="g_score"
                  />
            <!-- </div> -->
          <!-- </div> -->
          <!-- ESG Chart 종료 -->
    </div>
  </div>

    <RouterLink class="routerLink" :to="{ name: 'test' }">
      <p>ESG Mbti</p>
    </RouterLink>

  </div>
</template>

<script>
import Profile from '../../components/Profile.vue';
import Graph from '../../components/graph_mypage.vue';
import scrapList from '../../components/scrap_list.vue';
import recommendList from '../../components/recommend_list.vue';

import axios from 'axios';

export default {
  name: 'mypage',
  components: {
    Profile,Graph, scrapList, recommendList,
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
        this.recommend = res.data.corporates
        console.log(this.recommend)
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