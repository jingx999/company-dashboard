<template>
  <div class="page">
    <h4>部门绩效对比</h4>
    <div ref="chartRef" class="chart"></div>
  </div>
</template>

<script setup>
import {ref, onMounted, onBeforeUnmount} from 'vue'
import * as echarts from 'echarts'

const chartRef = ref(null)
let chartInstance = null

onMounted(()=>{
  if (!chartRef.value) return
  chartInstance = echarts.init(chartRef.value)
  chartInstance.setOption({
  title: { text: 'Q2 综合评分', left: 'center' },
    tooltip: {},
    radar: {
      indicator: [
        { name: '交付速度', max: 100 },
        { name: '代码质量', max: 100 },
        { name: '协作能力', max: 100 },
        { name: '创新性', max: 100 },
        { name: '客户满意度', max: 100 }
      ],
      shape: 'circle'
    },
    series: [{
      type: 'radar',
      data: [
        {
          name: '研发部',
          value: [85, 90, 75, 80, 88],
          symbolSize: 0
        }
      ],
      lineStyle: { color: '#256eff' },
      itemStyle: { color: '#256eff' },
      areaStyle: { opacity: 0.2 }
    }]
  })
})

onBeforeUnmount(()=>{
  chartInstance?.dispose()
})

</script>

<style scoped>
.page h4 {color:#1a4db8; margin-bottom: 20px;}
.chart {width: 100%; height: 400px; background: #f8fbff; border-radius:8px; padding:10px;}
</style>

