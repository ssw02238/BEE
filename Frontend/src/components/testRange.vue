<template>
  <div>
 <!-- <form v-on:submit="submitForm"> -->
    <!-- 문제 1번 -->
    <label for="customRange1" class="form-label1 question">Q 1. 나는 제로 웨이스트를 실천하는 기업에 대해 2개 이상 알고 있다.</label>
    
    <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots1"
        v-model="selected1"
        :aria-describedby="ariaDescribedby"
        name="radio-options-slots1"
      >
        <template>
          <b-form-radio value="1"> 매우 아니다</b-form-radio>
          <b-form-radio value="2">아니다</b-form-radio>          
          <b-form-radio value="3">보통</b-form-radio>
          <b-form-radio value="4">그렇다</b-form-radio>
          <b-form-radio value="5">매우 그렇다</b-form-radio>
        </template>
<div style="text-align: end;"> <strong>{{ selected1 }} 점</strong></div>
      </b-form-radio-group>
    </b-form-group>
    <hr>
    
      <!-- 문제 2번 -->
        <label for="customRange2" class="form-label2 question">Q 2. 정규직 근로자 비율이 70%를 넘어야 사회적으로 공헌하는 기업이라고 할 수 있다.</label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots2"
        v-model="selected2"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots2"
      >
        <template #first>
          <b-form-radio value="1">매우 아니다</b-form-radio>
          <b-form-radio value="2">아니다</b-form-radio>          
          <b-form-radio value="3">보통</b-form-radio>
          <b-form-radio value="4">그렇다</b-form-radio>
          <b-form-radio value="5">매우 그렇다</b-form-radio>
        </template>

<div style="text-align: end;"><strong>{{ selected2 }} 점</strong></div>
      </b-form-radio-group>
    </b-form-group>
  <hr>
<!-- 문제 3번 -->
        <label for="customRange3" class="form-label3 question">Q 3. 세무 조작, 부정부패 사건에 연류된 기업은 투자할 가치가 적다고 생각한다.</label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots3"
        v-model="selected3"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots3"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="1">매우 아니다</b-form-radio>
          <b-form-radio value="2">아니다</b-form-radio>          
          <b-form-radio value="3">보통</b-form-radio>
          <b-form-radio value="4">그렇다</b-form-radio>
          <b-form-radio value="5">매우 그렇다</b-form-radio>
        </template>

<div style="    text-align: end;"><strong>{{ selected3 }} 점</strong></div>
      </b-form-radio-group>
    </b-form-group>
<hr>
<!-- 문제 4번 -->
        <label for="customRange4" class="form-label4 question">Q 4. 평소 온실가스 배출량의 심각함을 인지하고 있다.</label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots4"
        v-model="selected4"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots4"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="1">매우 아니다</b-form-radio>
          <b-form-radio value="2">아니다</b-form-radio>          
          <b-form-radio value="3">보통</b-form-radio>
          <b-form-radio value="4">그렇다</b-form-radio>
          <b-form-radio value="5">매우 그렇다</b-form-radio>
        </template>

<div style="    text-align: end;"> <strong>{{ selected4 }} 점</strong></div>
      </b-form-radio-group>
    </b-form-group>
<hr>
<!-- 문제 5번 -->
        <label for="customRange5" class="form-label5 question">Q 5. 직원 평균 근속 년수가 길수록 노동 인권을 고려하는 기업이라고 생각한다. </label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots5"
        v-model="selected5"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots5"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="1">매우 아니다</b-form-radio>
          <b-form-radio value="2">아니다</b-form-radio>          
          <b-form-radio value="3">보통</b-form-radio>
          <b-form-radio value="4">그렇다</b-form-radio>
          <b-form-radio value="5">매우 그렇다</b-form-radio>
        </template>

<div  style="text-align: end;"><strong>{{ selected5 }} 점</strong></div>
      </b-form-radio-group>
    </b-form-group>
<hr>
<!-- 문제 6번 -->
        <label for="customRange6" class="form-label6 question">Q 6. 배당 성향이 높을수록 무조건 좋은 기업이라고 생각한다.</label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots6"
        v-model="selected6"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots6"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="5">매우 아니다</b-form-radio>
          <b-form-radio value="4">아니다</b-form-radio>          
          <b-form-radio value="3">보통</b-form-radio>
          <b-form-radio value="2">그렇다</b-form-radio>
          <b-form-radio value="1">매우 그렇다</b-form-radio>
        </template>

<div style="    text-align: end;"><strong>{{ selected6 }} 점</strong></div>
      </b-form-radio-group>
    </b-form-group>
<hr>
<!-- 문제 7번 -->
        <label for="customRange7" class="form-label7 question">Q 7. 제공하는 제품의 품질 향상을 위해서라면 폐기물 발생량은 감수해야 한다고 생각한다.</label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots7"
        v-model="selected7"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots7"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="5">매우 아니다</b-form-radio>
          <b-form-radio value="4">아니다</b-form-radio>          
          <b-form-radio value="3">보통</b-form-radio>
          <b-form-radio value="2">그렇다</b-form-radio>
          <b-form-radio value="1">매우 그렇다</b-form-radio>
        </template>

<div style="    text-align: end;"><strong>{{ selected7 }} 점</strong></div>
      </b-form-radio-group>
    </b-form-group>
<hr>
<!-- 문제 8번 -->
        <label for="customRange8" class="form-label8 question">Q 8. 기업 임원 중 여성 비율이 높을 수록 고용 평등을 실천하고 있다고 생각한다.</label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots8"
        v-model="selected8"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots8"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="1">매우 아니다</b-form-radio>
          <b-form-radio value="2">아니다</b-form-radio>          
          <b-form-radio value="3">보통</b-form-radio>
          <b-form-radio value="4">그렇다</b-form-radio>
          <b-form-radio value="5">매우 그렇다</b-form-radio>
        </template>

<div style="text-align: end;"><strong>{{ selected8 }} 점</strong></div>
      </b-form-radio-group>
    </b-form-group>
<hr>
<!-- 문제 9번 -->
        <label for="customRange9" class="form-label9 question">Q 9. 임원과 직원 보수 금액 차이가 작을수록 공평한 임금 체계를 가졌다고 생각한다.</label>
        <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio-group
        id="radio-slots9"
        v-model="selected9"

        :aria-describedby="ariaDescribedby"
        name="radio-options-slots9"
      >
        <!-- Radios in this slot will appear first -->
        <template #first>
          <b-form-radio value="1">매우 아니다</b-form-radio>
          <b-form-radio value="2">아니다</b-form-radio>          
          <b-form-radio value="3">보통</b-form-radio>
          <b-form-radio value="4">그렇다</b-form-radio>
          <b-form-radio value="5">매우 그렇다</b-form-radio>
        </template>

  <div style="text-align: end;"><strong>{{ selected9 }} 점</strong></div>
      </b-form-radio-group>
    </b-form-group>

  <button @click="submitForm" class="btn btn-lg btn-block mt-5 mb-5" type="submit" style="width:100%; background-color:#FABD01">제출하기</button>
 <!-- </form> -->

  </div>

  
</template>

<script>

import axios from 'axios'
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

        e_score:parseFloat(this.selected1) + parseFloat(this.selected4)+ parseFloat(this.selected7),
        s_score:parseFloat(this.selected2) + parseFloat(this.selected5)+ parseFloat(this.selected8),
        g_score:parseFloat(this.selected3) + parseFloat(this.selected6)+ parseFloat(this.selected9)
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
    submitForm: function () {
      const config = this.setToken()
      
      if (localStorage.getItem('mbti')){
     axios({
        method: 'put',
        url: 'http://127.0.0.1:8000/accounts/mbti/',
        data: {e_score:parseFloat(this.selected1) + parseFloat(this.selected4)+ parseFloat(this.selected7),
        s_score:parseFloat(this.selected2) + parseFloat(this.selected5)+ parseFloat(this.selected8),
        g_score:parseFloat(this.selected3) + parseFloat(this.selected6)+ parseFloat(this.selected9)},
        headers: config
      })      
        .then(res => {
          console.log('요청 제대로', res)         
          localStorage.setItem('mbti', res.data.mbti)
          this.$router.push({ name: 'mypage' })
          this.$router.go()
        })
        .catch(err => {
          console.log('axios 오류', err)
        }) }

      else {
     axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/mbti/',
        data: {e_score:parseFloat(this.selected1) + parseFloat(this.selected4)+ parseFloat(this.selected7),
        s_score:parseFloat(this.selected2) + parseFloat(this.selected5)+ parseFloat(this.selected8),
        g_score:parseFloat(this.selected3) + parseFloat(this.selected6)+ parseFloat(this.selected9)},
        headers: config
      })      
        .then(res => {
          console.log('요청 제대로', res)           
          localStorage.setItem('mbti', res.data.mbti)
          this.$router.push({ name: 'mypage' })
          this.$router.go()
        })
        .catch(err => {
          console.log('axios 오류', err)
        })}

    },
  }
}
// 현재 사용자한테 mbti 결과가 있으면 put 요청
// 없으면 post요청 
</script>

<style scoped>
.score {
  justify-content: space-around;
}
.question {
  margin-bottom: 10px;
}
#radio-slots1, #radio-slots2, #radio-slots3, #radio-slots4, #radio-slots5
,#radio-slots6, #radio-slots7, #radio-slots8, #radio-slots9{
  font-family: 'Pretendard-Regular';
}
</style>
