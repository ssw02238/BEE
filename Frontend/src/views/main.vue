<template>
  <div class="main-div">
    <h1>Ranks</h1>
    <hr style="color:yellow">

    <!-- 1위 기업 정보 --> 
    <div class="accordion accordion-flush" id="accordionFlushExample">
      <div class="accordion-item">
        <h2 class="accordion-header" id="flush-headingOne">
          <button class="accordion-button collapsed" id="font" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
            ESG TOP 1 {{ esg_top }}
            <span class="ms-5" style="color:yellow"><b>Click!</b></span>
          </button>
        </h2>
        <div id="flush-collapseOne" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample">
          <div class="accordion-body" id="font" style="background-color:black;">
            <Top 
            :e1="e1"
            :e2="e2"
            :s1="s1"
            :s2="s2"
            :s3="s3"
            :g1="g1"
            :g2="g2"
            :g3="g3"
            :g4="g4"
            :g5="g5"
            />
          </div>
        </div>
      </div>
    </div>

    <hr style="color:yellow">
    <!-- 기업 순위 --> 
    <h3 class="my-4">Monthly Ranking</h3>  
    <rankTable id="font" /> 

    <hr style="color:yellow">
    <!-- 오늘의 기업 --> 
    <div class="card mb-3" style="background-color:black;">
      <div class="row g-0">
        <div class="col-md-4" style="display:flex">
          <img src="@/assets/esg_char.jpg" class="img-fluid rounded-start" alt="esg character" style="align-items:center">
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h5 class="card-title mb-4">오늘의 기업 🎉 {{ news_top }}</h5>
              <ul class="list-group card-text" id="font">
                <li class="list-group-item">뉴스 제목 1</li>
                <li class="list-group-item">뉴스 제목 1</li>
                <li class="list-group-item">뉴스 제목 1</li>
              </ul>
          </div>
        </div>
      </div>
    </div>
    <hr style="color:yellow">


    <!-- ESG 성향 --> 
    <h3 class="my-4">{{ nickname }} 님의 ESG 성향</h3>  
    <Graphmain/>
  </div>
</template>

<script>
import axios from 'axios'
import rankTable from '../components/table.vue'
import Top from '../components/Top.vue'
import Graphmain from '../components/graph_main.vue'

export default {
  name: 'main',
  components: {
    rankTable,
    Top,
    Graphmain
  },
  data:function(){
    return{
      esg_top: '',
      e1: '',
      e2: '',
      s1: '',
      s2: '',
      s3: '',

      news_top: '포스코',
      nickname: '',
    };
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    // ESG 1위 기업 출력 
    getBestCorp: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/boards/bestcorp/',
        headers: this.setToken()
      })
        .then(res => {
          console.log('1위 esg 기업 정보', res.data)
          console.log(res.data.environment_evaluation)
          this.esg_top = res.data.name
          this.e1 = res.data.environment_evaluation[0].co2
          this.e2 = res.data.environment_evaluation[0].energy
          this.s1 = res.data.social_evaluation[0].woman_ratio
          this.s2 = res.data.social_evaluation[0].average_term
          this.s3 = res.data.social_evaluation[0].term_ratio
          this.g1 = res.data.governance_evaluation[0].board_ration
          this.g2 = res.data.governance_evaluation[0].board_independency
          this.g3 = res.data.governance_evaluation[0].largest_shareholder
          this.g4 = res.data.governance_evaluation[0].salary_gap
          this.g5 = res.data.governance_evaluation[0].dividen_ratio   

        })
        .catch(err => {
          console.log('오류', err)
        })
    },
    // 오늘의 기업 출력 
    getNewsTop: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/boards/hottestcorp/',
        headers: this.setToken()
      })
        .then(res => {
          console.log('1위 뉴스 기업 정보', res)
        })
        .catch(err => {
          console.log('오류', err)
        })
    },
  },
  async mounted() {
    this.nickname = localStorage.getItem('nickname')
    this.getBestCorp()
    // this.getNewsTop()
  }
}
</script>

<style scoped>
.main-div {
  width: 75%;
  margin: auto;
}
h1, h3 {
  color:#FABD02;
}
.accordion-button {
  background-color: #1b1b1b;
  color: white;
}
.card-title {
  color:#FABD02;
}
</style>