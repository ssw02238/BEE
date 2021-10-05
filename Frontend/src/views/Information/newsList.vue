<template>
  <div>
    <div class="mb-4">
        <p style="font-size:2rem; color:white;margin-left:150px">News</p>
        <p style="font-soze: 1.2rem; 
        margin-left:150px;
        background-color:black;
        color: #FABD02">
        Kospi 200개 기업의 ESG관련 뉴스를 확인해보세요
        </p>
    </div>
    <table class="table" style="width: 75%;margin:auto;">
    <thead>
      <tr>
        <th scope="col">No</th>
        <th scope="col">기사 제목</th>
        <!-- <th scope="col">기업</th> -->
        <th scope="col">날짜</th>
      </tr>
    </thead>

    <tbody v-for="(content, idx) in paginated" :key="idx">
      <tr>
        <!-- <th scope="row">1</th> -->
        <td>{{ 10 * (page - 1) + idx + 1 }} </td>
        <td class="news-link" @click="goPage(content.url)">{{ content.title }} </td>
        <!-- <td>{{ content.corporate}}</td>             -->
        <td>{{ content.date }} </td>
      </tr>
    </tbody>
    </table>

  <!-- pagination --> 
    <nav aria-label="Page navigation example" style="margin-top: 30px;" class="d-flex justify-content-center">
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
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'newsList',
  data() {
      return {
        news: [],
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
    // 뉴스 리스트 출력 
    getNews() {
      axios.get('boards/news/', {headers:this.setToken()})
      
        .then(res => {
          this.news = res.data
          console.log('받아온 뉴스', this.news)
        })
        .catch(err => {
          console.log('뉴스 오류', err)
        })
    },
    goPage(url){
        window.open(url, "_blank")
      },
    //paginated
    setPages() {
      let numberOfPages = Math.ceil(this.news.length / this.perPage);
      for (let index = 1; index <= numberOfPages; index ++) {
        this.pages.push(index);
      }
    },
    paginate(news) {
      let page = this.page
      let perPage = this.perPage
      let from = (page * perPage) - perPage;
      let to = (page * perPage);
      return  news.slice(from, to)
    },

    // scrap 하기 ??
    // getScrap() {
    //   axios.post('corporates/${corp_id}/scrap/', {headers:this.setToken()})
      
    //     .then(res => {
    //       console.log(res)
    //     })
    //     .catch(err => {
    //       console.log('오류', err)
    //     })
    // }
  },
  async mounted() {
    this.getNews()
  },
  computed: {
    paginated() {
      return this.paginate(this.news)
    }
  },
  watch: {
    news () {
      this.setPages();
      
    }
  },
}
</script>

<style>
th,td{
    text-align: center;
}
.news-link {
  text-decoration: underline; 
  text-underline-position:under;
}
.table {
  color:white;
  background-color:black;
}
td {
  font-family: 'Pretendard-Regular';
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