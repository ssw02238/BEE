<template>
  <div class="container">

<!-- Rank div 시작 -->
    <div class="card text-center top-card" style="background-color: black; margin: auto;">
      <div class="card-header" style="font-size:2rem; color:white; text-align:left;">
        Ranks
      </div>
      <!-- 드롭다운 -->
      <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false" style="float: right;">
          필터링
        </button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
          <li><a class="dropdown-item" href="#">E 점수 순</a></li>
          <li><a class="dropdown-item" href="#">S 점수 순</a></li>
          <li><a class="dropdown-item" href="#">G 점수 순</a></li>
        </ul>
      </div>
    <!-- 드롭다운 끝 -->

    <!-- 랭킹 테이블 시작 -->
      <div class="card-body" style="background-color: black;">
        <Table
        :rank="rank"/>
      </div>
    <!-- 랭킹 테이블 끝 -->
    </div>
    <!-- rank div 끝 -->



<!-- Graph div 시작 -->
    <div class="card text-center top-card" style="background-color: black; margin: auto;">
      <div class="card-header" style="font-size:2rem; color:white; text-align:left;">
        Graphs
      </div>
    <!-- Graph 시작 -->
      <div class="card-body graphs">
        
        <Graph/>
        
        <Graph2/>
        <Scrap/>
              </div>
<!-- Graph 끝 --> 

    </div>

  </div>
</template>

<script>
import axios from 'axios'

import Table from '../../components/table.vue'
import Graph from '../../components/graph_rank.vue'
import Graph2 from '../../components/graph_rank2.vue'
import Scrap from '../../components/scrap_rank.vue'
export default {
  name: 'esgRank',
  components: {
  Table,Graph,Graph2,Scrap
  },
  data() {
    return{
      rank: [],
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
    // ESG 전체 순위 리스트 조회 
    getESGRank() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/boards/esg-ranking/',
        headers: this.setToken()
      })
        .then(res => {
          this.rank = res.data.corp_data.slice(0, 10)
        })
        .catch(err => {
          console.log('전체 순위 오류', err)
        })
    },
  },
  async mounted() {
    this.getESGRank()
  }
}
</script>

<style scoped>
.graphs {
  background-color: black;  
  display: flex;
  justify-content: space-around;
}
</style>