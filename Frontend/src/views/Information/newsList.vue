<template>
  <div>
    <table class="table" style="width: 75%;margin:auto;">
  <thead>
    <tr>
      <th scope="col">No</th>
      <th scope="col">기사 제목</th>
      <th scope="col">기업</th>
      <th scope="col">날짜</th>
    </tr>
  </thead>

  <tbody v-for="(content, idx) in news" :key="idx">
    <tr>
      <th scope="row">1</th>
      <td>{{ idx }} </td>
      <td>{{ content.title }} </td>
      <td>{{ content.corporate}}</td>            
      <td>{{ content.date }} </td>
    </tr>
  </tbody>

</table>
 
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'newsList',
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
    getNews() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/boards/news/',
        headers: this.setToken()
      })
        .then(res => {
          this.news = res.data
          console.log('받아온 뉴스', this.news)
        })
        .catch(err => {
          console.log('뉴스 오류', err)
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