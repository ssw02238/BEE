<template>
<div class="row align">
    <!-- E table --> 
    <table class="table" style="width:30%;">
        <thead>
        <tr>
            <th scope="col">E</th>
            <th scope="col">점수</th>
        </tr>
        </thead>

        <tbody>
            <tr>
                <th scope="row">온실가스 배출량</th>
                <td>score1</td>
            </tr>
            <tr>
                <th scope="row">에너지 사용량</th>
                <td>score1</td>
            </tr>
        </tbody>
        </table>

    <!-- S table --> 
  <table class="table" style="width:30%;">
    <thead>
    <tr>
        <th scope="col">S</th>
        <th scope="col">점수</th>
    </tr>
    </thead>

    <tbody>
        <tr>
            <th scope="row">임원 내 여성 비율</th>
            <td>score1</td>
        </tr>
        <tr>
            <th scope="row">평균 근속 년수</th>
            <td>score1</td>
        </tr>
        <tr>
            <th scope="row">기간제 근로자 비율</th>
            <td>score1</td>
        </tr>
    </tbody>
    </table>

    <!-- g data --> 
     <table class="table" style="width:30%;">
    <thead>
    <tr>
        <th scope="col">G</th>
        <th scope="col">점수</th>
    </tr>
    </thead>

    <tbody>
        <tr>
            <th scope="row">사외이사 비율</th>
            <td>score1</td>
        </tr>
        <tr>
            <th scope="row">대표이사와 이사회 의장 일치 여부</th>
            <td>score1</td>
        </tr>
        <tr>
            <th scope="row">최대주주 지분율</th>
            <td>score1</td>
        </tr>
        <tr>
            <th scope="row">임원 / 직원 보수 비율</th>
            <td>score1</td>
        </tr>
        <tr>
            <th scope="row">배당 성향</th>
            <td>score1</td>
        </tr>
    </tbody>
    </table>
    </div>
</template>

<script>
export default {
    name: 'Top',
    
}
</script>

<style scoped>
.align {
    justify-content:space-around
}

</style>