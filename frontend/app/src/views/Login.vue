<template>
  <div>
    <div id="div-login">
      <form id="form-login" class="row g-3" @submit="onSubmit" @reset="onReset">
        <div
          v-show="showDismissibleAlert"
          class="alert alert-danger alert-dismissible fade show"
          role="alert"
        >
          <strong>E-mail</strong> ou <strong>Senha</strong> invalido.
        </div>
        <div class="text-center">
          <img
            src="https://www.taimin.com.br/images/brand.png?2"
            class="rounded"
            alt="logo"
          />
        </div>
        <!--EMAIL-->
        <div class="col-12">
          <label for="email" class="form-label"> E-mail </label>
          <input
            id="email"
            v-model="form.localEmail"
            type="email"
            class="form-control"
            placeholder="seuemail@taimin.com.br"
          />
        </div>
        <!--PASSWORD-->
        <div class="col-12">
          <label for="password" class="form-label"> Senha </label>
          <input
            id="password"
            v-model="form.localPassword"
            :type="type_password"
            class="form-control"
            placeholder="senha"
          />
        </div>
        <!--CHECK-->
        <div class="col-12">
          <div class="form-check">
            <input
              type="checkbox"
              id="showPass"
              class="form-check-input"
              @click="changePasswordType"
            />
            <label class="form-check-label" for="showPass">
              Mostrar senha
            </label>
          </div>
        </div>
        <div id="button-login" class="col-12">
          <DefaultButton buttonText="Acessar" />
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import login from "../js/login.js";
import checkLogin from "../js/checkLogin.js";
import DefaultButton from "../components/DefaultButton.vue";

export default {
  name: "Login",
  components: {
    DefaultButton,
  },
  data() {
    return {
      type_password: "password",
      showDismissibleAlert: false,
      form: {
        localEmail: "",
        localPassword: "",
      },
    };
  },
  methods: {
    changePasswordType: function (event) {
      this.type_password =
        this.type_password == "password" ? "text" : "password";
    },
    redirectToHome: function () {
      console.log("REDIRECT TO HOME");
      window.location.href = "/"
      // this.$router.push({
      //   name: "Home",
      //   path: "/",
      // });
    },
    onReset: function (event) {
      event.preventDefault();
      this.form.localEmail = "";
      this.form.localPassword = "";
    },
    onSubmit: async function (event) {
      event.preventDefault();
      console.log("VALIDANTE USER");
      const data = {
        email: this.form.localEmail,
        password: this.form.localPassword,
      };
      const resp = await login(data);
      if (resp) {
        this.showDismissibleAlert = false;
        this.redirectToHome();
      } else {
        this.showDismissibleAlert = true;
      }
    },
  },
  async mounted() {
    try {
      const data = await checkLogin();
      if (data) {
        this.$router.push({
          name: "Home",
          path: "/",
        });
      }
    } catch (error) {
      console.log("REQUEST ERROR");
    }
  },
};
</script>

<style scoped>
.div-body {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  align-content: center;
}

#form-login {
  display: flex;
  align-items: center;
  width: 550px;
  min-height: 250px;
  border: 2px solid #dc3545;
  border-radius: 7pt;
  padding: 20px;
}
#button-login {
  display: flex;
  justify-content: center;
}
</style>