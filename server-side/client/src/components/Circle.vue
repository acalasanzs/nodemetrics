<template>
    <div role="progressbar" aria-label="circle" valuenow="65%" which={{id}} id={{id}}></div>
</template>

<script>
    export default {
        name: 'circle_container',
        props: ["id"],
        methods: {
            update(pointer, percent) {
                const el = document.querySelector("#"+pointer+" .inside-circle");
                el.setAttribute("valuenow", percent + "%");
                el.style.background = `radial-gradient(closest-side, var(--bg) 90%, transparent 0 99.9%, var(--bg) 0),
    conic-gradient(var(--bg-2) calc(${percent} * 1%), var(--bg) 0)
    `
            }
        }
    }
</script>

<style scoped>
div[role="progressbar"] {
  --size: 7rem;
  width: var(--size);
  height: var(--size);
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: calc(var(--size) / 5);
  filter: drop-shadow(0 0 20px var(--bg-2));
  box-shadow: inset 0 0 20px var(--color-2);
  color: var(--color);
  transition: 0.125s ease;
}

div[role="progressbar"]::before {
  content: attr(valuenow);
  text-shadow: 0 0 3px var(--bg-2);
}
div[role="progressbar"]::after {
  position: absolute;
  font-size: 0.75rem;
  bottom: 20px;
  content: attr(which);
  text-shadow: 0 0 3px var(--bg-2);
}
</style>