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

    setInterval(() => {
        axios.get('http://localhost:3000/data')
    }, 250)
        .then((response => {
            console.log(response)
        }))
</script>