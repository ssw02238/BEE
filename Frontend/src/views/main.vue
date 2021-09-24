<template>
  <div class="main-div">
    <h1>Ranks</h1>
    <hr style="color:yellow">

    <!-- 1위 기업 정보 --> 
    <div class="accordion accordion-flush" id="accordionFlushExample">
      <div class="accordion-item">
        <h2 class="accordion-header" id="flush-headingOne">
          <button class="accordion-button collapsed" id="font" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
            ESG TOP 1 {{ top }}  🔔
          </button>
        </h2>
        <div id="flush-collapseOne" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample">
          <div class="accordion-body" id="font">
            <Top />
          </div>
        </div>
      </div>
    </div>

    <hr style="color:yellow">
    <!-- 기업 순위 --> 
    <h3 class="my-4">Monthly Ranking</h3>  
    <rankTable id="font" /> 

    <hr style="color:yellow">
    <!-- 오늘의 기업 --> 
    <div class="card mb-3">
      <div class="row g-0">
        <div class="col-md-4" style="display:flex">
          <img src="@/assets/esg_char.jpg" class="img-fluid rounded-start" alt="esg character" style="align-items:center">
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h5 class="card-title mb-4">오늘의 기업 🎉 {{ news_top }}</h5>
              <ul class="list-group card-text" id="font">
                <li class="list-group-item">뉴스 제목 1</li>
                <li class="list-group-item">뉴스 제목 1</li>
                <li class="list-group-item">뉴스 제목 1</li>
              </ul>
          </div>
        </div>
      </div>
    </div>
    <hr style="color:yellow">


    <!-- ESG 성향 --> 
    <h3 class="my-4">{{ nickname }} 님의 ESG 성향</h3>  
    <esgMbti/>
  </div>
</template>

<script>
import rankTable from '../components/table.vue'
import Top from '../components/Top.vue'
import esgMbti from '../components/esg_mbti.vue'

export default {
  name: 'main',
  components: {
    rankTable,
    Top,
    esgMbti
  },
  data:function(){
    return{
      top: '삼성전자',
      news_top: '포스코',
      nickname: '',
    };
  },
  async mounted() {
    this.nickname = localStorage.getItem('nickname')
  }
}
</script>

<style scoped>
.main-div {
  width: 75%;
  margin: auto;
}
h1, h3 {
  color:#FABD02;
}
.accordion-button {
  background-color: #ffdc74;
  color: black;
}
</style>