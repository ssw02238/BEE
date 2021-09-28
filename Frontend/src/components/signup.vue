<template>
<transition name="modal2">
        <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-container">

              <div class="modal-header">
                <slot name="header">
                  default header
                </slot>
              </div>

              <div class="modal-body">
                <slot name="body">
                  <form>
                    <div class="mb-3">
                      <label for="exampleInputEmail1" class="form-label">Email Id</label>
                      <input type="email" class="form-control" id="exampleInputEmail1" v-model="credentials.email" placeholder="name@example.com">
                    </div>
                    <div class="mb-3">
                      <label for="nickname" class="form-label">nickname</label>
                      <input type="text" class="form-control" id="nickname" v-model="credentials.nickname">
                    </div>
                    <div class="mb-3">
                      <label for="exampleInputPassword1" class="form-label">Password</label>
                      <input type="password" class="form-control" id="exampleInputPassword1" v-model="credentials.password">
                    </div>
                    <div class="mb-3">
                      <label for="passwordConfirmation" class="form-label">Password 확인</label>
                      <input type="password" class="form-control" id="passwordConfirmation" v-model="credentials.password_confirmation">
                    </div>
                  </form>
                </slot>
              </div>

              <div class="modal-footer">
                <slot name="footer">
                  <button type="submit" class="btn btn-warning" @click="[signup(credentials),$emit('close')]">회원가입</button>
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
  name: 'signup',
  data: function () {
    return {
      credentials: {
        email: null,
        nickname: null,
        password: null,
        password_confirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      })
        .then(res => {
          console.log(res)

          alert('회원가입에 성공하였습니다. 로그인을 진행해주세요')
          this.$router.push({ name: 'main' })
          this.$router.go()
        })
        .catch(err => {
          console.log('axios 오류', err)
        })
    }
  }
}
</script>
<style>
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