<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<script>
export default{
    data: function(){
        return {
            nombre: "",
            apellido: "",
            email: "",
            edad: "",
            mostrar: true
        }
    },
    mounted(){
        if(localStorage.getItem("user_nombre") != null){
          this.mostrar = false;
          this.nombre = localStorage.getItem("user_nombre");
          this.apellido = localStorage.getItem("user_apellido");
          this.email = localStorage.getItem("user_email");
          this.edad = localStorage.getItem("user_edad");
        }else{
          this.mostrar = true;
          this.nombre = "";
          this.apellido = "";
          this.email = "";
          this.edad = "";
        }
    },
    methods: {
      logout(){
        localStorage.clear();
        this.$router.push('/')
      }
  },
}
</script>

<template>
  <!-- Navbar -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img src="src/assets/roommies.png" height="40" alt=""/>
      </a>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <RouterLink to="/" class="nav-link" aria-current="page">Inicio</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/about" class="nav-link">About</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/profile" class="nav-link">Profile</RouterLink>
          </li>
        </ul>
        <ul class="navbar-nav d-flex flex-row ms-auto me-3">
          <li class="nav-item">
            <RouterLink to="/register" class="nav-link" v-show="mostrar">Register</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/login" class="nav-link" v-show="mostrar">Login</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/Profile" class="nav-link capi" v-show="!mostrar">{{ nombre }} {{ apellido }}</RouterLink>
            <button type="button" class="btn btn-danger" v-show="!mostrar" @click="logout">Cerrar sesión</button>
          </li>
          <li class="nav-item me-3 me-lg-0 dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown1" role="button" data-mdb-toggle="dropdown"
              aria-expanded="false">
              <img src="https://mdbootstrap.com/img/Photos/Avatars/img (31).jpg" class="rounded-circle" height="22"
                alt="" loading="lazy" />
            </a>
            <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown1">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li>
                <hr class="dropdown-divider" />
              </li>
              <li>
                <a class="dropdown-item" href="#">Something else here</a>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <!-- Navbar -->
  <RouterView />
</template>

<style scoped>
.nav {
  background-color: #e3f2fd;
}
.nav-item {
  color: rgb(185, 149, 29);

}
.nav-bg{
  background-color: white;
}
.form-white.input-group>.form-control:focus {
  border-color: #fff;
  box-shadow: inset 0 0 0 1px #fff;
}

.navbar-dark .navbar-nav .nav-link {
  color: #fff;
}

.navbar-dark .navbar-nav .nav-link:hover,
.navbar-dark .navbar-nav .nav-link:focus {
  color: rgba(255, 255, 255, 0.75);
}

.capi{
  text-transform: capitalize;
}
</style>

