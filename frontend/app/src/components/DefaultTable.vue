<template>
  <table class="table table-bordered shadow">
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
				<td >{{ bu.created_at }}</td>
				<td >{{ bu.updated_at }}</td>
				<td class="d-flex flex-row justify-content-around" style="max-width: 100px;">
					<button @click="loadEmployee(empl.id)" v-scroll-to="'#local-main'" type="button" class="btn btn-primary btn-sm m-0"><i class="bi bi-eye-fill"></i></button>
					<button @click="removeEmployee(empl.id)" type="button" class="btn btn-danger btn-sm m-0" ><i class="far fa-trash-alt"></i></button>
				</td>
			</tr>
		</tbody>
	</table>
</template>

<script>
export default {
    name: Table,
    tableColumn: {
        type: Array,
        default: []
    },
    tableValue: {
        type: Array,
        default: []
    },
    tableAction: {
        type: Object,
    }
}
</script>

<style scoped>

</style>