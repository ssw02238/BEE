<template>
  <div>
    <table class="table table-dark" style="width: 75%;margin:auto;">
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

    <b-table hover :items="items"></b-table>
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
        items: [
          { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
          { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          {
            age: 89,
            first_name: 'Geneva',
            last_name: 'Wilson',
            _rowVariant: 'danger'
          },
          {
            age: 40,
            first_name: 'Thor',
            last_name: 'MacDonald',
            _cellVariants: { age: 'info', first_name: 'warning' }
          },
          { age: 29, first_name: 'Dick', last_name: 'Dunlap' }
        ]
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
      // 오늘의 기업 출력 
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
</style>