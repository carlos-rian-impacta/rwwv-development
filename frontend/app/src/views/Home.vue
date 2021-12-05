<template>
  <div class="home d-flex justify-content-around">
    <div class="shadow card text-center rounded" style="width: 30%">
      <div class="card-header text-white bg-dark">
        Funcionários
      </div>
      <div class="card-body">
        <h5 class="card-title">Sobre Funcionários</h5>
        <p class="card-text">
          Nessa página você pode realizar o controle dos funcionários que usam o sistema.<br>
          Por meio da mesma você pode alterar permisssões, ativar e desativar, criar usuários etc.
        </p>
      </div>
      <div class="card-footer text-muted">
        <a href="/funcionario" class="btn btn-primary">Acessar</a>
      </div>
    </div>

    <div class="shadow card text-center" style="width: 30%">
      <div class="card-header text-white bg-dark">
        BUs (Unidade de Negócio)
      </div>
      <div class="card-body">
        <h5 class="card-title">Sobre BU</h5>
        <p class="card-text">
          BU ou Unidade de negócio em Português, são áreas/subdivisões que um Gerente de área (GA) é responsável.<br>
          Uma BU pode ter uma ou mais famílias de produtos.
        </p>
      </div>
      <div class="card-footer text-muted">
        <a href="/bu" class="btn btn-primary">Acessar</a>
      </div>
    </div>

    <div class="shadow card text-center" style="width: 30%">
      <div class="card-header text-white bg-dark">
        Orçamentos
      </div>
      <div class="card-body">
        <h5 class="card-title">Sobre Orçamentos</h5>
        <p class="card-text">
          Na página de orçamento você pode gerenciar e simular orçamentos.
        </p>
      </div>
      <div class="card-footer text-muted">
        <a href="/orcamento" class="btn btn-primary">Acessar</a>
      </div>
    </div>

  </div>
</template>

<script>
import checkLogin from '../js/checkLogin.js'
import redirectToLogin from '../js/redirectLogin'

export default {
  name: 'Home',
  data () {
    return {
      user: {
        first_name: "Usuário",
        last_name: "",
        active: true
      },
      role: {
        is_admin: false,
        can_simulate_budget: false,
        can_submit_budget: false,
        can_approve_budget: false,
        can_read_budget: false
      }
    }
  },
  async mounted (){
    try {
      const data = await checkLogin()
      if(!data){
        console.log("USER DOES NOT EXISTS.")
        redirectToLogin(this)
      } 
    } catch (error) {
      console.log("REQUEST ERROR")
      redirectToLogin(this)
    }
  }
}
</script>
