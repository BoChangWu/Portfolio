<template>
    <div id="intro">
        <div class="introCard">

        
            <h1>I'm Json Wu</h1>
            <div class="content">
                
                <p>這裡是關於我的網頁，<br>
                我的自傳以及作品都放在這裡<br>
                也有我的聯絡資訊可以聯絡到我<br><br>
                我來自新竹,淡江大學資訊傳播系畢業<br>
                還是學生的時候因為課程關係接觸 JavaScript<br>
                從此以後接觸程式語言,曾經<br>
                利用 C# 寫過遊戲<br>
                HTML,CSS,JavaScript撰寫前端<br>
                Node.js,Flask後端架設<br>
                MySQL,MongoDB資料庫語法<br>
                操作Linux系統利用Docker,Aws佈署網站<br><br>
                Python 資料分析,網路爬蟲<br>
                Tensorflow,Pytorch機器學習,深度學習以及OpenCV<br>
                </p>
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scope>
.introCard{
    margin: auto;
    width: 600px;
    height: 60%;
    background-color: #42b983;
    padding: 10px;
}
.content{
    height: 100%;
    display: flex;
    /* align-items: center; */
    justify-content: center;
}
p{  
    font-size: 18px;
    width: 500px;
    text-align: justify;
    font-weight: bold;
    margin: 20px;
}
#intro{
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>