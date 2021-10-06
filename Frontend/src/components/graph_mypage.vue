<!-- 레이더 차트 -->
<template>
    <div id="chart">
        <apexchart type="radar" height="250" :options="chartOptions" :series="series"></apexchart>
    </div>
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
        chartOptions: {
          chart: {
            id: 'vuechart-example'
          },
          xaxis: {
            categories: ["Environment", "Social", "Governance",]
          }
        },
        series: [{
          name: 'score',
          data: [],
        }],
        recommend: [],
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
      get_esg() {
      axios.get( 'accounts/profile_esg/', {headers:this.setToken()})

        .then(res => {
              
              this.series[0].data.push(res.data.mbti.e_score)
              this.series[0].data.push(res.data.mbti.s_score)
              this.series[0].data.push(res.data.mbti.g_score)
              this.recommend = res.data.recommend
              console.log(this.series[0].data)

          })
        .catch(err => {
          console.log('정보 가져오기 오류', err)
        })
  },
    }, 
    async mounted(){
      this.get_esg()
    }
  }
</script>
