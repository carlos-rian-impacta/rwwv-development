<template>
  <div class="container-fluid p-1 pe-2">
    <DefaultTitle titleText="Orçamentos" titleIcon="bi-briefcase-fill" />
    <form class="row g-0 p-3 px-4" @submit="onSubmit">
      <AlertMessage
        :alertShow="alerts.form.success"
        :alertText="alerts.form.successText"
        alertType="alert-success"
      />
      <AlertMessage
        :alertShow="alerts.form.error"
        :alertText="alerts.form.errorText"
        alertType="alert-danger"
      />

      <div class="accordion shadow" id="accordionPanelsStayOpenExample">
        <!-- accordion 1 -->
        <div class="accordion-item shadow">
          <h2 class="accordion-header" id="panelsStayOpen-headingOne">
            <button
              class="accordion-button"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#panelsStayOpen-collapseOne"
              aria-expanded="true"
              aria-controls="panelsStayOpen-collapseOne"
              :disabled="control.accordion.bu"
            >
              <i class="bi-plus-square-fill pe-2" style="font-size: 20px"></i>
              Informe nome, status e aprovador
            </button>
          </h2>
          <div
            id="panelsStayOpen-collapseOne"
            class="accordion-collapse collapse"
            :class="accordion.collOne"
            aria-labelledby="panelsStayOpen-headingOne"
          >
            <div class="accor-01 accordion-body" style="width: 100%">
              <div
                class="name status col-12"
                :class="field_required ? 'required' : ''"
              >
                <label for="name" class="form-label">Nome</label>
                <input
                  :disabled="disableFormBudget"
                  id="name"
                  v-model="form.status.name"
                  :class="borders.status_name"
                  type="text"
                  class="form-control"
                  placeholder="Orçamento referente ao ano de 2022"
                  data-bs-toggle="tooltip"
                  data-bs-placement="bottom"
                  title="O nome do status precisa ter pelo menos 5 letras."
                />
                <div class="invalid-feedback">
                  Deve ter pelo menos 5 caracteres e ser um nome único.
                </div>
              </div>

              <div
                class="selected col-12 required"
                :class="field_required ? 'required' : ''"
              >
                <label for="status" class="form-label">Status</label>
                <select
                  id="status"
                  v-model="form.status.status"
                  :class="borders.status"
                  class="form-select"
                  aria-label="Selecione o status"
                  :disabled="disableFormBudget"
                  data-bs-toggle="tooltip"
                  data-bs-placement="bottom"
                  title="Por padrão o status inicia como rascunho."
                  required
                >
                  <option>{{ form.status.status }}</option>
                </select>
                <div class="invalid-feedback">
                  Selecione o aprovador
                </div>
              </div>

              <div class="selected col-12 required">
                <label for="approver" class="form-label">Aprovador</label>
                <select
                  id="approver"
                  v-model="form.bu.approver"
                  :class="borders.approver"
                  class="form-select"
                  aria-label="Selecione o Aprovador"
                  @change="accordionOne"
                  :disabled="disableFormBudget"
                  data-bs-toggle="tooltip"
                  data-bs-placement="bottom"
                  title="Selecione o e-mail do aprovador"
                  required
                >
                  <option :selected="form.bu.approver">
                    {{ form.bu.approver }}
                  </option>
                  <option
                    v-for="b in form.approvers.filter(
                      (b) => b.email !== form.bu.approver
                    )"
                    :key="b.id"
                    :value="b.email"
                  >
                    {{ b.email }}
                  </option>
                </select>
              </div>

              <div class="btn-next col-12">
                <DefaultButton
                  @click="collapseAccordion('panelsStayOpen-collapseTwo', 'business')"
                  :disabled="disableFormBudget"
                  class="me-0 rounded-3 btn-sm"
                  buttonText="Próximo"
                  buttonColor="btn btn-outline-primary"
                  buttonIcon="bi-arrow-right-circle-fill"
                  buttonType="button"
                />
              </div>
            </div>
          </div>
        </div>
        <!-- accordion 2 -->
        <div class="accordion-item shadow">
          <h2 class="accordion-header" id="panelsStayOpen-headingTwo">
            <button
              class="accordion-button"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#panelsStayOpen-collapseTwo"
              aria-expanded="true"
              aria-controls="panelsStayOpen-collapseTwo"
              :disabled="control.accordion.bu"
            >
              <i class="bi-briefcase-fill pe-2" style="font-size: 20px"></i>
              Selecione uma BU e Família de Produto
            </button>
          </h2>
          <div
            id="panelsStayOpen-collapseTwo"
            class="accordion-collapse collapse"
            :class="accordion.collTwo"
            aria-labelledby="panelsStayOpen-headingTwo"
          >
            <div class="accor-01 accordion-body" style="width: 100%">
              <div class="selected col-12 required">
                <label for="business" class="form-label">BU</label>
                <select
                  id="business"
                  v-model="form.bu.name"
                  class="form-select"
                  :class="borders.name"
                  aria-label="Selecione a BU"
                  @change="listProductFamily()"
                  :disabled="disableForm"
                  data-bs-toggle="tooltip"
                  data-bs-placement="bottom"
                  title="Selecione uma BU"
                  required
                >
                  <option :selected="form.bu.name">{{ form.bu.name }}</option>
                  <option
                    v-for="b in form.bus_name.filter(
                      (b) => b.name !== form.bu.name
                    )"
                    :key="b.id"
                    :value="b.name"
                  >
                    {{ b.name }}
                  </option>
                </select>
              </div>

              <div class="selected col-12 required">
                <label for="product_family" class="form-label"
                  >Familia de Produto</label
                >
                <select
                  id="product_family"
                  v-model="form.bu.product_family"
                  :class="borders.product_family"
                  class="form-select"
                  aria-label="Selecione um produto"
                  @change="accordionOne"
                  :disabled="disableForm"
                  data-bs-toggle="tooltip"
                  data-bs-placement="bottom"
                  title="Selecione uma familia de produto"
                  required
                >
                  <option :selected="form.bu.product_family">
                    {{ form.bu.product_family }}
                  </option>
                  <option
                    v-for="b in form.product_family.filter(
                      (b) => b.product_family !== form.bu.product_family
                    )"
                    :key="b.id"
                    :value="b.product_family"
                  >
                    {{ b.product_family }}
                  </option>
                </select>
              </div>

              <div class="btn-next col-12">
                <DefaultButton
                  :disabled="disableForm"
                  @click="
                    collapseAccordion('panelsStayOpen-collapseThree', 'year')
                  "
                  class="me-0 rounded-3 btn-sm"
                  buttonText="Próximo"
                  buttonColor="btn btn-outline-primary"
                  buttonIcon="bi-arrow-right-circle-fill"
                  buttonType="button"
                />
              </div>
            </div>
          </div>
        </div>
        <!-- accordion 3 -->
        <div class="accordion-item shadow">
          <h2 class="accordion-header" id="panelsStayOpen-headingThree">
            <button
              class="accordion-button"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#panelsStayOpen-collapseThree"
              aria-expanded="true"
              aria-controls="panelsStayOpen-collapseThree"
              :disabled="control.accordion.bu"
            >
              <i class="bi-table pe-2" style="font-size: 20px"></i>
              Adicionar Orçamento
            </button>
          </h2>
          <div
            id="panelsStayOpen-collapseThree"
            class="accordion-collapse collapse"
            :class="accordion.collThree"
            aria-labelledby="panelsStayOpen-headingThree"
          >
            <div class="accor-01 accordion-body" style="width: 100%">
              <div class="d-flex justify-content-between" style="width: 100%">
                <div class="budget col-12 required">
                  <label for="year" class="form-label">Ano</label>
                  <select
                    id="year"
                    v-model="form.month.year"
                    class="form-select"
                    :class="borders.year"
                    aria-label="Selecione o Ano"
                    :disabled="disableForm"
                    required
                  >
                    <option :selected="form.month.year">
                      {{ form.month.year }}
                    </option>
                    <option v-if="form.month.year != 2021" value="2021">
                      2021
                    </option>
                    <option v-if="form.month.year != 2022" value="2022">
                      2022
                    </option>
                  </select>
                </div>

                <div class="budget col-12 required">
                  <label for="month" class="form-label">Mês</label>
                  <select
                    id="month"
                    v-model="form.month.month"
                    class="form-select"
                    :class="borders.month"
                    aria-label="Selecione o mês"
                    :disabled="disableForm"
                    required
                  >
                    <option :selected="form.month.month">
                      {{ form.month.month }}
                    </option>
                    <option
                      v-for="b in months.filter(
                        (b) => b.name !== form.month.month
                      )"
                      :key="b.value"
                      :value="b.name"
                    >
                      {{ b.name }}
                    </option>
                  </select>
                </div>

                <div class="budget col-12 required">
                  <label for="type" class="form-label">Tipo</label>
                  <select
                    id="type"
                    v-model="form.month.type"
                    :class="borders.type"
                    class="form-select"
                    aria-label="Selecione o Tipo"
                    :disabled="disableForm"
                    required
                  >
                    <option :selected="form.month.type">
                      {{ form.month.type }}
                    </option>
                    <option
                      v-if="form.month.type != 'Despesas'"
                      value="Despesas"
                    >
                      Despesas
                    </option>
                    <option v-if="form.month.type != 'Receita'" value="Receita">
                      Receita
                    </option>
                  </select>
                </div>

                <div class="col-12" style="max-width: 15%">
                  <label for="description" class="form-label">Valor</label>
                  <input
                    :disabled="disableForm"
                    v-model="form.month.value"
                    :class="borders.value"
                    type="number"
                    min="0"
                    class="form-control"
                    placeholder="valor"
                  />
                  <label for="description" class="form-label">{{
                    new Intl.NumberFormat("pt-BR", {
                      style: "currency",
                      currency: "BRL",
                    }).format(
                      form.month.value ? form.month.value.toFixed(2) : 0
                    )
                  }}</label>
                </div>

                <div class="col-12" style="max-width: 10%">
                  <label for="description" class="form-label">Custo %</label>
                  <input
                    :disabled="disableForm || form.month.type != 'Receita'"
                    id="cost"
                    v-model="form.month.cost"
                    :class="borders.cost"
                    type="number"
                    class="form-control"
                    placeholder="11.5"
                    v
                  />
                  <label for="description" class="form-label">{{
                    form.month.type == "Receita"
                      ? new Intl.NumberFormat("pt-BR", {
                          style: "currency",
                          currency: "BRL",
                        }).format(
                          (form.month.cost / 100) *
                            (form.month.value ? form.month.value : 0).toFixed(2)
                        )
                      : "R$ 0"
                  }}</label>
                </div>

                <div class="card" style="width: 18rem">
                  <div class="card-header" style="text-align: center">
                    <b>Resumo do Orçamento</b>
                  </div>
                  <ul class="list-group list-group-flush">
                    <li class="list-group-item">
                      <b>Custo:</b> {{ convertNumber(resume.cost) }}
                    </li>
                    <li class="list-group-item">
                      <b>Valor:</b> {{ convertNumber(resume.valor) }}
                    </li>
                    <li class="list-group-item">
                      <b>Resultado líquido:</b>
                      {{
                        convertNumber(
                          form.month.type != "Receita" ? 0 : resume.liquido
                        )
                      }}
                    </li>
                  </ul>
                </div>
              </div>
              <div class="d-flex flex-column bd-highlight" style="width: 100%">
                <div class="col-12 description">
                  <label for="description" class="form-label">Descrição</label>
                  <input
                    :disabled="disableForm"
                    id="description"
                    v-model="form.month.description"
                    type="text"
                    class="form-control"
                    placeholder="Descrição do orçamento."
                  />
                </div>

                <div class="col-12 description">
                  <label for="comment">Comentário</label>
                  <textarea
                    v-model="form.month.comment"
                    :disabled="disableForm"
                    class="form-control"
                    placeholder="Adicione um comentário."
                    id="comment"
                  >
                  </textarea>
                </div>
              </div>

              <DefaultButton
                class="action-button mb-2"
                buttonText="Adicionar"
                @click="addBudet"
                :buttonActive="disableForm"
                buttonColor="btn btn-secondary rounded-3 btn-sm"
                buttonIcon="bi bi-file-plus-fill"
                buttonType="button"
              />

              <div id="table-budget" class="d-flex flex-column bd-highlight" style="width: 100%">
                <table class="table table-bordered shadow">
                  <thead class="table table-dark border border-white">
                    <tr class="border border-secondary">
                      <th scope="col">Ano</th>
                      <th scope="col">Mês</th>
                      <th scope="col">BU</th>
                      <th scope="col">Família de Produto</th>
                      <th scope="col">Tipo</th>
                      <th scope="col">Valor</th>
                      <th scope="col">Custo</th>
                      <th scope="col">%</th>
                      <th scope="col">Remover</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="month in form.months" :key="month.value">
                      <td class="lines">{{ month.year }}</td>
                      <td class="lines">{{ month.month }}</td>
                      <td class="lines">{{ getBuById(month.bu_id) }}</td>
                      <td class="lines">{{ getFamilyById(month.bu_id) }}</td>
                      <td class="lines">{{ month.type }}</td>
                      <td class="lines">
                        {{
                          new Intl.NumberFormat("pt-BR", {
                            style: "currency",
                            currency: "BRL",
                          }).format(month.value)
                        }}
                      </td>
                      <td class="lines">
                        {{
                          new Intl.NumberFormat("pt-BR", {
                            style: "currency",
                            currency: "BRL",
                          }).format((month.cost / 100) * month.value)
                        }}
                      </td>
                      <td class="lines">{{ month.percent }}</td>
                      <td class="lines d-flex flex-row justify-content-around">
                        <button
                          @click="removeLine(month.id)"
                          type="button"
                          :disabled="control.buttons.remove"
                          class="btn btn-danger btn-sm m-0"
                          data-bs-toggle="tooltip"
                          data-bs-placement="left"
                          title="Remover linha"
                        >
                          <i class="bi-dash-circle-fill"></i>
                        </button>
                      </td>
                    </tr>
                    <tr class="table-dark border border-dark">
                      <td colspan="9">
                        <div
                          class="d-flex justify-content-around"
                          style="width: 100%"
                        >
                          <div style="font-size: 18px">
                            <i
                              class="bi bi-dash-circle"
                              style="font-size: 20px"
                            ></i>
                            Total de Despesas:
                            {{ convertNumber(form.totals.despesas) }}
                          </div>
                          <div style="font-size: 18px">
                            <i
                              class="bi bi-building"
                              style="font-size: 20px"
                            ></i>
                            Total de Custos:
                            {{ convertNumber(form.totals.cost) }}
                          </div>
                          <div style="font-size: 18px">
                            <i
                              class="bi bi-plus-circle"
                              style="font-size: 20px"
                            ></i>
                            Total de Receitas:
                            {{ convertNumber(form.totals.receita) }}
                          </div>

                          <div style="font-size: 18px">
                            <i
                              class="fa fa-balance-scale"
                              style="font-size: 20px"
                            ></i>
                            Resultado Liquido:
                            {{ convertNumber(form.totals.balanco) }}
                          </div>

                          <div style="font-size: 18px">
                            <i
                              class="fa fa-balance-scale"
                              style="font-size: 20px"
                            ></i>
                            % Liquido:
                            {{ convertNumber((form.totals.receita / (form.totals.despesas + form.totals.cost))) }}
                          </div>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
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
          buttonType="button"
        />
        <DefaultButton
          buttonType="submit"
          class="action-button me-3"
          buttonText="Salvar"
          :buttonActive="control.buttons.save"
          buttonColor="btn btn-success"
          buttonIcon="bi bi-check-circle-fill"
        />
        <DefaultButton
          class="action-button me-3"
          buttonText="Alterar"
          @click="onChange"
          :buttonActive="control.buttons.edit"
          buttonColor="btn btn-dark"
          buttonIcon="bi-arrow-up-circle-fill"
          buttonType="button"
        />
        <DefaultButton
          class="action-button me-3"
          buttonText="Cancelar"
          @click="onReset"
          buttonColor="btn btn-danger"
          buttonIcon="bi-x-circle-fill"
          buttonType="reset"
        />
      </div>
    </form>

    <div
      id="budget-table"
      class="table-func d-flex row g-0 px-4 border border-danger rounded p-3 mt-1 px-4"
    >
      <AlertMessage
        :alertShow="alerts.table.success"
        :alertText="alerts.table.successText"
        alertType="alert-success"
      />
      <AlertMessage
        :alertShow="alerts.table.error"
        :alertText="alerts.table.errorText"
        alertType="alert-danger"
      />
      <h5 class="card-title">Listagem de Orçamento</h5>
      <div class="status-card d-flex justify-content-between mb-2">
        <div class="card shadow" style="min-width: 49.8%">
          <div class="card-header">
            <b>Status</b>
          </div>
          <div class="card-body d-flex justify-content-around">
            <p class="text-start">
              <i
                class="bi bi-stickies-fill me-3"
                style="font-size: 1.3rem; color: black"
              ></i
              >Rascunho.
            </p>
            <p class="text-start">
              <i
                class="bi bi-question-circle-fill me-3"
                style="font-size: 1.3rem; color: blue"
              ></i
              >Aguardando aprovação.
            </p>
            <p class="text-start">
              <i
                class="bi bi-x-circle-fill me-3"
                style="font-size: 1.3rem; color: red"
              ></i
              >Reprovado.
            </p>
            <p class="text-start">
              <i
                class="bi bi-eraser-fill me-3"
                style="font-size: 1.3rem; color: gold"
              ></i
              >Refazer.
            </p>
            <p class="text-start">
              <i
                class="bi bi-check-circle-fill me-3"
                style="font-size: 1.3rem; color: green"
              ></i
              >Aprovado.
            </p>
          </div>
        </div>
        <div class="card shadow" style="min-width: 49.8%">
          <div class="card-header">
            <b>Ações</b>
          </div>
          <div class="card-body d-flex justify-content-around">
            <p class="text-start" id="visualizar">
              <button
                type="button" for="visualizar"
                class="button-micro btn btn-primary btn-sm m-0"
              >
                <i  for="visualizar" class="bi bi-eye-fill"></i>
              </button>
              Visualizar
            </p>

            <p class="text-start" id="solicitar">
              <button
                type="button" for="solicitar"
                class="button-micro btn btn-warning btn-sm m-0"
              >
                <i class="fa fa-paper-plane" for="solicitar"></i>
              </button>
              Solicitar aprovação
            </p>

            <p class="text-start">
              <button
                type="button"
                class="button-micro btn btn-success btn-sm m-0"
              >
                <i class="bi bi-check-circle-fill"></i>
              </button>
              Aprovar
            </p>

            <p class="text-start">
              <button
                type="button"
                class="button-micro btn btn-danger btn-sm m-0"
              >
                <i class="bi bi-x-circle-fill"></i>
              </button>
              Reprovar
            </p>

            <!-- <p class="text-start">
              <button
                type="button"
                class="button-micro btn btn-primary btn-sm m-0"
              >
                <i class="bi bi-pencil-square"></i>
              </button>
              Editar
            </p> -->
          </div>
        </div>
      </div>
      <table class="table table-bordered shadow">
        <thead class="table table-dark border border-white">
          <tr class="border border-secondary">
            <th scope="col">Nome</th>
            <th scope="col">Status</th>
            <th scope="col">Mensagem</th>
            <th scope="col">Última Atualização</th>
            <th scope="col">Despesas</th>
            <th scope="col">Custos</th>
            <th scope="col">Receita</th>
            <th scope="col">Valor líquido</th>
            <th scope="col">Ações</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="bud in budgetList" :key="bud.id">
            <td class="lines">{{ bud.name }}</td>
            <td class="lines">
              <i
                :class="getStatusIcon(bud.status)"
                :style="getStatusColor(bud.status)"
              ></i>
            </td>
            <td class="lines">
              {{ bud.status[bud.status.length - 1].message || "" }}
            </td>
            <td class="lines">
              {{
                new Date(
                  bud.status[bud.status.length - 1].updated_at
                ).toLocaleString("pt-BR") || ""
              }}
            </td>
            <td class="lines">
              {{
                new Intl.NumberFormat("pt-BR", {
                  style: "currency",
                  currency: "BRL",
                }).format(bud.total.g.toFixed(2))
              }}
            </td>
            <td class="lines">
              {{
                new Intl.NumberFormat("pt-BR", {
                  style: "currency",
                  currency: "BRL",
                }).format(bud.total.c.toFixed(2))
              }}
            </td>
            <td class="lines">
              {{
                new Intl.NumberFormat("pt-BR", {
                  style: "currency",
                  currency: "BRL",
                }).format(bud.total.r.toFixed(2))
              }}
            </td>
            <td class="lines">
              {{
                new Intl.NumberFormat("pt-BR", {
                  style: "currency",
                  currency: "BRL",
                }).format(bud.total.vl.toFixed(2))
              }}
            </td>
            <td class="d-flex flex-row justify-content-around">
              <button
                @click="loadBuget(bud.id)"
                v-scroll-to="'#table-budget'"
                type="button"
                class="btn btn-primary btn-sm m-0"
                data-bs-toggle="tooltip"
                data-bs-placement="left"
                title="Visualizar Orçamento"
              >
                <i class="bi bi-eye-fill"></i>
              </button>

              <button
                :disabled="
                  getStatusByList(bud.status) == 'draft' ? false : true
                "
                @click="changeStatus(bud.id)"
                type="button"
                class="btn btn-warning btn-sm m-0"
                data-bs-toggle="tooltip"
                data-bs-placement="left"
                title="Enviar para aprovação"
              >
                <i class="fa fa-paper-plane"></i>
              </button>

              <button
                :disabled="
                  getStatusByList(bud.status) == 'approve' &&
                  role.can_approve_budget
                    ? false
                    : true
                "
                @click="changeStatus(bud.id, 'approved', 'Orçamento aprovado.')"
                type="button"
                class="btn btn-success btn-sm m-0"
                data-bs-toggle="tooltip"
                data-bs-placement="left"
                title="Aprovar Orçamento"
              >
                <i class="bi bi-check-circle-fill"></i>
              </button>

              <button
                :disabled="
                  getStatusByList(bud.status) == 'approve' &&
                  role.can_approve_budget
                    ? false
                    : true
                "
                @click="changeStatus(bud.id, 'denied', 'Negado.')"
                type="button"
                class="btn btn-danger btn-sm m-0"
                data-bs-toggle="tooltip"
                data-bs-placement="left"
                title="Reprovar Orçamento"
              >
                <i class="bi bi-x-circle-fill"></i>
              </button>

              <!-- <button
                :disabled="
                  getStatusByList(bud.status) == 'draft' ||
                  getStatusByList(bud.status) == 'remake'
                    ? false
                    : true
                "
                @click="loadBuget(bud.id)"
                type="button"
                class="btn btn-primary btn-sm m-0"
                data-bs-toggle="tooltip"
                data-bs-placement="left"
                title="Editar Orçamento"
              >
                <i class="bi bi-pencil-square"></i>
              </button> -->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>


<script>
import checkLogin from "../js/checkLogin.js";
import redirectToLogin from "../js/redirectLogin";
import DefaultButton from "../components/DefaultButton.vue";
import DefaultTitle from "../components/DefaultTitle.vue";
import AlertMessage from "../components/AlertMessage.vue";
import BU from "../services/bu.js";
import Employee from "../services/employee.js";
import Budget from "../services/budget.js";
import StatusBudget from "../services/status.js";
import Approver from "../services/approver.js";
import Month from "../services/month.js";

export default {
  name: "Orcamento",
  components: {
    DefaultButton,
    DefaultTitle,
    AlertMessage,
  },
  methods: {
    calculateResume() {
      this.resume.cost =
        this.form.month.type == "Receita"
          ? (this.form.month.cost / 100) *
            (this.form.month.value ? this.form.month.value : 0)
          : 0;
      this.resume.valor = this.form.month.value ? this.form.month.value : 0;
      this.resume.liquido = this.resume.valor
        ? this.resume.valor - this.resume.cost
        : 0;
      console.log(
        "imposto:",
        this.resume.imposto,
        "cost:",
        this.resume.cost,
        "valor:",
        this.resume.valor,
        "liquido:",
        this.resume.liquido
      );
    },
    saveBudget(id_field) {
      this.getBu().then(
        this.getApprover().then(() => {
          const data = {
            name: this.form.status.name,
            employee_id: this.user.id,
          };
          Budget.createBudget(data)
            .then((resp) => {
              this.dataBudget.budget.data = resp.data;
              this.saveStatus().then(() => {
                this.saveApprover().then(() => {
                  console.log(
                    this.validation.status_name,
                    this.validation.status,
                    this.validation.approver
                  );
                  if (
                    this.validation.status_name &&
                    this.validation.status &&
                    this.validation.approver
                  ) {
                    this.disableForm = false;
                    this.disableFormBudget = true;
                    this.accordion.collTwo = "show";
                    this.accordion.collOne = "";
                    this.borders.approver = "";
                    this.borders.status_name = "";
                    this.borders.status = "";
                    window.setTimeout(function () {
                      document.getElementById(id_field).focus();
                    }, 1);
                  }
                  this.alerts.form.success = true;
                  this.alerts.form.successText =
                    "Orçamento criado com sucesso.";
                  this.budgetStatus = true;
                });
              });
            })
            .catch((err) => {
              console.log(err);
              this.alerts.form.error = true;
              this.alerts.form.errorText = err.response.data.detail;
              this.budgetStatus = false;
            })
            .finally(this.disableAlertForm());
        })
      );
    },
    convertNumber(value) {
      return (
        new Intl.NumberFormat("pt-BR", {
          style: "currency",
          currency: "BRL",
        }).format(value) || 0
      );
    },
    collapseAccordion(id_collapse, id_field, coll = true) {
      if (id_field == "year") {
        this.validationSelector(this.form.bu.name, "name");
        this.validationSelector(this.form.bu.product_family, "product_family");
        setTimeout(() => {
          if (this.validation.name && this.validation.product_family && coll) {
            this.accordion.collTwo = "";
            this.accordion.collThree = "show";
            window.setTimeout(function () {
              document.getElementById(id_field).focus();
            }, 1);
            this.getBu();
          }
        }, 100);
      } else if (id_field == "business") {
        this.validationSelector(this.form.status.status, "status");
        this.validationText(this.form.status.name, "status_name");
        this.validationSelector(this.form.bu.approver, "approver");
        if (
          this.validation.status_name &&
          this.validation.status &&
          this.validation.approver
        ) {
          this.saveBudget(id_field);
        }
      }
    },
    collapseNow(id_collapse, id_field) {
      var collapse = document.getElementById(id_collapse);
      window.setTimeout(function () {
        document.getElementById(id_field).focus();
      }, 1);
      return new bootstrap.Collapse(collapse, { show: true });
    },
    getBuById(id) {
      const data = this.allBUs.filter((v) => v.id == id);
      return data[0].name;
    },
    getFamilyById(id) {
      const data = this.allBUs.filter((v) => v.id == id);
      return data[0].product_family;
    },
    getStatusByList(status) {
      const st = status[status.length - 1];
      if (!st) {
        return "";
      }
      return st.status;
    },
    getStatusColor(status) {
      const icons = {
        draft: "color: black; font-size: 1.3rem",
        approve: "color: blue; font-size: 1.3rem",
        denied: "color: red; font-size: 1.3rem",
        remake: "color: gold; font-size: 1.3rem",
        approved: "color: green; font-size: 1.3rem",
      };
      const st = status[status.length - 1];
      if (!st) {
        return "";
      }
      return icons[st.status];
    },
    getStatusIcon(status) {
      const icons = {
        draft: "bi bi-stickies-fill",
        approve: "bi bi-question-circle-fill",
        denied: "bi bi-x-circle-fill",
        remake: "bi bi-eraser-fill",
        approved: "bi bi-check-circle-fill",
      };
      const st = status[status.length - 1];
      if (!st) {
        return "";
      }
      return icons[st.status];
    },
    calculateTotals(months) {
      const values = {
        g: 0,
        r: 0,
        c: 0,
        vl: 0,
      };
      months.forEach((val) => {
        if (val.type == "expenditure") {
          values.g += parseFloat(val.value);
        } else if (val.type == "income") {
          values.r += parseFloat(val.value);
          values.c += (val.cost / 100) * val.value;
        }
      });
      values.vl = values.r - (values.g + values.c);
      return values;
    },
    listBudgets() {
      Budget.listBudget(this.user.id)
        .then((resp) => {
          this.budgetList = resp.data.budgets;
          this.budgetList.forEach((v) => {
            const total = this.calculateTotals(v.months);
            v.total = total;
          });
          this.budgetList.forEach((v) => {
            Approver.listApproverByBudgetId(v.id)
              .then((resp) => {
                v.approver = resp.data.approver || "Sem aprovador";
              })
              .catch((err) => {
                console.log(err);
              });
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    listBUs(id) {
      BU.listBu(id)
        .then((resp) => {
          const names = [];
          this.form.bus = resp.data.business;
          for (var i in this.form.bus) {
            if (!names.includes(this.form.bus[i].name)) {
              this.form.bus_name.push(this.form.bus[i]);
              names.push(this.form.bus[i].name);
            }
          }
        })
        .catch((err) => {
          console.log(err.response.data);
        });
    },
    listAllBUs () {
      BU.listAllBu().then(resp => {
        this.allBUs = resp.data
      }).catch(err => {
        console.log(err)
      })
    },
    listProductFamily() {
      this.form.bu.product_family = "Selecione";
      const data = this.form.bus.filter((b) => b.name === this.form.bu.name);
      this.form.product_family = data;
      this.accordionOne();
    },
    listApprovers() {
      Employee.listEmployeeApprover()
        .then((resp) => {
          this.form.approvers = resp.data;
        })
        .catch((err) => {
          console.log(err.response.data);
        });
    },
    accordionOne() {
      const sel = "Selecione";

      if (
        this.form.bu.name != sel &&
        this.form.bu.product_family != sel &&
        this.form.bu.approver != sel
      ) {
        //this.control.accordion.status = false
      } else {
        //this.control.accordion.status = true
        //this.control.accordion.budget = true
      }
    },
    onReset(event) {
      this.bu = {
        id: "",
        name: "",
        product_family: "",
        description: "",
      };
      this.form.months = []
      this.control.buttons.new = false;
      this.control.buttons.save = true;
      this.control.buttons.edit = true;
      this.control.buttons.remove = true;
      this.disableForm = true;
      this.disableFormBudget = true;
      this.control.accordion.bu = false;
      this.control.accordion.status = false;
      this.control.accordion.budget = false;
      this.control.accordion.collapseOneArea = false;
      this.control.accordion.collapseTwoArea = true;
      this.control.accordion.collapseThreeArea = true;
      this.control.disableForm = true;
      this.validation.name = false;
      this.validation.product_family = false;
      this.validation.approver = false;
      this.validation.status_name = false;
      this.validation.status = false;
      this.validation.year = false;
      this.validation.month = false;
      this.validation.type = false;
      this.validation.value = false;
      this.validation.cost = false;
      this.validation.description = false;
      this.validation.comment = false;

      this.resume.imposto = 0;
      this.resume.cost = 0;
      this.resume.valor = 0;
      this.resume.liquido = 0;

      this.borders.bu = "";
      this.borders.product_family = "";
      this.borders.approver = "";
      this.borders.name = "";
      this.borders.status_name = "";
      this.borders.status = "";
      this.borders.year = "";
      this.borders.month = "";
      this.borders.type = "";
      this.borders.value = "";
      this.borders.cost = "";
      this.borders.description = "";
      this.borders.comment = "";
    },
    onNew(event) {
      this.bu = {
        id: "",
        name: "",
        product_family: "",
        description: "",
      };
      this.control.buttons.new = true;
      this.control.buttons.remove = false
      this.control.buttons.save = false;
      this.control.buttons.edit = true;
      this.disableFormBudget = false;
    },
    // Save
    changeStatus(id, status = "approve", message = "Enviado para aprovação") {
      if (confirm("Tem certeza que deseja alterar o status?")) {
        const data = {
          status: status,
          current: true,
          message: message,
          budget_id: id,
        };
        StatusBudget.createStatusBudget(data)
          .then((resp) => {
            console.log(resp.status, resp.data);
            this.listBudgets();
            this.alerts.table.success = true
            this.alerts.table.successText = 'O status foi alterado com sucesso.'
          })
          .catch((err) => {
            console.log(err);
            this.alerts.table.error = true
            this.alerts.table.errorText = 'Ops. Problema ao alterar o status. Error: ' + err.response.data
          }).finally(e => {
            this.disableAlertForm()
          })
      }
    },
    async getApprover() {
      Employee.listEmployeeByEmail(this.form.bu.approver)
        .then((resp) => {
          this.dataBudget.bu.approver = resp.data;
        })
        .catch((err) => {
          console.log("Approver", err);
        });
    },
    async getBu() {
      const data = this.form.bus.filter(
        (v) =>
          v.name == this.form.bu.name &&
          v.product_family == this.form.bu.product_family
      );
      this.dataBudget.bu.bu = data[0];
    },
    async saveStatus() {
      const status = this.status.filter(
        (v) => v.value == this.form.status.status
      )[0].name;
      const data = {
        status: status,
        current: true,
        budget_id: this.dataBudget.budget.data.id,
        message: status == "draft" ? "Rascunho" : "",
      };
      StatusBudget.createStatusBudget(data)
        .then((resp) => {
          this.dataBudget.budget.status = resp.data;
        })
        .catch((err) => {
          console.log(err.response.data);
        });
    },
    async saveApprover() {
      const data = {
        budget_id: this.dataBudget.budget.data.id,
        approver_id: this.dataBudget.bu.approver.id,
      };
      console.log(this.dataBudget.bu.approver);
      console.log(data);
      Approver.createApprover(data)
        .then((resp) => {
          console.log(resp.data);
        })
        .catch((err) => {
          console.log(err.response.data);
        });
    },
    onSubmit(event) {
      event.preventDefault();
      if (this.form.months.length < 1) {
        this.alerts.form.error = true;
        this.alerts.form.errorText =
          "O orçamento não pode ser salvo. Verifique se você preencheu todos os campos e adicionou pelo menos um orçamento!";
      } else {
        const len = this.form.months.length - 1;
        this.form.months.forEach((item, index) => {
          const data = { ...item };
          data.month = this.months.filter((v) => v.name == item.month)[0].value;
          data.type = item.type == "Receita" ? "income" : "expenditure";
          data.cost = data.cost || 0;
          Month.createMonth(data)
            .then((resp) => {
              console.log(resp.data);
            })
            .catch((err) => {
              console.log(err.response.data);
              console.log(err.request.data);
            });
          console.log("len", len, "index", index);
          if (len == index) {
            this.listBudgets();
            this.alerts.form.success = true;
            this.alerts.form.successText = "Orçamento gerado com sucesso.";
            this.onReset();
          }
        });
      }
      this.disableAlertForm();
    },
    // =======
    onChange(event) {
      event.preventDefault();
      const data = { ...this.bu };
      data.employee_id = this.localEmployeeId;
      console.log(data);
      if (confirm("Você tem certeza que deseja alterar?")) {
        BU.changeBu(this.bu.id, data)
          .then((resp) => {
            console.log(resp.data);
            this.listBus(this.localEmployeeId);

            this.onReset();

            this.control.events.alerts.form.successShow = true;
            this.control.events.alerts.form.successText =
              "BU alterada com sucesso.";
            this.disableAlertForm();
          })
          .catch((err) => {
            console.log(err.response.data);
            this.control.events.alerts.form.errorShow = true;
            if (err.response.status != 422) {
              this.control.events.alerts.form.errorText =
                err.response.data.detail;
            } else {
              this.control.events.alerts.form.errorText =
                "Error ao alterar a BU.";
            }
            this.disableAlertForm();
          });
      }
    },
    disableAlertForm() {
      setTimeout(() => {
        this.alerts.form.success = false;
        this.alerts.form.successText = "";
        this.alerts.form.error = false;
        this.alerts.form.errorText = "";
      }, 15000);
    },
    disableAlertTable() {
      setTimeout(() => {
        this.alerts.table.success = false;
        this.alerts.table.successText = "";
        this.alerts.table.error = false;
        this.alerts.table.errorText = "";
      }, 15000);
    },
    toReal(value) {
      return Intl.NumberFormat("pt-BR", {
        style: "currency",
        currency: "BRL",
      }).format(value);
    },
    validationOneAndTwo() {
      this.validationSelector(this.form.bu.name, "name");
      this.validationSelector(this.form.bu.product_family, "product_family");
      this.validationSelector(this.form.bu.approver, "approver");
      this.validationSelector(this.form.status.status, "status");
      this.validationText(this.form.status.name, "status_name");
    },
    addBudet() {
      this.getBu();
      setTimeout(() => {
        if (this.validateThree() && this.validateTwo()) {
          const data = {
            ...this.form.month,
            bu_id: this.dataBudget.bu.bu.id,
            budget_id: this.dataBudget.budget.data.id,
          };
          this.form.months.push(data);
          this.form.month.month = "Selecione";
          this.form.month.type = "Selecione";
          this.form.month.value = "";
          this.form.month.cost = 0;
          this.form.month.description = "";


          this.validation.cost = false;
          this.borders.cost = "";

          this.form.totals.receita = 0;
          this.form.totals.despesas = 0;
          this.form.totals.balanco = 0;
          //this.form.totals.percent = 0
          this.form.totals.cost = 0;
          this.form.month.id += 1;

          this.form.months.forEach((val) => {
            console.log(val);
            const value = val.value;
            if (val.type == "Despesas") {
              this.form.totals.despesas += parseFloat(value);
            } else if (val.type == "Receita") {
              this.form.totals.receita += parseFloat(value);
              this.form.totals.cost += value * (val.cost / 100);
            }
          });

          this.form.months.forEach((val) => {
            const value = val.value;
            if (val.type == "Despesas") {
              val.percent =
                ((value / this.form.totals.despesas) * 100).toFixed(2) + "%";
            } else if (val.type == "Receita") {
              val.percent =
                ((value / this.form.totals.receita) * 100).toFixed(2) + "%";
            }
          });
          this.form.totals.balanco =
            this.form.totals.receita -
            (this.form.totals.despesas + this.form.totals.cost);
          console.log(this.form.totals);
          this.validation.month = false;
          this.validation.type = false;
          this.validation.value = false;
          this.alerts.form.success = true;
          this.alerts.form.successText = "Item adicionado com sucesso.";
        } else {
          this.validationOneAndTwo();
          this.alerts.form.error = true;
          this.alerts.form.errorText =
            "Verifique se todos os campos foram preenchidos corretamente.";
        }
        setTimeout(() => {
          this.alerts.form.success = false;
          this.alerts.form.error = false;
        }, 10000);
      }, 250);
    },
    calculateLines() {
      this.form.totals.receita = 0;
      this.form.totals.despesas = 0;
      this.form.totals.balanco = 0;
      this.form.totals.cost = 0;

      this.form.months.forEach((val) => {
        console.log(val);
        const value = val.value;
        if (val.type == "Despesas") {
          this.form.totals.despesas += parseFloat(value);
        } else if (val.type == "Receita") {
          this.form.totals.receita += parseFloat(value);
          this.form.totals.cost += value * (val.cost / 100);
        }
      });

      this.form.months.forEach((val) => {
        const value = val.value;
        if (val.type == "Despesas") {
          val.percent =
            ((value / this.form.totals.despesas) * 100).toFixed(2) + "%";
        } else if (val.type == "Receita") {
          val.percent =
            ((value / this.form.totals.receita) * 100).toFixed(2) + "%";
        }
      });
      this.form.totals.balanco = this.form.totals.receita - (this.form.totals.despesas + this.form.totals.cost);
      console.log(this.form.totals);
    },
    removeLine(id) {
      const new_data = this.form.months.filter((val) => val.id != id);
      this.form.months = new_data;
      this.form.totals.receita = 0;
      this.form.totals.despesas = 0;
      this.form.totals.balanco = 0;
      this.form.totals.cost = 0;

      this.form.months.forEach((val) => {
        console.log(val);
        const value = val.value;
        if (val.type == "Despesas") {
          this.form.totals.despesas += parseFloat(value);
        } else if (val.type == "Receita") {
          this.form.totals.receita += parseFloat(value);
          this.form.totals.cost += value * (val.cost / 100);
        }
      });

      this.form.months.forEach((val) => {
        const value = val.value;
        if (val.type == "Despesas") {
          val.percent =
            ((value / this.form.totals.despesas) * 100).toFixed(2) + "%";
        } else if (val.type == "Receita") {
          val.percent =
            ((value / this.form.totals.receita) * 100).toFixed(2) + "%";
        }
      });
      this.form.totals.balanco =
        this.form.totals.receita -
        (this.form.totals.despesas + this.form.totals.cost);
      console.log(this.form.totals);
    },
    validationSelector(value, key) {
      if (value != "Selecione") {
        this.validation[key] = true;
        this.borders[key] = "is-valid";
      } else {
        this.validation[key] = false;
        this.borders[key] = "is-invalid";
      }
    },
    validationText(value, key, len = null) {
      if (value.length >= (len || 5)) {
        this.validation[key] = true;
        this.borders[key] = "is-valid";
      } else {
        this.validation[key] = false;
        this.borders[key] = "is-invalid";
      }
    },
    validationNumber(value, key) {
      if (typeof value === "number") {
        this.validation[key] = true;
        this.borders[key] = "is-valid";
      } else {
        this.validation[key] = false;
        this.borders[key] = "is-invalid";
      }
    },
    validateTwo() {
      this.validationSelector(this.form.bu.name, "name");
      this.validationSelector(this.form.bu.product_family, "product_family");
      if (this.validation.name && this.validation.product_family) {
        return true;
      }
      return false;
    },
    validateOne() {
      this.validationText(this.form.status.name, "status_name");
      this.validationSelector(this.form.status.status, "status");
      this.validationSelector(this.form.bu.approver, "approver");
      if (
        this.validation.status_name &&
        this.validation.status &&
        this.validation.approver
      ) {
        return true;
      }
      return false;
    },
    validateThree() {
      this.validationSelector(this.form.month.year, "year");
      this.validationSelector(this.form.month.month, "month");
      this.validationSelector(this.form.month.type, "type");
      this.validationNumber(this.form.month.value, "value");
      this.validationNumber(this.form.month.cost, "cost");
      if (
        this.validation.year &&
        this.validation.month &&
        this.validation.type &&
        this.validation.value &&
        this.validation.cost
      ) {
        return true;
      }
      return false;
    },
    loadBuget(budgetId) {
      this.onReset()
      const data = this.budgetList.filter((v) => v.id == budgetId)[0];
      const budget = {...data}

      const status = this.status.filter(
        (v) => v.name == budget.status[budget.status.length - 1].status
      )[0];
      budget.months.forEach(item => {
        item.type = item.type == 'income' ? 'Receita' : 'Despesas'
        item.month = this.months.filter(v => v.value == item.month)[0].name
      })
      this.form.status.name = budget.name;
      this.form.status.status = status.value;
      this.form.bu.approver = budget.approver.email;
      this.form.months =  budget.months
      this.calculateLines()
      this.accordion.collOne = "";
      this.accordion.collTwo = "show";
      this.accordion.collThree = "show";
      this.control.buttons.remove = true;
      this.control.buttons.new = true;
    },
  },
  watch: {
    "form.bu.name"(v) {
      this.validationSelector(v, "name");
    },
    "form.bu.product_family"(v) {
      this.validationSelector(v, "product_family");
    },
    "form.bu.approver"(v) {
      this.validationSelector(v, "approver");
    },
    "form.status.status"(v) {
      this.validationSelector(v, "status");
    },
    "form.status.name"(v) {
      this.validationText(v, "status_name");
    },
    "form.month.year"(v) {
      this.validationSelector(v, "year");
    },
    "form.month.month"(v) {
      this.validationSelector(v, "month");
    },
    "form.month.type"(v) {
      this.validationSelector(v, "type");
    },
    "form.month.cost"(v) {
      this.calculateResume();
      if (v) {
        this.validation.cost = true;
        this.borders.cost = "is-valid";
      } else {
        this.validation.cost = false;
        this.borders.cost = "is-invalid";
      }
    },
    "form.month.value"(v) {
      this.calculateResume();
      if (v) {
        this.validation.value = true;
        this.borders.value = "is-valid";
      } else {
        this.validation.value = false;
        this.borders.value = "is-invalid";
      }
    },
  },
  data() {
    return {
      allBUs: [],
      user: {},
      role: {},
      resume: {
        imposto: 0,
        cost: 0,
        valor: 0,
        liquido: 0,
      },
      disableFormBudget: true,
      disableForm: true,
      field_required: true,
      accordion: {
        collOne: "show",
        collTwo: "",
        collThree: "",
      },
      budgetStatus: false,
      status: [
        { name: "draft", value: "Rascunho" },
        { name: "approve", value: "Aguardando aprovação" },
        { name: "denied", value: "Negado" },
        { name: "remake", value: "Refazer" },
        { name: "approved", value: "Aprovado" },
      ],
      months: [
        { name: "Janeiro", value: 1 },
        { name: "Fevereiro", value: 2 },
        { name: "Março", value: 3 },
        { name: "Abril", value: 4 },
        { name: "Maio", value: 5 },
        { name: "Junho", value: 6 },
        { name: "Julho", value: 7 },
        { name: "Agosto", value: 8 },
        { name: "Setembro", value: 9 },
        { name: "Outubro", value: 10 },
        { name: "Novembro", value: 11 },
        { name: "Dezembro", value: 12 },
      ],
      form: {
        totals: {
          receita: 0,
          despesas: 0,
          balanco: 0,
          percent: 0,
          cost: 0,
        },
        bu: {
          name: "Selecione",
          product_family: "Selecione",
          approver: "Selecione",
        },
        status: {
          name: "",
          status: "Rascunho",
        },
        month: {
          year: "Selecione",
          month: "Selecione",
          type: "Selecione",
          value: 0,
          description: "",
          cost: 0,
          comment: "",
          id: 0,
        },
        product_family: [],
        bus: [],
        bus_name: [],
        months: [],
        approvers: [],
      },
      control: {
        accordion: {
          bu: false,
          status: false,
          budget: false,
          collapseOneArea: false,
          collapseTwoArea: true,
          collapseThreeArea: true,
        },
        disableForm: true,
        events: {
          alerts: {
            form: {
              successShow: false,
              successText: "",
              errorShow: false,
              errorText: "",
            },
            table: {
              successShow: false,
              successText: "",
              errorShow: false,
              errorText: "",
            },
          },
        },
        buttons: {
          new: false,
          save: true,
          edit: true,
          remove: true
        },
      },
      validation: {
        name: false,
        product_family: false,
        approver: false,
        status_name: false,
        status: false,
        year: false,
        month: false,
        type: false,
        value: false,
        cost: false,
        description: false,
        comment: false,
      },
      borders: {
        bu: "",
        product_family: "",
        approver: "",
        name: "",
        status_name: "",
        status: "",
        cost: "",
        year: "",
        month: "",
        type: "",
        value: "",
        cost: "",
        description: "",
        comment: "",
      },
      alerts: {
        form: {
          success: false,
          successText: "",
          error: false,
          errorText: "",
        },
        table: {
          success: false,
          successText: "",
          error: false,
          errorText: "",
        },
      },
      dataBudget: {
        bu: {
          bu: {},
          approver: {},
        },
        budget: {
          data: {},
          status: {},
        },
        months: {},
      },
      budgetList: [],
    };
  },
  async mounted() {
    try {
      const data = await checkLogin();
      if (!data) {
        console.log("USER DOES NOT EXISTS.");
        redirectToLogin(this);
        this.user = data;
      } else {
        this.listBUs(data.user.id);
        this.listAllBUs()
        this.listApprovers();
        this.user = data.user;
        this.role = data.role;
        this.listBudgets();
      }
    } catch (error) {
      console.log("REQUEST ERROR");
      redirectToLogin(this);
    }
  },
};
</script>

<style scoped>
.card-body {
  height: 70px !important;
  max-height: 200px;
  min-height: 50px;
}
.description{
  max-width: 80%;
}
#calulate.card-body {
  width: 20px;
  height: 10px;
}

#calulate {
  max-width: 10px;
}

.input-group .form-control {
  float: none;
}
.input-group .input-buttons {
  position: relative;
  z-index: 3;
}

.table-func,
form,
.container,
#accordionParent {
  min-width: 100%;
}
.selected,
.status {
  width: 25%;
  padding-right: 30px;
}
.btn-next {
  width: 20px;
  flex-grow: 1;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  justify-content: flex-end;
  align-items: flex-end;
  align-content: flex-end;
  margin-right: 0px !important;
}
.lines {
  text-align: center;
}
table {
  border-collapse: collapse;
  border-radius: 7px;
  overflow: hidden;
}

.button-micro {
  max-width: 32px;
  max-height: 32px;
}

form {
  border-bottom: red solid 1px;
  border-left: red solid 1px;
  border-right: red solid 1px;
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 4px;
}
.name {
  width: 35%;
}
.budget {
  max-width: 14%;
}

.col-12 {
  margin-top: 10px;
  margin-bottom: 10px;
}
.accor-01 {
  display: flex;
	flex-direction: row;
	flex-wrap: wrap;
	justify-content: space-between;
	align-items: center;
	align-content: flex-end;
}
.accordion-button {
  font-size: 18px;
  font-weight: 600;
}
</style>