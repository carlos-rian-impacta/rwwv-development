import { http } from "./config";

export default {
	listBu: (id) => {
		return http.get('/bu?employee_id=' + id)
	},
	listBuById: (id) => {
		return http.get('/bu/' + id)
	},
	listAllBu: () => {
		return http.get('/bu/all')
	},
	removeBu: (id) => {
		return http.delete('/bu/' + id)
	},
	createBu: (data) => { 
		return http.post('/bu', data, {
			headers: {}
		})
	},
	changeBu: (id, data) => {
		return http.patch('/bu/' + id, data)
	}
}