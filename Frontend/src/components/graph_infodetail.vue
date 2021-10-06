<!-- 인포디테일 차트 -->
<template>
    <div id="chart">
  <apexchart class="chart mt-5" type="radar" height="350" :options="chartOptions" :series="series"></apexchart>    </div>
  
</template>

<script>
import axios from 'axios'

import VueApexCharts from 'vue-apexcharts'
export default {
  components: {
    apexchart: VueApexCharts,
  },  
  data () {
      return {
        pk: '',
        chartOptions: {
          chart: {
            id: 'vuechart-example'
          },
          xaxis: {
            categories: ["Environment", "Social", "Governance",]
          }
        },
        series: [{
          name:'score',
          data: [],
        }]
      }
    },
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      },
      setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
      getScore(pk) {
        axios.get(`corporates/${pk}/detail/`, {headers:this.setToken()})
        .then(res => {
          this.E_rating = res.data.E_rating
          this.S_rating = res.data.S_rating
          this.G_rating = res.data.G_rating
          console.log(this.E_rating, 'e점수')
          this.series[0].data.push(this.E_rating)
          this.series[0].data.push(this.S_rating)
          this.series[0].data.push(this.G_rating)

          console.log(this.series, '넣은 데이터')
        })
        .catch(err => {
          console.log('자식에서 오류', err)
        })
      }
    },
    async mounted () {
      this.pk = this.$route.params.pk
      this.getScore(this.pk)
    }
}
</script>

<style scoped>
</style>