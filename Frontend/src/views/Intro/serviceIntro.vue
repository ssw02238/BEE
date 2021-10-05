<template>
  <div class="container">

    <!-- carousel --> 
    <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner" style="width:75%;margin: auto;">
        <div class="carousel-item active" style="display:block;">
          <img src="@/assets/1.jpg" class="d-block w-100" alt="image1">
          <div class="carousel-caption d-none d-md-block">
            <h5>Environmental Responsibility</h5>
            <p id="font"> 환경 경영 <br> 에너지 사용량, 온실가스 배출량으로 기준으로 평가합니다. </p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="@/assets/carousel2.jpg" class="d-block w-100" alt="image2">
          <div class="carousel-caption d-none d-md-block">
            <h5>Social Responsibility</h5>
            <p id="font">사회 책임 경영 <br> 평등한 고용 사회를 만들기 위해 임원 내 여성비율, 기간제 근로자 비율 등을 기준으로 평가합니다. </p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="@/assets/carousel1.jpg" class="d-block w-100" alt="image3">
          <div class="carousel-caption d-none d-md-block">
            <h5>Governance</h5>
            <p id="font">기업 지배 구조 <br> 투명한 지배구조를 갖춘 기업으로, 이사회 독립성, 배당 성향 등으로 평가합니다.  </p>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <hr style="border: solid 1px white;">
    <p style="text-align:center; font-size:2rem">지속 가능 투자를 선도하는 <br> World-Class ESG Valuation System</p>
    <!-- tab --> 
    <div style="width:75%;margin:auto;" class="mt-5">
      <ul class="nav nav-tabs" id="myTab" role="tablist">
        <li class="nav-item" role="presentation">
          <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home" type="button" role="tab" aria-controls="home" aria-selected="true">서비스 소개</button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile" type="button" role="tab" aria-controls="profile" aria-selected="false">서비스 목표</button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact" type="button" role="tab" aria-controls="contact" aria-selected="false">ESG 란?</button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#standard" type="button" role="tab" aria-controls="standard" aria-selected="false">평가 기준</button>
        </li>
      </ul>
      <div class="tab-content" id="myTabContent">
        <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
          <div id="font"> 
          <b>BEE(Best ESG Enterprise)</b>는 누구나 쉽게 기업의 비재무적 정보를 통한 ESG 평가를 확인할 수 있는 서비스를 제공합니다. <br><hr>
          저금리, 저성장 기조가 장기화되며 투자자들은 은행 예금 상품에 한계를 느끼고 있습니다. <br><br>
          동학 개미운동이라는 단어가 등장할 정도로 투자에 대한 관심도가 높아진 지금, 기업을 평가하는 새로운 기준인 <b>ESG</b>가 등장하게 되었습니다.<br><br>
          불안정한 ESG 지표에 대한 기준을 확립하고 실시간 점수를 제공함으로써 <b>투자자의 책임투자</b>와 <b>기업의 지속 가능 경영</b>을 독려하고자 합니다.<hr>
          <b>BEE</b>는 기업이 사회, 환경, 지배구조 부분에서 가치를 실현하는지 다각도에서 평가한 후, <b>비재무적 정보</b>를 활용하여 <b>지속 가능 경영</b>에 대한 정보를 제공하고자 합니다. 
          <b>BEE와 함께 새로운 투자 가치를 실현해보세요!</b>
            </div>
          </div>
        <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
          <div id="font"> 
           </div>
           </div>
        <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">
          <div id="font"> 
          <b>ESG 경영</b>이란 무엇일까요? <br><br>
          2004년 UN에서 처음 사용되어, 투자자가 <b>환경, 사회, 거버넌스</b>와 같은 ESG 요소를 통합적으로 고려하여 투자하는 것이
          건강한 투자라는 인식을 심어준 용어입니다. <hr>
          ESG 경영이란 'Environment', 'Social', 'Governance'의 앞 글자를 따서 만들어진 단어로<br><br>
          기업이 <b>친환경, 사회적 책임, 지배구조 개선</b> 등을 고려해야 지속 가능한 경영을 할 수 있다는 의미를 가지고 있습니다.<br><br>
          환경, 사회, 지배구조 관련 이슈뿐만 아니라 기업의 재무성과 <b>지속 가능성</b>에 영향을 미칠 수 있는 모든 <b>비재무적 요인</b>들을 포함하기도 합니다. 
          </div>
        </div>
        <div class="tab-pane fade" id="standard" role="tabpanel" aria-labelledby="contact-tab">
          <div id="font"> 
          ESG 평가는 어떻게 이루어지나요? <br><hr>
          평가는 <b>1년 단위의 데이터</b>를 기반으로 평가가 이루어집니다.<br><br>
          평가 지표는 크게 <b>Environment, Social, Governance, News</b> 4가지로 이루어져 있습니다.<br><br>
          <b>Environment</b> : 온실가스 배출량, 에너지 사용량 데이터를 기반으로 평가합니다.<br><br>
          <b>Social</b> : 임원 내 여성비율, 평균 근속년수, 기간제 근로자 비율 데이터를 기반으로 평가합니다.<br><br>
          <b>Governance</b> : 사외이사 비율, 대표이사와 이사회 의장 일치여부, 최대주주 지분율, 임원/직원 보수비율, 배당성향 데이터를 기반으로 평가합니다.<br><br>
          <b>뉴스 기사</b> : 매일 새롭게 올라오는 뉴스 기사를 분석하여 지속 가능 경영에 긍정적인 기사인지, 부정적인 기사인지 AI로 판별 후 점수에 반영합니다.
          </div>
        </div>
      </div>
    </div>

  </div>
</template> 

<script>

export default {
  name: 'serviceIntro',
}
</script>

<style scoped>
.nav {
  width: 98%;
}
img{
  width: 500px;
  height:600px;
  display: block; 
}
.tab-content {
  background-color: rgba(0,0,0,1);
  height: 300px;
  min-height: 300px;
  color:white;
  margin-top: 10px;
  margin-left: 5px;
  margin-bottom: 7rem;
  padding: 10px;
}
.nav-link {
  background-color: #FABD02;
  color:black;
  margin-right: 6px;
}

.carousel-item {
  height:500px;
}
b {
  color: #FABD02;
}

</style>