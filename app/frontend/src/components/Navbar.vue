<template>
  <nav class="navbar">
  </nav>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>
.navbar {
  background-color: white;
  height: 60px; /* Altura da Navbar */
  width: 100%; /* Largura total */
  position: fixed; /* Fixar no topo da página */
  top: 0; /* Alinhar ao topo */
  z-index: 900; /* Garantir que está sobreposta a outros elementos */

  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

</style>
