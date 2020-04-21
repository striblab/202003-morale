<script>

export let booster;

</script>

{#if booster.from_strib === "TRUE"}

<div class="card strib {booster.type}">
	<div class="text">
		<h5 class="stamp">{booster.timestamp} • <span class="green">Star Tribune</span></h5>
		<p>{@html booster.story} <a href="{booster.url}" target="_blank">Read more</a></p>
        <h4 class="author">{booster.name}, Star Tribune</h4>
	</div>
</div>

{:else}

<div class="card {booster.type}">
	<div class="text">
		<h5 class="stamp">{booster.timestamp}</h5>
			<p>{@html booster.story}</p>
      <h4 class="author">{booster.name}, {booster.city}</h4>
	</div>
</div>

{/if}
