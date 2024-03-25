<script setup lang="ts">
import { ref } from 'vue';


defineProps<{

  passages: {
    name: string;
    price: string;
    duration: string;
    seatType: string;
    seat: string;
    isFastest: boolean;
    isCheapest: boolean;
  }[];
}>();


</script>


<template>
  <div class="travel-option-item" v-for="(passage, index) in passages" :key="index">
    <div class="container-info">
      <div class="container-info-icon">
        <v-icon v-if="passage.isCheapest && !passage.isFastest" icon="mdi-hand-coin-outline"></v-icon>
        <v-icon v-else-if="!passage.isCheapest && passage.isFastest" icon="mdi-clock-check-outline"></v-icon>
        <v-icon v-else-if="passage.isCheapest && passage.isFastest && passage.seatType == 'Confort'" icon="mdi-clock-check-outline"></v-icon>
      </div>
      <div class="container-info-description">
        <p class="titte"> {{ passage.name }}</p>
        <p v-if="passage.seatType == 'Economica'" class="text">Poltrona: {{ passage.seat }} (Convencional)</p>
        <p v-if="passage.seatType == 'Confort'" class="text">Leito: {{ passage.seat }} (Completo)</p>
        <p class="text">Tempo estimado: {{ passage.duration }}</p>
      </div>
    </div>
    <div class="container-price">
      <p class="titte">Preço</p>
      <div class="text">{{ passage.price }}</div>
    </div>
  </div>
  <p v-if="passages.length > 0 && passages[0].isCheapest && passages[0].seatType == 'Confort'">Essa viagem é a mais rápida e mais barata.</p>


</template>

<style scoped>
.travel-option-item {
  display: flex;
  justify-content: space-between;
  border-radius: 8px;
  margin-bottom: 16px;
  gap: 8px;
}

.container-price {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #f1f1f1;
  padding: 10px;
  border-radius: 8px;
}

.container-info {
  display: flex;
  align-items: center;
  border-radius: 8px;
  background-color: #f1f1f1;
  width: 80%;
  min-width: 286px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.container-info-icon {
  background-color: #03a7b4;
  font-size: 24px;
  border-radius: 8px 0 0 8px;
  padding: 1.5rem;
  color: white;
  height: 100%
}

.container-info-description {
  font-size: 14px;
  color: #333;
  margin-left: 1rem;
  background-color: #f1f1f1
}

.container-price {
  display: flex;
  flex-direction: column;
  align-items: start;
  font-size: 16px;
  color: #333;
  width: 20%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 12px;
  min-width: 100px;
}

.titte {
  font-weight: bold;
}

p {
  font-size: 16px;
}
</style>
