<script>
import axios from 'axios';

    export default{
        data() {
            return {
                register: {
                    nombre: "",
                    apellido: "",
                    email: "",
                    edad: "",
                    password: ""
                }
            }
        },
        methods: {
            registerIt() {
                axios.post('http://127.0.0.1:5000/register', this.register)
                .then(response => {
                    axios.post('http://127.0.0.1:5000/get_user', this.register).then(data =>{     
                        localStorage.setItem("user_nombre",data.data.nombre);
                        localStorage.setItem("user_apellido",data.data.apellido);
                        localStorage.setItem("user_email",data.data.email);
                        localStorage.setItem("user_edad",data.data.edad);
                        this.$router.push("/profile");
                
                })
                    
                });
            }
        },
        mounted() {

        }
    }
</script>

<template>
    <section class="vh-100" style="background-color: #eee;">
    <div class="container h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-lg-12 col-xl-11">
            <div class="card text-black" style="border-radius: 25px;">
            <div class="card-body p-md-5">
                <div class="row justify-content-center">
                <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">

                    <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Registrate</p>

                    <form v-on:submit.prevent="registerIt" class="mx-1 mx-md-4">

                        <div class="d-flex flex-row align-items-center mb-4">
                            <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                            <div class="form-outline flex-fill mb-0">
                            <input type="text" id="form3Example1c" placeholder="Nombres" class="form-control" v-model="register.nombre"/>
                            </div>
                        </div>

                        <div class="d-flex flex-row align-items-center mb-4">
                            <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                            <div class="form-outline flex-fill mb-0">
                            <input type="text" id="form3Example1c" placeholder="Apellidos" class="form-control" v-model="register.apellido"/>
                            </div>
                        </div>

                        <div class="d-flex flex-row align-items-center mb-4">
                            <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                            <div class="form-outline flex-fill mb-0">
                            <input type="text" id="form3Example1c" placeholder="Edad" class="form-control" v-model="register.edad"/>
                            </div>
                        </div>

                        <div class="d-flex flex-row align-items-center mb-4">
                            <i class="fas fa-envelope fa-lg me-3 fa-fw"></i>
                            <div class="form-outline flex-fill mb-0">
                            <input type="email" id="form3Example3c" placeholder="Email" class="form-control" v-model="register.email"/>
                            </div>
                        </div>

                        <div class="d-flex flex-row align-items-center mb-4">
                            <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
                            <div class="form-outline flex-fill mb-0">
                            <input type="password" id="form3Example4c" placeholder="Contraseña" class="form-control" v-model="register.password"/>
                            </div>
                        </div>

                        <div class="d-flex flex-row align-items-center mb-4">
                            <i class="fas fa-key fa-lg me-3 fa-fw"></i>
                            <div class="form-outline flex-fill mb-0">
                            <input type="password" id="form3Example4cd" placeholder="Repite tu contraseña" class="form-control" />
                            </div>
                        </div>

                        <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                            <button type="submit" class="btn btn-primary btn-lg" @click="registerIt">Registrarse</button>
                        </div>

                    </form>

                </div>
                <div class="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2">

                    <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-registration/draw1.webp"
                    class="img-fluid" alt="Sample image">

                </div>
                </div>
            </div>
            </div>
        </div>
        </div>
    </div>
    </section>
</template>
