<template>
  <div class="container">
    <h1 class="corporate-name" style="display:inline">{{ corporate.name }}</h1>
    <!-- scrap list에 따른 분기 처리 진행할 것... -->
    <b-icon icon="star-fill" variant="warning" font-scale="2" class="scrap-btn" @click="addScrap" type="button" v-if="is_scrap"></b-icon>
    <b-icon icon="star" variant="warning" font-scale="2" class="scrap-btn" @click="addScrap" type="button" v-else></b-icon>
    <div class="scrap-score">
      <div class="ps-2">총점 {{ corporate.ESG_rating }} / 300</div>
    </div>
    <!-- ESG evalutaion --> 

    <div class="card">
      <div class="row g-0">
        <div class="col-md-4">
          <Graph
          />
        </div>

        <div class="col-md-8">
          <div class="card-body">
            <h5 class="card-title">E: {{ E_rating }} · S: {{ S_rating }} · G: {{ G_rating }}</h5> 
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
    <p style="color:#FABD02" v-if="newsList.length > 0" class="ps-2">클릭 후 해당 뉴스를 확인해보세요</p>
    
    <table v-if="newsList.length > 0" class="table table-dark table-hover">
      <thead>
        <tr>
          <th scope="col">No</th>
          <th scope="col">Title</th>
          <th scope="col">Date</th>
        </tr>
      </thead>
      <tbody id="font" v-for="(news, idx) in newsList" :key="idx" class="news-body" @click="goPage(news.url)">
          <th scope="row"><span class="table-text">{{ idx + 1 }}</span></th>
          <td><span class="news-link">{{ news.title }}</span></td>
          <td><span class="table-text">{{ news.date }}</span></td>
      </tbody>
    </table>
    <p v-else class="ps-2 text-center no-news">{{ corporate.name }}의 ESG 관련 뉴스가 없습니다. </p>
    <hr style="color:gold; height:8px;">

    <!-- 유사기업 보여주기 --> 
    <h2 class="corporate-name">유사 기업</h2>
    
    <div class="d-flex justify-content-around">
    <div v-for="corporate in recommends" :key="corporate.pk">
      <div class="dh card" >

        <div class="card-body" style="width: 250px; height: 140px;" @click="goDetail(corporate.pk)">       
          <div class="d-flex justify-content-between">
            <h5 class="mb-1">{{ corporate.name }} </h5>
            <!-- <small>스크랩 담기 ▲</small> -->
          </div>
          <!-- <p class="card-text mt-4">E: {{ corporate.E_rating.toFixed(2)}} S:{{ corporate.S_rating.toFixed(2) }} G:{{ corporate.G_rating.toFixed(2) }}</p> -->
          <p class="card-text mt-4">총점: {{ corporate.ESG_rating }}</p>

        </div>

      </div>
    </div>
  </div>
  <!-- <div class="dh"></div> -->
  </div>
</template>

<script>
import axios from 'axios'

import Top from '../../components/Top.vue'
import Graph from '../../components/graph_infodetail.vue' 
// import { mdiBookmarkOutline } from '@mdi/js';

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
      newsList: [],
      is_scrap: false,
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
    goDetail(pk) {
      this.$router.push({ name: 'infoDetail',  params: {pk: pk }})
    },  
    goPage(url){
      window.open(url, "_blank")
    },
    addScrap: function () {
      const config = this.setToken()
      axios.post(`corporates/${this.pk}/scrap/`,{}, {headers: config})
        .then(res => {
          // console.log(res)
          if (res.status == 201) {
            this.is_scrap = true
            // console.log(this.is_scrap)
          } else {
            this.is_scrap = false
            // console.log(this.is_scrap)
          }
        })
        .catch((error) => {
          // Error 😨
          if (error.response) {
            if (error.response.status === 404) {
              alert("존재하지 않는 기업입니다.")
            }
          } else if (error.request) {
            console.log(error.request);
          } else {
            console.log('Error', error.message);
          }
          console.log(error.config);
        });
    },
    getDetail(pk) {
      axios.get(`corporates/${pk}/detail/`, {headers:this.setToken()})
      
        .then(res => {
          const uid = parseInt(localStorage.getItem('uid'))
          if (res.data.scrap_user.includes(uid)) {
            this.is_scrap = true
          } else {
            this.is_scrap = false
          }
          this.corporate = res.data
          this.E_rating = this.corporate.E_rating
          this.S_rating = this.corporate.S_rating
          this.G_rating = this.corporate.G_rating
          
          if (this.corporate.environment_evaluation[0].co2 == 0) {
            this.e1 = '-'
          }
          else {
            this.e1 = this.corporate.environment_evaluation[0].co2
          }

          if (this.corporate.environment_evaluation[0].co2 == 0) {
            this.e2 = '-'
          }
          else {
            this.e2 = this.corporate.environment_evaluation[0].energy
          }
          // s score
          if (this.corporate.environment_evaluation[0].co2 == 0) {
            this.s1 = '-'
          }
          else {
            this.s1 = this.corporate.social_evaluation[0].woman_ratio
          }

          if (this.corporate.environment_evaluation[0].co2 == 0) {
            this.s2 = '-'
          }
          else {
            this.s2 = this.corporate.social_evaluation[0].average_term
          }
          if (this.corporate.environment_evaluation[0].co2 == 0) {
            this.s3 = '-'
          }
          else {
            this.s3 = this.corporate.social_evaluation[0].term_ratio
          }

          // g score
          if (this.corporate.environment_evaluation[0].co2 == 0) {
            this.g1 = '-'
          }
          else {
            this.g1 = this.corporate.governance_evaluation[0].board_ratio
          }
          if (this.corporate.governance_evaluation[0].board_independency == true) {
            this.g2 = '일치'
          }
          else if (this.corporate.governance_evaluation[0].board_independency == false) {
            this.g2 = '불일치'
          }
          else {
            this.g2 = '.'
          }

          if (this.corporate.environment_evaluation[0].co2 == 0) {
            this.g3 = '-'
          }
          else {
            this.g3 = this.corporate.governance_evaluation[0].largest_shareholder
          }

          if (this.corporate.environment_evaluation[0].co2 == 0) {
            this.g4 = '-'
          }
          else {
            this.g4 = this.corporate.governance_evaluation[0].salary_gap
          }

          if (this.corporate.environment_evaluation[0].co2 == 0) {
            this.g5 = '-'
          }
          else {
            this.g5 = this.corporate.governance_evaluation[0].dividen_ratio
          }
          this.newsList = this.corporate.news.reverse()
        })
        .catch(err => {
          console.log('정보 가져오기 오류', err)
        })
    },
    getRecom(pk) {
      axios.get(`corporates/${pk}/similarcorp/`, {headers:this.setToken()})

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
    this.getDetail(this.pk)
    this.getRecom(this.pk)
  },
   watch: {
    '$route.params.pk': function() {
      this.pk = this.$route.params.pk
      this.getDetail(this.pk)
      this.getRecom(this.pk)
      window.scrollTo(0, 0)
    }
  }
}
</script>

<style scoped>
.scrap-btn {
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
}
.scrap-btn:hover {
  transform: scale(1.15);
  -webkit-transform: scale(1.15);
  -moz-transform: scale(1.15);
  -ms-transform: scale(1.15);
  -o-transform: scale(1.15);
}
.corporate-name {
  color: #FABD02;
  /* background-color:rgb(0, 0, 0); */
  padding: 8px;
}
.no-news {
  color: #FABD02;
  padding-top: 8px;
  padding-bottom: 6px;
  font-size: 17px;
  word-spacing: 2.8px;
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
  background-color:rgb(0, 0, 0);
  color:white;
  position:relative;
}
/* .recomd:hover {
  background-color: rgba(255,255,255,0.55);
  background-color: rgba(255,255,255,0.55);
  cursor: pointer;
} */


.scrap-score {
  color:#e6cb7c;
  display: flex;
  justify-content: space-between;
  font-size: 1.3rem;
  background-color:black;
}
.news-link {
  color: white;
  background: transparent;
  white-space: normal;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  text-decoration: none; 
}
.table-text {
  color: white;
  background: transparent;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}
.news-body:hover {
  background-color: rgba(255,255,255,0.55);
  cursor: pointer;
}
.dh {
  width: 220px;
  height: 120px;
  background-color:rgb(0, 0, 0);
  color:white;
  position: relative;
  margin-top: 30px;
  margin-bottom: 50px;
  text-align: center;
  border-right: solid 1px rgb(68, 67, 67);
  border-left: solid 1px rgb(68, 67, 67);
}
.dh:hover {
  background-color: #242423;
  cursor: pointer;
}
.dh:before {
  content: "";
  position: absolute;
  top: -25px;
  left: 0;
  width: 220px;
  height: 0;
  border-left: 50px solid transparent;
  border-right: 50px solid transparent;
  border-bottom: 25px solid rgb(68, 67, 67);
}
.dh:after {
  content: "";
  position: absolute;
  bottom: -25px;
  left: 0;
  width: 220px;
  height: 0;
  border-left: 50px solid transparent;
  border-right: 50px solid transparent;
  border-top: 25px solid rgb(68, 67, 67);
}
</style>