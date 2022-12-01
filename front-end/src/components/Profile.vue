<template>
  
    <div>
      <section class="vh-100 gradient-custom">
      <h1 class="margin-auto">
        <span class="margin-auto_content">
          Bienvenido {{ nombre }} {{ apellido }} 
          </span>
      </h1>
      <h3 class="text-down"> ¿Listo para encontrar a tu rommie perfecto?</h3>
    
    </section>
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

<style>
@import url('https://fonts.googleapis.com/css2?family=Fjalla+One&display=swap');
</style>

<style scoped>
.capi{
  text-transform: capitalize;
}


.margin-auto {
  font-family: 'Fjalla One', sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top:200px;
  
}
.text-down{
  font-family: 'Fjalla One', sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top:5px;
        
}
</style>

<style scoped>
.gradient-custom {
/* fallback for old browsers */
background: #eee709;

/* Chrome 10-25, Safari 5.1-6 */
background: -webkit-linear-gradient(to right, rgb(226, 219, 15), rgb(192, 221, 7));

/* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
background: linear-gradient(to right, rgb(175, 203, 17), rgb(208, 255, 0))
}
</style>