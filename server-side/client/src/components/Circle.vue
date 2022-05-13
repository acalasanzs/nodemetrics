<template>
    <div class="circle" :id="id">
          <div class="circle-wrap">
            <span>{{id}}</span>
        <div class="circle">
          <div class="mask full">
            <div class="fill"></div>
          </div>
          <div class="mask half">
            <div class="fill"></div>
          </div>
          <div class="inside-circle"> 0% </div>
        </div>
      </div>
  </div>
</template>

<script>
    export default {
        name: 'circle_container',
        props: ["id"],
        methods: {
            update(pointer, percent) {
                const el = document.querySelector("#"+pointer+" .inside-circle");
                el.textContent = percent + "%";
                document.querySelector("#"+pointer+" .mask.full").style.transform = "rotate("+ 180 * (percent/100)+"deg";
                document.querySelector("#"+pointer+" .mask.half .fill").style.transform = "rotate("+ (-180 * (percent/100))+"deg";
            }
        }
    }
</script>

<style scoped>
.circle-wrap {
  width: 135px;
  height: 135px;
  background: var(--bg);;
  border-radius: 50%;
  border: 1px solid var(--bg);
  filter: drop-shadow(0 0 20px var(--bg-2));
}
.circle-wrap span{
  position: absolute;
  line-height: 120px;
  text-align: center;
  text-shadow: 0 0 3px var(--bg-2);
  left: 50%;
  transform: translateX(-50%);
  bottom: -26px;
  z-index: 99999999;
  font-size: .8rem;
  font-weight: 100;
  color: var(--color);
}
.circle-wrap .circle .mask,
.circle-wrap .circle .fill {
  width: 135px;
  height: 135px;
  position: absolute;
  border-radius: 50%;
}

.circle-wrap .circle .mask {
  clip: rect(0px, 150px, 150px, 75px);
}

.circle-wrap .inside-circle {
  width: 122px;
  height: 122px;
  border-radius: 50%;
  background: radial-gradient(var(--bg) 60%, var(--color-2));
  line-height: 120px;
  text-align: center;
  margin-top: 6.5px;
  margin-left: 6.5px;
  color: var(--color);
  position: absolute;
  z-index: 100;
  font-weight: 700;
  font-size: 2em;
}
/* 3rd progress bar */
.mask .fill {
  clip: rect(0px, 75px, 150px, 0px);
  background-color: var(--bg-2);
}

</style>