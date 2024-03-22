<script setup lang="ts">
import { defineProps } from 'vue';


defineProps<{
    option: {
        name: string;
        price: string;
        duration: string;
        seatType: string;
        seat: string;
        isFast: boolean;
    };
}>();


</script>


<template>
    <div class="travel-option-item">
        <div class="container-info">
            <div class="container-info-icon">
                <v-icon icon="mdi-hand-coin-outline"></v-icon>
            </div>
            <div class="container-info-description">
                <p class="titte"> {{ option.name }}</p>
                <p class="text">Leito: {{ option.seat }}</p>
                <p class="text">Tempo estimado: {{ option.duration }}</p>
            </div>
        </div>
        <div class="container-price">
          <p class="titte">Preço</p>
          <div class="text">{{ option.price }}</div>
        </div>
    </div>
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
  font-size: 18px;
  font-weight: bold;
  color: #333;
  width: 20%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 12px;
}

.titte {
  font-weight: bold;
}

p {
  font-size: 16px;
}
</style>
