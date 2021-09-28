<template>
  <div>

    <!-- 문제 1번 -->
    <label for="customRange1" class="form-label1">Q 1. 나는 제로 웨이스트를 실천하는 기업에 대해 2개 이상 알고 있다.</label>
    
    <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots1"
        v-model="selected1"
        :aria-describedby="ariaDescribedby"
        name="radio-options-slots1"
      >
        <template>
          <b-form-radio value="매우 아니다">매우 아니다</b-form-radio>
          <b-form-radio value="아니다">아니다</b-form-radio>          
          <b-form-radio value="보통">보통</b-form-radio>
          <b-form-radio value="그렇다">그렇다</b-form-radio>
          <b-form-radio value="매우 그렇다">매우 그렇다</b-form-radio>
        </template>
<div class="mt-3" style="text-align: end;">Selected: <strong>{{ selected1 }}</strong></div>
      </b-form-radio-group>
    </b-form-group>

    
      <!-- 문제 2번 -->
        <label for="customRange2" class="form-label2">Q 2. 정규직 근로자 비율이 70%를 넘어야 사회적으로 공헌하는 기업이라고 할 수 있다.</label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots2"
        v-model="selected2"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots2"
      >
        <template #first>
          <b-form-radio value="매우 아니다">매우 아니다</b-form-radio>
          <b-form-radio value="아니다">아니다</b-form-radio>          
          <b-form-radio value="보통">보통</b-form-radio>
          <b-form-radio value="그렇다">그렇다</b-form-radio>
          <b-form-radio value="매우 그렇다">매우 그렇다</b-form-radio>
        </template>

<div class="mt-3" style="    text-align: end;">Selected: <strong>{{ selected2 }}</strong></div>
      </b-form-radio-group>
    </b-form-group>

<!-- 문제 3번 -->
        <label for="customRange3" class="form-label3">Q 3. 세무 조작, 부정부패 사건에 연류된 기업은 투자할 가치가 적다고 생각한다.</label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots3"
        v-model="selected3"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots3"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="매우 아니다">매우 아니다</b-form-radio>
          <b-form-radio value="아니다">아니다</b-form-radio>          
          <b-form-radio value="보통">보통</b-form-radio>
          <b-form-radio value="그렇다">그렇다</b-form-radio>
          <b-form-radio value="매우 그렇다">매우 그렇다</b-form-radio>
        </template>

<div class="mt-3" style="    text-align: end;">Selected: <strong>{{ selected3 }}</strong></div>
      </b-form-radio-group>
    </b-form-group>

<!-- 문제 4번 -->
        <label for="customRange4" class="form-label4">Q 4. 평소 온실가스 배출량의 심각함을 인지하고 있다.</label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots4"
        v-model="selected4"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots4"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="매우 아니다">매우 아니다</b-form-radio>
          <b-form-radio value="아니다">아니다</b-form-radio>          
          <b-form-radio value="보통">보통</b-form-radio>
          <b-form-radio value="그렇다">그렇다</b-form-radio>
          <b-form-radio value="매우 그렇다">매우 그렇다</b-form-radio>
        </template>

<div class="mt-3" style="    text-align: end;">Selected: <strong>{{ selected4 }}</strong></div>
      </b-form-radio-group>
    </b-form-group>

<!-- 문제 5번 -->
        <label for="customRange5" class="form-label5">Q 5. 직원 평균 근속 년수가 길수록 노동 인권을 고려하는 기업이라고 생각한다. </label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots5"
        v-model="selected5"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots5"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="매우 아니다">매우 아니다</b-form-radio>
          <b-form-radio value="아니다">아니다</b-form-radio>          
          <b-form-radio value="보통">보통</b-form-radio>
          <b-form-radio value="그렇다">그렇다</b-form-radio>
          <b-form-radio value="매우 그렇다">매우 그렇다</b-form-radio>
        </template>

<div class="mt-3" style="    text-align: end;">Selected: <strong>{{ selected5 }}</strong></div>
      </b-form-radio-group>
    </b-form-group>

<!-- 문제 6번 -->
        <label for="customRange6" class="form-label6">Q 6. 배당 성향이 높을수록 무조건 좋은 기업이라고 생각한다.</label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots6"
        v-model="selected6"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots6"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="매우 아니다">매우 아니다</b-form-radio>
          <b-form-radio value="아니다">아니다</b-form-radio>          
          <b-form-radio value="보통">보통</b-form-radio>
          <b-form-radio value="그렇다">그렇다</b-form-radio>
          <b-form-radio value="매우 그렇다">매우 그렇다</b-form-radio>
        </template>

<div class="mt-3" style="    text-align: end;">Selected: <strong>{{ selected6 }}</strong></div>
      </b-form-radio-group>
    </b-form-group>

<!-- 문제 7번 -->
        <label for="customRange7" class="form-label7">Q 7. 제공하는 제품의 품질 향상을 위해서라면 폐기물 발생량은 감수해야 한다고 생각한다.</label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots7"
        v-model="selected7"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots7"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="매우 아니다">매우 아니다</b-form-radio>
          <b-form-radio value="아니다">아니다</b-form-radio>          
          <b-form-radio value="보통">보통</b-form-radio>
          <b-form-radio value="그렇다">그렇다</b-form-radio>
          <b-form-radio value="매우 그렇다">매우 그렇다</b-form-radio>
        </template>

<div class="mt-3" style="    text-align: end;">Selected: <strong>{{ selected7 }}</strong></div>
      </b-form-radio-group>
    </b-form-group>

<!-- 문제 8번 -->
        <label for="customRange8" class="form-label8">Q 8. 기업 임원 중 여성 비율이 높을 수록 고용 평등을 실천하고 있다고 생각한다.</label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots8"
        v-model="selected8"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots8"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="매우 아니다">매우 아니다</b-form-radio>
          <b-form-radio value="아니다">아니다</b-form-radio>          
          <b-form-radio value="보통">보통</b-form-radio>
          <b-form-radio value="그렇다">그렇다</b-form-radio>
          <b-form-radio value="매우 그렇다">매우 그렇다</b-form-radio>
        </template>

<div class="mt-3" style="    text-align: end;">Selected: <strong>{{ selected8 }}</strong></div>
      </b-form-radio-group>
    </b-form-group>

<!-- 문제 9번 -->
        <label for="customRange9" class="form-label2">Q 9. 임원과 직원 보수 금액 차이가 작을수록 공평한 임금 체계를 가졌다고 생각한다.</label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots9"
        v-model="selected9"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots2"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="매우 아니다">매우 아니다</b-form-radio>
          <b-form-radio value="아니다">아니다</b-form-radio>          
          <b-form-radio value="보통">보통</b-form-radio>
          <b-form-radio value="그렇다">그렇다</b-form-radio>
          <b-form-radio value="매우 그렇다">매우 그렇다</b-form-radio>
        </template>

<div class="mt-3" style="    text-align: end;">Selected: <strong>{{ selected9 }}</strong></div>
      </b-form-radio-group>
    </b-form-group>

  </div>

  
</template>

<script>

export default {
  name: 'test',
 data() {
      return {
        selected1: '',
        selected2: '',
        selected3: '',
        selected4: '',
        selected5: '',
        selected6: '',
        selected7: '',
        selected8: '',
        selected9: '',
      }
    }
  }
</script>

<style scoped>
.score {
  justify-content: space-around;
}
</style>