<script>

export let booster;

</script>

{#if booster.from_strib === "TRUE"}

<div class="card strib {booster.type}">
	<div class="text">
		<h5 class="stamp">{booster.timestamp}</h5>
		<p>{booster.story}</p>
		<h4 class="author">— {booster.name}</h4>
	</div>
</div>

{:else}

<div class="card {booster.type}">
	<div class="text">
		<h5 class="stamp">{booster.timestamp}</h5>
		<p>{booster.story}</p>
		<h4 class="author">— {booster.name}</h4>
	</div>
</div>

{/if}
