<template>
    <div id="work">
        <a href="http://ec2-54-254-209-235.ap-southeast-1.compute.amazonaws.com/">
            <h1>{{work.name}}</h1>
            <img :src="'/imgs/'+work.img" alt="" class="workpic">
        </a>
    </div>
</template>

<script>
export default {
    name:'Work',
    props:{
        work: Object,
    }
}
</script>

<style scoped>
.workpic{
    width: 250px;
    height: 125px;
}
#work{
    padding: 15px;
    width: 250px;
    height: 250px;
    background-color: #42b983;
    margin: 20px;
}
</style>