import { http } from "./config";

export default {
	createBudget: (data) => { 
		return http.post('/budget', data)
	},
	listBudget: (id) => {
		return http.get('/budget?employee_id=' + id)
	},
	listBudgetById: (id) => {
		return http.get('/budget/' + id)
	},
	removeBudget: (id) => {
		return http.delete('/budget/' + id)
	},
	changeBudget: (id, data) => {
		return http.patch('/budget/' + id, data)
	}
}