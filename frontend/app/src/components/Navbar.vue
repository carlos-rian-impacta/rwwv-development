<template>
	<nav class="navbar nav-tabs navbar-expand-lg border border-danger px-4 py-3 d-flex justify-content-between">
		<div class="navegation">
			<a 
				class="navbar-brand" 
				@click="$router.push('/')"
				href="/"
				data-bs-toggle="tooltip" 
				data-bs-placement="bottom" 
				title="Tela de inicio"
			>
				<i class="bi bi-house-fill"></i>
				Inicio
			</a>

			<a 
				class="navbar-brand" 
				@click="$router.push('/funcionario')"
				href="/funcionario"
				data-bs-toggle="tooltip" 
				data-bs-placement="bottom" 
				title="Tela de funcionários"
			>
				<i class="bi bi-people-fill"></i>
				Funcionários
			</a>

			<a 
				class="navbar-brand" 
				@click="$router.push('/bu')"
				href="/bu"
				data-bs-toggle="tooltip" 
				data-bs-placement="bottom" 
				title="Tela de BUs"
			>
				<i class="bi bi-briefcase-fill"></i>
				BUs
			</a>

			<a 
				class="navbar-brand" 
				@click="$router.push('/orcamento')"
				href="/orcamento"
				data-bs-toggle="tooltip" 
				data-bs-placement="bottom" 
				title="Tela de orçamentos"
			>
				<i class="bi bi-cash-stack"></i>
				Orçamentos
			</a>

		</div>
		<div class="user">
			<a 
				class="navbar-brand"
			>
				<i class="bi bi-person-circle"></i>
				{{ user.user ? user.user.first_name : 'Usuário' }}
			</a>

			<a v-show="user.user && user.user.first_name != 'Usuário'" class="navbar-brand" @click="exit" href="#">
				<i class="bi bi-box-arrow-right"></i>
				Sair do sistema
			</a>

		</div>
	</nav>
</template>

<script>
import redirectToLogin from '../js/redirectLogin'
export default {
    name: 'Navbar',
	methods: {
		default: function () {
			this.user = {
				"user": {
					"first_name": "Usuário",
					"last_name": "",
					"active": true
				},
				"role": {
					"is_admin": false,
					"can_simulate_budget": false,
					"can_submit_budget": false,
					"can_approve_budget": false,
					"can_read_budget": false
				}
			}
			this.logged = false
		},
		exit () {
			localStorage.removeItem("access_token")
			localStorage.removeItem("refresh_token")
			this.user.user.first_name = 'Usuário'
			console.log("removendo token")
			window.location.href = "/login"
			console.log("redicionando")
		}
	},
	props: {
		user: {
			type: Object,
			default: {
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
			}
		},
		logged: {
			type: Boolean,
			default: false
		}
	}
}
</script>

<style scoped>
.bi {
	font-size: 28px;
}
.navbar {
  background-color: #dc3545;
}
.navbar-brand {
	color: white;
	padding: 5px; 
	border: #dc3545 solid 1px;
	border-radius: 7px;
}

.navbar-brand:hover, 
.navbar-brand:focus, 
.navbar-brand:active, 
.open .dropdown-toggle.navbar-brand {  
 background-color: #d04f5c; 
 border: white solid 1px;
} 

.disabled-link {
  pointer-events: none;
}

</style>