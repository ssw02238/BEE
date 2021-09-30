<!-- 레이더 차트 -->
<template>
    <div id="chart">
                  <h5 style="color:white;"> ESG 성향 </h5>

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
          name: 'series-1',
          data: [],
        }]
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
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/profile_esg/`,
        headers: this.setToken()
      })
        .then(res => {
              this.e_score = res.data.e_score
              this.s_score = res.data.s_score
              this.g_score = res.data.g_score
              this.series[0].data.push(this.e_score)
              this.series[0].data.push(this.s_score)
              this.series[0].data.push(this.g_score)
              console.log(this.series[0].data)

          })
        .catch(err => {
          console.log('정보 가져오기 오류', err)
        })
  },
      open (link) {
        this.$electron.shell.openExternal(link)
      }
    }, 
    async mounted(){
      this.get_esg()
    }
  }
          
     
    
</script>
