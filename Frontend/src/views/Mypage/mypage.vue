<template>
  <div class="container">
    <div class="mb-5">
      <Profile />
    </div>


      <RouterLink class="routerLink" :to="{ name: 'test' }">
        <div>
          <button class="btn btn-lg btn-block" 
          style="width:100%; background-color:#FABD01;">
            ESG mbti 확인하기
          </button>
        </div>
      </RouterLink>
    
  <div class="mypage row">
    <scrapList
    :corporates="corporates"
    />
        <!-- 테이블 시작 -->
        <!-- <table class="table" style="width: 20%;margin: auto">
          <thead>
            <tr>
              <th scope="col">No</th>
              <th scope="col">스크랩 기업</th>
            </tr>
          </thead>
          <tbody>

            <tr v-for="(corporate, idx) in corporates" :key="idx">
              <th scope="row">1</th>
              <td> {{ corporate.name }} </td>
            </tr>
            <tr>
              <th scope="row">2</th>
              <td> {{ corporate.name }} </td>
            </tr>
            <tr v-if="coporates.length > 3">
              <th scope="row">3</th>
              <td> {{ corporate.name }} </td>
            </tr>
            <tr v-if="corporates.length > 4">
              <th scope="row">4</th>
              <td> {{ corporate.name }} </td>
            </tr>
          </tbody>
        </table> -->
      <!-- 테이블 종료 -->

      <!-- 추천 기업 --> 
      <table class="table" style="width: 25%; margin-right: 20%;">
          <thead>
            <tr>
              <th scope="col">No</th>
              <th scope="col">추천 기업</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">1</th>
              <td> 삼성전자 </td>
            </tr>
            <tr>
              <th scope="row">2</th>
              <td> LG 디스플레이 </td>
            </tr>
            <tr>
              <th scope="row">3</th>
              <td> CJ ENM </td>
            </tr>
            <!-- <tr>
              <th scope="row">4</th>
              <td> 녹십자 </td>
            </tr> -->
          </tbody>
        </table>
  
      <!-- ESG Chart 시작 -->
        <!-- <div class="card" style="width: 30%;margin: auto" > -->
          <!-- <div class="card-body"> -->

  </div>

    <RouterLink class="routerLink" :to="{ name: 'test' }">
      <p>ESG Mbti</p>
    </RouterLink>

  </div>
</template>

<script>
import Profile from '../../components/Profile.vue';
// import Graph from '../../components/graph_mypage.vue';
import scrapList from '../../components/scrap_list.vue';
import axios from 'axios';

export default {
  name: 'mypage',
  components: {
    Profile,scrapList,
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
      console.log(1)
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/profile/',
        headers: this.setToken()
      })
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
  },
  created: function () {
    this.getScrap()
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