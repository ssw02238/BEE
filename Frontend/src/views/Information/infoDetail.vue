<template>
  <div class="container">
    <h1 class="corporate-name">{{ corporate.name }} </h1>
    <div class="scrap-score">
      <div class="ps-2">Total: {{ corporate.ESG_rating.toFixed(0) }} / 300</div>
      <div class="scrap-button">
        ❤스❤크❤랩❤
      </div>
    </div>
    <!-- ESG evalutaion --> 

    <div class="card">
      <div class="row g-0">

        <div class="col-md-4">
          <Graph
          :E_rating="E_rating"
          :S_rating="S_rating"
          :G_rating="G_rating"/>
        </div>

        <div class="col-md-8">
          <div class="card-body">
            <h5 class="card-title">E: {{ corporate.E_rating.toFixed(2) }} / S: {{ corporate.S_rating.toFixed(2) }} / G: {{ corporate.G_rating.toFixed(2) }}</h5> 
            <hr style="color:gold; height:5px;">
            <div>
              <Top class="Top"
              :e1="e1"
              :e2="e2"
              :s1="s1"
              :s2="s2"
              :s3="s3"
              :g1="g1"
              :g2="g2"
              :g3="g3"
              :g4="g4"
              :g5="g5"/>
            </div>
          </div>
        </div>
      </div>
    </div>
    <hr style="color:gold; height:8px;">

    <!-- 뉴스 목록 --> 
    <h2 class="corporate-name">News</h2>
    <p class="ps-2">클릭 후 해당 뉴스를 확인해보세요</p>
    <table class="table table-dark table-hover">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Title</th>
          <th scope="col">Date</th>
        </tr>
      </thead>
      <tbody>
        <tr id="font">
          <th scope="row">1</th>
          <td>삼성전자... 에너지 배출량 개선 결과 발표</td>
          <td>2021-08-14</td>
        </tr>
      </tbody>
    </table>
    <hr style="color:gold; height:8px;">

    <!-- 유사기업 보여주기 --> 
    <h2 class="corporate-name">Recommendations</h2>
    
    <div class="d-flex justify-content-around">
    <div v-for="corporate in recommends" :key="corporate.pk" @click="goDetail(corporate.pk)">
      <div class="recomd card" >

        <div class="card-body" style="width: 250px; height: 140px;">       
          <div class="d-flex justify-content-between">
            <h5 class="mb-1">{{ corporate.name }} </h5>
            <small>스크랩 담기 ▲</small>
          </div>
          <p class="card-text mt-4" style="color:black;">E: {{ corporate.E_rating.toFixed(2)}} S:{{ corporate.S_rating.toFixed(2) }} G:{{ corporate.G_rating.toFixed(2) }}</p>
        </div>

      </div>
    </div>
  </div>
        
  </div>
</template>

<script>
import axios from 'axios'
import Top from '../../components/Top.vue'
import Graph from '../../components/graph_infodetail.vue' 
// import Scrap from '../../components/scrap_infodetail.vue' 
export default {
  name: 'infoDetail',
  components: {
    Graph,
    Top,
    // Scrap,
  },  
  data() {
    return {
      pk: '',
      corporate: [],
      E_rating: '',
      S_rating: '',
      G_rating: '',
      recommends:[],

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
    getDetail(pk) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/corporates/${pk}/detail/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log('디테일 정보', res.data)
          this.corporate = res.data
          this.E_rating = this.corporate.E_rating
          this.S_rating = this.corporate.S_rating
          this.G_rating = this.corporate.G_rating
          this.e1 = this.corporate.environment_evaluation[0].co2
          this.e2 = this.corporate.environment_evaluation[0].energy
          this.s1 = this.corporate.social_evaluation[0].woman_ratio
          this.s2 = this.corporate.social_evaluation[0].average_term
          this.s3 = this.corporate.social_evaluation[0].term_ratio
          this.g1 = this.corporate.governance_evaluation[0].board_ratio
          if (this.corporate.governance_evaluation[0].board_independency == true) {
            this.g2 = '일치'
          }
          else{
            this.g2 = '불일치'
          }
          this.g3 = this.corporate.governance_evaluation[0].largest_shareholder
          this.g4 = this.corporate.governance_evaluation[0].salary_gap
          this.g5 = this.corporate.governance_evaluation[0].dividen_ratio
        })
        .catch(err => {
          console.log('정보 가져오기 오류', err)
        })
    },
    getRecom(pk) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/corporates/${pk}/similarcorp/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log('추천 기업 정보', res.data.corporates)
          this.recommends = res.data.corporates
        })
        .catch(err => {
          console.log('추천 기업 정보 가져오기 오류', err)
        })
    }
  },
  async mounted() {
    this.pk = this.$route.params.pk
    console.log('pk번호 받아왔니?',this.pk)
    this.getDetail(this.pk)
    this.getRecom(this.pk)
  }
}
</script>

<style scoped>
.corporate-name {
  color: #FABD02;
  background-color:rgb(0, 0, 0);
  padding: 8px;
}
#chart {
  margin-top: 30px;
}
.card-title {
  color:#FABD02;
  text-align: center;
}
.card {
  background-color:black;
}
.recomd {
  margin-bottom: 50px;
  display:flex;
  justify-content: space-around;
  background-color:white;
}

.scrap-score {
  color:#e6cb7c;
  display: flex;
  justify-content: space-between;
  font-size: 1.3rem;
  background-color:black;
}

</style>