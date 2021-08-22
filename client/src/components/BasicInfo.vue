<template>
    <div id="basicinfo">
        <div class="basicContent">
            <div class="portfoCard">
                <span>吳 柏 承</span>
            </div>
            <div class="portfoCard">
                <span>1995/04/11</span>
            </div>
            <div class="portfoCard">
                <span>0988352832</span>
            </div>
            <div class="portfoCard">
                <span>j2223334555@gmail.com</span>
            </div>
            <div class="portfoCard">
                <span>淡江大學資訊傳播學系 畢業</span>
            </div>

        </div>
    </div>
</template>

<script>
export default {
    name: 'BasicInfo'
}
</script>

<style scoped>
    .basicContent{
        margin-top: 50px;
    }
    .portfoCard{
        background-color: #dbffed;
        margin: 30px;
        letter-spacing: 8px;
        font-weight: bold;
        font-size: 36px;
    }
</style>