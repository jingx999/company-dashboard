<template>
  <div class="dashboard">
    <h4>数据概览</h4>
    <div ref="barChartRef" class="chart"></div>
    <div ref="pieChartRef" class="chart"></div>
  </div>
</template>

<script setup>
import { onMounted, onBeforeUnmount, ref } from 'vue'
import * as echarts from 'echarts'

const barChartRef = ref(null)
const pieChartRef = ref(null)

let barChartInstance = null
let pieChartInstance = null

onMounted(() => {
  //初始化柱状图
  if (barChartRef.value) {
    barChartInstance = echarts.init(barChartRef.value)
    barChartInstance.setOption({
      title: { text: '销售柱状图', left: 'center' },
      xAxis: { type: 'category', data: ['A', 'B', 'C', 'D'] },
      yAxis: { type: 'value' },
      series: [{ data: [120, 200, 150, 80], type: 'bar', itemStyle: { color: '#256eff' } }],
    })
  }
  //初始化饼图
  if (pieChartRef.value) {
    pieChartInstance = echarts.init(pieChartRef.value)
    pieChartInstance.setOption({
      title: { text: '用户分布饼图', left: 'center' },
      series: [
        {
          type: 'pie',
          radius: '50%',
          data: [
            { value: 335, name: '直接访问' },
            { value: 310, name: '邮件营销' },
            { value: 234, name: '联盟广告' },
            { value: 135, name: '视频广告' },
          ],
          emphasis: {
            itemStyle: {
              shadowBlue: 10,
              shadowOffsetx: 0,
              shadowColor: 'rgba(0,0,0,0.5)',
            },
          },
        },
      ],
    })
  }

  // 响应窗口大小变化
  window.addEventListener('resize', () => {
    barChartInstance?.resize()
    pieChartInstance?.resize()
  })
})

onBeforeUnmount(() => {
  // 销毁实例，防止内存泄漏
  barChartInstance?.dispose()
  pieChartInstance?.dispose()
})
</script>

<style scoped>
.dashboard h4 {
  color: #1a4db8;
  margin-bottom: 20px;
}

.chart {
  width: 100%;
  height: 300px;
  margin-bottom: 30px;
  background-color: #f8fbff;
  border-radius: 8px;
  padding: 10px;
}
</style>
