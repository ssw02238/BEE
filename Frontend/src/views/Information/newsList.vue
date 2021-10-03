<template>
  <div>
    <table class="table" style="width: 75%;margin:auto;">
  <thead>
    <tr>
      <th scope="col">No</th>
      <th scope="col">기사 제목</th>
      <th scope="col">기업</th>
      <th scope="col">날짜</th>
      <th scope="col">스크랩</th>

    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>ESG 경영 논란 ~~~ </td>
      <td>ESG 경영 논란 ~~~ </td>
      <td>ESG 경영 논란 ~~~ </td>            
      <td>ESG 경영 논란 ~~~ </td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>ESG 경영 논란 ~~~ </td>
      <td>ESG 경영 논란 ~~~ </td>
      <td>ESG 경영 논란 ~~~ </td>            
      <td>ESG 경영 논란 ~~~ </td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>ESG 경영 논란 ~~~ </td>
      <td>ESG 경영 논란 ~~~ </td>
      <td>ESG 경영 논란 ~~~ </td>            
      <td>ESG 경영 논란 ~~~ </td>
    </tr>
  </tbody>
</table>
 
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'newsList',
  components: {
  },
  data() {
      return {
        news: [],
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
      getNews: function () {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/api/boards/news/',
          headers: this.setToken()
        })
          .then(res => {
            this.news = res.data
            console.log(this.news)
          })
          .catch(err => {
            console.log('오류', err)
          })
      },
      // scrap 하기 ??
      getScrap() {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/api/corporates/${corp_id}/scrap/',
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
          })
          .catch(err => {
            console.log('오류', err)
          })
      }
  },
  async mounted() {
    this.getNews()
  }
}
</script>

<style>
th,td{
    text-align: center;
}
.table {
  color:white;
  background-color:black;
}
td {
  font-family: 'Pretendard-Regular';
}
</style>