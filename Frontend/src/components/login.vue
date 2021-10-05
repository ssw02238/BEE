<template>
<transition name="modal">
        <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-container">

              <div class="modal-header">
                <slot name="header">
                </slot>
              </div>

              <div class="modal-body">
                <slot name="body">
                  <form>
                    <div class="mb-3 form-text">
                      <label for="exampleInputEmail1" class="form-label"> Email id</label>
                      <input type="id" class="form-control" id="idInput" v-model="credentials.email" placeholder="name@example.com">
                    </div>
                    <div class="mb-3">
                      <label for="exampleInputPassword1" class="form-label">Password</label>
                      <input type="password" class="form-control" id="exampleInputPassword1" v-model="credentials.password">
                    </div>
                  </form>
                </slot>
              </div>

              <div class="modal-footer">
                <slot name="footer">
                  <button type="submit" class="btn btn-warning" @click="[$emit('close'), login(credentials)]">로그인</button>
                  <button type="submit" class="btn btn-danger" @click="[$emit('close')]">취소</button>
                </slot>
              </div>
            </div>
          </div>
        </div>
      </transition>
</template>

<script>
import axios from 'axios'
export default {
  name: 'login',
  data: function() {
    return {
      credentials: {
        email: null, 
        password: null,
      }
    }
  },
  methods: {
    setToken: function () {
      const jwtToken = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${jwtToken}`
      }
      return config 
    },
    login: function () {
      console.log('login 확인')
      axios({
        method:'post',
        url:'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials
      })
      .then(res => {
        console.log('결과', res)
        localStorage.setItem('jwt', res.data.token)
        this.$emit('login')
      })
      .then(res => {
        console.log(res)
        axios({
          method:'get',
          url: 'http://127.0.0.1:8000/accounts/profile/',
          headers: this.setToken()
        })
      .then(res => {
        console.log('닉네임 받기', res.data)
        localStorage.setItem('uid', res.data.id)
        localStorage.setItem('nickname', res.data.nickname)
        localStorage.setItem('email', res.data.email)
        // 스크랩 리스트 넣기 (기업 디테일 페이지 이동 시 스크랩 분기 처리를 위해)
        this.$router.push({ name: 'main'})
        this.$router.go()
       })
      })
      .catch(err => {
        this.$router.push({ name: 'signup'})
        console.log('회원가입으로 이동')
        console.log(err)
      })
    }
  }
};
</script>
<style scoped>
.form-text {
  text-align: center;
}
.form-label {
  color:black;
  display: flex;
}
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
.modal-body,
.modal {
  color:#666 !important
}
</style>