<template>
    <div class="sidebar">
        <img src="../assets/logo.png" alt="Logo da Empresa" class="logo">
        <div class="sidebar-content">
            <span class="sidebar-title">
                <i class="fas fa-calculator"></i>
                Calculadora de Viagem
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
}

.logo {
    width: 180px;
    margin-bottom: 20px;

}

.sidebar-content {
    display: flex;
    align-items: center;

}

.sidebar-title {
    font-size: 18px;
    margin-left: 10px;
}
</style>