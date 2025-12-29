<template>
  <div class="page">
    <h4>区域用户分布</h4>
    <div ref="chartRef" class="chart"></div>
  </div>
</template>

<script setup>
import {ref, onMounted, onBeforeUnmount} from 'vue'
import * as echarts from 'echarts'

const chartRef = ref(null)
let chartInstance = null

onMounted(() => {
  if (!chartRef.value) return
  chartInstance = echarts.init(chartRef.value)
  chartInstance.setOption({
    title: { text: '各区域用户数量', left: 'center' },
    tooltip: {},
    xAxis: { type: 'category', data: ['华北', '华东', '华南', '华中', '西南', '西北', '东北'] },
    yAxis: { type: 'value' },
    series: [{
      type: 'effectScatter',
      symbolSize: (val) => val / 10,
      data: [150, 320, 280, 180, 120, 90, 110],
      itemStyle: { color: '#256eff' }
    }]
  })
})

onBeforeUnmount(()=> {
  chartInstance?.dispose()
})


</script>

<style scoped>
.page h4 {color:#1a4db8; margin-bottom: 20px;}
.chart {width:100%; height:400px; background:#f8fbff; border-radius:8px; padding:10px;}
</style>
