import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '@/views/Dashboard.vue'
import TrendAnalysis from '@/views/TrendAnalysis.vue'
import DistributionMap from '@/views/DistributionMap.vue'
import Performanceradar from '@/views/Performanceradar.vue'
import RealtimeMonitor from '@/views/RealtimeMonitor.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: Dashboard },
    {path: '/trend', component: TrendAnalysis},
    {path: '/distribution', component: DistributionMap},
    {path: '/performance', component: Performanceradar},
    {path: '/realtime', component: RealtimeMonitor}
  ],
})

export default router
