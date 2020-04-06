<script>

export let booster;

</script>

{#if booster.featured === "TRUE"}

<div class="card featured {booster.type}">
  <p>{booster.story}</p>
</div>

{:else}

<div class="card {booster.type}">
  <p>{booster.story}</p>
</div>

{/if}
