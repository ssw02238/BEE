<template>
  <div class="main-div">
    <h3>ESG Top 1</h3>
    <hr style="color:yellow">

    <!-- 1위 기업 정보 --> 
    <div class="accordion accordion-flush" id="accordionFlushExample">
      <div class="accordion-item">
        <h2 class="accordion-header" id="flush-headingOne">
          <button class="accordion-button collapsed" id="font" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
            {{ esg_top }}
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
    <div class="d-flex justify-content-between">
      <h3 class="my-4">ESG Ranks</h3>
      <RouterLink :to="{ name: 'esgRank' }" class="routerLink">
        <div type=button class="mt-4 pt-2 px-2" style="color:#FABD02;">더보기</div>
      </RouterLink>
    </div>
    <rankTable id="font" :paginated="paginated" :page="page"/> 

    <hr style="color:yellow">
    <!-- 오늘의 기업 --> 
    <!-- <h3 class="my-4">오늘의 기업</h3>
    <p id="font" style="color:#FABD02;">*오늘의 기업이란, 하루 ESG 기사 언급량 1위 기업을 의미합니다.</p> -->

    <div class="todaytest mt-4" style="display:flex; justify-content: space-between;">

    <div class="todaycorp" style="display:flex; align-items:center">
      
      <div style="width: 30%">
        <h4 class="card-title mt-3 mb-3">오늘의 기업</h4>
        <h4 class="mb-4">{{ todayCorp }}</h4>
        <p id="font" style="color:#FABD02">*오늘의 기업이란,<br> 하루 ESG 기사 언급량<br> 1위 기업을 의미합니다.</p>
      </div>
      <div style="width: 70%">
        <ul class="list-group card-text" id="font">
          <div v-for="(news, idx) in todayCorpNews" :key="idx">
            <li class="list-group-item">
              <div @click="goPage(news.url)" class="news-link">{{ news.title }}</div>
            </li>
          </div>
        </ul>
        <button class="btn btn-lg btn-block mt-2 detail-btn" 
        style="width:95%;"
        @click="goDetail(todayCorpPk)">회사 정보 확인</button>
      </div>
    </div>

  <!-- ESG 성향 --> 
    <div v-if="mbti" style="width: 50%; min-width:200px;">
      <h4>{{ nickname }} 님의 ESG 성향</h4>  
      <Graphmain/>
    </div>

    <div class="mbti d-flex flex-column justify-content-center" v-else style="width: 50%;">
      <RouterLink class="routerLink" :to="{ name: 'test' }">
        <div>
          <button class="btn btn-lg btn-block" 
          style="width:100%; background-color:#FABD01;">
            ESG mbti 확인하기
          </button>
        </div>
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
      todayCorp: '포스코', // 오늘의 기업
      todayCorpPk: '',
      todayCorpNews: [], // 오늘의 기업 뉴스
      nickname: '',
      mbti: '',
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
    goPage(url){
      window.open(url, "_blank")
    },
    // ESG 1위 기업 출력 
    getBestCorp: function () {
      axios.get('boards/bestcorp/', {headers:this.setToken()})
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
      axios.get('boards/esg-ranking/', {headers:this.setToken()})
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
      axios.get('boards/hottestcorp/', {headers:this.setToken()})
        .then(res => {
          console.log('오늘의 기업 정보', res)
          console.log(res.data)
          this.todayCorp = res.data.name
          this.todayCorpPk = res.data.pk
          this.todayCorpNews = res.data.news.slice(0, 3)
        })
        .catch(err => {
          console.log('오늘의 기업 오류', err)
        })
    },
    goDetail(pk) {
       console.log('여기 pk', pk)
      this.$router.push({ name: 'infoDetail',  params: {pk: pk }})
      },  
    goRank: function() {

    }
    
  },
  async mounted() {
    this.nickname = localStorage.getItem('nickname')
    this.mbti = localStorage.getItem('mbti')
    this.getBestCorp()
    this.getNewsTop()
    this.getESGRank()
  }
}
</script>

<style scoped>
.routerLink {
  font-size: 19px;
  text-decoration: none;
}
.routerLink:hover {
  text-decoration: underline;
  text-decoration-color: #FABD02;
  text-underline-position: under;
}
.detail-btn {
  background-color:#FABD02;
}
.detail-btn:hover {
  background-color: rgba(250,189,2, 0.8);
}
.news-link {
  color: white;
  white-space: normal;
  overflow: hidden;
  text-align: left;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  text-decoration: none;
}
.news-link:hover {
  text-decoration: underline;
  text-underline-position:under;
  cursor: pointer;
}
.main-div {
  width: 75%;
  margin: auto;
  margin-bottom: 100px;
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