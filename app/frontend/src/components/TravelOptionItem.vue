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
        <h4>{{ option.name }}</h4>
        <p>Preço: R$ {{ option.price }}</p>
        <p>{{ option.duration }}</p>
        <p>{{ option.seatType }}</p>
        <p>{{ option.seat }}</p>
        <p>{{ option.isFast }}</p>
    </div>
</template>


<style scoped>
.travel-option-item {
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 16px;
    margin-bottom: 16px;
}
</style>