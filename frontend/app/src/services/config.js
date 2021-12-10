import axios from "axios"

const baseURL = 'https://rwwvbackend.azurewebsites.net/v1/'
export const http = axios.create({
    baseURL: baseURL
})