import { http } from "./config";

export default {
	listApprover: () => {
		return http.get('/approver')
	},
	listApproverTrue: () => {
		return http.get('/approver?approver=true')
	},
	listApproverByBudgetId: (id) => {
		return http.get('/approver?budget_id=' +  id)
	},
	removeApprover: (id) => {
		return http.delete('/approver/' + id)
	},
	createApprover: (data) => { 
		return http.post('/approver/', data)
	},
	changeApprover: (id, data) => { 
		return http.patch('/approver/' + id, data)
	}
}