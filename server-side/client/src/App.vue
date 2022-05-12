<template>
    <div id="app">
        <button v-on:click="toggle='character-viewer'">View all characters</button>
        <button v-on:click="toggle='character-creator'">Create a character</button>
        <CharacterViewer v-show="toggle==='character-viewer'" />
        <CharacterCreator v-show="toggle==='character-creator'" />
    </div>
</template>

<script>
    import axios from 'axios'
    async function update() {
        const data = await axios.get('http://localhost:3000/')
        draw(data.data)
    }
    function draw(data) {
        console.log(data)
    }
    setInterval(update, 250);
</script>