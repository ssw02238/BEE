<template>
  <div class="test">
    <h2 class="mb-5">ESG mbti test</h2>
    <h5 style="color:yellow;">항목 별 점수가 다르니 주의하세요 : )</h5>
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