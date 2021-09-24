<template>
  <div>
    <label for="customRange3" class="form-label">질문 1</label>
    <input type="range" class="form-range" min="0" max="5" step="1" id="customRange3">
    <div class="score">
      <span>1</span>
      <span>3</span>
      <span>5</span>
    </div>
  </div>
</template>

<script>

export default {
  name: 'test',
}
</script>

<style scoped>
.score {
  justify-content: space-around;
}
</style>