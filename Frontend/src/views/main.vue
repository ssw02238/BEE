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
            <span class="ms-5"><b>▷ 확인하기</b></span>
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
    <rankTable id="font" :paginated="paginated" :page="page"/> 

    <hr style="color:yellow">
    <div class="todaytest mt-4" style="display:flex; justify-content: space-between;">

    <!-- 오늘의 기업 --> 
    <div class="todaycorp" style="display:flex; align-items:center">
      <div style="width: 30%">
        <h4 class="card-title mt-4 mb-4">오늘의 기업 <br> {{ news_top }}</h4>
        <p id="font">*오늘의 기업이란,<br> 하루 ESG 기사 언급량<br> 1위 기업을 의미합니다.</p>
      </div>
      <div style="width: 70%">
        <ul class="list-group card-text" id="font">
          <li class="list-group-item">ESG 경영 더는 두고볼 수 없다구여ㅛ!!!!!!!!!!!!</li>
          <li class="list-group-item">사회에 공헌하는 기업 포 스 코!!!!포스코!!!!!!!!!!!1</li>
          <li class="list-group-item">믓진 기업 포 스 코 ...포 스 코 ...포 스 코 ...</li>
        </ul>
        <button class="btn btn-lg btn-block mt-2" style="width:80%; background-color:#FABD01">회사 정보 확인</button>
      </div>
    </div>

  <!-- ESG 성향 --> 
    <div v-if="nickname" style="width: 50%; min-width:200px;">
      <h4>{{ nickname }} 님의 ESG 성향</h4>  
      <Graphmain/>
    </div>

    <div class="mbti" v-else style="width: 50%;">
      <RouterLink class="routerLink" :to="{ name: 'test' }">
          <button class="btn btn-lg btn-block" 
          style="width:100%; background-color:#FABD01;">
            ESG mbti 확인하기
          </button>
      </RouterLink>
    </div>

  </div>

    <hr style="color:yellow">

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
      g1:'',
      g2: '',
      g3:'',
      g4:'',
      g5:'',
      // 전체 순위
      paginated: '',
      page: 1,
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
        url: 'http://127.0.0.1:8000/boards/bestcorp/',
        headers: this.setToken()
      })
        .then(res => {
          console.log('1위 esg 기업 정보', res.data)
          this.esg_top = res.data.name
          this.e1 = res.data.environment_evaluation[0].co2
          this.e2 = res.data.environment_evaluation[0].energy
          this.s1 = res.data.social_evaluation[0].woman_ratio
          this.s2 = res.data.social_evaluation[0].average_term
          this.s3 = res.data.social_evaluation[0].term_ratio
          this.g1 = res.data.governance_evaluation[0].board_ratio
          if (res.data.governance_evaluation[0].board_independency == true) {
            this.g2 = '일치'
          }
          else{
            this.g2 = '불일치'
          }
          this.g3 = res.data.governance_evaluation[0].largest_shareholder
          this.g4 = res.data.governance_evaluation[0].salary_gap
          this.g5 = res.data.governance_evaluation[0].dividen_ratio   

        })
        .catch(err => {
          console.log('오류', err)
        })
    },
    // ESG 전체 순위 리스트 조회 
    getESGRank() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/boards/esg-ranking/',
        headers: this.setToken()
      })
        .then(res => {
          // console.log('전체 순위 리스트', res)
          this.paginated = res.data.corp_data.slice(0, 5)
          console.log(this.paginated)
        })
        .catch(err => {
          console.log('전체 순위 오류', err)
        })
    },
    // 오늘의 기업 출력 
    getNewsTop: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/boards/hottestcorp/',
        headers: this.setToken()
      })
        .then(res => {
          console.log('1위 뉴스 기업 정보', res)
        })
        .catch(err => {
          console.log('1위 뉴스 기업 오류', err)
        })
    },
    
  },
  async mounted() {
    this.nickname = localStorage.getItem('nickname')
    this.getBestCorp()
    this.getNewsTop()
    this.getESGRank()
  }
}
</script>

<style scoped>
.main-div {
  width: 75%;
  margin: auto;
}
h1, h3, h4, .mbti {
  color:#FABD02;
}
.accordion-button {
  background-color: #1b1b1b;
  color: white;
}

.list-group-item {
  background-color: black;
  color:white;
  text-decoration: underline; 
  text-underline-position:under;
}
.todaycorp {
  background-color:black;
  border: 1px solid rgb(224, 222, 222);
  text-align:center;
  padding: 10px;
  width:45%;
  min-width:200px;
}
</style>