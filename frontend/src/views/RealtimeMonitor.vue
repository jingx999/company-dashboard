<template>
  <div class="page">
    <h4>系统实时负载</h4>
    <div ref="chartRef" class="chart"></div>
    <p class="tip">数据每 2 秒自动更新（模拟）</p>
  </div>
</template>

<script setup>
import {ref,onMounted, onBeforeUnmount} from 'vue'
import * as echarts from 'echarts'

const chartRef = ref(null)
let chartInstance = null
let timer = null

onMounted(()=>{
  if (!chartRef.value) return
  chartInstance = echarts.init(chartRef.value)

  const data = []
  for (let i=0;i<20;i++) {
    data.push(Math.random() * 100)
  }

  chartInstance.setOption({
    title: { text: 'CPU 使用率 (%)', left: 'center' },
    tooltip: { trigger: 'axis' },
    xAxis: {
      type: 'category',
      show: false
    },
    yAxis: { type: 'value', min: 0, max: 100 },
    series: [{
      type: 'line',
      showSymbol: false,
      data,
      lineStyle: { color: '#256eff' }
    }]
  })

  // 模拟实时更新
  timer = setInterval(() => {
    const newData = [...data]
    newData.shift()
    newData.push(Math.random() * 100)
    chartInstance.setOption({
      series: [{ data: newData }]
    })
  }, 2000)
})

onBeforeUnmount(()=>{
  if (timer) clearInterval(timer)
  chartInstance?.dispose
})

</script>

<style scoped>
.page h2 { color: #1a4db8; margin-bottom: 20px; }
.chart { width: 100%; height: 350px; background: #f8fbff; border-radius: 8px; padding: 10px; }
.tip { text-align: center; color: #666; margin-top: 8px; font-size: 14px; }
</style>
