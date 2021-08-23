<template>
  <div id="nav">
    <router-link to="/">Info</router-link> |
    <router-link to="/works">Works</router-link> |
    <router-link to="/contact">Contact</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/trylogin" >TryLogin</router-link>
    <router-view @toggle-status="toggleStatus" /> <!--@function要在這邊下-->
  </div>
  
</template>
<script>
  export default {
    name: 'App',
    methods:{
      toggleStatus(){
        console.log('nice')
        this.$router.push("/")
      }
    }
  }

</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}


</style>
