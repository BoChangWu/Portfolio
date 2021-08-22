<template>
    <div id="trylogin">
        <h2>This page is just show you how I connect frontend with Server and DataBase</h2>
        <LoginForm/>
    </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'
export default {
    name:'TryLogin',
    components:{
        LoginForm,
    }
}
</script>

<style>

</style>