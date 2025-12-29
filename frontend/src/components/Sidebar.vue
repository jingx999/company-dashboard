<template>
  <nav class="sidebar">
    <ul>
      <li><router-link to="/">首页概览</router-link></li>
      <li><router-link to="/trend">趋势分析</router-link></li>
      <li><router-link to="/distribution">区域分布</router-link></li>
      <li><router-link to="/performance">性能对比</router-link></li>
      <li><router-link to="/realtime">实时监控</router-link></li>
      
    </ul>
  </nav>
</template>

<script setup>
// 无逻辑
</script>

<style scoped>
.sidebar {
  width: 200px;
  background-color: #d0e0ff;
  padding: 20px 0;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
}

.sidebar ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sidebar li {
  margin: 10px 0;
}

.sidebar a {
  text-decoration: none;
  color: #1a4db8;
  font-weight: bold;
  padding: 10px 20px;
  display: block;
  transition: background 0.2s;
}

.sidebar a:hover,
.sidebar a.router-link-exact-active {
  background-color: #a7c9ff;
  border-radius: 4px;
}
</style>
