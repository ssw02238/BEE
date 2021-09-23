<template>
  <div>

    <h1 style='color:red;'>여기다가 작성하시면 됩니다</h1>

<div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner" style=" width:900px;margin: auto;">
    <div class="carousel-item active" style="display:block;">
      <img src="@/assets/1.jpg" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Environment Responsibility</h5>
        <p>환경에 대한 텍스트 작성</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="@/assets/2.jpg" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Social Responsibility</h5>
        <p>사회분야에 대한 텍스트 작성</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="@/assets/1.jpg" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Governanve</h5>
        <p>지배구조에 대한 텍스트 작성 </p>
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


  </div>
</template> 

<script>

export default {
  name: 'serviceIntro',
}
</script>

<style scoped>
img{
  width: 500px;
  height:600px;
  display: block; 

}
</style>