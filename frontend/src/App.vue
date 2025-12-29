<template>
  <div class="app-container">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="content">
        <router-view />
      </main>
    </div>
  </div>
</template>

<script setup>
import Header from './components/Header.vue'
import Sidebar from './components/Sidebar.vue'
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: #e6f0ff;
}

.main-layout {
  display: flex;
  /* flex-wrap: wrap; */
  flex: 1;
  overflow: hidden;
}

.content {
  flex: 1 1 300px;
  padding: 20px;
  background-color: white;
  border-radius: 8px;
  margin: 16px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
</style>
