<template>
    <div class="page">
        <h4>关键指标趋势</h4>
        <div ref="chartRef" class="chart"></div>
    </div>
</template>

<script setup>
import {ref,onMounted,onBeforeUnmount} from 'vue'
import * as echarts from 'echarts'

const chartRef = ref(null)
let chartInstance = null

onMounted(() => {
    if (!chartRef.value) return
    chartInstance = echarts.init(chartRef.value)
    chartInstance.setOption({
        title:{text:'月度活跃用户&订单量', left:'center'},
        tooltip:{trigger:'axis'},
        legend:{data:['活跃用户', '订单量'],top:'bottom'},
        xAxis:{
            type:'category',
            data:['1月', '2月', '3月', '4月', '5月', '6月']
        },
        yAxis:[{ type: 'value', name: '用户数' }, { type: 'value', name: '订单数' }],
        series:[
            {
                name: '活跃用户',
                type: 'line',
                data: [120, 132, 101, 134, 90, 230],
                smooth: true,
                itemStyle: { color: '#256eff' }
            },
            {
                name: '订单量',
                type: 'line',
                yAxisIndex: 1,
                data: [80, 90, 70, 100, 60, 150],
                smooth: true,
                itemStyle: { color: '#ff7f50' }
            }
        ]
    })
})

onBeforeUnmount(() => {
    chartInstance?.dispose()
})

</script>

<style scoped>
.page h4 { color: #1a4db8; margin-bottom: 20px; }
.chart { width: 100%; height: 400px; background: #f8fbff; border-radius: 8px; padding: 10px; }
</style>


