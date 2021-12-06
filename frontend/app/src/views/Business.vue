<template>
	<div class="container-fluid p-1 pe-2">
    <DefaultTitle 
      id="header-budget"
      titleText="Business Unit (Unidade de Negócio)" 
      titleIcon="bi-briefcase-fill"
    />
    
    <form class="row g-0 p-3 px-4 d-flex justify-content-center" @submit="onSubmit">
      <AlertMessage 
        :alertShow="control.events.alerts.form.successShow"  
        :alertText="control.events.alerts.form.successText" 
        alertType="alert-success"/>
      <AlertMessage  
        :alertShow="control.events.alerts.form.errorShow"
        :alertText="control.events.alerts.form.errorText" 
        alertType="alert-danger"/>

      <h5 class="card-title pb-0 pt-0">Dados</h5>
      <div class="fields row shadow border border-1 rounded p-4">
        <div class="min-len col-12" :class="field_required ? 'required' : ''">
          <label for="name" class="form-label">Nome</label>
          <input
            :disabled="disableForm"
            id="name"
            v-model="bu.name"
            :class="borders.name"
            type="text"
            class="form-control"
            placeholder="ARTROSCOPIA"
          />
          <div class="invalid-feedback">
            O nome da BU deve ter pelo menos 5 caracteres.
          </div>
        </div>

        <div class="min-len col-12" :class="field_required ? 'required' : ''">
          <label for="product_family" class="form-label">Família de Produto</label>
          <input
            :disabled="disableForm"
            id="product_family"
            v-model="bu.product_family"
            :class="borders.product_family"
            type="text"
            class="form-control"
            placeholder="CAIXA DE OTICA"
          />
          <div class="invalid-feedback">
            A família de produto deve ter pelo menos 5 caracteres.
          </div>
        </div>

        <div class="col-12">
          <label for="description" class="form-label">Descrição</label>
          <input
            :disabled="disableForm"
            id="description"
            v-model="bu.description"
            type="text"
            class="form-control"
            placeholder="Caixa usada para... "
          />
        </div>
      </div>

      <div class="buttons mt-4 d-flex flex-row p-0">
        <DefaultButton 
          class="action-button me-3" 
          buttonText="Novo" 
          @click="onNew" 
          :buttonActive="control.buttons.new" 
          buttonColor="btn btn-primary" 
          buttonIcon="bi bi-plus-circle-fill" 
          buttonType="button"/>
        <DefaultButton 
          buttonType="submit"
          class="action-button me-3" 
          buttonText="Salvar" 
          v-scroll-to="'#header-budget'"
          :buttonActive="control.buttons.save" 
          buttonColor="btn btn-success" 
          buttonIcon="bi bi-check-circle-fill"/>
        <DefaultButton 
          class="action-button me-3" 
          buttonText="Alterar"
          @click="onChange"
          :buttonActive="control.buttons.edit" 
          buttonColor="btn btn-dark" 
          buttonIcon="bi-arrow-up-circle-fill" 
          buttonType="button" />
        <DefaultButton 
          class="action-button me-3" 
          buttonText="Cancelar" 
          @click="onReset" 
          buttonColor="btn btn-danger" 
          buttonIcon="bi-x-circle-fill" 
          buttonType="reset"/>
      </div>
    </form>


    <div id="bu-table" class="table-func d-flex row g-0 px-4 border border-danger rounded p-3 mt-1 px-4">

      <AlertMessage 
        :alertShow="control.events.alerts.table.successShow"  
        :alertText="control.events.alerts.table.successText" 
        alertType="alert-success"/>
      <AlertMessage  
        :alertShow="control.events.alerts.table.errorShow"
        :alertText="control.events.alerts.table.errorText" 
        alertType="alert-danger"/>

      <h5 class="card-title">Listagem de BUs</h5>
      <table class="table table-bordered shadow shadow">
        <thead class="table table-dark border border-white">
          <tr class="border border-secondary">
            <th scope="col">Nome</th>
            <th scope="col">Família de Produto</th>
            <th scope="col">Descrição</th>
            <th scope="col">Criado</th>
            <th scope="col">Atualizado</th>
            <th scope="col">Ações</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="bu in bus" :key="bu.id">
            <td >{{ bu.name }}</td>
            <td >{{ bu.product_family }}</td>
            <td >{{ bu.description }}</td>
            <td >{{ new Date(bu.created_at).toLocaleString('pt-BR') }}</td>
            <td >{{ new Date(bu.updated_at).toLocaleString('pt-BR') }}</td>
            <td style="max-width: 100px;">
              <button @click="loadBu(bu.id)" type="button" class="btn btn-primary btn-sm me-3"><i class="bi bi-eye-fill"></i></button>
              <button @click="removeBu(bu.id)" v-scroll-to="'#bu-table'" type="button" class="btn btn-danger btn-sm" ><i class="far fa-trash-alt"></i></button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
	</div>
</template>

<script>
import checkLogin from '../js/checkLogin.js'
import redirectToLogin from "../js/redirectLogin";
import DefaultButton from "../components/DefaultButton.vue";
import DefaultTitle from "../components/DefaultTitle.vue";
import AlertMessage from "../components/AlertMessage.vue";
import BU from '../services/bu.js'

export default {
	name: 'Business',
  components: {
    DefaultButton,
    DefaultTitle,
    AlertMessage
  },
	props:{
    employeeId: {
      type: String,
      require: true
    }
  },
	methods: {
		listBus (id) {
			BU.listBu(id)
      .then((resp) => {
        console.log(resp.data)
        this.bus = resp.data.business
      }).catch((err) => {
        console.log(err.request)
        console.log(err.response)
      });
		},
    removeBu (id) {
      if (confirm("Você tem certeza que deseja excluir a BU?")) {
        BU.removeBu(id)
        .then( (resp) => {
          this.control.events.alerts.table.successShow = true
          this.control.events.alerts.table.successText = 'BU removida com sucesso'
          this.listBus(this.localEmployeeId)
          this.disableAlertTable()
        }).catch ((err) => {
          console.log(err.response.data)
          this.control.events.alerts.table.errorShow = true
          if (err.response.status != 422) {
            this.control.events.alerts.table.errorText = err.response.data.detail
          }else {
            this.control.events.alerts.table.errorText = 'Erro ao remover a BU.'
          }
          this.disableAlertTable()
        })
      }
    },
    loadBu (id) {
      this.bus.forEach(element => {
        if (element.id == id) {
          const data = {...element}
          this.bu = data
          this.control.buttons.new = true
          this.control.buttons.save = true
          this.control.buttons.edit = false
          this.disableForm = false
          this.localEmployeeId = element.employee_id
          console.log(data)
          return
        }
      });
    },
    onReset (event) {
      this.disableForm = true
      this.bu.id = ''
      this.bu.name = ''
      this.bu.product_family = ''
      this.bu.description = ''

      this.control.buttons.new = false
      this.control.buttons.save = true
      this.control.buttons.edit = true
      this.validation.name = false
      this.validation.product_family = false
      
      this.borders.name = ''
      this.borders.product_family = ''
    },
    onNew (event) {
      this.disableForm = false
      this.bu.id = ''
      this.bu.name = ''
      this.bu.product_family = ''
      this.bu.description = ''

      this.control.buttons.new = true
      this.control.buttons.save = false
      this.control.buttons.edit = true
      this.validation.name = false
      this.validation.product_family = false
      
      this.borders.name = ''
      this.borders.product_family = ''
    },
    onSubmit(event) {
      event.preventDefault();
      if (!this.validation.name || !this.validation.product_family) {
        this.control.events.alerts.form.errorShow = true
        this.control.events.alerts.form.errorText = 'Verifique se todos os campos requeridos estão preenchidos corretamente.'
        this.disableAlertForm()
        return  
      }

      const data = {...this.bu}
      data.employee_id = this.localEmployeeId
      BU.createBu(data)
        .then( (resp) => {
          this.listBus(this.localEmployeeId)
          this.onReset()
          this.control.events.alerts.form.successShow = true
          this.control.events.alerts.form.successText = 'BU adicionada com sucesso.'
          this.disableAlertForm()
        }).catch( (err) => {
          this.control.events.alerts.form.errorShow = true
          if (err.response.status != 422){
            this.control.events.alerts.form.errorText = err.response.data.detail
          }else {
            his.control.events.alerts.form.errorText = 'Erro ao inserir a nova BU. Por favor, cheque os campos e tente novamente.'
          }
          this.disableAlertForm()
        })
    },
    onChange(event) {
      if (!this.validation.name || !this.validation.product_family) {
        this.control.events.alerts.form.errorShow = true
        this.control.events.alerts.form.errorText = "Verifique se todos os campos requeridos foram preenchidos corretamente."
        this.disableAlertForm()
        return
      }
      event.preventDefault();
      const data = {...this.bu}
      data.employee_id = this.localEmployeeId
      console.log(data)
      if (confirm('Você tem certeza que deseja alterar?')) {
        BU.changeBu(this.bu.id, data)
          .then( (resp) => {
            console.log(resp.data)
            this.listBus(this.localEmployeeId)

            this.onReset()

            this.control.events.alerts.form.successShow = true
            this.control.events.alerts.form.successText = 'BU alterada com sucesso.'
            this.disableAlertForm()
          }).catch( (err) => {
            console.log(err.response.data)
            this.control.events.alerts.form.errorShow = true
            if (err.response.status != 422) {
              this.control.events.alerts.form.errorText = err.response.data.detail
            }else {
              this.control.events.alerts.form.errorText = 'Error ao alterar a BU.'
            }
            this.disableAlertForm()
          })
      }
    },
    disableAlertForm () {
      setTimeout( () => {
        this.control.events.alerts.form.successShow = false
        this.control.events.alerts.form.successText = ''
        this.control.events.alerts.form.errorShow = false
        this.control.events.alerts.form.errorText = ''
      }, 15000)
    },
    disableAlertTable () {
      setTimeout( () => {    
        this.control.events.alerts.table.successShow = false
        this.control.events.alerts.table.successText = ''
        this.control.events.alerts.table.errorShow = false
        this.control.events.alerts.table.errorText = ''
      }, 15000)
    },
    changeBorder(value, key) {
      if (value.length >= 5) {
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
    'bu.name' (v) {
      this.changeBorder(v, 'name')
    },
    'bu.product_family' (v) {
      this.changeBorder(v, 'product_family')
    },
  },
	data () {
		return {
      localEmployeeId: '',
      bus: [],
      bu: {
        id: '',
        name: '',
        product_family: '',
        description: ''
      },
      validation: {
        name: false,
        product_family: false,
      },
      borders: {
        name: "",
        product_family: ""
      },
      control: {
        events: {
          alerts: {
            form: {
              successShow: false,
              successText: '',
              errorShow: false,
              errorText:''
            },
            table: {
              successShow: false,
              successText: '',
              errorShow: false,
              errorText:''
            }
          }
        },
        buttons: {
          new: false,
          save: true,
          edit: true,
        }
      },
      disableForm: true,
      field_required: true
    }
	},
  async mounted() {
    if (this.employeeId !== undefined) {
      this.listBus(this.employeeId)
      this.localEmployeeId = this.employeeId
    }else {
      const me = await checkLogin()
      this.listBus(me.user.id)
      this.localEmployeeId = me.user.id
    }
  }
}
</script>

<style scoped>
.table-func, form, .container {
  min-width: 100%;
}
th, tr{
  text-align: center;
}
.min-len {
  width: 50%;
}
.col-12 {
  padding: 5px 3px 5px 3px;
}

form {
  border-bottom: red solid 1px;
  border-left: red solid 1px;
  border-right: red solid 1px;
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 4px;
}

</style>>
