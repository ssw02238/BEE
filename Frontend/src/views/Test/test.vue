<template>
  <div class="test">
    <h2 class="mb-2">ESG mbti test</h2>
    <p class="mb-4" id="font" style="color:white;">항목 별 점수가 다르니 주의하세요 : )</p>
    <testRange /> 
  </div>
</template>

<script>
import testRange from '../../components/testRange.vue'
export default {
  name: 'test',
  components: {
    testRange,
  }
}
</script>

<style scoped>
.test {
  width: 40%;
  margin: auto;
  color: #FABD02
}
</style>