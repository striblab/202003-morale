<script>

export let booster;

</script>

{#if booster.featured === "TRUE"}

<div class="card featured {booster.type}">
  <audio>
    <source src="{booster.asset}" type="audio/wav"/>
  </audio>
  <p>{booster.story}</p>
</div>

{:else}

<div class="card {booster.type}">
  <audio>
    <source src="{booster.asset}"/>
  </audio>
  <p>{booster.story}</p>
</div>

{/if}
