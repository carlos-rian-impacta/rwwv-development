import { http } from "./config";

export default {
	listEmployee: () => {
		return http.get('/employees')
	},
	listEmployeeByEmail: (email) => {
		return http.get('/employees?email=' + email)
	},
	listEmployeeApprover: () => {
		return http.get('/employees?approver=true')
	},
	removeEmployee: (id) => {
		return http.delete('/employees/' + id)
	},
	createEmployee: (data) => { 
		return http.post('/employees', data)
	},
	changeEmployee: (id, data) => { 
		return http.patch('/employees/' + id, data)
	}
}