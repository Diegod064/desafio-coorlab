<template>
    <div class="sidebar">
        <img src="../assets/logo.png" alt="Logo da Empresa" class="logo">
        <div class="sidebar-content">
            <span class="sidebar-item">
                <v-icon icon="mdi-calculator-variant-outline" />
                <p>Calculadora de Viagem</p>
            </span>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Sidebar'
}
</script>

<style scoped>
.sidebar {
    width: 250px;
    height: 100vh;
    background-color: #292e3f;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1000;
    padding: 16px 8px;
    color: #fafafa;
}

.logo {
    width: 180px;
    margin-bottom: 40px;
    margin-left: 8px;

}

.sidebar-content {
    display: flex;
    align-items: center;

}

.sidebar-item {
    display: flex;
    font-size: 18px;
    margin-left: 8px;
    align-content: center;
    gap: 4px;
}
</style>