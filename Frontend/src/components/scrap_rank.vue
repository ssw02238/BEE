<!-- 세로 막대 차트 -->
<template>
    <div id="chart">
        
      <p class="card-text" style="font-size:1.5rem;">스크랩 순위</p>
<table class="table table" style="width:150px">
  <thead>
    <tr>
      <th scope="col">No</th>
      <th scope="col">기업 명</th>

    </tr>
  </thead>
  <tbody>
    <tr @click="moveToDetail(corporates[0].pk)">
      <th scope="row">1</th>
      <td>{{ corporates[0].name }}</td>
    </tr>
    <tr @click="moveToDetail(corporates[1].pk)">
      <th scope="row">2</th>
      <td>{{ corporates[1].name }}</td>
    </tr>
    <tr @click="moveToDetail(corporates[2].pk)">
      <th scope="row">3</th>
      <td>{{ corporates[2].name }}</td>
    </tr>
  </tbody>
</table>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'scrap_rank',
  data: function () {
    return {
      corporates: [],
    }
  },
  methods: {
    getRank: function () {
        axios.get('boards/popularcorp/')
      .then(res => {
        // console.log(res)
        this.corporates = res.data
      }) 
      .catch(err => {
        console.log(err)
      })
    },
    moveToDetail: function (id) {
      console.log(id)
    }
  },
  async mounted() {
    this.getRank()
  }
}
</script>
<style scoped>
th, td {
  color:#f3c438
}
p {
  color: #FABD02
}
</style>