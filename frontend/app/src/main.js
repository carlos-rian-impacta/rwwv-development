import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VCalendar from 'v-calendar'
import VueScrollTo  from 'vue-scrollto';
import money from 'v-money'

import '@fortawesome/fontawesome-free/js/all'

const app = createApp(App);
app.use(VCalendar, {
    locales: {
        'pt-BR': {
        firstDayOfWeek: 1,
        masks: {
          L: 'DD-MM-YYYY',
        }
      } 
    }
  });
app.use(money, {
  decimal: ',',
  thousands: '.',
  prefix: 'R$ ',
  precision: 2,
  masked: false
})
app.use(VueScrollTo)
app.use(router).mount('#app')
