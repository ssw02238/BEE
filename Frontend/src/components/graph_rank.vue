<!-- 세로 막대 차트 -->
<template>
    <div id="chart">
      <p class="card-text" style="font-size:1.5rem;">평균 점수</p>
        <apexchart style="color:#FABD02;" class="chart" type="bar" height="200" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>

<script>
import axios from 'axios'
import VueApexCharts from 'vue-apexcharts'
export default {
    name: 'graph_rank',
    components: {
        apexchart: VueApexCharts,
    },
    data() {
        return {
            series: [{
              data: []
          }],
          chartOptions: {

            fill: {
                colors: ['#FABD02']
            },
            plotOptions: {
              bar: {
                borderRadius: 4,
              }
            },
            dataLabels: {
              enabled: false,
            },
            xaxis: {
              categories: ['E Score', 'S Score', 'G Score'],
              labels: {
                  style: {
                      colors: ['#FABD02','#FABD02','#FABD02'],
                      fontSize: '15px',
                      fontFamily: 'Pretendard-Regular'
                  }
              }
            },
          },
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
    getESGRank() {
      axios.get('boards/esg-ranking/', {headers:this.setToken()})
            .then(res => {
              this.e_avg = res.data.e_average
              this.s_avg = res.data.s_average
              this.g_avg = res.data.g_average
              this.series[0].data.push(this.e_avg)
              this.series[0].data.push(this.s_avg)
              this.series[0].data.push(this.g_avg)
              // console.log(this.series[0].data)
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
p{
  color: #FABD02
}
</style>