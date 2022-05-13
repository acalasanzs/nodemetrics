<template>
    <div id="app">
        <div class="circles">
            <circle_container id="CPU"/>
            <circle_container id="RAM"/>
            <circle_container id="DISK"/>
            <circle_container id="GPU" v-show="false"/>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import circle_container from './components/Circle.vue'
    async function update() {
        const data = await axios.get('http://localhost:3001/')
        draw(data.data)
    }
    function draw(data) {
        circle_container.methods.update("CPU", data[0])
        circle_container.methods.update("RAM", data[1])
        circle_container.methods.update("DISK", data[2])
        if (data.length > 3) {
            document.getElementById("GPU").style = "";
            circle_container.methods.update("GPU", data[3])
        }
    }
    setInterval(update, 250);
    export default {
        name: 'App',
        components: {
            circle_container,
        },
    }
</script>
<style>
html{
  --bg: #111111;
  --color: #a29bfe;
  --color-2: #a29bfe80;
  --bg-2: #6c5ce7;
}
body {
  font-family: "Roboto", sans-serif;
  background: var(--bg);
  display: flex;
  width: 100%;
  height: 100vh;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  align-items: center;
  justify-content: center;

}
.circles{
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: center;
  gap: 6rem;
  align-items: center;
}
</style>