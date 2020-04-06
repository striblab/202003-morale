<script>
  export let booster;

  let w = 300;
  let h = 200;

</script>

{#if booster.featured === "TRUE"}

<div class="card featured {booster.type}">

  <video width="{w}" height="{h}" controls>
    <source src="{booster.asset}" type="video/mp4">
  </video>
  <p>{booster.story}</p>

</div>

{:else}

<div class="card {booster.type}">

  <video width="{w}" height="{h}" controls>
    <source src="{booster.asset}" type="video/mp4">
  </video>
  <p>{booster.story}</p>

</div>

{/if}
