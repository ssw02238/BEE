<!-- 도넛 차트 -->
<template>
    <div id="chart">
        <apexchart style="color:#FABD02;" class="chart" type="donut" height="200" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>

<script>
import axios from 'axios'

import VueApexCharts from 'vue-apexcharts'
export default {
    components: {
        apexchart: VueApexCharts,
    },
    data() {
        return {
            recommends: [],
            series: [],
            
            chartOptions: {
                labels: ['E Score', 'S Score', 'G Score'],
                fill: {
                    colors:['#008ffb', '#00E396', '#FEB019']
                },
            },
            }
    },
    methods: {
    getRecom(pk) {
      axios.get(`corporates/${pk}/similarcorp/`, {headers:this.setToken()})

        .then(res => {
          console.log('추천 기업 정보', res.data.corporates)
          this.recommends = res.data.corporates
        })
        .catch(err => {
          console.log('추천 기업 정보 가져오기 오류', err)
        })
    }
    },
    async mounted() {
      this.getESGRank()
    }
}
</script>
<style scoped>

</style>