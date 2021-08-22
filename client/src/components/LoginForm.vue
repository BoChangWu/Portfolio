<template>
    <div id="loginform">
        <form action="">
            <div id="inputarea">
            <input type="text" id="email" placeholder="Email">            
            <br>
            <input type="password" id="pwd" placeholder="Password">
            </div>
            <div id="buttonarea">
                <button>Sign in</button>
                <button>Sign up</button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: 'LoginForm',

}
</script>

<style scoped>
#loginform{
    display: flex;
    align-items: center;
    justify-content: center;
}
form{
    border-radius: 10px;
    width: 40%;
    height: 500px;
    background-color: #42b983;
}

input{
    border: none;
    border-radius: 5px;
    width: 200px;
    height: 30px;
    margin: 20px;
}
#inputarea{
    margin-top: 30%;
}
#buttonarea{
    margin-top: 30px;
}
button{
    border: none;
    margin: 20px;
    width: 80px;
    height: 40px;
    background-color: #73efb5;
    border-radius: 10px;
}
button:hover{
    background-color: #2c3e50;
    color: #fff;
    transform: scale(110%);
}
</style>