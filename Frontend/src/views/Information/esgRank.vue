<template>
  <div class="container">

<!-- Rank div 시작 -->
    <div class="card text-center top-card" style="background-color: black; margin: auto;">
      <div class="d-flex justify-content-between align-items-center">
        <div class="card-header" style="font-size:2rem; color:#f3c438; text-align:left;">
          Ranks
        </div>
        <div class="d-flex align-items-center">
          <searchBar/>
          <!-- 드롭다운 -->
          <div class="dropdown mx-3">
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false" style="float: right;">
              필터링
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li><a class="dropdown-item" href="#" @click="getErank()">E 순위</a></li>
              <li><a class="dropdown-item" href="#" @click="getSrank()">S 순위</a></li>
              <li><a class="dropdown-item" href="#" @click="getGrank()">G 순위</a></li>
              <li><a class="dropdown-item" href="#" @click="getESGRank()">ESG 순위</a></li>
            </ul>
          </div>
        </div>
      </div>
    <!-- 드롭다운 끝 -->

    <!-- 랭킹 테이블 시작 -->
      <div class="card-body" style="background-color: black;">
        <Table
        :page = "page"
        :paginated="paginated"/>
      </div>
    <!-- pagination --> 
    <nav aria-label="Page navigation example" style="margin: auto">
      <ul class="pagination">
        <li class="page-item">
          <button type="button" class="page-link" v-if="page > 1" @click="page--"> Previous </button>
        </li>
        <li class="page-item disabled">
          <button type="button" class="page-link" v-if="page == 1" @click="page--" style="background-color: black;"> Previous </button>
        </li>
        <li class="page-item">
          <button type="button" class="page-link" v-for="pageNumber in pages.slice(page-1, page+5)" :key="pageNumber" @click="page = pageNumber"> {{pageNumber}} </button>
        </li>
        <li class="page-item">
          <button type="button" @click="page++" v-if="page < pages.length" class="page-link"> Next </button>
        </li>
      </ul>
    </nav>  
    <!-- 랭킹 테이블 끝 -->
    </div>
    <!-- rank div 끝 -->
    <hr style="color:yellow; height:5px;">
<!-- Graph div 시작 -->
    <div class="card text-center top-card" style="background-color: black; margin: auto;">
      <div class="card-header" style="font-size:2rem; color:#f3c438; text-align:left;">
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
import SearchBar from '../../components/SearchBar.vue'
export default {
  name: 'esgRank',
  components: {
  Table,Graph,Graph2,Scrap,SearchBar
  },
  data() {
    return{
      rank: [],
      // page
      page: 1,
      perPage: 10,
      pages: []
      
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
      axios.get('boards/esg-ranking/', {headers:this.setToken()})

        .then(res => {
          this.rank = res.data.corp_data
        })
        .catch(err => {
          console.log('전체 순위 오류', err)
        })
    },
    setPages() {
      let numberOfPages = Math.ceil(this.rank.length / this.perPage);
      for (let index = 1; index <= numberOfPages; index ++) {
        this.pages.push(index);
        // console.log(this.pages, '페이지 세팅')
      }
    },
    paginate(rank) {
      let page = this.page
      let perPage = this.perPage
      let from = (page * perPage) - perPage;
      let to = (page * perPage);
      console.log('잘린 애들', rank.slice(from, to))
      console.log('현재 페이지', page)
      return  rank.slice(from, to)
    },
    getErank() {
      axios.get('boards/e-ranking/', {headers:this.setToken()})

        .then(res => {
          console.log('e순위', this.rank)
          this.rank = res.data
        })
        .catch(err => {
          console.log('E 순위 오류', err)
        })
    },
    getSrank() {
      axios.get('boards/s-ranking/', {headers:this.setToken()})

        .then(res => {
          this.rank = res.data
          console.log('s순위', this.rank)
        })
        .catch(err => {
          console.log('s 순위 오류', err)
        })
    },
    getGrank() {
        axios.get('boards/g-ranking/', {headers:this.setToken()})

        .then(res => {
          this.rank = res.data
          console.log('g순위', this.rank)
        })
        .catch(err => {
          console.log('G 순위 오류', err)
        })
    }
  },
  async mounted () {
    this.getESGRank()
  },
  computed: {
    paginated() {
      return this.paginate(this.rank)
    }
  },
  watch: {
    rank () {
      this.setPages();
      
    }
  },
}
</script>

<style scoped>
.graphs {
  background-color: black;  
  display: flex;
  justify-content: space-around;
}
button.page-link {
  display: inline-block;
}
button.page-link {
    font-size: 20px;
    color: #FABD02;
    font-weight: 500;
    background-color: black;  
}
</style>