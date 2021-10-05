<!-- 레이더 차트 -->
<template>
    <div id="chart">
                  <!-- <h5 style="color:white;"> ESG 성향 </h5> -->

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
          // console.log(res.data.mbti.e_score)
              // if (res.data.mbti) {
              //   this.series[0].data[0] = res.data.mbti.e_score
              //   this.series[0].data[1] = res.data.mbti.s_score
              //   this.series[0].data[2] = res.data.mbti.g_score
              // }
              
              this.series[0].data.push(res.data.mbti.e_score)
              this.series[0].data.push(res.data.mbti.s_score)
              this.series[0].data.push(res.data.mbti.g_score)
              this.recommend = res.data.recommend
              console.log(this.series[0].data)
                            console.log("dd")

          })
        .catch(err => {
          console.log('정보 가져오기 오류', err)
        })
  },
      // open (link) {
      //   this.$electron.shell.openExternal(link)
      // }
    }, 
    async mounted(){
      this.get_esg()
    }
  }
          
     
    
</script>
