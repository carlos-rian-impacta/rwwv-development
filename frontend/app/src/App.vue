<template>
  <div class="div-main">
    <Navbar :user="user" :logged="logged"/>
    <router-view class="div-body shadow" />
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
import checkLogin from "./js/checkLogin.js";
import Navbar from "./components/Navbar.vue";

export default {
  components: {
    Navbar,
  },
  methods: {
    redirectToLogin: function () {
      console.log("REDIRECT TO LOGIN");
      this.$router.push("/login");
    },
  },
  data() {
    return {
      user: {
				"user": {
					"first_name": "Usuário",
					"last_name": "",
					"active": false
				},
				"role": {
					"is_admin": false,
					"can_simulate_budget": false,
					"can_submit_budget": false,
					"can_approve_budget": false,
					"can_read_budget": false
				}
			},
      logged: false
    };
  },
  mounted() {
      checkLogin().then( data => {
        if (!data) {
          console.log("USER DOES NOT EXISTS.");
          this.redirectToLogin();

        } else {
          this.user = data
          this.logged = true
          this.i += 1
        }
      }).catch(error => {
        console.log("REQUEST ERROR");
        this.redirectToLogin();
      })
  },
};
</script> 

<style scoped>
.div-body {
  margin: 5px 3px !important;
  padding: 20px;
  min-height: calc(100vh - 75px);
  min-width: 100vh;
  bottom: 0;
  
	display: flex;
	flex-direction: row;
	flex-wrap: wrap;
	justify-content: flex-start;
	align-items: stretch;
	align-content: flex-start;
}
</style>
<style>
.col-12.required .form-label:after {
  content:"*";color:red;
}
table {
  border-collapse: collapse;
  border-radius: 7px;
  overflow: hidden;
}
th {
  text-align: center;
}
</style>