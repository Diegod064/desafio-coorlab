<script setup lang="ts">
import Navbar from './components/Navbar.vue'
import Sidebar from './components/Sidebar.vue'
</script>

<template>
  <div class="home">
    <Navbar />
    <Sidebar />
    <div class="container">
      
      <div class="header">
        <i class="fas fa-calculator"></i>
        <span>Calculadora de Viagem</span>
      </div>

      <div class="content-container">
        <div class="left-container">
          <div class="title">
            <i class="fas fa-dollar-sign"></i>
            <h3>Calcule o Valor da Viagem</h3>
          </div>
          <!-- Inputs -->
          <div class="inputs">
            <div class="input-group">
              <label for="destino">Destino:</label>
              <input type="text" id="destino">
            </div>
            <div class="input-group">
              <label for="data">Data:</label>
              <input type="date" id="data">
            </div>
          </div>
          
          <button class="buscar-btn">Buscar</button>
        </div>

        <!-- Container da direita (será implementado posteriormente) -->
        <div class="right-container">
          <!-- Conteúdo da direita -->
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  min-height: 100vh;
}

.container {
  width: 72%; /* Ajuste conforme necessário */
  /* height: 520px; */
  max-width: 1280px;
  margin-top: 80px; /* Altura da navbar */
  margin-left: 280px; /* Largura da sidebar */
  margin-right: 16px;
  /* padding: 20px; */
  background-color: #fafafa; /* Cor de fundo do container principal */
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Drop shadow */
}

/* @media (max-width: 992px) {
  .container {
    margin-left: 0; 
    width: 100%; 
  }
} */

.header {
  background-color: #292e3f;
  color: #fafafa;
  padding: 10px 0;
  text-align: center;
  border-radius: 8px 8px 0 0;
}

.header i {
  margin-right: 5px;
}

.content-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
  padding: 20px;
}

.left-container {
  background-color: #f3f3f3;
  color: #2d2d2d;
  padding: 20px;
  border-radius: 4px;
  width: calc(40% - 10px);
  margin: auto;
  display: flex;
  flex-direction: column;
  height: 380px;
  justify-content: center; /* Centraliza horizontalmente */
  align-items: center; /* Centraliza verticalmente */
  
}

.left-container .title {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.left-container .title i {
  margin-right: 10px;
}

.left-container .inputs {
  margin-bottom: 20px;
}

.left-container .input-group {
  margin-bottom: 10px;
}

.left-container label {
  display: block;
  margin-bottom: 5px;
}

.left-container input[type="text"],
.left-container input[type="date"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  box-sizing: border-box;
  color: #2d2d2d;
  background-color: #fafafa
}

.buscar-btn {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}

.right-container {
  width: calc(60% - 10px); /* Divide o espaço pela metade e subtrai a margem */
}
</style>