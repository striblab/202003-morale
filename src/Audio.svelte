<script>

export let booster;

</script>

{#if booster.featured === "TRUE"}

<div class="card featured {booster.type}">
	<audio controls>
		<source src="{booster.asset}"/>
	</audio>
	<div class="text">
		<h5 class="stamp">{booster.timestamp}</h5>
		<p>{booster.story}</p>
		<h4 class="author">— {booster.name}</h4>
	</div>
</div>

{:else}

<div class="card {booster.type}">
	<audio>
		<source src="{booster.asset}" controls/>
	</audio>
	<div class="text">
		<h5 class="stamp">{booster.timestamp}</h5>
		<p>{booster.story}</p>
		<h4 class="author">— {booster.name}</h4>
	</div>
</div>

{/if}
