<script setup lang="ts">
import { onMounted, ref } from 'vue';
import Navbar from './components/Navbar.vue';
import Sidebar from './components/Sidebar.vue';
import TravelOptionItem from './components/TravelOptionItem.vue';


const destination = ref('');
const date = ref('');
const cities = ref<string[]>([]);
const noDataSelected = ref(true);
const searchResults = ref([]);
const dialog = ref(false)

const handleSearch = () => {
  if (!destination.value || !date.value) {
    console.log("Por favor, preencha todos os campos");
    noDataSelected.value = true;
    dialog.value = true;
    console.log(dialog.value)
  } else {
    console.log(`Estas são as melhores alternativas de viagem para a data selecionada ${destination.value} ${date.value}`);
    noDataSelected.value = false;
    searchTravels();
    console.log(searchResults.value)
  }
}

const handleClear = () => {
  noDataSelected.value = true;
  searchResults.value = []
  destination.value = '';
  date.value = '';
}

const sampleObj = {
  name: 'Nome da opção',
  price: '100.00',
  duration: '2 horas',
  seatType: 'Economica',
  seat: 'A23',
  isFast: true

}


const searchTravels = () => {
  const queryParams = new URLSearchParams({
    destino: destination.value,
    data: date.value
  });

  return new Promise((resolve, reject) => {
    fetch(`http://localhost:3000/travels?${queryParams.toString()}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        resolve(data);
        searchResults.value = data;
      })
      .catch(error => {
        reject(error);
      });
  });
};

const fetchCities = () => {
  fetch('http://localhost:3000/fetch-cities')
    .then(response => response.json())
    .then(data => {
      cities.value = data;
    })
    .catch(error => {
      console.error('Error fetching cities:', error);
    });
};

onMounted(() => {
  fetchCities();
});



</script>


<template>
  <div class="home">
    <Navbar />
    <Sidebar />
    <div class="container">

      <div class="header">
        <v-icon icon="mdi-truck-delivery-outline" />
        <span>Calculadora de Viagem</span>
      </div>
      <v-dialog v-model="dialog" width="auto">
              <div class="modal">
                <v-icon>mdi-exclamation-thick</v-icon>
                <p>Insira os valores para realizar a cotação</p>
                <v-btn @click="dialog = false">Fechar</v-btn>
              </div>
            </v-dialog>

      <div class="content-container">
        <div class="left-container">
          <div class="left-container-content">
            <div class="title">
              <v-icon icon="mdi-hand-coin-outline"></v-icon>
              <h3>Calcule o Valor da Viagem</h3>
            </div>
            <div class="inputs">
              <div class="input-group">
                <label for="destino">Destino:</label>
                <v-select label="select" :items="cities" variant="outlined" v-model="destination"></v-select>
              </div>
              <div class="input-group">
                <label for="data">Data:</label>
                <input label="asdasd" type="date" id="data" v-model="date">

              </div>
            </div>
            <button class="search-btn" @click="handleSearch">Buscar</button>
          </div>

        </div>

        <div class="right-container">
          <div class="right-container-content" v-if="noDataSelected">
            <h3>Não há nenhum dado seleciondo</h3>
          </div>

          <div class="right-container-content" v-else>
            <h3>Estas são as melhores alternativas de viagem para a data selecionada</h3>
            <div>
              <TravelOptionItem :passages=searchResults></TravelOptionItem>
            </div>
            <button class="clear-btn" @click="handleClear">Limpar</button>
            
          </div>
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
  width: 72%;
  max-width: 1280px;
  margin-top: 80px;
  margin-left: 280px;
  margin-right: 16px;
  background-color: #fafafa;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.header {
  display: flex;
  background-color: #292e3f;
  color: #fafafa;
  padding: 16px;
  text-align: start;
  border-radius: 8px 8px 0 0;
  align-content: center;
  gap: 4px;
}

.header i {
  margin-right: 5px;
}

.content-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 16px;
  padding: 20px 8px;
}

.left-container {
  background-color: #f3f3f3;
  color: #2d2d2d;
  padding: 20px;
  border-radius: 4px;
  width: calc(32%);
  margin: auto;
  display: flex;
  flex-direction: column;
  height: 420px;
  justify-content: center;

}

.left-container-content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 360px;
}

.left-container .title {
  display: flex;
  align-items: center;
  justify-content: center;
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
.select{
  background-color: white;
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
}

.search-btn {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  background-color: #03a7b4;
  width: 80%;
  align-self: center;
}

.clear-btn {
  background-color: #f2a42f;
  color: black;
  border: none;
  padding: 4px 20px;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  width: 200px;
  margin-left: auto;
}

.right-container {
  color: #2d2d2d;
  padding: 20px;
  border-radius: 4px;
  width: calc(64%);
  margin: auto;
  display: flex;
  flex-direction: column;
  height: 420px;
  justify-content: center;
  align-items: center;
}

.right-container-content h3 {
  margin-bottom: 16px
}

.right-container-content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 360px;
}

.modal {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  background-color: #ffffff;
  padding-top: 2.5rem;
  padding-bottom: 1.5rem;
  padding-left: 5rem;
  padding-right: 5rem;
  border-radius: 1rem;
}

.modal p {
  font-size: 1.2rem;
}

.modal button {
  background-color: #03a8b4;
  color: #024b55;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  text-transform: none;
}
</style>