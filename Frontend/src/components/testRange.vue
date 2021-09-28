<template>
  <div>
    <label for="customRange3" class="form-label">질문 1. 나는 제로 웨이스트를 실천하는 기업에 대해 2개 이상 알고 있다.</label>
    <b-form-group label="Radios using options and slots" v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots"
        v-model="selected"
        :options="options"
        :aria-describedby="ariaDescribedby"
        name="radio-options-slots"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="매우 아니다">매우 아니다</b-form-radio>
          <b-form-radio value="아니다">아니다</b-form-radio>          
          <b-form-radio value="보통">보통</b-form-radio>
          <b-form-radio value="그렇다">그렇다</b-form-radio>
          <b-form-radio value="매우 그렇다">매우 그렇다</b-form-radio>
        </template>

      </b-form-radio-group>
    </b-form-group>

    <div class="mt-3">Selected: <strong>{{ selected }}</strong></div>
    <!--  -->
        <label for="customRange3" class="form-label">질문 2. 평소 온실가스 배출량의 심각함을 인지하고 있다.</label>
        <b-form-group label="Radios using options and slots" v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots"
        v-model="selected"
        :options="options"
        :aria-describedby="ariaDescribedby"
        name="radio-options-slots"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="매우 아니다">매우 아니다</b-form-radio>
          <b-form-radio value="아니다">아니다</b-form-radio>          
          <b-form-radio value="보통">보통</b-form-radio>
          <b-form-radio value="그렇다">그렇다</b-form-radio>
          <b-form-radio value="매우 그렇다">매우 그렇다</b-form-radio>
        </template>

      </b-form-radio-group>
    </b-form-group>

    <div class="mt-3">Selected: <strong>{{ selected }}</strong></div>

        <label for="customRange3" class="form-label">질문 3. 제공하는 제품의 품질 향상을 위해서라면 폐기물 발생량은 감수해야 한다고 생각한다.</label>
    <input type="range" class="form-range" min="0" max="5" step="1" id="customRange3">
    <div class="score">
      <span>1</span>
      <span>3</span>
      <span>5</span>
    </div>

        <label for="customRange3" class="form-label">질문 4.</label>
    <input type="range" class="form-range" min="0" max="5" step="1" id="customRange3">
    <div class="score">
      <span>1</span>
      <span>3</span>
      <span>5</span>
    </div>

        <label for="customRange3" class="form-label">질문 1</label>
    <input type="range" class="form-range" min="0" max="5" step="1" id="customRange3">
    <div class="score">
      <span>1</span>
      <span>3</span>
      <span>5</span>
    </div>

        <label for="customRange3" class="form-label">질문 1</label>
    <input type="range" class="form-range" min="0" max="5" step="1" id="customRange3">
    <div class="score">
      <span>1</span>
      <span>3</span>
      <span>5</span>
    </div>

        <label for="customRange3" class="form-label">질문 1</label>
    <input type="range" class="form-range" min="0" max="5" step="1" id="customRange3">
    <div class="score">
      <span>1</span>
      <span>3</span>
      <span>5</span>
    </div>

        <label for="customRange3" class="form-label">질문 1</label>
    <input type="range" class="form-range" min="0" max="5" step="1" id="customRange3">
    <div class="score">
      <span>1</span>
      <span>3</span>
      <span>5</span>
    </div>

        <label for="customRange3" class="form-label">질문 1</label>
    <input type="range" class="form-range" min="0" max="5" step="1" id="customRange3">
    <div class="score">
      <span>1</span>
      <span>3</span>
      <span>5</span>
    </div>

        <label for="customRange3" class="form-label">질문 1</label>
    <input type="range" class="form-range" min="0" max="5" step="1" id="customRange3">
    <div class="score">
      <span>1</span>
      <span>3</span>
      <span>5</span>
    </div>

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
 data() {
      return {
        selected: '',
      }
    }
  }
</script>

<style scoped>
.score {
  justify-content: space-around;
}
</style>