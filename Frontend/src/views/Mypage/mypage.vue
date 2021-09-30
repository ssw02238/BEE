<template>
  <div class="container">
    <div class="mb-5">
      <Profile />
    </div>
  <div class="mypage row">
        <!-- 테이블 시작 -->
        <table class="table" style="width: 20%;margin: auto">
          <thead>
            <tr>
              <th scope="col">No</th>
              <th scope="col">스크랩 기업</th>

            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">1</th>
              <td> 삼성전자 </td>
            </tr>
            <tr>
              <th scope="row">2</th>
              <td> 올리브영 </td>
            </tr>
            <tr>
              <th scope="row">3</th>
              <td> 삼성 디스플레이 </td>
            </tr>
            <tr>
              <th scope="row">4</th>
              <td> 삼성전자 </td>
            </tr>
          </tbody>
        </table>
      <!-- 테이블 종료 -->

      <!-- 추천 기업 --> 
      <table class="table" style="width: 20%;margin: auto">
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
            <tr>
              <th scope="row">4</th>
              <td> 녹십자 </td>
            </tr>
          </tbody>
        </table>
  
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
import axios from 'axios'
import Profile from '../../components/Profile.vue';
import Graph from '../../components/graph_mypage.vue';

export default {
  name: 'mypage',
  components: {
    Profile,Graph
  },
  data(){
    return{
      e_score: '',
      s_score: '',
      g_score: '',
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
      get_esg() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/profile_esg/`,
        headers: this.setToken()
      })
        .then(res => {
          this.e_score = res.data.e_score
          this.s_score = res.data.s_score
          this.g_score = res.data.g_score
          console.log('디테일 정보', res.data)
          
          })
        .catch(err => {
          console.log('정보 가져오기 오류', err)
        })
  }}
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