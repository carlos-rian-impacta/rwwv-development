<template>

  <div id="local-main" class="container-fluid p-1 pe-2">
    <DefaultTitle 
      titleText="Funcionários" 
      titleIcon="bi-people-fill"
    />
    
    <form class="row g-0 p-3 px-4" @submit="onSubmit">
      <AlertMessage :alertShow="disableAlert" v-for="al in alertList" :key="al" :alertText="al" alertType="alert-danger"/>
      <AlertMessage :alertShow="successAlert" :alertText="successMessage" alertType="alert-success"/>

      <h5 class="card-title pb-0 pt-0">Dados</h5>
      <div class="fields shadow border border-1 rounded p-4">
        <div class="col-12 required">
          <label for="email" class="form-label">E-mail</label>
          <input
            :disabled="disableForm"
            id="email"
            v-model="employee.email"
            :class="borders.email"
            type="email"
            class="form-control"
            placeholder="seuemail@taimin.com.br"
          />
          <div class="invalid-feedback">
            O email deve ser um email da taimin, ou seja, @taimin.com.br!
          </div>
        </div>

        <div class="col-12" :class="buttonUpdateDisable ? 'required' : ''">
          <label for="password" class="form-label">Senha</label>
          <input
            :disabled="disableForm"
            id="password"
            v-model="employee.password"
            :class="borders.password"
            type="password"
            class="form-control"
            placeholder="Senha"
          />
          <div class="invalid-feedback">
            A senha precisa ter pelo menos 8 caracteres contendo 1 caracter especial, 1 número e 1 letra maiúscula.
          </div>
        </div>

        <div class="col-12">
          <label for="first_name" class="form-label">Nome</label>
          <input
            :disabled="disableForm"
            id="first_name"
            v-model="employee.first_name"
            type="text"
            class="form-control"
            placeholder="Ex: Pedro"
          />
        </div>

        <div class="col-12">
          <label for="last_name" class="form-label">Sobrenome</label>
          <input
            :disabled="disableForm"
            id="last_name"
            v-model="employee.last_name"
            type="text"
            class="form-control"
            placeholder="Ex: Silva"
          />
        </div>

        <div id="div-min-len" class="col-12 required">
          <label for="position" class="form-label">Cargo</label>
          <select
            :disabled="disableForm"
            v-model="employee.position"
            class="form-select"
            aria-label="Selecione o cargo."
            :class="borders.position"
            required
          >
            <option :selected="employee.position"> {{ employee.position }} </option>
            <!-- posi.key !== 'analyst' -->
            <option v-for="pos in position.filter((posi) => posi.value !== employee.position )" :key="pos.key" :value="pos.value">{{ pos.value}}</option>
          </select>
        </div>

        <div id="div-min-len" class="col-12">
          <label for="birth_date" class="form-label">Data de nascimento</label>
          <v-date-picker v-model="employee.birth_date" locale="pt-BR">
            <template v-slot="{ inputValue, inputEvents }">
              <input
                class="form-control"
                :disabled="disableForm"
                :value="inputValue"
                v-on="inputEvents"
              />
            </template>
          </v-date-picker>
        </div>
      </div>
      <h5 class="card-title pb-0 pt-4">Permissões</h5>
      <div class="checks d-flex flex-row shadow border border-1 rounded p-2">
        <div class="form-check form-switch">
          <label for="active" class="form-label">Ativo</label>
          <input
            id="active"
            :disabled="disableForm"
            v-model="employee.active"
            type="checkbox"
            class="form-check-input"
          />
        </div>
        <div class="form-check form-switch">
          <label for="is_admin" class="form-label">Administrador</label>
          <input
            id="is_admin"
            :disabled="disableForm"
            v-model="employee.is_admin"
            type="checkbox"
            class="form-check-input"
          />
        </div>
        <div class="form-check form-switch">
          <label for="can_simulate_budget" class="form-label">Simular Orçamento</label>
          <input
            id="can_simulate_budget"
            :disabled="disableForm"
            v-model="employee.can_simulate_budget"
            type="checkbox"
            class="form-check-input"
          />
        </div>
        <div class="form-check form-switch">
          <label for="can_submit_budget" class="form-label">Criar Orçamento</label>
          <input
            id="can_submit_budget"
            :disabled="disableForm"
            v-model="employee.can_submit_budget"
            type="checkbox"
            class="form-check-input"
          />
        </div>
        <div class="form-check form-switch">
          <label for="can_approve_budget" class="form-label">Aprovar Orçamento</label>
          <input
            id="can_approve_budget"
            :disabled="disableForm"
            v-model="employee.can_approve_budget"
            type="checkbox"
            class="form-check-input"
          />
        </div>
        <div class="form-check form-switch">
          <label for="can_read_budget" class="form-label">Ver Orçamento</label>
          <input
            id="can_read_budget"
            :disabled="disableForm"
            v-model="employee.can_read_budget"
            type="checkbox"
            class="form-check-input"
          />
        </div>
      </div>

      <div class="buttons mt-4 d-flex flex-row p-0">
        <DefaultButton class="action-button me-3" buttonText="Novo" @click="enableForm" :buttonActive="buttonNewDisable" buttonColor="btn btn-primary" buttonIcon="bi bi-plus-circle-fill" buttonType="button"/>
        <DefaultButton class="action-button me-3" buttonText="Salvar" :buttonActive="buttonCreateDisable" buttonColor="btn btn-success" buttonIcon="bi bi-check-circle-fill"/>
        <DefaultButton class="action-button me-3" buttonText="Alterar" @click="changeEmployee" :buttonActive="buttonUpdateDisable" buttonColor="btn btn-dark" buttonIcon="bi-arrow-up-circle-fill" buttonType="button" />
        <DefaultButton class="action-button me-3" buttonText="Cancelar" @click="onReset" buttonColor="btn btn-danger" buttonIcon="bi-x-circle-fill" buttonType="reset"/>
      </div>
    </form>

    <div class="table-func d-flex row g-0 border border-danger rounded p-3 mt-1 px-4">
      <AlertMessage :alertShow="removeAlert" :alertText="removeMessage" alertType="alert-success"/>
      <AlertMessage :alertShow="removeAlertError" :alertText="removeMessageError" alertType="alert-danger"/>
      <h5 class="card-title">Listagem de Funcionários</h5>
      <table class="table table-bordered shadow">
        <thead class="table table-dark border border-white">
          <tr class="border border-secondary">
            <th scope="col">E-mail</th>
            <th scope="col">Cargo</th>
            <th scope="col">Nome</th>
            <th scope="col">Ativo</th>
            <th scope="col">Administrador</th>
            <th scope="col">Simular</th>
            <th scope="col">Criar</th>
            <th scope="col">Aprovar</th>
            <th scope="col">Ver</th>
            <th scope="col" style="width: 100px;">Ação</th>
            <th scope="col" style="width: 100px;">BUs</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="empl in employees" :key="empl.id">
            <td >{{ empl.email }}</td>
            <td >{{ position_pt[empl.position] }}</td>
            <td >{{ empl.first_name }} {{ empl.last_name }}</td>
            <td class="active"><i :class="isActive(empl.active)" style="font-size: 1.2rem; color: cornflowerblue;" ></i> </td>
            <td class="active"><i :class="isActive(empl.can_simulate_budget)" style="font-size: 1.2rem; color: cornflowerblue;" ></i> </td>
            <td class="active"><i :class="isActive(empl.can_submit_budget)" style="font-size: 1.2rem; color: cornflowerblue;" ></i> </td>
            <td class="active"><i :class="isActive(empl.can_approve_budget)" style="font-size: 1.2rem; color: cornflowerblue;" ></i> </td>
            <td class="active"><i :class="isActive(empl.can_read_budget)" style="font-size: 1.2rem; color: cornflowerblue;" ></i> </td>
            <td class="active"><i :class="isActive(empl.is_admin)" style="font-size: 1.2rem; color: cornflowerblue;" ></i> </td>
            <td class="d-flex flex-row justify-content-around" style="max-width: 100px;">
              <button 
                @click="loadEmployee(empl.id)" 
                v-scroll-to="'#local-main'" 
                type="button" 
                class="btn btn-primary btn-sm m-0"
                data-bs-toggle="tooltip" 
                data-bs-placement="left" 
                title="Ver dados do funcionário"
                ><i class="bi bi-eye-fill"></i>
              </button>
              <button 
                @click="removeEmployee(empl.id)" 
                type="button" 
                class="btn btn-danger btn-sm m-0"
                data-bs-toggle="tooltip" 
                data-bs-placement="left" 
                title="Excluir funcionário"
              ><i class="far fa-trash-alt"></i></button>
            </td>
            <td style="max-width: 100px; text-align: center;">
              <button
                @click="redirectToBu(empl.id)"
                type="button" 
                class="btn btn-success btn-sm m-0"
                data-bs-toggle="tooltip" 
                data-bs-placement="left" 
                title="Ver BUs"
              ><i class="bi bi-arrow-up-right-square-fill"></i>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

  </div>
  <!-- <DefaultTemplate v-else/> -->
</template>

<script>
import checkLogin from "../js/checkLogin.js";
import redirectToLogin from "../js/redirectLogin";
import DefaultButton from "../components/DefaultButton.vue";
import DefaultTitle from "../components/DefaultTitle.vue";
import AlertMessage from "../components/AlertMessage.vue";
import DefaultTemplate from "../components/NotAccessable.vue";
import Employee from '../services/employee.js'

const positionData = {
  list: [
    {key: "analyst", value: "Analista"},
    {key: "manager", value: "Gerente"},
    {key: "director", value: "Diretor"},
  ],
  pt: {
    Analista: "analyst",
    Gerente: "manager",
    Diretor: "director",
  },
  en: {
    analyst: "Analista",
    manager: "Gerente",
    director: "Diretor",
  }
}
const alertMsg = {
  email: 'Email invalido, o e-mail precisa ter "@taimin.com.br".',
  password: 'A senha precisa ter mais de 8 caracteres com no minimo 1 letra maiúscula, 1 número e 1 caracter especial.',
  first_name: 'Nome invalido.',
  last_name: 'Sobrenome invalido.',
  birth_date: 'Data de nascimento invalida.',
  position: 'Somente os cargos de Analista, Gerente e Diretor são aceitos.'
}

export default {
  name: "Employee",
  components: {
    DefaultButton,
    DefaultTitle,
    AlertMessage,
    DefaultTemplate
  },
  methods: {
    isActive(value) {
      return value ? 'bi bi-check-circle-fill':'bi bi-check-circle'
    },
    loadEmployee(id) {
      this.buttonUpdateDisable = false
      this.employees.forEach(element => {
        if (element.id == id) {
          const data = {...element}
          console.log(data)
          data.position = positionData.en[data.position]
          
          this.employee = data
          this.disableForm = false
          this.buttonNewDisable = true
          this.buttonCreateDisable = true
          return
        }
      });
    },
    listEmployee() {
      Employee.listEmployee().then((resp) => {
          this.employees = resp.data
        }).catch((err) => {
          console.log("ERROR LIST EMPLOYEES")
        })
    },
    createEmployee() {
      if (!this.validation.email || !this.validation.password || !this.validation.position) {
        this.alertList = ['Verifique se todos os campos requeridos foram preenchidos corretamente.']
        this.disableAlert = true
            setTimeout(() => {
              this.alertList = []
              this.disableAlert = false
            }, 15000)
        return
      }
      if (confirm("Tem certeza que deseja adicionar o funcionário?")){
        const data = {...this.employee}
        console.log(data)
        data.position = positionData.pt[data.position]
        data.birth_date = data.birth_date.toISOString().split('T')[0]
        console.log(data)
        
        Employee.createEmployee(data)
          .then((resp) => {
            this.listEmployee()
            this.onReset()
            this.successMessage = 'Funcionário adicionado com sucesso.'
            this.successAlert = true
            setTimeout(() => {
              this.successMessage = ''
              this.successAlert = false
            }, 10000)
          }).catch((err) => {
            if (err.response.status == 422) {
              console.log(err.response.data)
              this.alertList = err.response.data.detail.map((d) => {
                const key = d.loc.slice(-1)[0]
                return alertMsg[key]
              })
            }else if (err.response.status == 400) {
              this.alertList = ['O e-mail informado já existe.']
            }
            this.disableAlert = true
            setTimeout(() => {
              this.alertList = []
              this.disableAlert = false
            }, 10000)
          })
      }
    },
    removeEmployee(id) {
      if (confirm("Você tem certeza?")){
        Employee.removeEmployee(id)
          .then(() => {
            console.log("REMOVE EMPLOYEE.")
            this.removeAlert = true
            this.removeMessage = 'Funcionário removido com sucess.'
            this.listEmployee()
            setTimeout(() => {
              this.removeMessage = ''
              this.removeAlert = false
            }, 10000)
          }).catch((err) => {
            console.log("DON'T REMOVE EMPLOYEE.")
            if (err.response.status == 400) { 
              this.removeMessageError = 'Problema para remover o funcionário. Há uma ou mais unidades de négocio associada ao mesmo.'
              this.removeAlertError = true
              setTimeout(() => {
                this.removeMessageError = ''
                this.removeAlertError = false
              }, 10000)
            }
            console.log(err.response.data)
          });
      }
      
    },
    changeEmployee() {
      if (!this.validation.email) {
        this.alertList = ['Verifique se todos os campos requeridos foram preenchidos corretamente.']
        this.disableAlert = true
            setTimeout(() => {
              this.alertList = []
              this.disableAlert = false
            }, 10000)
        return
      }
      if (confirm("Tem certeza que deseja alterar o funcionário?")) {
        const data = {...this.employee}
        console.log(data)
        data.position = positionData.pt[data.position]
        try {
          data.birth_date = data.birth_date.toISOString().split('T')[0]
        } catch (error) {
          console.log('Erro ao converter a data.')
        }
        Employee.changeEmployee(data.id, data)
          .then((resp) => {
            this.listEmployee()
            this.onReset()
            this.successMessage = 'Funcionário alterado com sucesso.'
            this.successAlert = true
            setTimeout(() => {
              this.successMessage = ''
              this.successAlert = false
            }, 10000)
          }).catch((err) => {
            console.log(err)
            if (err.response.status == 422) {
              console.log(err.response.data)
              this.alertList = err.response.data.detail.map((d) => {
                const key = d.loc.slice(-1)[0]
                return alertMsg[key]
              })
            }else if (err.response.status == 400) {
              this.alertList = [err.response.data.detail]
            }
            this.disableAlert = true
            setTimeout(() => {
              this.alertList = []
              this.disableAlert = false
            }, 10000)
          })
      }
    },
    onReset(event) {
      this.employee.email = ""
      this.employee.password = ""
      this.employee.first_name = ""
      this.employee.last_name = ""
      this.employee.birth_date = new Date(2000, 1, 1)
      this.employee.position = positionData.en.analyst
      this.employee.active = false
      this.employee.can_simulate_budget = false
      this.employee.can_submit_budget = false
      this.employee.can_approve_budget = false
      this.employee.can_read_budget = false
      this.employee.is_admin = false
      this.buttonUpdateDisable = true
      this.disableForm = true
      this.buttonNewDisable = false
      this.buttonCreateDisable = true
      this.validation.email = false
      this.validation.password = false
      this.validation.position = false
      this.borders.email = ''
      this.borders.password = ''
      this.borders.position = ''
    },
    onSubmit(event) {
      event.preventDefault();
      console.log(this.employee)
      this.createEmployee()
    },
    enableButton() {
      if (this.employee.email != '' && this.employee.password != '' && this.employee.position != '' && this.buttonUpdateDisable) {
        this.buttonCreateDisable = true
      }else {
        this.buttonCreateDisable = false
      }
    },
    enableForm() {
      this.disableForm = false
      this.buttonCreateDisable = false
      this.buttonNewDisable = true
      this.changeBorder(true, 'position')
    },
    redirectToBu(id) {
      this.$router.push(
        { 
          name: 'bu', 
          params: { 
            employeeId: id
          }
        }
      )
    },
    changeBorder(status, key) {
      if (status) {
        this.validation[key] = true
        this.borders[key] = "is-valid";
      } else {
        this.validation[key] = false
        this.borders[key] = "is-invalid";
      }
      if (this.disableForm) {
        this.validation[key] = false
        this.borders[key] = "";
      }
    }
  },
  watch: {
    'employee.email' (v) {
      const r = '^[a-z0-9.]+@taimin\.com\.br'
      console.log(v.match(r))
      this.changeBorder(v.match(r), 'email')
    },
    'employee.password'(v) {
      const r = '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})'
      if (!v) {
        return
      }
      this.changeBorder(v.match(r), 'password')
      console.log(v.match(r))
    },
    'employee.position'(v) {
      this.changeBorder(true, 'position')
    },
  },
  data () {
    return {
      employee: {
        email: "",
        password: "",
        first_name: "",
        last_name: "",
        birth_date: new Date(2000, 1, 1),
        position: positionData.en.analyst,
        active: false,
        can_simulate_budget: false,
        can_submit_budget: false,
        can_approve_budget: false,
        can_read_budget: false,
        is_admin: false,
      },
      permission: {
        is_admin: false
      },
      borders: {
        email: '',
        password: '',
        position: ''
      },
      validation: {
        email: false,
        password: false,
        position: false
      },
      employees: [],
      position: positionData.list,
      position_pt: positionData.en,
      buttonCreateDisable: true,
      buttonUpdateDisable: true,
      buttonNewDisable: false,
      disableForm: true,
      disableAlert: false,
      alertList: [],
      successMessage: '',
      successAlert: false,
      removeAlert: false,
      removeMessage: '',
      removeAlertError: false,
      removeMessageError: ''
    };
  },
  async beforeMount() {
    try {
      const data = await checkLogin();
      if (!data) {
        console.log("USER DOES NOT EXISTS.");
        redirectToLogin(this);
      }
      else {
        if (data.role.is_admin) {
          this.listEmployee()
          this.permission.is_admin = data.role.is_admin
        }
      }
    } catch (error) {
      console.log("REQUEST ERROR");
      redirectToLogin(this);
    }
  },
};
</script>

<style scoped>  
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css");

/* NEW */

/* fields */
.fields {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: baseline;
  align-content: space-around;
}
.col-12 {
  max-width: 50%;
  min-width: 30%;
  padding: 5px 3px 5px 3px;
}

#div-min-len {
  max-width: 15% !important;
  min-width: 5%;
}
.form-check {
  margin: 10px;
  margin-left: 20px;
}
form {
  border-bottom: red solid 1px;
  border-left: red solid 1px;
  border-right: red solid 1px;
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 4px;
}
/* tables */
.table-func, .container {
  min-width: 100%;
}

.active {
  text-align: center;
  width: 100px;
}

th, tr{
  text-align: center;
}

</style>