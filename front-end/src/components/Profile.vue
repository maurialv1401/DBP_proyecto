<template>
    <div>
      <h1 class="capi">Bienvenido {{ nombre }} {{ apellido }}</h1>
      <button class="boton" @click="logout">Cerrar sesión</button>
    </div>
  </template>
  
<script>
import axios from 'axios';

export default {
  name: 'Profile-Page',
  data() {
    return {
      nombre: '',
      apellido: '',
      email: '',
      edad: ''
    };
  },
  mounted(){
    if(localStorage.getItem('user_nombre')){
      this.nombre = localStorage.getItem('user_nombre');
      this.apellido = localStorage.getItem('user_apellido');
      this.email = localStorage.getItem('user_email');
      this.edad = localStorage.getItem('user_edad');
    }else{
      this.$router.push('/login');
    }
  },
  methods: {
      logout(){
        localStorage.clear();
        this.$router.push('/')
      }
  },
};
</script>

<style scoped>
.capi{
  text-transform: capitalize;
}

.boton{
  text-align: right;
}
</style>