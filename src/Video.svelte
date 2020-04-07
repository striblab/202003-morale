<script>
  export let booster;

  let w = 300;
  let h = 450;

</script>

{#if booster.featured === "TRUE"}

<div class="card featured {booster.type}">
  <video height="800" controls>
    <source src="{booster.asset}" type="video/mp4">
  </video>
  <div class="text">
    <h5 class="stamp">{booster.timestamp}</h5>
    <p>{booster.story}</p>
    <h4 class="author">— {booster.name}</h4>
  </div>
</div>

{:else}

<div class="card {booster.type}">
  <video width="{w}" height="{h}" controls>
    <source src="{booster.asset}" type="video/mp4">
  </video>
  <div class="text">
    <h5 class="stamp">{booster.timestamp}</h5>
    <p>{booster.story}</p>
    <h4 class="author">— {booster.name}</h4>
  </div>

</div>

{/if}
